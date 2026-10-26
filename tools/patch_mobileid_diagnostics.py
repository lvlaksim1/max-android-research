#!/usr/bin/env python3
"""Instrument original MAX test APK with redacted Mobile ID event times only.
Does not capture or transfer URLs, tokens, SIM identifiers, HTTP headers/body or codes.
"""
import argparse
import re
from pathlib import Path

PREFIX = "Lru/oneme/research/MobileIdTrace;"
LOGGER = r'''.class public final Lru/oneme/research/MobileIdTrace;
.super Ljava/lang/Object;
.field private static context:Landroid/content/Context;

.method public static init(Landroid/content/Context;)V
    .registers 1
    sput-object p0, Lru/oneme/research/MobileIdTrace;->context:Landroid/content/Context;
    return-void
.end method

.method public static mobileIdRequest()V
    .registers 1
    const-string v0, "bridge_request"
    invoke-static {v0}, Lru/oneme/research/MobileIdTrace;->record(Ljava/lang/String;)V
    return-void
.end method

.method public static mobileIdHttp()V
    .registers 1
    const-string v0, "cellular_http_attempt"
    invoke-static {v0}, Lru/oneme/research/MobileIdTrace;->record(Ljava/lang/String;)V
    return-void
.end method

.method private static record(Ljava/lang/String;)V
    .registers 8
    .catch Ljava/lang/Exception; {:try_start .. :try_end} :handler
    :try_start
    sget-object v0, Lru/oneme/research/MobileIdTrace;->context:Landroid/content/Context;
    if-eqz v0, :end
    const/4 v1, 0x0
    invoke-virtual {v0, v1}, Landroid/content/Context;->getExternalFilesDir(Ljava/lang/String;)Ljava/io/File;
    move-result-object v0
    if-eqz v0, :end
    new-instance v1, Ljava/io/File;
    const-string v2, "mobileid-research.jsonl"
    invoke-direct {v1, v0, v2}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V
    new-instance v3, Ljava/io/FileOutputStream;
    const/4 v2, 0x1
    invoke-direct {v3, v1, v2}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;Z)V
    new-instance v4, Ljava/lang/StringBuilder;
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V
    const-string v5, "{\"schema\":1,\"time_ms\":"
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v0
    invoke-virtual {v4, v0, v1}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;
    const-string v5, ",\"event\":\""
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v5, "\"}\n"
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    const-string v1, "UTF-8"
    invoke-virtual {v0, v1}, Ljava/lang/String;->getBytes(Ljava/lang/String;)[B
    move-result-object v0
    invoke-virtual {v3, v0}, Ljava/io/FileOutputStream;->write([B)V
    invoke-virtual {v3}, Ljava/io/FileOutputStream;->close()V
    :end
    :try_end
    return-void
    :handler
    move-exception v0
    return-void
.end method
'''

def find(root, suffix):
    matches = sorted(root.glob("smali*/" + suffix))
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one {suffix}, found {len(matches)}")
    return matches[0]

def patch_method(path, method_pattern, call):
    source = path.read_text(encoding="utf-8")
    matches = [x for x in re.finditer(r"^\.method[^\n]*$", source, re.M)
               if re.search(method_pattern, x.group(0))]
    if len(matches) != 1:
        raise SystemExit(f"{path}: expected one method {method_pattern}, found {len(matches)}")
    m = matches[0]
    end = source.find("\n.end method", m.end())
    if end < 0:
        raise SystemExit("method missing end")
    method = source[m.start():end]
    regs = re.search(r"^[ \t]*\.(?:registers|locals)[ \t]+\d+[ \t]*$", method, re.M)
    if regs is None or call in method:
        raise SystemExit("Cannot safely instrument method")
    pos = m.start() + regs.end()
    source = source[:pos] + "\n    " + call + source[pos:]
    path.write_text(source, encoding="utf-8")
    print("instrumented", path, m.group(0))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("decoded", type=Path)
    root = parser.parse_args().decoded
    application = find(root, "one/me/android/OneMeApplication.smali")
    delegate = find(root, "defpackage/dol.smali")
    cellular = find(root, "defpackage/fcl.smali")
    patch_method(application, r"\sonCreate\(\)V",
                 f"invoke-static {{p0}}, {PREFIX}->init(Landroid/content/Context;)V")
    patch_method(delegate, r"\sa\(Ljava/lang/String;Ljava/lang/String;Ldefpackage/b55;\)Ljava/lang/Object;",
                 f"invoke-static {{}}, {PREFIX}->mobileIdRequest()V")
    patch_method(cellular, r"\sa\(Ljava/lang/String;Ldefpackage/d55;\)Ljava/lang/Object;",
                 f"invoke-static {{}}, {PREFIX}->mobileIdHttp()V")
    file = delegate.parent.parent / "ru/oneme/research/MobileIdTrace.smali"
    if file.exists():
        raise SystemExit("Already instrumented")
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(LOGGER, encoding="utf-8")
    print("created redacted logger", file)

if __name__ == "__main__":
    main()
