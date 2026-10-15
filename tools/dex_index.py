#!/usr/bin/env python3
"""Read DEX string pools for offline static inspection."""
import json
import re
import struct
import sys
import zipfile

def u32(data, offset):
    return struct.unpack_from("<I", data, offset)[0]

def leb(data, offset):
    value = 0
    for index in range(5):
        byte = data[offset + index]
        value |= (byte & 127) << (7 * index)
        if byte < 128:
            return value, offset + index + 1
    raise ValueError("Invalid DEX string length")

def scan(data):
    if data[:3] != b"dex":
        raise ValueError("Not DEX")
    strings = []
    for i in range(u32(data, 56)):
        off = u32(data, u32(data, 60) + i * 4)
        _, off = leb(data, off)
        end = data.find(bytes([0]), off)
        strings.append(data[off:end].decode("utf-8", "replace"))
    return {"strings": len(strings), "classes": u32(data,96),
            "methods": u32(data,88),
            "urls": sorted(set(x for x in strings if x.startswith(("https://","http://")) and len(x)<250))}

if __name__ == "__main__":
    with zipfile.ZipFile(sys.argv[1]) as z:
        print(json.dumps({name:scan(z.read(name)) for name in ("classes.dex","classes2.dex","classes3.dex")},indent=2))
