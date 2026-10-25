#!/usr/bin/env python3
"""Offline marker-to-source index for verified MAX APK decompiled with JADX."""
import collections
import hashlib
import json
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]); apk = pathlib.Path(sys.argv[2])
sample = json.loads(pathlib.Path('evidence/sample.json').read_text())
actual = hashlib.sha256(apk.read_bytes()).hexdigest()
if actual != sample['sha256'] or apk.stat().st_size != sample['bytes']:
    sys.exit('APK checksum/size mismatch')
markers = ['InputPhoneScreen','ConfirmPhoneScreen','AUTH_OTP','AUTH_CHECK_CALL',
           'AUTH_CALL_OUT','AUTH_BY_TRACK','AUTH_QR_APPROVE','AUTH_CHECK_PASSWORD',
           'AUTH_2FA','api2.oneme.ru','api-tg.oneme.ru','api/v3/ws',
           'tokenRefresh','refreshToken','accessToken','refresh_token','access_token',
           'verifyOtp','checkOtp','requestOtp','sendOtp','verifyCode','requestCode',
           'AuthRepository','AuthApi','AuthService','AuthRequest','AuthResponse',
           'LoginRequest','LoginResponse','Authorization','Bearer','sessionToken']
names = re.compile(r'(auth|login|token|session|otp|confirmphone|inputphone|account|password|verification|mobileid|checkcall|phoneauth)',re.I)
counter=collections.Counter(); ranked=[]
java_files=sorted(root.rglob('*.java'))
if not java_files: sys.exit('JADX did not generate Java files')
for f in java_files:
    path=f.relative_to(root).as_posix()
    try: lines=f.read_text(encoding='utf-8',errors='replace').splitlines()
    except OSError: continue
    hits=[]
    for i,line in enumerate(lines,1):
        lower=line[:3500].lower()
        match=[x for x in markers if x.lower() in lower]
        for x in match: counter[x]+=1
        if match and len(hits)<30: hits.append((i,match,line[:3500]))
    if not hits and not names.search(path): continue
    strong=['AUTH_OTP','AUTH_CHECK_CALL','AUTH_CALL_OUT','AUTH_BY_TRACK','AUTH_QR_APPROVE',
            'AUTH_CHECK_PASSWORD','AUTH_2FA','api/v3/ws','requestOtp','verifyOtp',
            'refreshToken','accessToken','AuthRepository','AuthApi','AuthService']
    score=(10 if names.search(f.name) else 0)+8*sum(any(x in m for x in strong) for _,m,_ in hits)+min(20,len(hits))
    if 'ru/ok/' in path or 'one/me/' in path: score+=3
    ranked.append((score,path,hits))
ranked.sort(key=lambda x:(-x[0],x[1]))
def safe(s):
    s=s.replace('|','\\|').replace(chr(96),"'").strip()
    s=re.sub(r'(?i)(Bearer\s+)[A-Za-z0-9._~+/=-]{12,}',r'\1[REDACTED]',s)
    s=re.sub(r'(?i)((?:api[_-]?key|secret|password|access[_-]?token|refresh[_-]?token)\w*\s*=\s*)("[^"]+"|\x27[^\x27]+\x27)',r'\1"[REDACTED]"',s)
    return s[:400]
def row(*xs):return '| '+' | '.join(str(x) for x in xs)+' |'
report=['# MAX 26.35.1: указатель кода авторизации','','Автоматический статический разбор точного APK с помощью JADX.','Это перечень кандидатов, а НЕ подтверждённая последовательность сетевых запросов.','',
        'SHA-256: '+actual,'Обработано файлов Java: '+str(len(java_files)),
        'Файлов-кандидатов: '+str(len(ranked)),'',
        '## Частота маркеров','',row('Маркер','Совпадений'),'|---|---:|']
for m in markers: report.append(row(m,counter[m]))
report+=['','## Приоритет ручного разбора','',row('Приоритет','Путь Java-файла','Маркеры'),'|---:|---|---|']
for score,path,hits in ranked[:150]:
    report.append(row(score,path,safe(', '.join(sorted(set(x for _,ms,_ in hits for x in ms))) or 'имя файла')))
report+=['','## Ограничения','','Одни названия, строки или их количество не устанавливают назначение сервера, порядок обмена или формат токенов.','Для этого нужно проследить вызывающие функции и поля сериализации, затем проверить журнал реального входа.','']
match_report=['# MAX 26.35.1: ссылки на участки кода','','Автоматические совпадения строк в выводе JADX. Возможны ошибки декомпиляции.','SHA-256: '+actual,'']
for score,path,hits in ranked[:120]:
    if not hits: continue
    match_report+=['## '+path+' (приоритет '+str(score)+')']
    for i,ms,line in hits[:9]:match_report.append('- Строка '+str(i)+'; '+', '.join(ms)+': '+safe(line))
    match_report.append('')
pathlib.Path('docs/auth-code-index-26.35.1.md').write_text('\n'.join(report)+'\n')
pathlib.Path('evidence/auth-code-matches-26.35.1.md').write_text('\n'.join(match_report)+'\n')
print('Java files:',len(java_files),'candidates:',len(ranked))
print('Top files:',[(s,p) for s,p,_ in ranked[:15]])
