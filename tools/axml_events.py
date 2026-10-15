#!/usr/bin/env python3
"""Decode Android binary XML start tags to structured JSON; stdlib only.

This is a partial structural decoder for investigative use, not a full
resource-resolving Android parser or a replacement for apktool/aapt2.
"""
import json
import struct
import sys
import zipfile

def u16(data, at): return struct.unpack_from("<H", data, at)[0]
def u32(data, at): return struct.unpack_from("<I", data, at)[0]

def utf8_len(data, at):
    n = data[at]; at += 1
    if n & 128:
        n = ((n & 127) << 8) | data[at]; at += 1
    return n, at

def utf16_len(data, at):
    n = u16(data, at); at += 2
    if n & 0x8000:
        n = ((n & 0x7fff) << 16) | u16(data, at); at += 2
    return n, at

def decode_pool(data, base, header_size):
    count = u32(data, base + 8)
    flags = u32(data, base + 16)
    strings_start = u32(data, base + 20)
    result = []
    for i in range(count):
        off = base + strings_start + u32(data, base + header_size + 4 * i)
        if flags & 0x100:
            _, off = utf8_len(data, off)
            size, off = utf8_len(data, off)
            result.append(data[off:off + size].decode("utf-8", "replace"))
        else:
            size, off = utf16_len(data, off)
            result.append(data[off:off + size * 2].decode("utf-16le", "replace"))
    return result

def events_from_binary_xml(data):
    if u16(data, 0) != 0x0003:
        raise ValueError("Not Android binary XML (ResXMLTree)")
    pos = 8
    pool = []
    namespaces = {}
    events = []
    while pos + 8 <= len(data):
        kind, header, size = struct.unpack_from("<HHI", data, pos)
        if size < 8 or pos + size > len(data):
            raise ValueError(f"Damaged XML chunk at {pos}")
        if kind == 0x0001:
            pool = decode_pool(data, pos, header)
        elif kind == 0x0100:
            prefix, ns = u32(data, pos+16), u32(data, pos+20)
            if prefix < len(pool) and ns < len(pool):
                namespaces[pool[ns]] = pool[prefix]
        elif kind == 0x0102:
            lineno = u32(data, pos+8)
            name_idx = u32(data, pos+20)
            name = pool[name_idx] if name_idx < len(pool) else f"?{name_idx}"
            attr_offset = u16(data, pos+24)
            attr_size = u16(data, pos+26)
            count = u16(data, pos+28)
            attrs = {}
            for index in range(count):
                start = pos + 16 + attr_offset + attr_size * index
                ns, key_idx, raw_idx = struct.unpack_from("<III", data, start)
                _, _, dtype, val = struct.unpack_from("<HBBI", data, start+12)
                key = pool[key_idx] if key_idx < len(pool) else f"?{key_idx}"
                if ns < len(pool) and pool[ns] in namespaces:
                    key = namespaces[pool[ns]] + ":" + key
                if raw_idx < len(pool): value = pool[raw_idx]
                elif dtype == 0x03 and val < len(pool): value = pool[val]
                elif dtype == 0x12: value = bool(val)
                elif dtype in (0x10, 0x11): value = val
                elif dtype == 0x01: value = f"@0x{val:08x}"
                else: value = f"type_{dtype:02x}:0x{val:08x}"
                attrs[key] = value
            events.append({"line": lineno, "tag": name, "attributes": attrs})
        pos += size
    return events

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python tools/axml_events.py base.apk AndroidManifest.xml")
    with zipfile.ZipFile(sys.argv[1]) as archive:
        data = archive.read(sys.argv[2])
    print(json.dumps(events_from_binary_xml(data), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
