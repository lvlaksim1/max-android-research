#!/usr/bin/env python3
"""Offline targeted source trace for MAX WebAppVerifyMobileId.

Run only against the SHA-256 verified owner-provided MAX 26.35.1 APK.
Produces bounded class excerpts to facilitate manual analysis.
No auth, network traffic, or device spoofing.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

if len(sys.argv) != 3:
    sys.exit("usage: python scripts/max_mobileid_trace.py <jadx-sources> <apk>")
src=Path(sys.argv[1]); apk=Path(sys.argv[2])
sample=json.loads(Path("evidence/sample.json").read_text(encoding="utf-8"))
with apk.open("rb") as f:
    digest=hashlib.file_digest(f, "sha256").hexdigest()
if digest != sample["sha256"] or apk.stat().st_size != sample["bytes"]:
    sys.exit("APK hash or byte length differs from research reference")

targets={
    "a8l": [r"WebAppVerifyMobileId",r"jolVar",r"verifyMobileId"],
    "dol": [r"WebAppVerifyMobileId",r"public final Object f\("],
    "jol": [r"class jol",r"String",r"serializer"],
    "ajk": [r"class ajk",r"code",r"toString"],
    "bj9": [r"class bj9",r"public bj9",r"boolean"],
    "mj9": [r"class mj9",r"public .* b\("],
    "s1k": [r"class s1k",r"WebApp",r"verify"],
}
patterns=[
    "WebAppVerifyMobileId","VerifyMobileIdResponseInfo",
    "verifyMobileId","mobileid.", "MobileId",
    "getNetworkOperator()", "getSimOperator()", "getLine1Number",
]
allhits=[]
for path in sorted(src.rglob("*.java")):
    text=path.read_text(encoding="utf-8",errors="replace")
    match=[s for s in patterns if s in text]
    if match:
        allhits.append((path,match))

def excerpt(path, anchors, radius=18, limit=8):
    if not path.exists(): return ["(class not found)"]
    lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
    hit=[]
    for i,l in enumerate(lines):
        if any(re.search(a,l,re.I) for a in anchors):
            hit.append(i)
    filtered=[]
    for i in hit:
        if len(filtered)>=limit: break
        if filtered and i-filtered[-1]<max(2,radius//2):continue
        filtered.append(i)
    ranges=[]
    for i in filtered:
        a=max(0,i-radius);b=min(len(lines),i+radius+1)
        if ranges and a<=ranges[-1][1]:
            ranges[-1]=(ranges[-1][0],max(b,ranges[-1][1]))
        else:ranges.append((a,b))
    out=[f"File lines: {len(lines)}, matched locations: {len(hit)}."]
    for a,b in ranges:
        out.append(f"Lines {a+1}–{b}:")
        for idx in range(a,b):
            line=lines[idx]
            # Kotlin compiler metadata is not executable business logic.
            if "@Metadata(" in line and len(line)>300: line="[Kotlin metadata annotation omitted]"
            line=line[:380].replace("`","'")
            out.append(f"{idx+1:>5}: {line}")
    return out

md=[
    "# MAX 26.35.1 — трассировка WebAppVerifyMobileId (статический анализ)",
    "",
    f"SHA256 исходного APK: `{digest}`; обнаружено Java-файлов с признаками: {len(allhits)}.",
    "Контент получен из JADX, не из сетевых ответов. Ошибки декомпилятора и обфускация могут скрывать отдельные пути.",
    "",
    "## Файлы с признаками Mobile ID",
    "",
    "| Путь | Совпавшие маркеры |","|---|---|"
]
for path,hits in allhits[:110]:
    md.append(f"| `{path.relative_to(src).as_posix()}` | {', '.join(hits[:5])} |")
if len(allhits)>110:
    md.append(f"| Ещё файлов | {len(allhits)-110} |")
md.extend(["","## Ключевые классы и фрагменты исполнения",""])
for name,anchors in targets.items():
    path=src/"defpackage"/(name+".java")
    md.extend([f"### `defpackage/{name}.java`", "", "```java"])
    md.extend(excerpt(path,anchors,radius=25 if name in ("a8l","dol") else 17,limit=5))
    md.extend(["```",""])
md.extend(["## Углублённое изучение обработчика и его зависимостей", ""])
deep_classes = {
    "dol": (100, 240),
    "gol": (1, 120),
    "hol": (1, 115),
    "eol": (1, 155),
    "zik": (1, 110),
    "ajk": (1, 60),
    "col": (1, 100),
    "ekl": (1, 160),
    "j01": (1, 110)
}
for name, (lo, hi) in deep_classes.items():
    path=src/"defpackage"/(name+".java")
    md.extend([f"### `{path.relative_to(src)}`", "", "```java"])
    if path.exists():
        lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
        md.append(f"Total lines: {len(lines)}. Examined: {lo}–{min(hi,len(lines))}.")
        for idx in range(lo-1,min(hi,len(lines))):
            line=lines[idx]
            if len(line)>600 or "@Metadata(" in line:
                line="[long Kotlin metadata/codegen omitted]"
            md.append(f"{idx+1:>5}: {line[:380].replace(chr(96), chr(39))}")
    else:
        md.append("(class not found)")
    md.extend(["```",""])

md.extend(["## Сетевая реализация запроса и обратная доставка", ""])
network_classes={"bol": (1,250),"qrk":(1,230),"gj9":(1,90),"qi4":(1,155)}
for name,(lo,hi) in network_classes.items():
    path=src/"defpackage"/(name+".java")
    md.extend([f"### `{path.relative_to(src)}`", "", "```java"])
    if path.exists():
        lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
        md.append(f"Total lines: {len(lines)}, excerpt: {lo}–{min(hi,len(lines))}")
        for idx in range(lo-1,min(hi,len(lines))):
            line=lines[idx]
            if len(line)>600 or "@Metadata(" in line:
                line="[long generated metadata omitted]"
            md.append(f"{idx+1:>5}: {line[:350].replace(chr(96), chr(39))}")
    else:
        md.append("(class not found)")
    md.extend(["```",""])

md.extend(["## Трассировка выбора сети и обработки результата", ""])
focus={
 "ekl": ["verifyMobileIdJob","NetworkRequest.Builder","ConnectivityManager","addTransportType","requestNetwork","getSocketFactory","bindProcessToNetwork","TRANSPORT_CELLULAR","new qrk","bol"],
 "qrk": ["case 13:","case 17:","WebAppNoNetworkException","ajk","dol","gol"],
 "aj9": ["class aj9","public final","collect"," c("],
 "n9l": ["getSocketFactory","NetworkRequest"],
 "zik": ["VERIFY_MOBILE_ID"],
}
for name,queries in focus.items():
    path=src/"defpackage"/(name+".java")
    md.extend([f"### `{path.relative_to(src)}` — опорные фрагменты", "", "```java"])
    if path.exists():
        lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
        hits=[i for i,l in enumerate(lines) if any(q in l for q in queries)]
        ranges=[]
        for i in hits:
            a=max(0,i-12); b=min(len(lines),i+26)
            if ranges and a<=ranges[-1][1]:
                ranges[-1]=(ranges[-1][0],max(ranges[-1][1],b))
            else: ranges.append((a,b))
        md.append(f"Total lines: {len(lines)}; matches: {len(hits)}")
        used=0
        for a,b in ranges:
            if used>=520: break
            md.append(f"Excerpt {a+1}–{b}")
            for n in range(a,b):
                if used>=520:break
                line=lines[n]
                if "@Metadata(" in line or len(line)>600:line="[compiler metadata omitted]"
                md.append(f"{n+1:>5}: {line[:340].replace(chr(96), chr(39))}")
                used+=1
    else:
        md.append("(class not found)")
    md.extend(["```",""])

md.extend(["## Сотовый HTTP-клиент (проверка тайм-аутов и результата)", ""])
for name,lim in [("fcl",380),("m3g",100),("bcl",130),("dcl",130)]:
    path=src/"defpackage"/(name+".java")
    md.extend([f"### `{path.relative_to(src)}`", "", "```java"])
    if path.exists():
        lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
        md.append(f"Lines: {len(lines)}; printed first {min(len(lines),lim)}")
        for idx,line in enumerate(lines[:lim],1):
            if "@Metadata(" in line or len(line)>600:line="[generated metadata omitted]"
            md.append(f"{idx:>5}: {line[:400].replace(chr(96), chr(39))}")
    else: md.append("(class not found)")
    md.extend(["```",""])

md.extend([
    "## Применение результатов",
    "",
    "Этот отчёт предназначен для ручной проверки того, какие поля, обработчики и результаты связаны с вызовом мини-приложения.",
    "Он не содержит исполняемых рекомендаций по подмене Mobile ID или серверного подтверждения.",
    "Наличие класса не доказывает, что конкретный запуск мини-приложения использовал данный путь.",
    ""
])
dest=Path("docs/mobileid-bridge-trace-26.35.1.md")
dest.write_text("\n".join(md),encoding="utf-8")
print("Created",dest, "hits",len(allhits))
