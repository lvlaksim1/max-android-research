#!/usr/bin/env python3
"""Reproducible, read-only audit of MAX Android telephony API *references*.

Reports where the verified APK calls or mentions Android telephony APIs.
Never runs the app, invokes protected APIs, or forges device identity.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: max_telephony_audit.py <jadx-sources> <verified-apk>")
src, apk = Path(sys.argv[1]), Path(sys.argv[2])
info = json.loads(Path("evidence/sample.json").read_text(encoding="utf-8"))
with apk.open("rb") as f:
    digest = hashlib.file_digest(f, "sha256").hexdigest()
if digest != info["sha256"] or apk.stat().st_size != info["bytes"]:
    raise SystemExit("Reference APK does not match committed evidence")

terms = [
    "getLine1Number", "getPhoneNumber(", "getSimSerialNumber",
    "getSubscriberId", "getNetworkOperator(", "getNetworkOperatorName(",
    "getSimOperator(", "getSimOperatorName(", "getSimState(",
    "SubscriptionManager", "TelephonyManager", "getActiveSubscriptionInfo",
    "getDefaultSubscriptionId", "READ_PHONE_NUMBERS", "READ_PHONE_STATE",
    "TelephonyCallback", "CarrierPrivileges", "MobileId",
]
pattern = re.compile("|".join(re.escape(x) for x in terms))
files_checked = 0
hits = {term: [] for term in terms}
for path in sorted(src.rglob("*.java")):
    files_checked += 1
    relative = path.relative_to(src).as_posix()
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        continue
    for n, line in enumerate(lines, 1):
        matched = [term for term in terms if term in line]
        if matched:
            # Compact and bounded, without embedding full application code.
            excerpt = line.strip()[:200].replace("|", "\\|").replace("`", "'")
            for term in matched:
                hits[term].append((relative, n, excerpt))

out = ["# MAX 26.35.1 — проверка получения номера SIM из APK",
       "", f"Проверен оригинал `base.apk` ({digest}); исходных Java: **{files_checked}**.",
       "Проверка статическая, без запуска, сетевых запросов или изменения SIM.",
       "", "## Сводка вызовов и ссылок"]
out += ["", "| Маркер | Найдено строк |", "|---|---:|"]
out += [f"| `{term}` | {len(hits[term])} |" for term in terms]
out += ["", "## Найденные обращения (по 12 на маркер)", ""]
for term in terms:
    if not hits[term]:
        continue
    out += [f"### `{term}`", ""]
    for p, ln, excerpt in hits[term][:12]:
        out.append(f"- `{p}:{ln}` — `{excerpt}`")
    if len(hits[term]) > 12:
        out.append(f"- Остальные {len(hits[term])-12} строк не приведены")
    out.append("")
out += [
    "## Интерпретация",
    "",
    "- Ссылки на API и строки ещё не доказывают использование конкретного пути во время привязки устройства.",
    "- Возвращённый Android API номер SIM не является доказательством владения номером или успешной проверки Mobile ID.",
    "- Проверка доверенного устройства может проводиться через мобильного оператора вне локального чтения номера.",
    "- В отчёте нет сетевых токенов, пользовательских номеров, кодов подтверждения и рекомендаций по обходу привязки.",
    "",
    "Источники: официальный Android API `SubscriptionManager.getPhoneNumber` и справка MAX по Mobile ID.",
    "",
]
dest = Path("docs/telephony-api-audit-26.35.1.md")
dest.write_text("\n".join(out), encoding="utf-8")
print("Wrote", dest, "files", files_checked)
for term in terms:
    print(term, len(hits[term]))
