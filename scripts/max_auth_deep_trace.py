#!/usr/bin/env python3
"""Focused, reproducible offline trace of MAX account-authentication call graph."""
import collections
import hashlib
import json
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
apk = pathlib.Path(sys.argv[2])
sample = json.loads(pathlib.Path("evidence/sample.json").read_text())
digest = hashlib.file_digest(apk.open("rb"), "sha256").hexdigest()
assert digest == sample["sha256"] and apk.stat().st_size == sample["bytes"]
files = sorted(root.rglob("*.java"))
assert files
OUT = pathlib.Path("evidence")
OUT.mkdir(exist_ok=True)

target = [
 "ki0","ji0","wh0","vh0","mvf","k7a","a7a","aj0",
 "bj0","ej0","cj0","dj0","u6j","bqc","f7j","ctc",
 "bcc","ccc","z6j","v99","wpc","dq4","yr0","u79","lp4",
 "s1c","r1c","p1c","n3a","h16","azc","fh0","wi",
 "tdd","t6a","ph0","oh0","cj3",
 "f0f","cqe","th0","i7a","f6f","g0f","d0f","q1a","hog","mag","lag",
 "r1g","k5a","s5a","dcc","gci","i00","dle","m8a","rh0","gh0",
 "u6","c5h","gn0","sk2","mse","l7a","c7j","k8a","gh6","er","e7a","z7a","e9a","k6a","d5h","acc","n4a",
 "dtc","qi0","e5h","j6h","f6h","st5","o57","v6j","i00","jn0","pck","i9g","f4j","o6a",
]
# Exact symbol/constant searches. Ignore incidental shared short strings.
patterns = collections.OrderedDict([
 ("auth use-case references", r"\b(?:new\s+ki0\s*\(|ki0(?:Var)?\.[a-zA-Z0-9_]+|new\s+ej0\s*\(|new\s+wh0\s*\()"),
 ("AUTH to LOGIN handoff", r"\bf0f(?:Var)?\.[a-zA-Z0-9_]+\(|new\s+f0f\s*\(|new\s+th0\s*\(|\.containsKey\(\"LOGIN\"\)|\"LOGIN\""),
 ("network login implementation", r"\b(?:new\s+i7a\s*\(|new\s+r1g\s*\(|r1gVar\.[a-zA-Z0-9_]+\(|new\s+dcc\s*\()"),
 ("LOGIN constructor call sites", r"\bnew\s+k7a\s*\("),
 ("AUTH request / code verification", r"\bnew\s+(?:bqc|aj0)\s*\(\s*tdd\.(?:m|l|u)|\bnew\s+(?:aj0|bqc)\s*\("),
 ("auth response parser", r"AUTH_CONFIRM|authTokenType|verifyCode|session\.sequence|START_AUTH|CHECK_CODE|tokenType"),
 ("token lifecycle", r"refreshToken|accessToken|authToken|tokenRefresh|AuthToken|LoginToken|SessionToken|refresh_token|access_token"),
 ("account storage", r"EncryptedSharedPreferences|MasterKey|AccountInitializer|SessionRepository|AccountRepository|accountToken"),
 ("auth token persistence", r"authToken|refreshToken|expiresInSecs|tokenCreationEpochInSecs|putProfile|user\.auth|server\.login|saveToken|tokenStore"),
 ("session init to LOGIN", r"SESSION_INIT|Send Login command|new\s+i7a\s*\(|new\s+c5h\s*\(|new\s+gn0\s*\("),
 ("exact account token keys", r"auth\.token|auth\.account\.name|user\.Phone|server\.host|server\.port|server\.useTls"),
 ("packet/session encoder", r"getOutputStream\(|getInputStream\(|SSLSocket|TLS|encodedPayload|sendPacket|readPacket|writePacket|packetVersion"),
 ("network / handshake", r"api2\.oneme\.ru|api-tg\.oneme\.ru|wss://|https://|SESSION_INIT|SESSION_AUTH|sessionSeed|initializeSessionSeed"),
])
compiled = {k: re.compile(p, re.I) for k,p in patterns.items()}
# Avoid copying every occurrence of popular constants into public evidence.
limits = {key: 60 for key in compiled}
limits["LOGIN constructor call sites"] = 90
limits["auth use-case references"] = 90
limits["network / handshake"] = 85
limits["AUTH to LOGIN handoff"] = 80
limits["auth token persistence"] = 95
limits["session init to LOGIN"] = 90
limits["exact account token keys"] = 95
limits["packet/session encoder"] = 60
locations={key:[] for key in compiled}
class_path={}
for file in files:
    rel=file.relative_to(root).as_posix()
    class_path.setdefault(file.stem, []).append(rel)
    try:
        rows=file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        continue
    hits_in_file=collections.defaultdict(list)
    for line_no, line in enumerate(rows,1):
        for category, pat in compiled.items():
            if pat.search(line):
                hits_in_file[category].append(line_no)
    for cat, indexes in hits_in_file.items():
        entries=locations[cat]
        if len(entries) < limits[cat]:
            entries.append((rel, indexes[:8], rows))
def safe(s):
    s=s.replace("|","\\|").replace("\`","'").strip()
    s=re.sub(r"(?i)(Bearer\s+)[A-Za-z0-9._~+/=-]{12,}",r"\1[REDACTED]",s)
    return s[:340]

sources=["# MAX 26.35.1 — исходные классы и модели авторизации",
 "", "Точное совпадение SHA-256: "+digest,
 "Файлы Java из JADX; номер строки относится к декомпилированному представлению.",
 "Показаны первые 450 строк файла. Для крупных классов оставлены поисковые маркеры.",
 ""]
for name in target:
    paths=class_path.get(name,[])
    if not paths:
        continue
    for rel in paths[:2]:
        rows=(root / rel).read_text(encoding="utf-8",errors="replace").splitlines()
        # Bigger client classes are truncated, preserve initial definitions and method signatures.
        limit=530 if name in {"ki0","wh0","mvf","k7a","a7a","aj0","bqc","u6j","f7j","ctc","s1c","r1c","p1c","f0f","cqe","th0","i7a","hog","mag","lag","r1g","u6","c5h","gn0","sk2","mse","l7a","c7j","k8a","gh6","er","dtc","qi0","e5h","d5h","j6h","st5","o57","v6j"} else 260
        sources += [f"## {rel} ({len(rows)} строк)", "", "~~~java"]
        for idx, ln in enumerate(rows[:limit],1):
            sources.append(f"{idx:4}: {safe(ln)}")
        sources += ["~~~", ""]
        if len(rows)>limit:
            sig=re.compile(r"\b(?:public|private|protected|static)\b.*\b(?:Object|void|String|boolean|int|long|byte\[\]|[a-z]\w*)\s+[a-z]\w*\s*\(")
            matched=[(idx,ln) for idx,ln in enumerate(rows[limit:],limit+1) if sig.search(ln)]
            sources.append("Поздние сигнатуры: " + "; ".join(str(idx)+" "+safe(ln) for idx,ln in matched[:24]))
            sources.append("")
(OUT/"auth-deep-source-26.35.1.md").write_text("\n".join(sources)+"\n",encoding="utf-8")

matches=["# MAX 26.35.1 — перекрёстные ссылки авторизации",
 "", "Подтверждено контрольной суммой: "+digest,
 "Ссылки — адреса в декомпилированном тексте. Статическое упоминание не доказывает выполнение.",
 ""]
for cat, found in locations.items():
    matches += [f"## {cat}", f"Файлов с совпадениями (первые {limits[cat]}): {len(found)}", ""]
    for rel, idxs, rows in found:
        matches += ["### "+rel, "~~~text"]
        shown=set()
        for idx in idxs[:5]:
            for at in range(max(1,idx-4),min(len(rows),idx+5)+1):
                if at not in shown:
                    matches.append(f"{at:4}: {safe(rows[at-1])}")
                    shown.add(at)
            matches.append("--")
        matches += ["~~~",""]
(OUT/"auth-deep-crossrefs-26.35.1.md").write_text("\n".join(matches)+"\n",encoding="utf-8")
print("APK", digest, "files",len(files))
print("Generated source lines",len(sources), "crossref lines",len(matches))
print("Sizes:",[(p.name,p.stat().st_size) for p in [OUT/"auth-deep-source-26.35.1.md",OUT/"auth-deep-crossrefs-26.35.1.md"]])
