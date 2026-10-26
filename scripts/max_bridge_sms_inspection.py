#!/usr/bin/env python3
"""Static listing of MAX Android's mini-app JavaScript bridge API.

No runtime, credentials, request bodies or changes to client behavior.
"""
import hashlib,json,pathlib,re,sys
src=pathlib.Path(sys.argv[1]); apk=pathlib.Path(sys.argv[2]); info=json.loads(pathlib.Path("evidence/sample.json").read_text())
with apk.open("rb") as f: h=hashlib.file_digest(f,"sha256").hexdigest()
assert h==info["sha256"] and apk.stat().st_size==info["bytes"]
patterns=["addJavascriptInterface", "JavascriptInterface", "evaluateJavascript",
          "WebAppVerifyMobileId", "WebAppPostEvent", "WebAppProxy",
          "TelegramWebviewProxy","window.webkit.messageHandlers","postEvent",
          "WebAppNoNetworkException","no_cellular","WebAppCallback","JsBridge"]
founds=[]
for path in sorted(src.rglob("*.java")):
    data=path.read_text(encoding="utf-8",errors="replace")
    lns=data.splitlines()
    match=[(i+1,x.strip()) for i,x in enumerate(lns) if any(k.lower() in x.lower() for k in patterns)]
    if match: founds.append((path,len(lns),match))
report=["# Android MAX 26.35.1 — структура JS bridge (read-only)","","APK sha256: `"+h+"`.",
        "Анализ: исходники JADX; `WebAppVerifyMobileId` и `no_cellular` без вызовов сервера.", "", "## Индекс классов", ""]
for p,n,m in founds:
    if "/one/me/webapp/" in str(p) or any("addJavascriptInterface" in x or "JavascriptInterface" in x for _,x in m) or any("WebAppVerifyMobileId" in x for _,x in m):
        report.append(f"- `{p.relative_to(src)}`: строк {n}, совпадений {len(m)}.")
report.extend(["","## Основные места внедрения JavascriptInterface/JS API",""])
included=0
for p,n,m in founds:
    if not any("addJavascriptInterface" in x or "JavascriptInterface" in x or "WebAppVerifyMobileId" in x or "no_cellular" in x for _,x in m):
        continue
    report.extend([f"### `{p.relative_to(src)}`","", "```java"])
    lns=p.read_text(encoding="utf-8",errors="replace").splitlines()
    ranges=[]
    for i,x in m:
        if any(k in x for k in ("addJavascriptInterface", "JavascriptInterface", "WebAppVerifyMobileId", "no_cellular", "WebAppProxy")):
            a=max(i-15,1);b=min(i+21,n)
            if ranges and a<=ranges[-1][1]:ranges[-1]=(ranges[-1][0],max(b,ranges[-1][1]))
            else:ranges.append((a,b))
    count=0
    for a,b in ranges[:12]:
        for k in range(a,b+1):
            x=lns[k-1]
            if len(x)>450 or "@Metadata(" in x:x="[generated annotation omitted]"
            report.append(f"{k}: {x[:350]}")
            count+=1
            if count>210:break
        if count>210:break
    report.extend(["```",""])
    included+=1
    if included>=48:break
dst=pathlib.Path("docs/webapp-jsbridge-inspection-26.35.1.md")
dst.write_text("\n".join(report),encoding="utf-8")
print("Found",len(founds),"related Java classes, reported",included,"; bytes",dst.stat().st_size)
