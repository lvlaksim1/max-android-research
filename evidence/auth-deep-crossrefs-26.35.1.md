# MAX 26.35.1 — перекрёстные ссылки авторизации

Подтверждено контрольной суммой: e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc
Ссылки — адреса в декомпилированном тексте. Статическое упоминание не доказывает выполнение.

## auth use-case references
Файлов с совпадениями (первые 90): 2

### defpackage/j7a.java
~~~text
  19: return new eac(x5Var.d(122), x5Var.d(7));
  20: case 1:
  21: return new d4g(x5Var.d(31), x5Var.d(176), x5Var.d(259));
  22: case 2:
  23: return new wh0(x5Var.d(122), x5Var.d(194));
  24: case 3:
  25: return new ki0(x5Var.d(122), x5Var.d(194));
  26: case 4:
  27: return new ej0(x5Var.d(122), x5Var.d(383), x5Var.d(118));
  28: case 5:
--
  29: return wca.c;
  30: case 6:
--
  31: return new pcd(((Context) x5Var.c(13)).getApplicationContext(), "exoplayer_internal.db", null, 1, (byte) 1);
  32: case 7:
--
~~~

### defpackage/wi.java
~~~text
 500: ki0 ki0Var = (ki0) dq4Var.i.getValue();
 501: String str2 = (String) this.j;
 502: String str3 = dq4Var.e;
 503: this.f = (byte) 1;
 504: obj = ki0Var.a(str2, str3, this);
 505: if (obj != ka5Var) {
 506: }
 507: return ka5Var;
 508: }
 509: if (b == 1) {
--
~~~

## LOGIN constructor call sites
Файлов с совпадениями (первые 90): 1

### defpackage/i7a.java
~~~text
 189: byte[] bArr2 = this.g;
 190: long j = this.k;
 191: zcg zcgVar2 = n3aVar.o;
 192: zm9[] zm9VarArr2 = hog.i0;
 193: return new k7a(str, zA, i3, bArr2, j, jI, str3, ((Number) zcgVar2.s(n3aVar, zm9VarArr2[9])).longValue(), ((Number) n3aVar.K.s(n3aVar, zm9VarArr2[33])).longValue(), dleVarU.b.a().s() ? ((Number) n3aVar.O0.s(n3aVar, n3a.g1[33])).longValue() : 0L, u07Var, ((Boolean) dleVarU.b.j7.a(j9e.w8[427]).i()).booleanValue() ? (String) n3aVar.r.s(n3aVar
 194: }
 195: 
 196: /* JADX WARN: Code duplicated, block: B:8:0x0016  */
 197: /* JADX WARN: Code restructure failed: missing block: B:27:0x0062, code lost:
 198: 
--
~~~

## AUTH request / code verification
Файлов с совпадениями (первые 60): 32

### defpackage/bwj.java
~~~text
  65: }
  66: xnm.y(obj);
  67: zm9[] zm9VarArr = dwj.y;
  68: zsc zscVarE1 = dwjVar.e1();
  69: bqc bqcVar = new bqc((String) null);
  70: this.f = true;
  71: Object objB = zscVarE1.B(bqcVar, this);
  72: return objB == ka5Var ? ka5Var : objB;
  73: case 1:
  74: ja5 ja5Var = (ja5) this.g;
--
 107: }
 108: xnm.y(obj);
 109: zm9[] zm9VarArr2 = dwj.y;
 110: zsc zscVarE2 = dwjVar.e1();
 111: bqc bqcVar2 = new bqc((String) null);
 112: this.f = true;
 113: Object objB2 = zscVarE2.B(bqcVar2, this);
 114: return objB2 == ka5Var ? ka5Var : objB2;
 115: }
 116: }
--
~~~

### defpackage/c2h.java
~~~text
  52: try {
  53: if (i2 == 0) {
  54: xnm.y(objB);
  55: long[] jArr = this.e;
  56: bqc bqcVar = jArr.length == 0 ? new bqc((long[]) null) : new bqc(jArr);
  57: a2h a2hVar = this.a;
  58: if (a2hVar == null) {
  59: a2hVar = null;
  60: }
  61: zsc zscVar = (zsc) a2hVar.w.getValue();
--
~~~

### defpackage/cj0.java
~~~text
 284: bcc bccVar2 = (bcc) ((z6j) ej0Var.b.getValue()).i.get();
 285: byte[] bArrA = v99Var.a(bccVar2 != null ? bccVar2.d : null);
 286: ctc ctcVar = (ctc) ej0Var.a.getValue();
 287: ctcVar.getClass();
 288: objB = ctcVar.a().a.b(new aj0(i7, iNextIndex, str5, bArrA), this);
 289: if (objB != ka5Var) {
 290: }
 291: return ka5Var;
 292: this.f = null;
 293: this.i = null;
--
~~~

### defpackage/d20.java
~~~text
  25: }
  26: 
  27: @Override // defpackage.ft
  28: public final Object n() {
  29: return new bqc(this.f, this.h);
  30: }
  31: }
--
~~~

### defpackage/d77.java
~~~text
 912: Object objI = a77Var2.d;
 913: int i2 = a77Var2.f;
 914: if (i2 == 0) {
 915: xnm.y(objI);
 916: bqc bqcVar = new bqc(0, 50, j, "FAVORITE_STICKERS", (String) null);
 917: zsc zscVar = (zsc) this.f.getValue();
 918: a77Var2.f = 1;
 919: objI = a08.I(zscVar, bqcVar, this.a, 0L, 0, false, null, null, null, a77Var2, 252);
 920: ka5 ka5Var = ka5.a;
 921: if (objI == ka5Var) {
--
~~~

### defpackage/dte.java
~~~text
 715: int iOrdinal = va9Var.ordinal();
 716: ka5 ka5Var = ka5.a;
 717: if (iOrdinal == 0) {
 718: zsc zscVar = (zsc) rp9Var.getValue();
 719: bqc bqcVar = new bqc(tdd.y, (byte) 15);
 720: bqcVar.h("trackId", str);
 721: bqcVar.a("delete", true);
 722: bxjVar.f = 1;
 723: objB = zscVar.B(bqcVar, bxjVar);
 724: } else {
--
~~~

### defpackage/dwj.java
~~~text
  94: xnm.y(objB);
  95: zsc zscVarE1 = e1();
  96: String str2 = this.d;
  97: String string = charSequence.toString();
  98: u6j bqcVar = new bqc(tdd.x, (byte) 14);
  99: bqcVar.h("trackId", str2);
 100: bqcVar.h("password", string);
 101: xvjVar.d = str;
 102: xvjVar.e = null;
 103: xvjVar.h = 1;
--
 426: return s1kVar;
 427: }
 428: xnm.y(n4gVar2);
 429: zsc zscVarE1 = e1();
 430: bqc bqcVar = new bqc();
 431: cwjVar.d = charSequence;
 432: cwjVar.g = 1;
 433: n4gVar2 = zscVarE1.B(bqcVar, cwjVar);
 434: } catch (Throwable th) {
 435: n4gVar = new n4g(th);
--
 459: return s1kVar;
 460: }
 461: zsc zscVarE2 = e1();
 462: String string = charSequence.toString();
 463: bqc bqcVar2 = new bqc(tdd.w, (byte) 10);
 464: bqcVar2.h("trackId", str);
 465: bqcVar2.h("password", string);
 466: cwjVar.d = null;
 467: cwjVar.g = 2;
 468: n4gVar2 = zscVarE2.B(bqcVar2, cwjVar);
--
~~~

### defpackage/ec0.java
~~~text
 295: j3 = p9bVar.b;
 296: str4 = s90VarK.e;
 297: o08 o08Var5 = o08Var3;
 298: ka5Var = ka5Var3;
 299: bqcVar = new bqc(tdd.N3, (byte) 6);
 300: bqcVar.f(j8, "audioId");
 301: if (jA != 0) {
 302: bqcVar.f(jA, "chatId");
 303: }
 304: if (j3 > 0) {
--
 696: j3 = p9bVar.b;
 697: str4 = s90VarK.e;
 698: o08 o08Var6 = o08Var3;
 699: ka5Var = ka5Var3;
 700: bqcVar = new bqc(tdd.N3, (byte) 6);
 701: bqcVar.f(j11, "audioId");
 702: if (jA != 0) {
 703: bqcVar.f(jA, "chatId");
 704: }
 705: if (j3 > 0) {
--
~~~

### defpackage/fwc.java
~~~text
  17: public final Object a(rk2 rk2Var) {
  18: f7j f7jVar = (f7j) this.a.getValue();
  19: String strC = ((dtc) this.c.getValue()).c();
  20: if (strC != null) {
  21: return f7jVar.a.b(new bqc(((hog) ((c74) this.b.getValue())).s(), strC), rk2Var);
  22: }
  23: k3g.t("Required value was null.");
  24: return null;
  25: }
  26: 
--
~~~

### defpackage/gvk.java
~~~text
  57: String strC = ((dtc) this.d.getValue()).c();
  58: if (strC == null) {
  59: objB = null;
  60: } else {
  61: objB = ((f7j) this.c.getValue()).a.b(new bqc(((hog) ((c74) rp9Var.getValue())).s(), strC), fvkVar);
  62: }
  63: ka5 ka5Var = ka5.a;
  64: if (objB == ka5Var) {
  65: return ka5Var;
  66: }
--
~~~

### defpackage/i2j.java
~~~text
 356: }
 357: } else {
 358: wwj wwjVar = (wwj) this.h;
 359: zsc zscVarE1 = wwjVar.e1();
 360: bqc bqcVar = new bqc(wwjVar.f, str, (byte) 21);
 361: this.g = null;
 362: this.f = true;
 363: objB = zscVarE1.B(bqcVar, this);
 364: if (objB == ka5Var5) {
 365: return ka5Var5;
--
 406: try {
 407: if (!z9) {
 408: xnm.y(obj);
 409: zsc zscVar = (zsc) ((rxj) this.h).d.getValue();
 410: bqc bqcVar2 = new bqc();
 411: this.g = null;
 412: this.f = true;
 413: objB2 = zscVar.B(bqcVar2, this);
 414: if (objB2 == ka5Var6) {
 415: return ka5Var6;
--
 450: if (!z10) {
 451: xnm.y(obj);
 452: zm9[] zm9VarArr2 = syj.u;
 453: zsc zscVar2 = (zsc) syjVar.j.getValue();
 454: bqc bqcVar3 = new bqc(syjVar.c, null, (byte) 21);
 455: this.g = null;
 456: this.f = true;
 457: objB3 = zscVar2.B(bqcVar3, this);
 458: if (objB3 == ka5Var7) {
 459: return ka5Var7;
--
~~~

### defpackage/iha.java
~~~text
 538: iufVar3.a = str6;
 539: if (str6.length() == 0) {
 540: try {
 541: zsc zscVarE1 = dwjVar.e1();
 542: bqc bqcVar = new bqc();
 543: this.i = null;
 544: this.h = str;
 545: this.g = iufVar3;
 546: this.f = (byte) 2;
 547: objB = zscVarE1.B(bqcVar, this);
--
 557: xnm.y(objB);
 558: iufVar.a = ((xh0) objB).c;
 559: zm9[] zm9VarArr = dwj.y;
 560: zsc zscVarE2 = dwjVar.e1();
 561: bqc bqcVar2 = new bqc((String) iufVar.a, null, (byte) 21);
 562: this.i = null;
 563: this.h = str2;
 564: this.g = iufVar;
 565: this.f = (byte) 3;
 566: objB2 = zscVarE2.B(bqcVar2, this);
--
 596: iufVar = iufVar3;
 597: str2 = str;
 598: zm9[] zm9VarArr2 = dwj.y;
 599: zsc zscVarE3 = dwjVar.e1();
 600: bqc bqcVar3 = new bqc((String) iufVar.a, null, (byte) 21);
 601: this.i = null;
 602: this.h = str2;
 603: this.g = iufVar;
 604: this.f = (byte) 3;
 605: objB2 = zscVarE3.B(bqcVar3, this);
--
 683: iufVar.a = ((xh0) objB).c;
 684: try {
 685: zm9[] zm9VarArr3 = dwj.y;
 686: zsc zscVarE4 = dwjVar.e1();
 687: bqc bqcVar4 = new bqc((String) iufVar.a, null, (byte) 21);
 688: this.i = null;
 689: this.h = str2;
 690: this.g = iufVar;
 691: this.f = (byte) 3;
 692: objB2 = zscVarE4.B(bqcVar4, this);
--
~~~

### defpackage/j20.java
~~~text
  28: }
  29: 
  30: @Override // defpackage.ft
  31: public final Object n() {
  32: bqc bqcVar = new bqc((tdd) null, (byte) 3);
  33: int i = this.f;
  34: if (i == 0) {
  35: k3g.t("type must not be null");
  36: return null;
  37: }
--
~~~

### defpackage/j61.java
~~~text
  80: byte b = this.f;
  81: long j = this.g;
  82: switch (b) {
  83: case 0:
  84: bqc bqcVar = new bqc(tdd.l3, (byte) 22);
  85: bqcVar.f(j, "botId");
  86: return bqcVar;
  87: default:
  88: return new q68(j, va4.s1((List) this.h));
  89: }
--
~~~

### defpackage/ki0.java
~~~text
  32: xnm.y(objB);
  33: ctc ctcVar = (ctc) this.a.getValue();
  34: ji0Var.g = 1;
  35: f7j f7jVarA = ctcVar.a();
  36: bqc bqcVar = new bqc(tdd.m, (byte) 11);
  37: if (str2 == null \|\| str2.length() == 0) {
  38: k3g.t("AuthCmd param 'token' can't be null");
  39: return null;
  40: }
  41: bqcVar.h("token", str2);
--
~~~

### defpackage/l20.java
~~~text
  31: }
  32: 
  33: @Override // defpackage.ft
  34: public final Object n() {
  35: bqc bqcVar = new bqc((tdd) null, (byte) 4);
  36: int i = this.f;
  37: if (i == 0) {
  38: k3g.t("type must not be null");
  39: return null;
  40: }
--
~~~

### defpackage/lyj.java
~~~text
  58: if (!z) {
  59: xnm.y(obj);
  60: zm9[] zm9VarArr = myj.o;
  61: zsc zscVar = (zsc) myjVar.e.getValue();
  62: bqc bqcVar = new bqc(12, myjVar.c, (String) null, (String) null, Collections.singletonList(ovj.g));
  63: this.g = null;
  64: this.f = true;
  65: obj = zscVar.B(bqcVar, this);
  66: if (obj == ka5Var) {
  67: return ka5Var;
--
 101: }
 102: xnm.y(obj);
 103: zm9[] zm9VarArr2 = myj.o;
 104: zsc zscVar2 = (zsc) myjVar.e.getValue();
 105: bqc bqcVar2 = new bqc(myjVar.c);
 106: this.f = true;
 107: Object objB = zscVar2.B(bqcVar2, this);
 108: return objB == ka5Var ? ka5Var : objB;
 109: }
 110: }
--
~~~

### defpackage/lz8.java
~~~text
 569: }
 570: }
 571: }
 572: zsc zscVarE1 = wwjVar.e1();
 573: bqc bqcVar = new bqc(16, wwjVar.f, str2, ya9Var.b, fy9VarD);
 574: this.j = null;
 575: this.h = mdjVar;
 576: this.f = true;
 577: objB = zscVarE1.B(bqcVar, this);
 578: ka5 ka5Var = ka5.a;
--
 634: if (idjVar == null && mdjVar == null) {
 635: vv6Var.e(new fxj(true));
 636: zsc zscVarE1 = wwjVar.e1();
 637: String string = charSequence.toString();
 638: bqc bqcVar = new bqc(tdd.A, (byte) 20);
 639: bqcVar.h("trackId", str);
 640: bqcVar.h("password", string);
 641: this.j = null;
 642: this.f = true;
 643: objB = zscVarE1.B(bqcVar, this);
--
~~~

### defpackage/m24.java
~~~text
  34: try {
  35: if (i2 == 0) {
  36: xnm.y(objI);
  37: zsc zscVar = (zsc) this.a.getValue();
  38: bqc bqcVar = new bqc(tdd.E1, (byte) 27);
  39: String str = this.b;
  40: l24Var2.f = 1;
  41: objI = a08.I(zscVar, bqcVar, str, 0L, 0, false, null, null, null, l24Var2, 252);
  42: ka5 ka5Var = ka5.a;
  43: if (objI == ka5Var) {
--
~~~

### defpackage/mbc.java
~~~text
 706: }
 707: try {
 708: zsc zscVar = this.a;
 709: String str2 = this.g;
 710: bqc bqcVar = new bqc(jM);
 711: gbcVar2.e = null;
 712: gbcVar2.d = jM;
 713: gbcVar2.h = 1;
 714: j = jM;
 715: i2 = 2;
--
~~~

### defpackage/mwe.java
~~~text
 314: throw new IllegalArgumentException("Required value was null.");
 315: }
 316: zm9[] zm9VarArr = wwj.G;
 317: zsc zscVarE1 = wwjVar.e1();
 318: bqc bqcVar = new bqc(16, wwjVar.f, str2, ya9Var.b, fy9VarD);
 319: this.g = null;
 320: this.f = true;
 321: obj = zscVarE1.B(bqcVar, this);
 322: ka5 ka5Var = ka5.a;
 323: if (obj == ka5Var) {
--
~~~

### defpackage/n20.java
~~~text
  25: }
  26: 
  27: @Override // defpackage.ft
  28: public final Object n() {
  29: return new bqc(this.f, this.h);
  30: }
  31: 
  32: @Override // defpackage.ru0
  33: public final void x(x6j x6jVar) {
  34: o20 o20Var = (o20) x6jVar;
--
~~~

### defpackage/n73.java
~~~text
 169: @Override // defpackage.ft
 170: public final Object n() {
 171: switch (this.f) {
 172: case 0:
 173: bqc bqcVar = new bqc((tdd) null, (byte) 29);
 174: bqcVar.f(this.h, "chatId");
 175: bqcVar.f(this.i, "lastEventTime");
 176: bqcVar.a("forAll", this.j);
 177: return bqcVar;
 178: default:
--
~~~

### defpackage/p24.java
~~~text
  35: xnm.y(obj);
  36: p3d p3dVar = (p3d) this.a.getValue();
  37: o24Var.f = 1;
  38: f7j f7jVar = (f7j) p3dVar.a.getValue();
  39: bqc bqcVar = new bqc(tdd.w1, (byte) 28);
  40: bqcVar.h("link", str);
  41: bqcVar.h("linkType", uw9Var.name());
  42: Object objB = f7jVar.a.b(bqcVar, o24Var);
  43: ka5 ka5Var = ka5.a;
  44: if (objB == ka5Var) {
--
~~~

### defpackage/s8i.java
~~~text
 121: zsc zscVar = (zsc) this.b.getValue();
 122: j2 = j;
 123: i2 = i;
 124: try {
 125: bqc bqcVar = new bqc(2, i2 == true ? 1 : 0, j2, (String) null, str);
 126: q8iVar.d = null;
 127: j2 = j;
 128: try {
 129: q8iVar.e = j2;
 130: int i5 = i;
--
 198: try {
 199: if (i3 == 0) {
 200: xnm.y(objB);
 201: zsc zscVar = (zsc) this.b.getValue();
 202: bqc bqcVar = new bqc(3, i, j, (String) null, str);
 203: r8iVar.f = 1;
 204: objB = zscVar.B(bqcVar, r8iVar);
 205: ka5 ka5Var = ka5.a;
 206: if (objB == ka5Var) {
 207: return ka5Var;
--
~~~

### defpackage/sa2.java
~~~text
  78: tdd tddVar = null;
  79: Object obj = this.g;
  80: switch (b) {
  81: case 0:
  82: bqc bqcVar = new bqc(tddVar, b2);
  83: bqcVar.h("conversationId", (String) obj);
  84: return bqcVar;
  85: case 1:
  86: List list = (List) obj;
  87: q68 q68Var = new q68(tddVar, b2);
--
~~~

### defpackage/uwj.java
~~~text
  84: wwj wwjVar2 = this.i;
  85: CharSequence charSequence = this.j;
  86: try {
  87: zsc zscVarE1 = wwjVar2.e1();
  88: bqc bqcVar = new bqc(wwjVar2.f, charSequence.toString(), (byte) 21);
  89: this.h = null;
  90: this.f = ya9Var;
  91: this.g = true;
  92: objB = zscVarE1.B(bqcVar, this);
  93: if (objB == ka5Var) {
--
 189: try {
 190: zsc zscVarE2 = wwjVar7.e1();
 191: String str3 = wwjVar7.f;
 192: String string = charSequence4.toString();
 193: bqc bqcVar2 = new bqc(tdd.B, (byte) 19);
 194: bqcVar2.h("trackId", str3);
 195: bqcVar2.h("hint", string);
 196: this.h = null;
 197: this.f = ya9Var3;
 198: this.g = true;
--
~~~

### defpackage/w1j.java
~~~text
1024: int i2 = u1jVar2.f;
1025: if (i2 == 0) {
1026: xnm.y(objI);
1027: zsc zscVar = (zsc) this.e.getValue();
1028: bqc bqcVar = new bqc(0, 50, j, "FAVORITE_STICKER_SETS", (String) null);
1029: u1jVar2.f = 1;
1030: objI = a08.I(zscVar, bqcVar, this.j, 0L, 1, false, null, null, null, u1jVar2, 244);
1031: ka5 ka5Var = ka5.a;
1032: if (objI == ka5Var) {
1033: return ka5Var;
--
~~~

### defpackage/wh0.java
~~~text
  36: Long l = mvfVar.e;
  37: int i3 = l != null ? 1 : 0;
  38: vh0Var.g = 1;
  39: ctcVar.getClass();
  40: bqc bqcVar = new bqc(tdd.u, (byte) 12);
  41: if (str == null \|\| str.length() == 0) {
  42: k3g.t("AuthConfirmCmd param 'token' can't be null");
  43: return null;
  44: }
  45: bqcVar.h("token", str);
--
~~~

### defpackage/y30.java
~~~text
 311: vp5 vp5Var = (vp5) this.g;
 312: String str = (String) this.h;
 313: py2 py2Var = vp5.J1;
 314: zsc zscVar = (zsc) vp5Var.H.getValue();
 315: bqc bqcVar = new bqc(tdd.y2, (byte) 23);
 316: bqcVar.h("conversationId", str);
 317: this.f = true;
 318: n4gVar = zscVar.B(bqcVar, this);
 319: if (n4gVar == ka5Var) {
 320: return ka5Var;
--
~~~

### defpackage/yr0.java
~~~text
 811: xnm.y(obj);
 812: String str = (String) this.k;
 813: zm9[] zm9VarArr = wwj.G;
 814: zsc zscVarE1 = wwjVar.e1();
 815: bqc bqcVar = new bqc(wwjVar.f, str, (byte) 9);
 816: this.i = null;
 817: this.g = null;
 818: this.f = (byte) 1;
 819: obj = zscVarE1.B(bqcVar, this);
 820: if (obj == ka5Var) {
--
 879: xnm.y(obj);
 880: String str2 = (String) this.k;
 881: zm9[] zm9VarArr = syj.u;
 882: zsc zscVar = (zsc) syjVar.j.getValue();
 883: bqc bqcVar = new bqc(str, str2, (byte) 9);
 884: this.i = null;
 885: this.g = null;
 886: this.f = (byte) 1;
 887: objB = zscVar.B(bqcVar, this);
 888: if (objB == ka5Var) {
--
~~~

### defpackage/zi0.java
~~~text
  37: try {
  38: if (i2 == 0) {
  39: xnm.y(objB);
  40: zsc zscVar = (zsc) this.a.getValue();
  41: bqc bqcVar = new bqc(tdd.H3, (byte) 17);
  42: bqcVar.h("qrLink", str);
  43: yi0Var.f = 1;
  44: objB = zscVar.B(bqcVar, yi0Var);
  45: if (objB == ka5Var) {
  46: return ka5Var;
--
~~~

## auth response parser
Файлов с совпадениями (первые 60): 17

### defpackage/acc.java
~~~text
 232: f09.p(this.b.a, "Skipping " + fldVar.b.a.getClass().getName() + " because session not initialized");
 233: }
 234: } else {
 235: f09.F(this.b.a, vg9.y("Removing ", fldVar.b.a.getClass().getName(), " because it has wrong connection number"), new Object[0]);
 236: fldVar.b.c.f(new l6j("session.sequence", "Task has wrong connection number", null));
 237: arrayList.add(fldVar);
 238: }
 239: } else if (i == 2 && (cldVar = fldVar.d) != null) {
 240: try {
 241: try {
--
~~~

### defpackage/aj0.java
~~~text
   9: super(tdd.l);
  10: this.c = i2;
  11: h("phone", str);
  12: if (i == 1) {
  13: str2 = "START_AUTH";
  14: } else {
  15: if (i != 2) {
  16: throw null;
  17: }
  18: str2 = "RESEND";
--
~~~

### defpackage/bqc.java
~~~text
 133: }
 134: break;
 135: default:
 136: h("trackId", str);
 137: h("verifyCode", str2);
 138: break;
 139: }
 140: }
 141: 
 142: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
--
~~~

### defpackage/cp5.java
~~~text
 912: switch (str) {
 913: case "mt_instanceid":
 914: case "lastName":
 915: case "trackId":
 916: case "verifyCode":
 917: case "pushToken":
 918: case "aId":
 919: case "text":
 920: case "email":
 921: case "phone":
--
~~~

### defpackage/cxd.java
~~~text
  23: break;
  24: case "token":
  25: this.c = e0c.r0(bebVar);
  26: break;
  27: case "tokenType":
  28: this.f = exd.n(e0c.r0(bebVar));
  29: break;
  30: default:
  31: bebVar.N();
  32: break;
--
  40: Long l = this.e;
  41: String strJ = exd.j(this.f);
  42: StringBuilder sbS = pq0.s("{token='", str, "', profile=", strValueOf, ", phone=");
  43: sbS.append(l);
  44: sbS.append(", tokenType=");
  45: sbS.append(strJ);
  46: sbS.append("}");
  47: return sbS.toString();
  48: }
  49: }
--
~~~

### defpackage/d8a.java
~~~text
  36: n3aVar.q0.z(n3aVar, n3a.g1[6], l6jVar.b);
  37: ((dtc) this.c.getValue()).d(true, false);
  38: return;
  39: }
  40: if ("session.sequence".equals(l6jVar.b)) {
  41: o1d o1dVar3 = f09.g;
  42: if (o1dVar3 != null && o1dVar3.b(c6aVar)) {
  43: o1dVar3.c(c6aVar, "d8a", "onLoginFail_" + i + ": skip " + l6jVar, null);
  44: return;
  45: }
--
~~~

### defpackage/dj0.java
~~~text
  20: public final Object w(Object obj) {
  21: Throwable th = this.e;
  22: long j = this.f;
  23: xnm.y(obj);
  24: return Boolean.valueOf((th instanceof TamErrorException) && g4a.c(((TamErrorException) th).a.b, "session.sequence") && j < 3);
  25: }
  26: }
--
~~~

### defpackage/dxd.java
~~~text
  30: break;
  31: case "token":
  32: this.c = e0c.r0(bebVar);
  33: break;
  34: case "tokenType":
  35: this.h = exd.n(e0c.r0(bebVar));
  36: break;
  37: case "retries":
  38: this.d = e0c.m0(bebVar, 0);
  39: break;
--
  80: } else {
  81: str = "CALL_DELAY";
  82: }
  83: StringBuilder sbA = vg9.A(i, "{token='", strN, "', retries=", ", codeDelay=");
  84: s95.z(i2, i3, ", codeLength=", ", tokenType=", sbA);
  85: w7g.C(sbA, strJ, ", callDelay=", i4, ", requestType=");
  86: return w7g.w(sbA, str, "}");
  87: }
  88: }
--
~~~

### defpackage/exd.java
~~~text
 223: }
 224: if (str.equals("PHONE_CONFIRM")) {
 225: return 4;
 226: }
 227: k3g.t("No enum constant ru.ok.tamtam.api.commands.base.PhoneBindTokenType.".concat(str));
 228: return 0;
 229: }
 230: }
--
~~~

### defpackage/fi0.java
~~~text
  28: }
  29: 
  30: @Override // defpackage.mv0
  31: public final String toString() {
  32: return "Response(profile=" + this.d + ", tokenTypes='" + f09.O(this.c) + "')";
  33: }
  34: }
--
~~~

### defpackage/g7a.java
~~~text
 428: } catch (Throwable th) {
 429: if (th instanceof TamErrorException) {
 430: TamErrorException tamErrorException = th;
 431: String str3 = tamErrorException.a.b;
 432: if (g4a.c(str3, "session.sequence")) {
 433: f09.d0(this.j, "login2_error: SESSION_SEQUENCE", new Object[0]);
 434: } else if (g4a.c(str3, "client.task.ignored")) {
 435: f09.d0(this.j, "login2_error: TASK_IGNORED", new Object[0]);
 436: } else {
 437: ((d8a) this.g.getValue()).a(tamErrorException.a, 2);
--
~~~

### defpackage/hi0.java
~~~text
  28: }
  29: 
  30: @Override // defpackage.mv0
  31: public final String toString() {
  32: return "Response(profile=" + this.d + ", tokenTypes='" + f09.O(this.c) + "')";
  33: }
  34: }
--
~~~

### defpackage/ki0.java
~~~text
  39: return null;
  40: }
  41: bqcVar.h("token", str2);
  42: if (str == null \|\| str.length() == 0) {
  43: k3g.t("AuthCmd param 'verifyCode' can't be null when param 'authTokenType' is 'PHONE' or 'PHONE_CONFIRM'");
  44: return null;
  45: }
  46: bqcVar.h("verifyCode", str);
  47: bqcVar.h("authTokenType", "CHECK_CODE");
  48: objB = f7jVarA.a.b(bqcVar, ji0Var);
--
  49: if (objB != ka5Var) {
  50: }
  51: return ka5Var;
--
  52: }
--
~~~

### defpackage/tdd.java
~~~text
  66: public static final tdd q = new tdd("PROMOTED_CONTENT_CALLBACK", 11, 10, fj0.f);
  67: public static final tdd r = new tdd("LOGOUT", 12, 20);
  68: public static final tdd s = new tdd("SYNC", 13, 21);
  69: public static final tdd t = new tdd("CONFIG", 14, 22, qzd.e);
  70: public static final tdd u = new tdd("AUTH_CONFIRM", 15, 23);
  71: public static final tdd v = new tdd("AUTH_CREATE_TRACK", 16, 112, r74.b);
  72: public static final tdd w = new tdd("AUTH_CHECK_PASSWORD", 17, 113, lrh.d);
  73: public static final tdd x = new tdd("AUTH_LOGIN_CHECK_PASSWORD", 18, 115, cp5.c);
  74: public static final tdd y = new tdd("AUTH_LOGIN_PROFILE_DELETE", 19, 116, cg6.b);
  75: public static final tdd z = new tdd("AUTH_LOGIN_RESTORE_PASSWORD", 20, 101, bwb.b);
--
~~~

### defpackage/th0.java
~~~text
 333: }
 334: 
 335: @Override // defpackage.mv0
 336: public final String toString() {
 337: return "{profile=" + this.f + ",tokenTypes=" + f09.O(this.c) + ",passwordChallenge=" + this.e + ",}";
 338: }
 339: }
--
~~~

### defpackage/uh0.java
~~~text
  91: } else {
  92: bebVar.N();
  93: }
  94: } else if (iHashCode != 110541305) {
  95: if (iHashCode == 141498579 && strR0.equals("tokenType")) {
  96: try {
  97: strS0 = e0c.s0(bebVar, null);
  98: } catch (Throwable th5) {
  99: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
 100: Iterator it3 = q1h.a.iterator();
--
 138: w8aVar3 = w8aVar2;
 139: i = 1;
 140: break;
 141: default:
 142: k3g.t(vg9.y("No such value ", strS0, " for LoginTokenType"));
 143: return null;
 144: }
 145: }
 146: i = 1;
 147: bebVar.N();
--
~~~

### defpackage/wh0.java
~~~text
  42: k3g.t("AuthConfirmCmd param 'token' can't be null");
  43: return null;
  44: }
  45: bqcVar.h("token", str);
  46: bqcVar.h("tokenType", "REGISTER");
  47: if (str2 == null \|\| str2.length() == 0) {
  48: k3g.t("AuthConfirmCmd param 'firstName' can't be null");
  49: return null;
  50: }
  51: bqcVar.h("firstName", str2);
--
~~~

## token lifecycle
Файлов с совпадениями (первые 60): 33

### com/google/android/gms/auth/api/signin/GoogleSignInOptions.java
~~~text
 100: for (int i = 0; i < length; i++) {
 101: hashSet.add(new Scope(1, jSONArray.getString(i)));
 102: }
 103: String strOptString = jSONObject.has("accountName") ? jSONObject.optString("accountName") : null;
 104: return new GoogleSignInOptions(3, new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), jSONObject.has("serverClientId") ? jSONObject.optString("se
 105: }
 106: 
 107: public static HashMap c(ArrayList arrayList) {
 108: HashMap map = new HashMap();
 109: if (arrayList != null) {
--
~~~

### com/vk/push/core/auth/AuthTokenResult.java
~~~text
   6: import defpackage.mj0;
   7: import kotlin.Metadata;
   8: 
   9: /* JADX INFO: loaded from: classes2.dex */
  10: @Metadata(d1 = {"\u0000\f\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0087\b\u0018\u0000 \u00022\u00020\u0001:\u0001\u0003¨\u0006\u0004"}, d2 = {"Lcom/vk/push/core/auth/AuthTokenResult;", "Landroid/os/Parcelable;", "CREATOR", "mj0", "core_release"}, k = 1, mv = {1, 7, 1}, xi = 48)
  11: public final /* data */ class AuthTokenResult implements Parcelable {
  12: public static final mj0 CREATOR = new mj0();
  13: public final String a;
  14: 
  15: public AuthTokenResult(String str) {
--
  16: this.a = str;
--
  17: }
  18: 
  19: @Override // android.os.Parcelable
  20: public final int describeContents() {
--
  24: public final boolean equals(Object obj) {
  25: if (this == obj) {
  26: return true;
  27: }
  28: return (obj instanceof AuthTokenResult) && this.a.equals(((AuthTokenResult) obj).a);
  29: }
  30: 
  31: public final int hashCode() {
  32: return this.a.hashCode();
  33: }
--
  34: 
  35: public final String toString() {
  36: return a15.q(new StringBuilder("AuthTokenResult(token="), this.a, ')');
  37: }
  38: 
  39: @Override // android.os.Parcelable
  40: public final void writeToParcel(Parcel parcel, int i) {
  41: parcel.writeString(this.a);
--
~~~

### defpackage/b28.java
~~~text
 217: arrayList2.clear();
 218: }
 219: dma dmaVar = (dma) zo5Var.b;
 220: dmaVar.getClass();
 221: dmaVar.setSessionToken(wwaVar.b);
 222: return;
 223: case 13:
 224: MediaTypePickerWidget mediaTypePickerWidget = (MediaTypePickerWidget) this.b;
 225: List list = (List) this.c;
 226: if (mediaTypePickerWidget.getView() != null) {
--
~~~

### defpackage/dwj.java
~~~text
 130: obj = n4gVar;
 131: if (!(obj instanceof n4g)) {
 132: fi0 fi0Var = (fi0) obj;
 133: if (!fi0Var.c.containsKey("LOGIN")) {
 134: f09.d0(this.f, "Can't auth with password because loginToken empty", new Object[0]);
 135: this.u = null;
 136: this.r.e(new exj(0, 6, dnm.e(null)));
 137: return s1kVar;
 138: }
 139: xvjVar.d = null;
--
~~~

### defpackage/gn0.java
~~~text
 113: } else {
 114: str = "REGISTERED";
 115: }
 116: sb.append(str);
 117: sb.append(", authToken=");
 118: sb.append(this.c);
 119: sb.append(", refreshToken=");
 120: sb.append(this.d);
 121: sb.append(", expiresInSecs=");
 122: sb.append(this.e);
--
 123: sb.append(", tokenCreationEpochInSecs=");
 124: sb.append(this.f);
--
~~~

### defpackage/hb3.java
~~~text
  13: 
  14: public static void a(hb3 hb3Var, long j, long j2, long j3, long j4, dx5 dx5Var) {
  15: String str = hb3Var.c;
  16: StringBuilder sbS = s95.s(j, "from: chatId = ", ", time = ", qo9.C(Long.valueOf(j3)));
  17: sbS.append(", chatAccessToken=true");
  18: f09.p(str, sbS.toString());
  19: f7j.b((f7j) hb3Var.b.getValue(), new db3(((hog) ((c74) hb3Var.a.getValue())).g(), j, j2, j3, j4, false, 0L, dx5Var, 7552));
  20: }
  21: 
  22: public static long b(hb3 hb3Var, long j, long j2, long j3, long j4, long j5, dx5 dx5Var, boolean z) {
--
  25: String strC2 = qo9.C(Long.valueOf(j4));
  26: StringBuilder sbS = s95.s(j, "from-to: chatId = ", ", time = ", strC);
  27: sbS.append(", backwardTime = ");
  28: sbS.append(strC2);
  29: sbS.append(", chatAccessToken=true");
  30: f09.p(str, sbS.toString());
  31: return f7j.b((f7j) hb3Var.b.getValue(), new db3(((hog) ((c74) hb3Var.a.getValue())).g(), j, j2, j3, j5, z, j4, dx5Var, 6400));
  32: }
  33: 
  34: public static void c(hb3 hb3Var, long j, long j2, long j3, long j4, long j5, dx5 dx5Var) {
--
  37: String strC2 = qo9.C(Long.valueOf(j4));
  38: StringBuilder sbS = s95.s(j, "to: chatId = ", ", time = ", strC);
  39: sbS.append(", backwardTime = ");
  40: sbS.append(strC2);
  41: sbS.append(", chatAccessToken=true");
  42: f09.p(str, sbS.toString());
  43: f7j.b((f7j) hb3Var.b.getValue(), new db3(((hog) ((c74) hb3Var.a.getValue())).g(), j, j2, j3, j5, false, j4, dx5Var, 6528));
  44: }
  45: }
--
~~~

### defpackage/hg7.java
~~~text
 116: if (strNextName.equals("name")) {
 117: strNextString = jsonReader.nextString();
 118: } else if (strNextName.equals("fid")) {
 119: strNextString2 = jsonReader.nextString();
 120: } else if (strNextName.equals("refreshToken")) {
 121: strNextString3 = jsonReader.nextString();
 122: } else if (strNextName.equals("authToken")) {
 123: jsonReader.beginObject();
 124: while (jsonReader.hasNext()) {
 125: String strNextName2 = jsonReader.nextName();
--
 126: if (strNextName2.equals("token")) {
 127: jy7VarA.c = jsonReader.nextString();
--
~~~

### defpackage/hog.java
~~~text
   7: import me.leolin.shortcutbadger.BuildConfig;
   8: 
   9: /* JADX INFO: loaded from: classes.dex */
  10: public abstract class hog extends a4 implements c74 {
  11: public static final /* synthetic */ zm9[] i0 = {new c4c(hog.class, "_userId", "get_userId()J"), a15.f(luf.a, hog.class, "contactsLastSync", "getContactsLastSync()J"), new c4c(hog.class, "currentProxyList", "getCurrentProxyList()Ljava/lang/String;"), new c4c(hog.class, "currentProxyListTtlInSec", "getCurrentProxyListTtlInSec()I"), new c4c(
  12: public final zcg A;
  13: public final zcg B;
  14: public final zcg C;
  15: public final zcg D;
  16: public final zcg E;
--
~~~

### defpackage/jg7.java
~~~text
 124: ui1 ui1Var = hg7Var.c;
 125: if (!ui1Var.f()) {
 126: throw new FirebaseInstallationsException("Firebase Installations Service is unavailable. Please try again later.");
 127: }
 128: URL urlA = hg7.a("projects/" + str3 + "/installations/" + str2 + "/authTokens:generate");
 129: int i = 0;
 130: while (true) {
 131: if (i > 1) {
 132: throw new FirebaseInstallationsException("Firebase Installations Service is unavailable. Please try again later.");
 133: }
--
~~~

### defpackage/jj0.java
~~~text
  17: byte b = this.b;
  18: u6a u6aVar = this.c;
  19: switch (b) {
  20: case 0:
  21: return u6aVar.f("AuthTokenIPC");
  22: case 1:
  23: return u6aVar.f("PushesIPC");
  24: default:
  25: return u6aVar.f("Notifier");
  26: }
--
~~~

### defpackage/k27.java
~~~text
   1: package defpackage;
   2: 
   3: import com.vk.push.core.auth.Auth;
   4: import com.vk.push.core.auth.AuthTokenResult;
   5: import com.vk.push.core.auth.AuthorizedResult;
   6: import com.vk.push.core.base.AidlResult;
   7: import com.vk.push.core.base.AsyncCallback;
   8: import com.vk.push.core.hostinfo.MasterElections;
   9: import com.vk.push.core.masterhost.MasterHost;
--
 174: case 19:
 175: ((Auth) obj).A((AsyncCallback) obj2);
 176: return s1kVar;
 177: case 20:
 178: return new p4g(((AuthTokenResult) ((AidlResult) obj).a).a);
 179: case 21:
 180: return new p4g(new d0m((RegisterForPushesResult) ((AidlResult) obj).a, (yw) obj2));
 181: case 22:
 182: ((Auth) obj).z((AsyncCallback) obj2);
 183: return s1kVar;
--
~~~

### defpackage/ki0.java
~~~text
  39: return null;
  40: }
  41: bqcVar.h("token", str2);
  42: if (str == null \|\| str.length() == 0) {
  43: k3g.t("AuthCmd param 'verifyCode' can't be null when param 'authTokenType' is 'PHONE' or 'PHONE_CONFIRM'");
  44: return null;
  45: }
  46: bqcVar.h("verifyCode", str);
  47: bqcVar.h("authTokenType", "CHECK_CODE");
  48: objB = f7jVarA.a.b(bqcVar, ji0Var);
--
  49: if (objB != ka5Var) {
  50: }
  51: return ka5Var;
  52: }
--
~~~

### defpackage/kj0.java
~~~text
   1: package defpackage;
   2: 
   3: import com.vk.push.core.auth.AuthTokenResult;
   4: 
   5: /* JADX INFO: loaded from: classes2.dex */
   6: public final class kj0 {
   7: public final g68 a;
   8: public final d68 b;
--
 119: obj = ((p4g) objB).a;
 120: }
 121: kj0Var.f.a(new x1g(kj0Var.g.a("request_intermediate_token"), obj, ywVar.a, yh0Var.a));
 122: xnm.y(obj);
 123: return new AuthTokenResult(((ba9) obj).a);
 124: yh0 yh0Var2 = (yh0) objB;
 125: String str2 = yh0Var2.b;
 126: String str3 = yh0Var2.a;
 127: if (zti.n0(str2)) {
 128: k3g.o("Auth token is blank");
--
 147: kj0Var = this;
 148: yh0Var = yh0Var2;
 149: kj0Var.f.a(new x1g(kj0Var.g.a("request_intermediate_token"), obj, ywVar.a, yh0Var.a));
 150: xnm.y(obj);
 151: return new AuthTokenResult(((ba9) obj).a);
 152: }
 153: return ka5Var;
 154: }
 155: 
 156: public final void c() {
--
~~~

### defpackage/l6h.java
~~~text
  44: if (a(packageManager, "androidx.media3.session.MediaSessionService", componentName)) {
  45: i3 = 1;
  46: } else {
  47: if (!a(packageManager, "android.media.browse.MediaBrowserService", componentName)) {
  48: kw7.k(componentName, ". Manifest doesn't declare one of either MediaSessionService, MediaLibraryService, MediaBrowserService or MediaBrowserServiceCompat. Use service's full name.", "Failed to resolve SessionToken for ");
  49: throw null;
  50: }
  51: i2 = 101;
  52: }
  53: if (i2 != 101) {
--
~~~

### defpackage/lbj.java
~~~text
   4: import android.os.IBinder;
   5: import android.os.Parcel;
   6: import android.os.RemoteException;
   7: import com.vk.push.common.exception.SdkIsNotInitializedException;
   8: import com.vk.push.core.auth.AuthTokenResult;
   9: import com.vk.push.core.base.AidlResult;
  10: import com.vk.push.core.base.AsyncCallback;
  11: import com.vk.push.core.test.TestPushPayload;
  12: import com.vk.push.core.test.TestPushProvider;
  13: import java.util.UUID;
--
  69: if (asyncCallbackC2 != null) {
  70: c().d("receive IPC getIntermediateToken", null);
  71: ((lzg) this.h.getValue()).getClass();
  72: try {
  73: asyncCallbackC2.Y(new AidlResult(new AuthTokenResult(UUID.randomUUID().toString())));
  74: } catch (RemoteException e) {
  75: c().e("Test get intermediate token has failed", e);
  76: }
  77: }
  78: } else if (asyncCallbackC2 != null) {
--
~~~

### defpackage/li0.java
~~~text
  33: return this.a.hashCode();
  34: }
  35: 
  36: public final String toString() {
  37: return "AuthTokenData(appToToken=" + this.a + ')';
  38: }
  39: }
--
~~~

### defpackage/m6h.java
~~~text
 138: return this.j;
 139: }
 140: 
 141: public final String toString() {
 142: return "SessionToken {pkg=" + this.e + " type=" + this.b + " libraryVersion=" + this.c + " interfaceVersion=" + this.d + " service=" + this.f + " IMediaSession=" + this.h + " extras=" + this.i + "}";
 143: }
 144: }
--
~~~

### defpackage/mj0.java
~~~text
   1: package defpackage;
   2: 
   3: import android.os.Parcel;
   4: import android.os.Parcelable;
   5: import com.vk.push.core.auth.AuthTokenResult;
   6: import me.leolin.shortcutbadger.BuildConfig;
   7: 
   8: /* JADX INFO: loaded from: classes2.dex */
   9: public final class mj0 implements Parcelable.Creator {
  10: @Override // android.os.Parcelable.Creator
--
  12: String string = parcel.readString();
  13: if (string == null) {
  14: string = BuildConfig.FLAVOR;
  15: }
  16: return new AuthTokenResult(string);
  17: }
  18: 
  19: @Override // android.os.Parcelable.Creator
  20: public final Object[] newArray(int i) {
  21: return new AuthTokenResult[i];
--
  22: }
  23: }
--
~~~

### defpackage/n6h.java
~~~text
 111: return null;
 112: }
 113: 
 114: public final String toString() {
 115: return pq0.h(this.a, "}", new StringBuilder("SessionToken {legacy, uid="));
 116: }
 117: }
--
~~~

### defpackage/ojm.java
~~~text
  27: bundle.putBoolean("com.google.android.gms.signin.internal.offlineAccessRequested", false);
  28: bundle.putBoolean("com.google.android.gms.signin.internal.idTokenRequested", false);
  29: bundle.putString("com.google.android.gms.signin.internal.serverClientId", null);
  30: bundle.putBoolean("com.google.android.gms.signin.internal.usePromptModeForAuthCode", true);
  31: bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);
  32: bundle.putString("com.google.android.gms.signin.internal.hostedDomain", null);
  33: bundle.putString("com.google.android.gms.signin.internal.logSessionId", null);
  34: bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);
  35: return new onh(context, looper, nt4Var, bundle, xa8Var, ya8Var);
  36: case 1:
--
  37: throw s95.i(obj);
  38: case 2:
  39: case 4:
--
~~~

### defpackage/p73.java
~~~text
 508: f(j4, "backwardTime");
 509: a("getChat", false);
 510: a("getMessages", true);
 511: if (str != null && str.length() != 0) {
 512: h("chatAccessToken", str);
 513: }
 514: h("itemType", dx5Var.name());
 515: a("interactive", z);
 516: }
 517: }
--
~~~

### defpackage/qzb.java
~~~text
  13: @Override // defpackage.x6j
  14: public final void c(beb bebVar, String str) {
  15: str.getClass();
  16: switch (str) {
  17: case "chatAccessToken":
  18: this.e = e0c.r0(bebVar);
  19: break;
  20: case "chat":
  21: this.d = r53.c(bebVar);
  22: break;
--
~~~

### defpackage/sk2.java
~~~text
  11: public final rp9 d;
  12: public final z9g e = c45.Q();
  13: 
  14: static {
  15: c4c c4cVar = new c4c(sk2.class, "tokenRefreshJob", "getTokenRefreshJob()Lkotlinx/coroutines/Job;");
  16: luf.a.getClass();
  17: f = new zm9[]{c4cVar};
  18: }
  19: 
  20: public sk2(yi2 yi2Var, rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3) {
--
~~~

### defpackage/sm0.java
~~~text
  86: StringBuilder sb = new StringBuilder("InstallationResponse{uri=");
  87: sb.append(this.a);
  88: sb.append(", fid=");
  89: sb.append(this.b);
  90: sb.append(", refreshToken=");
  91: sb.append(this.c);
  92: sb.append(", authToken=");
  93: sb.append(this.d);
  94: sb.append(", responseCode=");
  95: int i = this.e;
--
  96: if (i != 1) {
  97: str = i != 2 ? "null" : "BAD_CONFIG";
--
~~~

### defpackage/swa.java
~~~text
  26: MediaSession mediaSessionA = a(context, bundle, str);
  27: this.a = mediaSessionA;
  28: rwa rwaVar = new rwa(this);
  29: this.b = rwaVar;
  30: this.c = new wwa(mediaSessionA.getSessionToken(), rwaVar);
  31: this.e = bundle;
  32: mediaSessionA.setFlags(3);
  33: }
  34: 
  35: public MediaSession a(Context context, Bundle bundle, String str) {
--
~~~

### defpackage/ug9.java
~~~text
  70: try {
  71: if (i5 == 0) {
  72: xnm.y(n4gVar);
  73: if (str4 == null \|\| zti.n0(str4)) {
  74: f09.d0(ug9.class.getName(), "link or chatAccessToken must not be null", new Object[0]);
  75: return null;
  76: }
  77: zsc zscVar = (zsc) this.a.getValue();
  78: p73 p73Var = new p73(tdd.x1, (byte) 5);
  79: if (str4 != null && str4.length() != 0) {
--
~~~

### defpackage/uh0.java
~~~text
 138: w8aVar3 = w8aVar2;
 139: i = 1;
 140: break;
 141: default:
 142: k3g.t(vg9.y("No such value ", strS0, " for LoginTokenType"));
 143: return null;
 144: }
 145: }
 146: i = 1;
 147: bebVar.N();
--
~~~

### defpackage/wbi.java
~~~text
 129: if (account != null) {
 130: jSONObject2.put("accountName", account.name);
 131: }
 132: jSONObject2.put("idTokenRequested", googleSignInOptions.d);
 133: jSONObject2.put("forceCodeForRefreshToken", googleSignInOptions.f);
 134: jSONObject2.put("serverAuthRequested", googleSignInOptions.e);
 135: if (!TextUtils.isEmpty(str10)) {
 136: jSONObject2.put("serverClientId", str10);
 137: }
 138: if (!TextUtils.isEmpty(str9)) {
--
~~~

### defpackage/wi.java
~~~text
  11: import android.os.CancellationSignal;
  12: import android.os.RemoteException;
  13: import android.util.Log;
  14: import androidx.camera.core.ImageCaptureException;
  15: import com.vk.push.core.auth.AuthTokenResult;
  16: import com.vk.push.core.base.AidlException;
  17: import com.vk.push.core.base.AidlResult;
  18: import com.vk.push.core.base.AsyncCallback;
  19: import java.io.File;
  20: import java.util.ArrayList;
--
2254: ((u6a) z3jVar.getValue()).a("Getting intermediate token has failed", aidlResultA.a());
2255: ((AsyncCallback) this.i).Y(aidlResultA);
2256: return s1kVar;
2257: shVar.getClass();
2258: aidlResultA = new AidlResult((AuthTokenResult) objB4);
2259: } catch (Exception e) {
2260: aidlResultA = sh.a(e);
2261: }
2262: ((AsyncCallback) this.i).Y(aidlResultA);
2263: break;
--
~~~

### defpackage/wpc.java
~~~text
 127: try {
 128: JSONObject jSONObject = new JSONObject();
 129: jSONObject.put("Fid", gn0Var.a);
 130: jSONObject.put("Status", s95.G(gn0Var.b));
 131: jSONObject.put("AuthToken", gn0Var.c);
 132: jSONObject.put("RefreshToken", gn0Var.d);
 133: jSONObject.put("TokenCreationEpochInSecs", gn0Var.f);
 134: jSONObject.put("ExpiresInSecs", gn0Var.e);
 135: jSONObject.put("FisError", gn0Var.g);
 136: gg7 gg7Var = (gg7) this.c;
--
 137: gg7Var.a();
--
 213: jSONObject = new JSONObject();
 214: }
 215: String strOptString = jSONObject.optString("Fid", null);
 216: int iOptInt = jSONObject.optInt("Status", 0);
 217: String strOptString2 = jSONObject.optString("AuthToken", null);
 218: String strOptString3 = jSONObject.optString("RefreshToken", null);
 219: long jOptLong = jSONObject.optLong("TokenCreationEpochInSecs", 0L);
 220: long jOptLong2 = jSONObject.optLong("ExpiresInSecs", 0L);
 221: String strOptString4 = jSONObject.optString("FisError", null);
 222: int i2 = s95.J(5)[iOptInt];
--
 223: if (i2 == 0) {
--
~~~

### defpackage/xla.java
~~~text
  67: IInterface iInterfaceQueryLocalInterface = binder2.queryLocalInterface("android.support.v4.media.session.IMediaSession");
  68: lq8Var = (iInterfaceQueryLocalInterface == null \|\| !(iInterfaceQueryLocalInterface instanceof nq8)) ? new lq8(binder2) : (nq8) iInterfaceQueryLocalInterface;
  69: }
  70: if (lq8Var != null) {
  71: ylaVar.h = new wwa(mediaBrowser.getSessionToken(), lq8Var);
  72: }
  73: }
  74: } catch (IllegalStateException e) {
  75: i5a.e("MediaBrowserCompat", "Unexpected IllegalStateException", e);
  76: }
--
  80: if (amaVar != null) {
  81: yla ylaVar2 = (yla) amaVar.b;
  82: wwa wwaVar = ylaVar2.h;
  83: if (wwaVar == null) {
  84: wwa wwaVar2 = new wwa(ylaVar2.b.getSessionToken(), null);
  85: ylaVar2.h = wwaVar2;
  86: wwaVar = wwaVar2;
  87: }
  88: zna znaVar = kpaVar.b;
  89: znaVar.R0(new mn9(kpaVar, wwaVar, (byte) 8));
--
~~~

### defpackage/yh0.java
~~~text
  27: 
  28: public final String toString() {
  29: StringBuilder sb = new StringBuilder("AuthData(authType=");
  30: sb.append(this.a);
  31: sb.append(", authToken=");
  32: return a15.q(sb, this.b, ')');
  33: }
  34: }
--
~~~

### defpackage/zjn.java
~~~text
  74: jy7 jy7Var = x0n.a;
  75: if (jy7Var.b <= 3) {
  76: Log.d((String) jy7Var.c, ((String) jy7Var.d).concat("Revoking access"));
  77: }
  78: String strD3 = wbi.a(context).d("refreshToken");
  79: x0n.a(context);
  80: if (!z) {
  81: b3n b3nVar = new b3n(wjmVar, (byte) 1);
  82: wjmVar.a(b3nVar);
  83: basePendingResult2 = b3nVar;
--
~~~

## account storage
Файлов с совпадениями (первые 60): 60

### defpackage/a1n.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import me.leolin.shortcutbadger.BuildConfig;
   5: import one.me.android.initialization.AccountInitializer;
   6: import org.json.JSONException;
   7: import org.json.JSONObject;
   8: 
   9: /* JADX INFO: loaded from: classes3.dex */
  10: public abstract class a1n {
--
  31: } catch (Throwable th) {
  32: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  33: Iterator it = q1h.a.iterator();
  34: while (it.hasNext()) {
  35: AccountInitializer accountInitializer = ((z6) it.next()).a;
  36: try {
  37: f09.c0("Payload", "error while parse payload", th);
  38: accountInitializer.c().j().d().a(null, th);
  39: } catch (Throwable th2) {
  40: f09.c0("Payload", "failed to collect exception", th2);
--
  41: }
  42: }
  43: int iG = s95.G(iqg.a);
--
  60: j = 0;
  61: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  62: Iterator it2 = q1h.a.iterator();
  63: while (it2.hasNext()) {
  64: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  65: try {
  66: f09.c0("Payload", "error while parse payload", th3);
  67: accountInitializer2.c().j().d().a(null, th3);
  68: } catch (Throwable th4) {
  69: f09.c0("Payload", "failed to collect exception", th4);
--
  70: }
  71: }
  72: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/a8g.java
~~~text
  25: import java.util.TreeMap;
  26: import java.util.concurrent.RejectedExecutionException;
  27: import kotlin.NoWhenBranchMatchedException;
  28: import kotlin.collections.a;
  29: import one.me.android.initialization.AccountInitializer;
  30: 
  31: /* JADX INFO: loaded from: classes.dex */
  32: public abstract /* synthetic */ class a8g {
  33: public static final o3j a = new o3j((byte) 0, "REMOVED_TASK");
  34: public static final o3j b = new o3j((byte) 0, "CLOSED_EMPTY");
--
  72: } catch (Throwable th) {
  73: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  74: Iterator it = q1h.a.iterator();
  75: while (it.hasNext()) {
  76: AccountInitializer accountInitializer = ((z6) it.next()).a;
  77: try {
  78: f09.c0("Payload", "error while parse payload", th);
  79: accountInitializer.c().j().d().a(null, th);
  80: } catch (Throwable th2) {
  81: f09.c0("Payload", "failed to collect exception", th2);
--
  82: }
  83: }
  84: int iG = s95.G(iqg.a);
--
 100: } catch (Throwable th3) {
 101: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 102: Iterator it2 = q1h.a.iterator();
 103: while (it2.hasNext()) {
 104: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 105: try {
 106: f09.c0("Payload", "error while parse payload", th3);
 107: accountInitializer2.c().j().d().a(null, th3);
 108: } catch (Throwable th4) {
 109: f09.c0("Payload", "failed to collect exception", th4);
--
 110: }
 111: }
 112: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/akn.java
~~~text
   2: 
   3: import java.text.DecimalFormat;
   4: import java.util.Iterator;
   5: import kotlin.NoWhenBranchMatchedException;
   6: import one.me.android.initialization.AccountInitializer;
   7: 
   8: /* JADX INFO: loaded from: classes3.dex */
   9: public abstract class akn {
  10: public static final String a(long j) {
  11: if (j < 0) {
--
  51: } catch (Throwable th) {
  52: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  53: Iterator it = q1h.a.iterator();
  54: while (it.hasNext()) {
  55: AccountInitializer accountInitializer = ((z6) it.next()).a;
  56: try {
  57: f09.c0("Payload", "error while parse payload", th);
  58: accountInitializer.c().j().d().a(null, th);
  59: } catch (Throwable th2) {
  60: f09.c0("Payload", "failed to collect exception", th2);
--
  61: }
  62: }
  63: int iG = s95.G(iqg.a);
--
  84: } catch (Throwable th3) {
  85: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  86: Iterator it2 = q1h.a.iterator();
  87: while (it2.hasNext()) {
  88: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  89: try {
  90: f09.c0("Payload", "error while parse payload", th3);
  91: accountInitializer2.c().j().d().a(null, th3);
  92: } catch (Throwable th4) {
  93: f09.c0("Payload", "failed to collect exception", th4);
--
  94: }
  95: }
  96: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/b0n.java
~~~text
   5: import java.util.Iterator;
   6: import java.util.LinkedHashMap;
   7: import java.util.Map;
   8: import kotlin.NoWhenBranchMatchedException;
   9: import one.me.android.initialization.AccountInitializer;
  10: import org.json.JSONException;
  11: import org.json.JSONObject;
  12: 
  13: /* JADX INFO: loaded from: classes2.dex */
  14: public abstract class b0n {
--
  39: } catch (Throwable th) {
  40: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  41: Iterator it = q1h.a.iterator();
  42: while (it.hasNext()) {
  43: AccountInitializer accountInitializer = ((z6) it.next()).a;
  44: try {
  45: f09.c0("Payload", "error while parse payload", th);
  46: accountInitializer.c().j().d().a(null, th);
  47: } catch (Throwable th2) {
  48: f09.c0("Payload", "failed to collect exception", th2);
--
  49: }
  50: }
  51: int iG = s95.G(iqg.a);
--
  68: } catch (Throwable th3) {
  69: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  70: Iterator it2 = q1h.a.iterator();
  71: while (it2.hasNext()) {
  72: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  73: try {
  74: f09.c0("Payload", "error while parse payload", th3);
  75: accountInitializer2.c().j().d().a(null, th3);
  76: } catch (Throwable th4) {
  77: f09.c0("Payload", "failed to collect exception", th4);
--
  78: }
  79: }
  80: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/be.java
~~~text
  15: import java.util.LinkedHashSet;
  16: import java.util.List;
  17: import kotlin.NoWhenBranchMatchedException;
  18: import me.leolin.shortcutbadger.BuildConfig;
  19: import one.me.android.initialization.AccountInitializer;
  20: import one.me.android.root.RootController;
  21: import one.me.chatmedia.viewer.ChatMediaViewerScreen;
  22: import one.me.chats.list.ChatsListWidget;
  23: import one.me.chatscreen.ChatScreen;
  24: import one.me.profile.screens.media.ChatMediaListWidget;
--
 509: } catch (Throwable th3) {
 510: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 511: Iterator it2 = q1h.a.iterator();
 512: while (it2.hasNext()) {
 513: AccountInitializer accountInitializer = ((z6) it2.next()).a;
 514: try {
 515: f09.c0("Payload", "error while parse payload", th3);
 516: accountInitializer.c().j().d().a(null, th3);
 517: } catch (Throwable th4) {
 518: f09.c0("Payload", "failed to collect exception", th4);
--
 519: }
 520: }
 521: int iG = s95.G(iqg.a);
--
 536: } catch (Throwable th5) {
 537: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
 538: Iterator it3 = q1h.a.iterator();
 539: while (it3.hasNext()) {
 540: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
 541: try {
 542: f09.c0("Payload", "error while parse payload", th5);
 543: accountInitializer2.c().j().d().a(null, th5);
 544: } catch (Throwable th6) {
 545: f09.c0("Payload", "failed to collect exception", th6);
--
 546: }
 547: }
 548: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/bj0.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes2.dex */
   8: public final class bj0 extends x6j {
   9: public final String c;
  10: public final int d;
--
  99: } catch (Throwable th) {
 100: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 101: Iterator it = q1h.a.iterator();
 102: while (it.hasNext()) {
 103: AccountInitializer accountInitializer = ((z6) it.next()).a;
 104: try {
 105: f09.c0("Payload", "error while parse payload", th);
 106: accountInitializer.c().j().d().a(null, th);
 107: } catch (Throwable th2) {
 108: f09.c0("Payload", "failed to collect exception", th2);
--
 109: }
 110: }
 111: int iG = s95.G(iqg.a);
--
 135: } catch (Throwable th3) {
 136: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 137: Iterator it2 = q1h.a.iterator();
 138: while (it2.hasNext()) {
 139: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 140: try {
 141: f09.c0("Payload", "error while parse payload", th3);
 142: accountInitializer2.c().j().d().a(r7, th3);
 143: } catch (Throwable th4) {
 144: f09.c0("Payload", "failed to collect exception", th4);
--
 145: }
 146: }
 147: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/btc.java
~~~text
  10: import java.util.concurrent.atomic.AtomicBoolean;
  11: import java.util.concurrent.atomic.AtomicReference;
  12: import java.util.function.UnaryOperator;
  13: import one.me.android.OneMeApplication;
  14: import one.me.android.initialization.AccountInitializer;
  15: 
  16: /* JADX INFO: loaded from: classes.dex */
  17: public final class btc {
  18: public final /* synthetic */ AccountInitializer a;
  19: public final /* synthetic */ OneMeApplication b;
--
  20: 
  21: public btc(AccountInitializer accountInitializer, OneMeApplication oneMeApplication) {
  22: this.a = accountInitializer;
  23: this.b = oneMeApplication;
--
  24: }
  25: 
  26: public final void a() {
--
  27: AccountInitializer accountInitializer = this.a;
--
  28: qm6 qm6Var = accountInitializer.a;
  29: qm6Var.a();
  30: StringBuilder sb = new StringBuilder();
  31: sb.append("Total tasks durations: ");
  32: xs7 xs7Var = (xs7) qm6Var.b;
--
~~~

### defpackage/bwb.java
~~~text
   5: import java.util.Iterator;
   6: import java.util.List;
   7: import java.util.Set;
   8: import kotlin.NoWhenBranchMatchedException;
   9: import one.me.android.initialization.AccountInitializer;
  10: import one.video.calls.sdk.net.signaling.wt.nal.internal.WebTransportSocket;
  11: import org.json.JSONObject;
  12: import org.webrtc.PeerConnectionFactory;
  13: import org.webrtc.ScreenCapturerAndroid;
  14: import ru.ok.android.onelog.impl.BuildConfig;
--
1283: } catch (Throwable th) {
1284: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
1285: Iterator it = q1h.a.iterator();
1286: while (it.hasNext()) {
1287: AccountInitializer accountInitializer = ((z6) it.next()).a;
1288: try {
1289: f09.c0("Payload", "error while parse payload", th);
1290: accountInitializer.c().j().d().a(null, th);
1291: } catch (Throwable th2) {
1292: f09.c0("Payload", "failed to collect exception", th2);
--
1293: }
1294: }
1295: int iG = s95.G(iqg.a);
--
1310: } catch (Throwable th3) {
1311: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
1312: Iterator it2 = q1h.a.iterator();
1313: while (it2.hasNext()) {
1314: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
1315: try {
1316: f09.c0("Payload", "error while parse payload", th3);
1317: accountInitializer2.c().j().d().a(null, th3);
1318: } catch (Throwable th4) {
1319: f09.c0("Payload", "failed to collect exception", th4);
--
1320: }
1321: }
1322: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/c1n.java
~~~text
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Iterator;
   5: import me.leolin.shortcutbadger.BuildConfig;
   6: import one.me.android.initialization.AccountInitializer;
   7: 
   8: /* JADX INFO: loaded from: classes3.dex */
   9: public abstract class c1n {
  10: public static int a(int i, boolean z) {
  11: return w7g.n(i, 31, z);
--
  22: } catch (Throwable th) {
  23: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  24: Iterator it = q1h.a.iterator();
  25: while (it.hasNext()) {
  26: AccountInitializer accountInitializer = ((z6) it.next()).a;
  27: try {
  28: f09.c0("Payload", "error while parse payload", th);
  29: accountInitializer.c().j().d().a(null, th);
  30: } catch (Throwable th2) {
  31: f09.c0("Payload", "failed to collect exception", th2);
--
  32: }
  33: }
  34: int iG = s95.G(iqg.a);
--
  53: } catch (Throwable th3) {
  54: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  55: Iterator it2 = q1h.a.iterator();
  56: while (it2.hasNext()) {
  57: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  58: try {
  59: f09.c0("Payload", "error while parse payload", th3);
  60: accountInitializer2.c().j().d().a(null, th3);
  61: } catch (Throwable th4) {
  62: f09.c0("Payload", "failed to collect exception", th4);
--
  63: }
  64: }
  65: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/cg6.java
~~~text
   7: import java.util.List;
   8: import javax.net.ssl.SSLSocket;
   9: import kotlin.NoWhenBranchMatchedException;
  10: import one.me.android.MainActivity;
  11: import one.me.android.initialization.AccountInitializer;
  12: 
  13: /* JADX INFO: loaded from: classes.dex */
  14: public final class cg6 implements f84, wbj, sw5, y74, xr4, w95, ic5, rl4 {
  15: public static final cg6 b = new cg6(1);
  16: public static final cg6 c = new cg6(2);
--
  41: } catch (Throwable th) {
  42: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  43: Iterator it = q1h.a.iterator();
  44: while (it.hasNext()) {
  45: AccountInitializer accountInitializer = ((z6) it.next()).a;
  46: try {
  47: f09.c0("Payload", "error while parse payload", th);
  48: accountInitializer.c().j().d().a(null, th);
  49: } catch (Throwable th2) {
  50: f09.c0("Payload", "failed to collect exception", th2);
--
  51: }
  52: }
  53: int iG = s95.G(iqg.a);
--
  70: } catch (Throwable th3) {
  71: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  72: Iterator it2 = q1h.a.iterator();
  73: while (it2.hasNext()) {
  74: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  75: try {
  76: f09.c0("Payload", "error while parse payload", th3);
  77: accountInitializer2.c().j().d().a(null, th3);
  78: } catch (Throwable th4) {
  79: f09.c0("Payload", "failed to collect exception", th4);
--
  80: }
  81: }
  82: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/cgi.java
~~~text
   5: import android.util.Range;
   6: import android.widget.ImageView;
   7: import java.util.Iterator;
   8: import kotlin.NoWhenBranchMatchedException;
   9: import one.me.android.initialization.AccountInitializer;
  10: 
  11: /* JADX INFO: loaded from: classes3.dex */
  12: public abstract class cgi {
  13: public static final String[] a = {"audio/mpeg-L1", "audio/mpeg-L2", "audio/mpeg"};
  14: public static final int[] b = {44100, 48000, 32000};
--
  58: } catch (Throwable th) {
  59: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  60: Iterator it = q1h.a.iterator();
  61: while (it.hasNext()) {
  62: AccountInitializer accountInitializer = ((z6) it.next()).a;
  63: try {
  64: f09.c0("Payload", "error while parse payload", th);
  65: accountInitializer.c().j().d().a(null, th);
  66: } catch (Throwable th2) {
  67: f09.c0("Payload", "failed to collect exception", th2);
--
  68: }
  69: }
  70: int iG = s95.G(iqg.a);
--
  89: } catch (Throwable th3) {
  90: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  91: Iterator it2 = q1h.a.iterator();
  92: while (it2.hasNext()) {
  93: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  94: try {
  95: f09.c0("Payload", "error while parse payload", th3);
  96: accountInitializer2.c().j().d().a(null, th3);
  97: } catch (Throwable th4) {
  98: f09.c0("Payload", "failed to collect exception", th4);
--
  99: }
 100: }
 101: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/cp5.java
~~~text
  14: import java.util.Map;
  15: import java.util.Objects;
  16: import kotlin.NoWhenBranchMatchedException;
  17: import me.leolin.shortcutbadger.BuildConfig;
  18: import one.me.android.initialization.AccountInitializer;
  19: import org.json.JSONException;
  20: import org.json.JSONObject;
  21: 
  22: /* JADX INFO: loaded from: classes.dex */
  23: public class cp5 implements f84, o6a, rl4, e3g, kwi, fhk, h5a, ek9, ic5, w95 {
--
  71: } catch (Throwable th) {
  72: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  73: Iterator it = q1h.a.iterator();
  74: while (it.hasNext()) {
  75: AccountInitializer accountInitializer = ((z6) it.next()).a;
  76: try {
  77: f09.c0("Payload", "error while parse payload", th);
  78: accountInitializer.c().j().d().a(null, th);
  79: } catch (Throwable th2) {
  80: f09.c0("Payload", "failed to collect exception", th2);
--
  81: }
  82: }
  83: int iG = s95.G(iqg.a);
--
  98: } catch (Throwable th3) {
  99: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 100: Iterator it2 = q1h.a.iterator();
 101: while (it2.hasNext()) {
 102: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 103: try {
 104: f09.c0("Payload", "error while parse payload", th3);
 105: accountInitializer2.c().j().d().a(null, th3);
 106: } catch (Throwable th4) {
 107: f09.c0("Payload", "failed to collect exception", th4);
--
 108: }
 109: }
 110: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/cpi.java
~~~text
   5: import java.util.AbstractMap;
   6: import java.util.Iterator;
   7: import kotlin.NoWhenBranchMatchedException;
   8: import me.leolin.shortcutbadger.BuildConfig;
   9: import one.me.android.initialization.AccountInitializer;
  10: 
  11: /* JADX INFO: loaded from: classes2.dex */
  12: public abstract class cpi {
  13: public static final int[][] a = {new int[]{-46922, -30155}, new int[]{-14019, -31958}, new int[]{-15408683, -16529630}, new int[]{-16197645, -11298561}, new int[]{-4220929, -11374849}};
  14: 
--
  29: } catch (Throwable th) {
  30: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  31: Iterator it = q1h.a.iterator();
  32: while (it.hasNext()) {
  33: AccountInitializer accountInitializer = ((z6) it.next()).a;
  34: try {
  35: f09.c0("Payload", "error while parse payload", th);
  36: accountInitializer.c().j().d().a(null, th);
  37: } catch (Throwable th2) {
  38: f09.c0("Payload", "failed to collect exception", th2);
--
  39: }
  40: }
  41: int iG = s95.G(iqg.a);
--
  57: } catch (Throwable th3) {
  58: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  59: Iterator it2 = q1h.a.iterator();
  60: while (it2.hasNext()) {
  61: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  62: try {
  63: f09.c0("Payload", "error while parse payload", th3);
  64: accountInitializer2.c().j().d().a(null, th3);
  65: } catch (Throwable th4) {
  66: f09.c0("Payload", "failed to collect exception", th4);
--
  67: }
  68: }
  69: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/d0n.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes2.dex */
   8: public abstract class d0n {
   9: public static w8b a(beb bebVar) {
  10: int iP0;
--
  18: } catch (Throwable th) {
  19: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  20: Iterator it = q1h.a.iterator();
  21: while (it.hasNext()) {
  22: AccountInitializer accountInitializer = ((z6) it.next()).a;
  23: try {
  24: f09.c0("Payload", "error while parse payload", th);
  25: accountInitializer.c().j().d().a(null, th);
  26: } catch (Throwable th2) {
  27: f09.c0("Payload", "failed to collect exception", th2);
--
  28: }
  29: }
  30: int iG = s95.G(iqg.a);
--
  44: } catch (Throwable th3) {
  45: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  46: Iterator it2 = q1h.a.iterator();
  47: while (it2.hasNext()) {
  48: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  49: try {
  50: f09.c0("Payload", "error while parse payload", th3);
  51: accountInitializer2.c().j().d().a(null, th3);
  52: } catch (Throwable th4) {
  53: f09.c0("Payload", "failed to collect exception", th4);
--
  54: }
  55: }
  56: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/d4f.java
~~~text
   8: import java.util.Map;
   9: import java.util.concurrent.CancellationException;
  10: import java.util.concurrent.ConcurrentHashMap;
  11: import me.leolin.shortcutbadger.BuildConfig;
  12: import one.me.android.initialization.AccountInitializer;
  13: import one.me.promoted.events.ParseErrorException;
  14: import org.json.JSONArray;
  15: import org.json.JSONException;
  16: import org.json.JSONObject;
  17: 
--
 280: HashMap map2 = new HashMap();
 281: map2.put("reason", "empty_response");
 282: to6 to6Var = az7.w;
 283: if (to6Var != null) {
 284: f09.c0(((AccountInitializer) ((g09) to6Var.a).a).d, "Pmb parse error", new ParseErrorException("promo_parse_error: " + map2));
 285: }
 286: vcmVar = new vcm("Empty response");
 287: } else {
 288: JSONObject jSONObjectOptJSONObject = jSONObject.optJSONObject("promo");
 289: if (jSONObjectOptJSONObject == null) {
--
 291: map3.put("reason", "missing_section");
 292: map3.put("section", "promo");
 293: to6 to6Var2 = az7.w;
 294: if (to6Var2 != null) {
 295: f09.c0(((AccountInitializer) ((g09) to6Var2.a).a).d, "Pmb parse error", new ParseErrorException("promo_parse_error: " + map3));
 296: }
 297: vcmVar = new vcm("Response doesn't have section: promo");
 298: } else {
 299: JSONArray jSONArrayOptJSONArray = jSONObjectOptJSONObject.optJSONArray("banners");
 300: if (jSONArrayOptJSONArray == null) {
--
 301: HashMap map4 = new HashMap();
 302: map4.put("reason", "missing_banners_field");
 303: to6 to6Var3 = az7.w;
 304: if (to6Var3 != null) {
 305: f09.c0(((AccountInitializer) ((g09) to6Var3.a).a).d, "Pmb parse error", new ParseErrorException("promo_parse_error: " + map4));
 306: }
 307: vcmVar = new vcm("Missing banner field");
 308: } else if (jSONArrayOptJSONArray.length() == 0) {
 309: HashMap map5 = new HashMap();
 310: map5.put("reason", "no_banners");
--
 311: to6 to6Var4 = az7.w;
 312: if (to6Var4 != null) {
 313: f09.c0(((AccountInitializer) ((g09) to6Var4.a).a).d, "Pmb parse error", new ParseErrorException("promo_parse_error: " + map5));
 314: }
 315: vcmVar = new vcm("No banners in response");
 316: } else {
 317: sxe sxeVar = new sxe((byte) 17);
 318: ArrayList arrayList3 = new ArrayList();
--
~~~

### defpackage/d7.java
~~~text
   1: package defpackage;
   2: 
   3: import one.me.android.initialization.AccountInitializer;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final /* synthetic */ class d7 implements o08 {
   7: public final /* synthetic */ byte a;
   8: public final /* synthetic */ AccountInitializer b;
--
   9: 
  10: public /* synthetic */ d7(AccountInitializer accountInitializer, byte b) {
  11: this.a = b;
  12: this.b = accountInitializer;
  13: }
--
  14: 
  15: @Override // defpackage.o08
--
  16: public final Object c() {
  17: byte b = this.a;
--
  18: AccountInitializer accountInitializer = this.b;
  19: switch (b) {
  20: case 0:
  21: return (j5b) vg9.u(accountInitializer, 39);
  22: case 1:
  23: cf7 cf7Var = (cf7) vg9.u(accountInitializer, 205);
--
~~~

### defpackage/df7.java
~~~text
  13: import java.util.Random;
  14: import java.util.concurrent.CountDownLatch;
  15: import kotlin.NoWhenBranchMatchedException;
  16: import me.leolin.shortcutbadger.BuildConfig;
  17: import one.me.android.initialization.AccountInitializer;
  18: import org.json.JSONException;
  19: import org.json.JSONObject;
  20: 
  21: /* JADX INFO: loaded from: classes.dex */
  22: public final class df7 implements f84, wik, ux6, ic5, swf, ek9, ezb, rl4 {
--
 276: } catch (Throwable th) {
 277: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 278: Iterator it = q1h.a.iterator();
 279: while (it.hasNext()) {
 280: AccountInitializer accountInitializer = ((z6) it.next()).a;
 281: try {
 282: f09.c0("Payload", "error while parse payload", th);
 283: accountInitializer.c().j().d().a(null, th);
 284: } catch (Throwable th2) {
 285: f09.c0("Payload", "failed to collect exception", th2);
--
 286: }
 287: }
 288: int iG = s95.G(iqg.a);
--
 304: } catch (Throwable th3) {
 305: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 306: Iterator it2 = q1h.a.iterator();
 307: while (it2.hasNext()) {
 308: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 309: try {
 310: f09.c0("Payload", "error while parse payload", th3);
 311: accountInitializer2.c().j().d().a(str, th3);
 312: } catch (Throwable th4) {
 313: f09.c0("Payload", "failed to collect exception", th4);
--
 314: }
 315: }
 316: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/dte.java
~~~text
  12: import java.util.List;
  13: import java.util.Map;
  14: import kotlin.NoWhenBranchMatchedException;
  15: import me.leolin.shortcutbadger.BuildConfig;
  16: import one.me.android.initialization.AccountInitializer;
  17: import one.me.profileedit.screens.adminpermissions.ProfileEditAdminPermissionsWidget;
  18: import one.me.stories.viewer.viewer.UserStoriesScreen;
  19: 
  20: /* JADX INFO: loaded from: classes2.dex */
  21: public final class dte implements kbh, fv4, y18, g18, a7i, szd, rwf, hu0 {
--
  43: } catch (Throwable th) {
  44: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  45: Iterator it = q1h.a.iterator();
  46: while (it.hasNext()) {
  47: AccountInitializer accountInitializer = ((z6) it.next()).a;
  48: try {
  49: f09.c0("Payload", "error while parse payload", th);
  50: accountInitializer.c().j().d().a(null, th);
  51: } catch (Throwable th2) {
  52: f09.c0("Payload", "failed to collect exception", th2);
--
  53: }
  54: }
  55: int iG = s95.G(iqg.a);
--
  69: } catch (Throwable th3) {
  70: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  71: Iterator it2 = q1h.a.iterator();
  72: while (it2.hasNext()) {
  73: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  74: try {
  75: f09.c0("Payload", "error while parse payload", th3);
  76: accountInitializer2.c().j().d().a(null, th3);
  77: } catch (Throwable th4) {
  78: f09.c0("Payload", "failed to collect exception", th4);
--
  79: }
  80: }
  81: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/dya.java
~~~text
   5: import java.io.IOException;
   6: import java.util.Iterator;
   7: import java.util.List;
   8: import me.leolin.shortcutbadger.BuildConfig;
   9: import one.me.android.initialization.AccountInitializer;
  10: import one.me.messages.list.ui.MessagesListWidget;
  11: import one.me.notifications.settings.screens.other.OtherNotificationsSettingsScreen;
  12: import org.webrtc.PeerConnectionFactory;
  13: import org.webrtc.Predicate;
  14: 
--
 130: } catch (Throwable th) {
 131: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 132: Iterator it = q1h.a.iterator();
 133: while (it.hasNext()) {
 134: AccountInitializer accountInitializer = ((z6) it.next()).a;
 135: try {
 136: f09.c0("Payload", "error while parse payload", th);
 137: accountInitializer.c().j().d().a(null, th);
 138: } catch (Throwable th2) {
 139: f09.c0("Payload", "failed to collect exception", th2);
--
 140: }
 141: }
 142: int iG = s95.G(iqg.a);
--
 161: } catch (Throwable th3) {
 162: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 163: Iterator it2 = q1h.a.iterator();
 164: while (it2.hasNext()) {
 165: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 166: try {
 167: f09.c0("Payload", "error while parse payload", th3);
 168: accountInitializer2.c().j().d().a(null, th3);
 169: } catch (Throwable th4) {
 170: f09.c0("Payload", "failed to collect exception", th4);
--
 171: }
 172: }
 173: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/e0c.java
~~~text
  33: import java.util.Map;
  34: import java.util.Set;
  35: import kotlin.collections.a;
  36: import me.leolin.shortcutbadger.BuildConfig;
  37: import one.me.android.initialization.AccountInitializer;
  38: import one.me.sdk.richvector.AnimationTarget;
  39: import one.me.sdk.richvector.EnhancedVectorDrawable;
  40: import one.me.sdk.richvector.internal.element.GroupElement;
  41: import one.me.sdk.richvector.internal.element.PathElement;
  42: import org.msgpack.core.MessageIntegerOverflowException;
--
 294: } catch (Throwable th) {
 295: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 296: Iterator it = q1h.a.iterator();
 297: while (it.hasNext()) {
 298: AccountInitializer accountInitializer = ((z6) it.next()).a;
 299: try {
 300: f09.c0("Payload", "error while parse payload", th);
 301: accountInitializer.c().j().d().a(null, th);
 302: } catch (Throwable th2) {
 303: f09.c0("Payload", "failed to collect exception", th2);
--
 304: }
 305: }
 306: int iG = s95.G(iqg.a);
--
 346: i = 0;
 347: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 348: Iterator it2 = q1h.a.iterator();
 349: while (it2.hasNext()) {
 350: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 351: try {
 352: f09.c0("Payload", "error while parse payload", th3);
 353: accountInitializer2.c().j().d().a(r11, th3);
 354: } catch (Throwable th4) {
 355: f09.c0("Payload", "failed to collect exception", th4);
--
 356: }
 357: }
 358: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/eb3.java
~~~text
   2: 
   3: import java.util.Iterator;
   4: import java.util.LinkedHashSet;
   5: import java.util.List;
   6: import one.me.android.initialization.AccountInitializer;
   7: 
   8: /* JADX INFO: loaded from: classes3.dex */
   9: public final class eb3 extends x6j {
  10: public final List c;
  11: public final r53 d;
--
  29: } catch (Throwable th) {
  30: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  31: Iterator it = q1h.a.iterator();
  32: while (it.hasNext()) {
  33: AccountInitializer accountInitializer = ((z6) it.next()).a;
  34: try {
  35: f09.c0("Payload", "error while parse payload", th);
  36: accountInitializer.c().j().d().a(null, th);
  37: } catch (Throwable th2) {
  38: f09.c0("Payload", "failed to collect exception", th2);
--
  39: }
  40: }
  41: int iG = s95.G(iqg.a);
--
  60: } catch (Throwable th3) {
  61: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  62: Iterator it2 = q1h.a.iterator();
  63: while (it2.hasNext()) {
  64: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  65: try {
  66: f09.c0("Payload", "error while parse payload", th3);
  67: accountInitializer2.c().j().d().a(null, th3);
  68: } catch (Throwable th4) {
  69: f09.c0("Payload", "failed to collect exception", th4);
--
  70: }
  71: }
  72: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/eb8.java
~~~text
  13: import java.io.IOException;
  14: import java.util.concurrent.ExecutorService;
  15: import me.leolin.shortcutbadger.BuildConfig;
  16: import one.me.aboutappsettings.AboutAppSettingsScreen;
  17: import one.me.android.initialization.AccountInitializer;
  18: import one.me.appearancesettings.multitheme.AppearanceSettingsMultiThemeScreen;
  19: import one.me.background.wake.BackgroundCheckReceiver;
  20: import one.me.background.wake.BackgroundListenService;
  21: import one.me.calls.ui.ui.call.panels.CallBottomPanelWidget;
  22: import one.me.chatmedia.viewer.video.BaseVideoViewerWidget;
--
 103: case 3:
 104: e6 e6Var = (e6) obj;
 105: return nm9.I(e6Var.b, ((vxc) ((k6j) e6Var.g.getValue())).a(), 2, new c6(e6Var, r4, r5));
 106: case 4:
 107: return (av8) vg9.u((AccountInitializer) obj, 799);
 108: case 5:
 109: wj2 wj2Var = ((AccountSwitcherBottomSheet) obj).u;
 110: return new g8(wj2Var.getAccessor().d(ScreenCapturerAndroid.FRAME_RESUBMIT_DELAY_MILLIS), wj2Var.getAccessor().d(7), wj2Var.getAccessor().d(197), (q1a) wj2Var.getAccessor().c(35));
 111: case 6:
 112: o9 o9Var = (o9) obj;
--
~~~

### defpackage/ehc.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes.dex */
   8: public final class ehc implements f84 {
   9: public static final ehc a;
  10: public static final String b;
--
  35: } catch (Throwable th) {
  36: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  37: Iterator it = q1h.a.iterator();
  38: while (it.hasNext()) {
  39: AccountInitializer accountInitializer = ((z6) it.next()).a;
  40: try {
  41: f09.c0("Payload", "error while parse payload", th);
  42: accountInitializer.c().j().d().a(null, th);
  43: } catch (Throwable th2) {
  44: f09.c0("Payload", "failed to collect exception", th2);
--
  45: }
  46: }
  47: int iG = s95.G(iqg.a);
--
  65: } catch (Throwable th3) {
  66: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  67: Iterator it2 = q1h.a.iterator();
  68: while (it2.hasNext()) {
  69: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  70: try {
  71: f09.c0("Payload", "error while parse payload", th3);
  72: accountInitializer2.c().j().d().a(null, th3);
  73: } catch (Throwable th4) {
  74: f09.c0("Payload", "failed to collect exception", th4);
--
  75: }
  76: }
  77: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/ekn.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes2.dex */
   8: public abstract class ekn {
   9: public static rji a(beb bebVar) {
  10: int iP0;
--
  14: } catch (Throwable th) {
  15: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  16: Iterator it = q1h.a.iterator();
  17: while (it.hasNext()) {
  18: AccountInitializer accountInitializer = ((z6) it.next()).a;
  19: try {
  20: f09.c0("Payload", "error while parse payload", th);
  21: accountInitializer.c().j().d().a(null, th);
  22: } catch (Throwable th2) {
  23: f09.c0("Payload", "failed to collect exception", th2);
--
  24: }
  25: }
  26: int iG = s95.G(iqg.a);
--
  41: } catch (Throwable th3) {
  42: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  43: Iterator it2 = q1h.a.iterator();
  44: while (it2.hasNext()) {
  45: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  46: try {
  47: f09.c0("Payload", "error while parse payload", th3);
  48: accountInitializer2.c().j().d().a(null, th3);
  49: } catch (Throwable th4) {
  50: f09.c0("Payload", "failed to collect exception", th4);
--
  51: }
  52: }
  53: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/elk.java
~~~text
   5: import java.util.Iterator;
   6: import java.util.List;
   7: import kotlin.NoWhenBranchMatchedException;
   8: import me.leolin.shortcutbadger.BuildConfig;
   9: import one.me.android.initialization.AccountInitializer;
  10: 
  11: /* JADX INFO: loaded from: classes3.dex */
  12: public final class elk implements Serializable {
  13: public final String a;
  14: public final long b;
--
  48: } catch (Throwable th2) {
  49: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th2);
  50: Iterator it2 = q1h.a.iterator();
  51: while (it2.hasNext()) {
  52: AccountInitializer accountInitializer = ((z6) it2.next()).a;
  53: try {
  54: f09.c0("Payload", "error while parse payload", th2);
  55: accountInitializer.c().j().d().a(null, th2);
  56: } catch (Throwable th3) {
  57: f09.c0("Payload", "failed to collect exception", th3);
--
  58: }
  59: }
  60: int iG2 = s95.G(iqg.a);
--
  82: } catch (Throwable th4) {
  83: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th4);
  84: Iterator it3 = q1h.a.iterator();
  85: while (it3.hasNext()) {
  86: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
  87: try {
  88: f09.c0("Payload", "error while parse payload", th4);
  89: accountInitializer2.c().j().d().a(null, th4);
  90: } catch (Throwable th5) {
  91: f09.c0("Payload", "failed to collect exception", th5);
--
  92: }
  93: }
  94: int iG3 = s95.G(iqg.a);
--
~~~

### defpackage/f0c.java
~~~text
   9: import java.util.List;
  10: import java.util.RandomAccess;
  11: import java.util.Set;
  12: import kotlin.NoWhenBranchMatchedException;
  13: import one.me.android.initialization.AccountInitializer;
  14: import one.me.chats.list.ChatsListWidget;
  15: import one.me.sdk.arch.Widget;
  16: 
  17: /* JADX INFO: loaded from: classes.dex */
  18: public final class f0c implements f84, w95, hq7, yda, i6c, rl4 {
--
 136: } catch (Throwable th) {
 137: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 138: Iterator it = q1h.a.iterator();
 139: while (it.hasNext()) {
 140: AccountInitializer accountInitializer = ((z6) it.next()).a;
 141: try {
 142: f09.c0("Payload", "error while parse payload", th);
 143: accountInitializer.c().j().d().a(null, th);
 144: } catch (Throwable th2) {
 145: f09.c0("Payload", "failed to collect exception", th2);
--
 146: }
 147: }
 148: int iG = s95.G(iqg.a);
--
 162: } catch (Throwable th3) {
 163: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 164: Iterator it2 = q1h.a.iterator();
 165: while (it2.hasNext()) {
 166: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 167: try {
 168: f09.c0("Payload", "error while parse payload", th3);
 169: accountInitializer2.c().j().d().a(null, th3);
 170: } catch (Throwable th4) {
 171: f09.c0("Payload", "failed to collect exception", th4);
--
 172: }
 173: }
 174: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/f0n.java
~~~text
   4: import java.util.ArrayList;
   5: import java.util.HashSet;
   6: import java.util.Iterator;
   7: import kotlin.NoWhenBranchMatchedException;
   8: import one.me.android.initialization.AccountInitializer;
   9: import org.json.JSONArray;
  10: import org.json.JSONException;
  11: import org.json.JSONObject;
  12: import org.webrtc.MediaStreamTrack;
  13: 
--
 150: } catch (Throwable th) {
 151: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 152: Iterator it = q1h.a.iterator();
 153: while (it.hasNext()) {
 154: AccountInitializer accountInitializer = ((z6) it.next()).a;
 155: try {
 156: f09.c0("Payload", "error while parse payload", th);
 157: accountInitializer.c().j().d().a(null, th);
 158: } catch (Throwable th2) {
 159: f09.c0("Payload", "failed to collect exception", th2);
--
 160: }
 161: }
 162: int iG = s95.G(iqg.a);
--
 177: } catch (Throwable th3) {
 178: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 179: Iterator it2 = q1h.a.iterator();
 180: while (it2.hasNext()) {
 181: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 182: try {
 183: f09.c0("Payload", "error while parse payload", th3);
 184: accountInitializer2.c().j().d().a(null, th3);
 185: } catch (Throwable th4) {
 186: f09.c0("Payload", "failed to collect exception", th4);
--
 187: }
 188: }
 189: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/fd9.java
~~~text
   4: import android.util.Log;
   5: import java.util.ArrayList;
   6: import java.util.Iterator;
   7: import java.util.Map;
   8: import one.me.android.initialization.AccountInitializer;
   9: import org.json.JSONException;
  10: import org.json.JSONObject;
  11: 
  12: /* JADX INFO: loaded from: classes2.dex */
  13: public class fd9 implements gl9, ezb, fv4, frc {
--
 133: } catch (Throwable th) {
 134: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 135: Iterator it = q1h.a.iterator();
 136: while (it.hasNext()) {
 137: AccountInitializer accountInitializer = ((z6) it.next()).a;
 138: try {
 139: f09.c0("Payload", "error while parse payload", th);
 140: accountInitializer.c().j().d().a(null, th);
 141: } catch (Throwable th2) {
 142: f09.c0("Payload", "failed to collect exception", th2);
--
 143: }
 144: }
 145: int iG = s95.G(iqg.a);
--
~~~

### defpackage/g6g.java
~~~text
   8: import java.util.Iterator;
   9: import java.util.List;
  10: import java.util.concurrent.Callable;
  11: import java.util.concurrent.Executor;
  12: import one.me.android.initialization.AccountInitializer;
  13: import org.webrtc.PeerConnection;
  14: 
  15: /* JADX INFO: loaded from: classes3.dex */
  16: public final class g6g implements jb0, f01, wik, n84, rl4, g18, m09, v6a, snj, zt2, swi, ezb, kr8, dhf, ei1, x87, fv4 {
  17: public static final g6g b = new g6g((byte) 1);
--
 241: } catch (Throwable th) {
 242: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 243: Iterator it = q1h.a.iterator();
 244: while (it.hasNext()) {
 245: AccountInitializer accountInitializer = ((z6) it.next()).a;
 246: try {
 247: f09.c0("Payload", "error while parse payload", th);
 248: accountInitializer.c().j().d().a(null, th);
 249: } catch (Throwable th2) {
 250: f09.c0("Payload", "failed to collect exception", th2);
--
 251: }
 252: }
 253: int iG = s95.G(iqg.a);
--
~~~

### defpackage/gd9.java
~~~text
   6: import java.util.ArrayList;
   7: import java.util.Iterator;
   8: import java.util.List;
   9: import me.leolin.shortcutbadger.BuildConfig;
  10: import one.me.android.initialization.AccountInitializer;
  11: import org.json.JSONArray;
  12: import org.json.JSONObject;
  13: 
  14: /* JADX INFO: loaded from: classes2.dex */
  15: public final class gd9 implements hwa, btf, kwi, f01 {
--
  53: } catch (Throwable th) {
  54: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  55: Iterator it = q1h.a.iterator();
  56: while (it.hasNext()) {
  57: AccountInitializer accountInitializer = ((z6) it.next()).a;
  58: try {
  59: f09.c0("Payload", "error while parse payload", th);
  60: accountInitializer.c().j().d().a(null, th);
  61: } catch (Throwable th2) {
  62: f09.c0("Payload", "failed to collect exception", th2);
--
  63: }
  64: }
  65: int iG = s95.G(iqg.a);
--
  82: } catch (Throwable th3) {
  83: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  84: Iterator it2 = q1h.a.iterator();
  85: while (it2.hasNext()) {
  86: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  87: try {
  88: f09.c0("Payload", "error while parse payload", th3);
  89: accountInitializer2.c().j().d().a(null, th3);
  90: } catch (Throwable th4) {
  91: f09.c0("Payload", "failed to collect exception", th4);
--
  92: }
  93: }
  94: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/gfa.java
~~~text
   6: import java.util.LinkedHashMap;
   7: import java.util.List;
   8: import java.util.Set;
   9: import me.leolin.shortcutbadger.BuildConfig;
  10: import one.me.android.initialization.AccountInitializer;
  11: 
  12: /* JADX INFO: loaded from: classes3.dex */
  13: public final class gfa implements Serializable {
  14: public final Serializable a;
  15: 
--
  25: } catch (Throwable th) {
  26: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  27: Iterator it = q1h.a.iterator();
  28: while (it.hasNext()) {
  29: AccountInitializer accountInitializer = ((z6) it.next()).a;
  30: try {
  31: f09.c0("Payload", "error while parse payload", th);
  32: accountInitializer.c().j().d().a(null, th);
  33: } catch (Throwable th2) {
  34: f09.c0("Payload", "failed to collect exception", th2);
--
  35: }
  36: }
  37: int iG = s95.G(iqg.a);
--
  54: } catch (Throwable th3) {
  55: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  56: Iterator it2 = q1h.a.iterator();
  57: while (it2.hasNext()) {
  58: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  59: try {
  60: f09.c0("Payload", "error while parse payload", th3);
  61: accountInitializer2.c().j().d().a(null, th3);
  62: } catch (Throwable th4) {
  63: f09.c0("Payload", "failed to collect exception", th4);
--
  64: }
  65: }
  66: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/h7.java
~~~text
   2: 
   3: import android.content.Context;
   4: import android.text.TextPaint;
   5: import java.util.Map;
   6: import one.me.android.initialization.AccountInitializer;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class h7 extends x1j implements e18 {
  10: public final /* synthetic */ byte e;
  11: public final /* synthetic */ AccountInitializer f;
--
  12: 
  13: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  14: public /* synthetic */ h7(AccountInitializer accountInitializer, b55 b55Var, byte b) {
  15: super(2, b55Var);
  16: this.e = b;
--
  17: this.f = accountInitializer;
  18: }
  19: 
--
  20: @Override // defpackage.e18
  21: public final Object invoke(Object obj, Object obj2) {
  22: byte b = this.e;
--
  34: 
  35: @Override // defpackage.hv0
  36: public final b55 u(b55 b55Var, Object obj) {
  37: byte b = this.e;
  38: AccountInitializer accountInitializer = this.f;
  39: switch (b) {
  40: case 0:
  41: return new h7(accountInitializer, b55Var, (byte) 0);
  42: default:
  43: return new h7(accountInitializer, b55Var, (byte) 1);
--
~~~

### defpackage/hm4.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes2.dex */
   8: public final class hm4 {
   9: public final /* synthetic */ byte a;
  10: public final Object b;
--
  22: } catch (Throwable th) {
  23: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  24: Iterator it = q1h.a.iterator();
  25: while (it.hasNext()) {
  26: AccountInitializer accountInitializer = ((z6) it.next()).a;
  27: try {
  28: f09.c0("Payload", "error while parse payload", th);
  29: accountInitializer.c().j().d().a(null, th);
  30: } catch (Throwable th2) {
  31: f09.c0("Payload", "failed to collect exception", th2);
--
  32: }
  33: }
  34: int iG = s95.G(iqg.a);
--
  49: } catch (Throwable th3) {
  50: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  51: Iterator it2 = q1h.a.iterator();
  52: while (it2.hasNext()) {
  53: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  54: try {
  55: f09.c0("Payload", "error while parse payload", th3);
  56: accountInitializer2.c().j().d().a(null, th3);
  57: } catch (Throwable th4) {
  58: f09.c0("Payload", "failed to collect exception", th4);
--
  59: }
  60: }
  61: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/hq.java
~~~text
   3: import java.util.Iterator;
   4: import java.util.List;
   5: import kotlin.NoWhenBranchMatchedException;
   6: import me.leolin.shortcutbadger.BuildConfig;
   7: import one.me.android.initialization.AccountInitializer;
   8: 
   9: /* JADX INFO: loaded from: classes3.dex */
  10: public final class hq {
  11: public final long a;
  12: public final String b;
--
  35: } catch (Throwable th) {
  36: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  37: Iterator it = q1h.a.iterator();
  38: while (it.hasNext()) {
  39: AccountInitializer accountInitializer = ((z6) it.next()).a;
  40: try {
  41: f09.c0("Payload", "error while parse payload", th);
  42: accountInitializer.c().j().d().a(null, th);
  43: } catch (Throwable th2) {
  44: f09.c0("Payload", "failed to collect exception", th2);
--
  45: }
  46: }
  47: int iG = s95.G(iqg.a);
--
  67: } catch (Throwable th3) {
  68: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  69: Iterator it2 = q1h.a.iterator();
  70: while (it2.hasNext()) {
  71: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  72: try {
  73: f09.c0("Payload", "error while parse payload", th3);
  74: accountInitializer2.c().j().d().a(null, th3);
  75: } catch (Throwable th4) {
  76: f09.c0("Payload", "failed to collect exception", th4);
--
  77: }
  78: }
  79: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/hsd.java
~~~text
  15: import java.util.regex.Matcher;
  16: import java.util.regex.Pattern;
  17: import kotlin.NoWhenBranchMatchedException;
  18: import me.leolin.shortcutbadger.BuildConfig;
  19: import one.me.android.initialization.AccountInitializer;
  20: 
  21: /* JADX INFO: loaded from: classes2.dex */
  22: public abstract class hsd {
  23: public static final by0 a = new by0((byte) 17);
  24: 
--
 330: } catch (Throwable th) {
 331: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 332: Iterator it = q1h.a.iterator();
 333: while (it.hasNext()) {
 334: AccountInitializer accountInitializer = ((z6) it.next()).a;
 335: try {
 336: f09.c0("Payload", "error while parse payload", th);
 337: accountInitializer.c().j().d().a(null, th);
 338: } catch (Throwable th2) {
 339: f09.c0("Payload", "failed to collect exception", th2);
--
 340: }
 341: }
 342: int iG = s95.G(iqg.a);
--
 357: } catch (Throwable th3) {
 358: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 359: Iterator it2 = q1h.a.iterator();
 360: while (it2.hasNext()) {
 361: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 362: try {
 363: f09.c0("Payload", "error while parse payload", th3);
 364: accountInitializer2.c().j().d().a(null, th3);
 365: } catch (Throwable th4) {
 366: f09.c0("Payload", "failed to collect exception", th4);
--
 367: }
 368: }
 369: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/ih0.java
~~~text
  12: import java.util.NoSuchElementException;
  13: import kotlin.NoWhenBranchMatchedException;
  14: import kotlin.collections.a;
  15: import one.me.android.fresco.FrescoExecutorFeature$ToggleService;
  16: import one.me.android.initialization.AccountInitializer;
  17: import org.json.JSONException;
  18: import org.json.JSONObject;
  19: import ru.ok.tracer.lite.TracerLite;
  20: import ru.ok.tracer.lite.crash.report.TracerCrashReportLite;
  21: 
--
  69: } catch (Throwable th) {
  70: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  71: Iterator it = q1h.a.iterator();
  72: while (it.hasNext()) {
  73: AccountInitializer accountInitializer = ((z6) it.next()).a;
  74: try {
  75: f09.c0("Payload", "error while parse payload", th);
  76: accountInitializer.c().j().d().a(null, th);
  77: } catch (Throwable th2) {
  78: f09.c0("Payload", "failed to collect exception", th2);
--
  79: }
  80: }
  81: int iG = s95.G(iqg.a);
--
  98: } catch (Throwable th3) {
  99: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 100: Iterator it2 = q1h.a.iterator();
 101: while (it2.hasNext()) {
 102: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 103: try {
 104: f09.c0("Payload", "error while parse payload", th3);
 105: accountInitializer2.c().j().d().a(null, th3);
 106: } catch (Throwable th4) {
 107: f09.c0("Payload", "failed to collect exception", th4);
--
 108: }
 109: }
 110: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/jl9.java
~~~text
  21: import java.util.Iterator;
  22: import java.util.List;
  23: import java.util.Set;
  24: import kotlin.NoWhenBranchMatchedException;
  25: import one.me.android.initialization.AccountInitializer;
  26: import org.json.JSONObject;
  27: import ru.ok.tamtam.nano.ProtoException;
  28: 
  29: /* JADX INFO: loaded from: classes2.dex */
  30: public final class jl9 implements gl9, i6c, o6a, p5e, hpc, v6j, snj, ezb, ek9, frc {
--
 173: } catch (Throwable th) {
 174: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 175: Iterator it = q1h.a.iterator();
 176: while (it.hasNext()) {
 177: AccountInitializer accountInitializer = ((z6) it.next()).a;
 178: try {
 179: f09.c0("Payload", "error while parse payload", th);
 180: accountInitializer.c().j().d().a(null, th);
 181: } catch (Throwable th2) {
 182: f09.c0("Payload", "failed to collect exception", th2);
--
 183: }
 184: }
 185: int iG = s95.G(iqg.a);
--
 200: } catch (Throwable th3) {
 201: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 202: Iterator it2 = q1h.a.iterator();
 203: while (it2.hasNext()) {
 204: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 205: try {
 206: f09.c0("Payload", "error while parse payload", th3);
 207: accountInitializer2.c().j().d().a(null, th3);
 208: } catch (Throwable th4) {
 209: f09.c0("Payload", "failed to collect exception", th4);
--
 210: }
 211: }
 212: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/k1j.java
~~~text
  13: import java.util.ArrayList;
  14: import java.util.List;
  15: import java.util.Set;
  16: import java.util.concurrent.CancellationException;
  17: import one.me.android.initialization.AccountInitializer;
  18: import one.me.pinbars.PinBarsWidget;
  19: import org.webrtc.PeerConnectionFactory;
  20: 
  21: /* JADX INFO: loaded from: classes.dex */
  22: public final class k1j extends x1j implements h18 {
--
  53: k1jVar3.f = (Throwable) obj2;
  54: k1jVar3.w(s1kVar);
  55: return s1kVar;
  56: case 3:
  57: k1j k1jVar4 = new k1j((AccountInitializer) this.g, (b55) obj3, b2);
  58: k1jVar4.f = (Throwable) obj2;
  59: k1jVar4.w(s1kVar);
  60: return s1kVar;
  61: case 4:
  62: k1j k1jVar5 = new k1j(this.g, (b55) obj3, (byte) 4);
--
 163: case 3:
 164: Throwable th4 = (Throwable) this.f;
 165: xnm.y(obj);
 166: if (!(th4 instanceof CancellationException)) {
 167: ((czc) ((yw6) vg9.u((AccountInitializer) this.g, 232))).a(th4);
 168: }
 169: return s1kVar;
 170: case 4:
 171: Throwable th5 = (Throwable) this.f;
 172: xnm.y(obj);
--
~~~

### defpackage/k7.java
~~~text
   1: package defpackage;
   2: 
   3: import one.me.android.initialization.AccountInitializer;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class k7 extends x1j implements e18 {
   7: public final /* synthetic */ byte e;
   8: public boolean f;
--
   9: public final /* synthetic */ AccountInitializer g;
  10: 
  11: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  12: public /* synthetic */ k7(AccountInitializer accountInitializer, b55 b55Var, byte b) {
  13: super(2, b55Var);
  14: this.e = b;
--
  15: this.g = accountInitializer;
  16: }
  17: 
--
  18: @Override // defpackage.e18
  19: public final Object invoke(Object obj, Object obj2) {
  20: byte b = this.e;
--
  30: 
  31: @Override // defpackage.hv0
  32: public final b55 u(b55 b55Var, Object obj) {
  33: byte b = this.e;
  34: AccountInitializer accountInitializer = this.g;
  35: switch (b) {
  36: case 0:
  37: return new k7(accountInitializer, b55Var, (byte) 0);
  38: default:
  39: return new k7(accountInitializer, b55Var, (byte) 1);
--
~~~

### defpackage/klc.java
~~~text
   9: import java.util.ArrayList;
  10: import java.util.List;
  11: import java.util.concurrent.CancellationException;
  12: import one.me.android.OneMeApplication;
  13: import one.me.android.initialization.AccountInitializer;
  14: import org.webrtc.PeerConnectionFactory;
  15: 
  16: /* JADX INFO: loaded from: classes.dex */
  17: public final class klc extends x1j implements e18 {
  18: public final /* synthetic */ byte e;
--
 109: return klcVar;
 110: case 1:
 111: return new klc((OneMeApplication) this.g, (j7) obj2, b55Var, (byte) 1);
 112: case 2:
 113: return new klc((AccountInitializer) this.g, (OneMeApplication) obj2, b55Var, (byte) 2);
 114: case 3:
 115: klc klcVar2 = new klc(obj2, b55Var, (byte) 3);
 116: klcVar2.g = obj;
 117: return klcVar2;
 118: case 4:
--
 291: }
 292: return s1kVar2;
 293: case 2:
 294: s1k s1kVar3 = s1k.a;
 295: AccountInitializer accountInitializer = (AccountInitializer) this.g;
 296: ka5 ka5Var3 = ka5.a;
 297: boolean z3 = this.f;
 298: if (!z3) {
 299: xnm.y(obj);
 300: z3j z3jVarD = accountInitializer.c().getAccessor().d(7);
--
 301: d0i d0iVar = new d0i(z3jVarD, accountInitializer.c().getAccessor().d(213));
 302: OneMeApplication oneMeApplication = (OneMeApplication) this.h;
 303: this.f = true;
 304: f09.p("PrefetchThemeBackgroundUseCase", "Prefetch chat themes.");
 305: String str = u34.j.a(oneMeApplication).h().c;
--
 306: fy9 fy9VarG = er0.g();
--
~~~

### defpackage/kwm.java
~~~text
  13: import java.util.concurrent.ExecutorService;
  14: import java.util.concurrent.Executors;
  15: import kotlin.NoWhenBranchMatchedException;
  16: import me.leolin.shortcutbadger.BuildConfig;
  17: import one.me.android.initialization.AccountInitializer;
  18: import org.json.JSONArray;
  19: import org.json.JSONException;
  20: import org.json.JSONObject;
  21: import ru.ok.android.api.http.NoHttpApiEndpointException;
  22: 
--
 112: } catch (Throwable th2) {
 113: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th2);
 114: Iterator it2 = q1h.a.iterator();
 115: while (it2.hasNext()) {
 116: AccountInitializer accountInitializer = ((z6) it2.next()).a;
 117: try {
 118: f09.c0("Payload", "error while parse payload", th2);
 119: accountInitializer.c().j().d().a(null, th2);
 120: } catch (Throwable th3) {
 121: f09.c0("Payload", "failed to collect exception", th3);
--
 122: }
 123: }
 124: int iG2 = s95.G(iqg.a);
--
 141: } catch (Throwable th4) {
 142: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th4);
 143: Iterator it3 = q1h.a.iterator();
 144: while (it3.hasNext()) {
 145: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
 146: try {
 147: f09.c0("Payload", "error while parse payload", th4);
 148: accountInitializer2.c().j().d().a(str2, th4);
 149: } catch (Throwable th5) {
 150: f09.c0("Payload", "failed to collect exception", th5);
--
 151: }
 152: }
 153: int iG3 = s95.G(iqg.a);
--
~~~

### defpackage/l6.java
~~~text
  11: import java.util.function.IntConsumer;
  12: import kotlin.NoWhenBranchMatchedException;
  13: import one.me.android.DailyAnalyticsWorker;
  14: import one.me.android.di.ConcurrentComponent;
  15: import one.me.android.initialization.AccountInitializer;
  16: import one.me.stories.core.workers.StoriesCleanupScheduler$StoriesCleanupWorker;
  17: import one.me.upload.cleanup.UploadsCleanupScheduler$UploadsCleanupWorker;
  18: import org.json.JSONObject;
  19: import org.webrtc.PeerConnectionFactory;
  20: import ru.ok.tamtam.android.messages.comments.MessageCommentsCleanupScheduler$MessageCommentsCleanupWorker;
--
  22: 
  23: /* JADX INFO: loaded from: classes.dex */
  24: public final /* synthetic */ class l6 implements o08 {
  25: public final /* synthetic */ byte a;
  26: public final /* synthetic */ AccountInitializer b;
  27: 
  28: public /* synthetic */ l6(AccountInitializer accountInitializer, byte b) {
  29: this.a = b;
  30: this.b = accountInitializer;
  31: }
--
  32: 
  33: /* JADX WARN: Multi-variable type inference failed */
--
  34: /* JADX WARN: Type inference failed for: r15v10 */
  35: /* JADX WARN: Type inference failed for: r15v11 */
--
  62: ?? r110 = 0;
  63: byte b5 = 0;
  64: switch (b) {
  65: case 0:
  66: AccountInitializer accountInitializer = this.b;
  67: ((qw4) vg9.u(accountInitializer, 241)).a();
  68: ((n83) s95.k(accountInitializer, 144)).s();
  69: j9e j9eVarF = accountInitializer.c().f();
  70: vck vckVar = (vck) vg9.u(accountInitializer, 138);
  71: mvi mviVar = new mvi(j9eVarF, vckVar, accountInitializer.c().getAccessor().d(161), accountInitializer.c().getAccessor().d(127));
--
~~~

### defpackage/lgc.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import one.me.android.initialization.AccountInitializer;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public final class lgc implements f84 {
   8: public static final lgc a;
   9: public static final /* synthetic */ zm9[] b;
--
  30: } catch (Throwable th) {
  31: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  32: Iterator it = q1h.a.iterator();
  33: while (it.hasNext()) {
  34: AccountInitializer accountInitializer = ((z6) it.next()).a;
  35: try {
  36: f09.c0("Payload", "error while parse payload", th);
  37: accountInitializer.c().j().d().a(null, th);
  38: } catch (Throwable th2) {
  39: f09.c0("Payload", "failed to collect exception", th2);
--
  40: }
  41: }
  42: int iG = s95.G(iqg.a);
--
  78: } catch (Throwable th3) {
  79: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  80: Iterator it2 = q1h.a.iterator();
  81: while (it2.hasNext()) {
  82: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  83: try {
  84: f09.c0("Payload", "error while parse payload", th3);
  85: accountInitializer2.c().j().d().a(null, th3);
  86: } catch (Throwable th4) {
  87: f09.c0("Payload", "failed to collect exception", th4);
--
  88: }
  89: }
  90: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/lhj.java
~~~text
  19: import java.util.List;
  20: import java.util.Set;
  21: import kotlin.NoWhenBranchMatchedException;
  22: import me.leolin.shortcutbadger.BuildConfig;
  23: import one.me.android.initialization.AccountInitializer;
  24: 
  25: /* JADX INFO: loaded from: classes2.dex */
  26: public abstract class lhj {
  27: public static final String[] a = {"_id", "lookup"};
  28: public static final String[] b = {"contact_id", "mimetype", "data2", "data3", "data5", "_id", "data1", "display_name", "photo_uri"};
--
 451: } catch (Throwable th) {
 452: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 453: Iterator it = q1h.a.iterator();
 454: while (it.hasNext()) {
 455: AccountInitializer accountInitializer = ((z6) it.next()).a;
 456: try {
 457: f09.c0("Payload", "error while parse payload", th);
 458: accountInitializer.c().j().d().a(null, th);
 459: } catch (Throwable th2) {
 460: f09.c0("Payload", "failed to collect exception", th2);
--
 461: }
 462: }
 463: int iG = s95.G(iqg.a);
--
 488: } catch (Throwable th3) {
 489: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 490: Iterator it2 = q1h.a.iterator();
 491: while (it2.hasNext()) {
 492: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 493: try {
 494: f09.c0("Payload", "error while parse payload", th3);
 495: accountInitializer2.c().j().d().a(null, th3);
 496: } catch (Throwable th4) {
 497: f09.c0("Payload", "failed to collect exception", th4);
--
 498: }
 499: }
 500: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/ljn.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes3.dex */
   8: public abstract class ljn {
   9: public static b2i a(beb bebVar) {
  10: int iP0;
--
  14: } catch (Throwable th) {
  15: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  16: Iterator it = q1h.a.iterator();
  17: while (it.hasNext()) {
  18: AccountInitializer accountInitializer = ((z6) it.next()).a;
  19: try {
  20: f09.c0("Payload", "error while parse payload", th);
  21: accountInitializer.c().j().d().a(null, th);
  22: } catch (Throwable th2) {
  23: f09.c0("Payload", "failed to collect exception", th2);
--
  24: }
  25: }
  26: int iG = s95.G(iqg.a);
--
  41: } catch (Throwable th3) {
  42: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  43: Iterator it2 = q1h.a.iterator();
  44: while (it2.hasNext()) {
  45: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  46: try {
  47: f09.c0("Payload", "error while parse payload", th3);
  48: accountInitializer2.c().j().d().a(null, th3);
  49: } catch (Throwable th4) {
  50: f09.c0("Payload", "failed to collect exception", th4);
--
  51: }
  52: }
  53: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/lrh.java
~~~text
   9: import java.util.Map;
  10: import java.util.concurrent.atomic.AtomicReference;
  11: import kotlin.NoWhenBranchMatchedException;
  12: import one.me.android.concurrent.SingleCoreFeature$ToggleService;
  13: import one.me.android.initialization.AccountInitializer;
  14: import one.me.webapp.util.WebAppNfcService;
  15: import org.json.JSONObject;
  16: 
  17: /* JADX INFO: loaded from: classes.dex */
  18: public final class lrh implements tl4, f84, w95, r4b, ijh, rl4 {
--
 161: } catch (Throwable th) {
 162: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 163: Iterator it = q1h.a.iterator();
 164: while (it.hasNext()) {
 165: AccountInitializer accountInitializer = ((z6) it.next()).a;
 166: try {
 167: f09.c0("Payload", "error while parse payload", th);
 168: accountInitializer.c().j().d().a(null, th);
 169: } catch (Throwable th2) {
 170: f09.c0("Payload", "failed to collect exception", th2);
--
 171: }
 172: }
 173: int iG = s95.G(iqg.a);
--
 187: } catch (Throwable th3) {
 188: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 189: Iterator it2 = q1h.a.iterator();
 190: while (it2.hasNext()) {
 191: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 192: try {
 193: f09.c0("Payload", "error while parse payload", th3);
 194: accountInitializer2.c().j().d().a(null, th3);
 195: } catch (Throwable th4) {
 196: f09.c0("Payload", "failed to collect exception", th4);
--
 197: }
 198: }
 199: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/m6.java
~~~text
   1: package defpackage;
   2: 
   3: import one.me.android.initialization.AccountInitializer;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final /* synthetic */ class m6 implements l4l {
   7: public final /* synthetic */ AccountInitializer a;
   8: 
--
   9: public /* synthetic */ m6(AccountInitializer accountInitializer) {
  10: this.a = accountInitializer;
  11: }
  12: 
--
  13: @Override // defpackage.l4l
  14: public long now() {
--
  15: return ((hog) ((c74) s95.k(this.a, 92))).f();
--
~~~

### defpackage/m7.java
~~~text
   1: package defpackage;
   2: 
   3: import android.os.Handler;
   4: import java.util.concurrent.atomic.AtomicBoolean;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes.dex */
   8: public final class m7 extends x1j implements e18 {
   9: public /* synthetic */ Object e;
  10: public final /* synthetic */ AtomicBoolean f;
--
  11: public final /* synthetic */ AccountInitializer g;
  12: public final /* synthetic */ Handler h;
  13: 
  14: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  15: public m7(AtomicBoolean atomicBoolean, AccountInitializer accountInitializer, Handler handler, b55 b55Var) {
  16: super(2, b55Var);
--
  17: this.f = atomicBoolean;
  18: this.g = accountInitializer;
  19: this.h = handler;
  20: }
--
  21: 
  22: @Override // defpackage.e18
  23: public final Object invoke(Object obj, Object obj2) {
--
~~~

### defpackage/myb.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import java.util.LinkedHashSet;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes3.dex */
   8: public final class myb extends x6j {
   9: public final long c;
  10: public final LinkedHashSet d;
--
  37: } catch (Throwable th) {
  38: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  39: Iterator it = q1h.a.iterator();
  40: while (it.hasNext()) {
  41: AccountInitializer accountInitializer = ((z6) it.next()).a;
  42: try {
  43: f09.c0("Payload", "error while parse payload", th);
  44: accountInitializer.c().j().d().a(null, th);
  45: } catch (Throwable th2) {
  46: f09.c0("Payload", "failed to collect exception", th2);
--
  47: }
  48: }
  49: int iG = s95.G(iqg.a);
--
~~~

### defpackage/n6.java
~~~text
  23: import java.util.concurrent.ConcurrentHashMap;
  24: import java.util.concurrent.atomic.AtomicInteger;
  25: import java.util.concurrent.locks.LockSupport;
  26: import java.util.concurrent.locks.ReentrantReadWriteLock;
  27: import one.me.android.initialization.AccountInitializer;
  28: import one.me.chats.list.ChatsListWidget;
  29: import org.webrtc.PeerConnectionFactory;
  30: import ru.ok.tamtam.exception.UserNotFoundException;
  31: import ru.ok.tracer.minidump.Minidump;
  32: 
--
 203: case 0:
 204: ((l6) this.b).c();
 205: return;
 206: case 1:
 207: dtc dtcVarA = ((AccountInitializer) this.b).c().a();
 208: dtcVarA.getClass();
 209: f09.p("dtc", "invalidate");
 210: if (dtcVarA.b()) {
 211: return;
 212: }
--
~~~

### defpackage/n7.java
~~~text
   4: import android.util.ArrayMap;
   5: import io.jsonwebtoken.Claims;
   6: import java.util.ArrayList;
   7: import java.util.List;
   8: import one.me.android.initialization.AccountInitializer;
   9: 
  10: /* JADX INFO: loaded from: classes.dex */
  11: public final class n7 extends x1j implements q08 {
  12: public final /* synthetic */ byte e;
  13: public boolean f;
--
  37: byte b = this.e;
  38: Object obj = this.g;
  39: switch (b) {
  40: case 0:
  41: return new n7((AccountInitializer) obj, b55Var, (byte) 0);
  42: default:
  43: return new n7((w1j) obj, b55Var, (byte) 1);
  44: }
  45: }
  46: 
--
  54: boolean z = this.f;
  55: try {
  56: if (!z) {
  57: xnm.y(obj);
  58: z3j z3jVarD = ((AccountInitializer) this.g).c().getAccessor().d(32);
  59: AccountInitializer accountInitializer = (AccountInitializer) this.g;
  60: b78 b78Var = new b78(z3jVarD, new z3j(new eb8(accountInitializer, (byte) 4)), accountInitializer.c().getAccessor().d(709), ((AccountInitializer) this.g).c().getAccessor().d(684), ((AccountInitializer) this.g).c().getAccessor().d(512), ((AccountInitializer) this.g).c().getAccessor().d(444));
  61: qzd qzdVar = fe6.b;
  62: long jU = az7.U(5, me6.e);
  63: f0 f0Var = new f0(b78Var, b55Var, b);
--
  64: this.f = true;
--
  65: obj = jd0.i0(jU, f0Var, this);
--
~~~

### defpackage/ngd.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes2.dex */
   8: public final class ngd {
   9: /* JADX WARN: Can't fix incorrect switch cases order, some code will duplicate */
  10: /* JADX WARN: Code duplicated, block: B:192:0x02b0 A[Catch: all -> 0x00a2, TRY_LEAVE, TryCatch #3 {all -> 0x00a2, blocks: (B:189:0x02a1, B:190:0x02aa, B:192:0x02b0, B:196:0x02cd, B:197:0x02d1, B:201:0x02dc, B:202:0x02e1, B:203:0x02e2, B:27:0x0063, B:28:0x006c, B:30:0x0072, B:34:0x008e, B:35:0x0092, B:38:0x009c, B:39:0x00a1, B:42:0x00a6, B
--
  35: } catch (Throwable th2) {
  36: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th2);
  37: Iterator it2 = q1h.a.iterator();
  38: while (it2.hasNext()) {
  39: AccountInitializer accountInitializer = ((z6) it2.next()).a;
  40: try {
  41: f09.c0("Payload", "error while parse payload", th2);
  42: accountInitializer.c().j().d().a(null, th2);
  43: } catch (Throwable th3) {
  44: f09.c0("Payload", "failed to collect exception", th3);
--
  45: }
  46: }
  47: int iG2 = s95.G(iqg.a);
--
  65: } catch (Throwable th4) {
  66: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th4);
  67: Iterator it3 = q1h.a.iterator();
  68: while (it3.hasNext()) {
  69: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
  70: try {
  71: f09.c0("Payload", "error while parse payload", th4);
  72: accountInitializer2.c().j().d().a(str, th4);
  73: } catch (Throwable th5) {
  74: f09.c0("Payload", "failed to collect exception", th5);
--
  75: }
  76: }
  77: int iG3 = s95.G(iqg.a);
--
~~~

### defpackage/nkn.java
~~~text
   2: 
   3: import android.content.Context;
   4: import java.util.Iterator;
   5: import kotlin.NoWhenBranchMatchedException;
   6: import one.me.android.initialization.AccountInitializer;
   7: 
   8: /* JADX INFO: loaded from: classes2.dex */
   9: public abstract class nkn {
  10: public static k58 a(Context context) {
  11: a08.y();
--
  31: } catch (Throwable th2) {
  32: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th2);
  33: Iterator it2 = q1h.a.iterator();
  34: while (it2.hasNext()) {
  35: AccountInitializer accountInitializer = ((z6) it2.next()).a;
  36: try {
  37: f09.c0("Payload", "error while parse payload", th2);
  38: accountInitializer.c().j().d().a(null, th2);
  39: } catch (Throwable th3) {
  40: f09.c0("Payload", "failed to collect exception", th3);
--
  41: }
  42: }
  43: int iG2 = s95.G(iqg.a);
--
  60: } catch (Throwable th4) {
  61: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th4);
  62: Iterator it3 = q1h.a.iterator();
  63: while (it3.hasNext()) {
  64: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
  65: try {
  66: f09.c0("Payload", "error while parse payload", th4);
  67: accountInitializer2.c().j().d().a(null, th4);
  68: } catch (Throwable th5) {
  69: f09.c0("Payload", "failed to collect exception", th5);
--
  70: }
  71: }
  72: int iG3 = s95.G(iqg.a);
--
~~~

### defpackage/nm9.java
~~~text
  30: import java.util.Map;
  31: import java.util.Set;
  32: import java.util.TimeZone;
  33: import kotlinx.coroutines.DispatchException;
  34: import one.me.android.initialization.AccountInitializer;
  35: import org.json.JSONArray;
  36: import org.json.JSONException;
  37: import org.xmlpull.v1.XmlPullParser;
  38: import ru.oneme.app.R;
  39: import sun.misc.Unsafe;
--
 250: } catch (Throwable th) {
 251: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 252: Iterator it2 = q1h.a.iterator();
 253: while (it2.hasNext()) {
 254: AccountInitializer accountInitializer = ((z6) it2.next()).a;
 255: try {
 256: f09.c0("Payload", "error while parse payload", th);
 257: accountInitializer.c().j().d().a(null, th);
 258: } catch (Throwable th2) {
 259: f09.c0("Payload", "failed to collect exception", th2);
--
 260: }
 261: }
 262: int iG = s95.G(iqg.a);
--
 284: } catch (Throwable th3) {
 285: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 286: Iterator it3 = q1h.a.iterator();
 287: while (it3.hasNext()) {
 288: AccountInitializer accountInitializer2 = ((z6) it3.next()).a;
 289: try {
 290: f09.c0("Payload", "error while parse payload", th3);
 291: accountInitializer2.c().j().d().a(r8, th3);
 292: } catch (Throwable th4) {
 293: f09.c0("Payload", "failed to collect exception", th4);
--
 294: }
 295: }
 296: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/nt6.java
~~~text
   8: import java.util.LinkedHashSet;
   9: import java.util.concurrent.CountDownLatch;
  10: import kotlin.NoWhenBranchMatchedException;
  11: import me.leolin.shortcutbadger.BuildConfig;
  12: import one.me.android.initialization.AccountInitializer;
  13: import ru.ok.tamtam.models.bots.Button$Intent;
  14: import ru.ok.tamtam.models.button.ButtonType;
  15: 
  16: /* JADX INFO: loaded from: classes.dex */
  17: public final class nt6 implements f84, g18, ev8, ezb {
--
  67: } catch (Throwable th) {
  68: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  69: Iterator it = q1h.a.iterator();
  70: while (it.hasNext()) {
  71: AccountInitializer accountInitializer = ((z6) it.next()).a;
  72: try {
  73: f09.c0("Payload", "error while parse payload", th);
  74: accountInitializer.c().j().d().a(null, th);
  75: } catch (Throwable th2) {
  76: f09.c0("Payload", "failed to collect exception", th2);
--
  77: }
  78: }
  79: int iG = s95.G(iqg.a);
--
  97: } catch (Throwable th3) {
  98: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  99: Iterator it2 = q1h.a.iterator();
 100: while (it2.hasNext()) {
 101: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 102: try {
 103: f09.c0("Payload", "error while parse payload", th3);
 104: accountInitializer2.c().j().d().a(null, th3);
 105: } catch (Throwable th4) {
 106: f09.c0("Payload", "failed to collect exception", th4);
--
 107: }
 108: }
 109: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/o6.java
~~~text
   1: package defpackage;
   2: 
   3: import android.content.IntentFilter;
   4: import one.me.android.OneMeApplication;
   5: import one.me.android.initialization.AccountInitializer;
   6: import one.me.android.mytracker.MyTrackerWrapper$MyTrackerException;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final /* synthetic */ class o6 implements o08 {
  10: public final /* synthetic */ byte a;
--
  11: public final /* synthetic */ AccountInitializer b;
  12: public final /* synthetic */ OneMeApplication c;
  13: 
  14: public /* synthetic */ o6(OneMeApplication oneMeApplication, AccountInitializer accountInitializer, byte b) {
  15: this.a = b;
  16: this.c = oneMeApplication;
--
  17: this.b = accountInitializer;
  18: }
  19: 
--
  20: /* JADX WARN: Type inference fix 'apply assigned field type' failed
  21: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
  22: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
--
  30: @Override // defpackage.o08
  31: public final Object c() {
  32: byte b = this.a;
  33: s1k s1kVar = s1k.a;
  34: AccountInitializer accountInitializer = this.b;
  35: OneMeApplication oneMeApplication = this.c;
  36: switch (b) {
  37: case 0:
  38: rp9 rp9VarG = accountInitializer.c().g();
  39: j9e j9eVarF = accountInitializer.c().f();
--
~~~

### defpackage/pdc.java
~~~text
   8: import java.util.ArrayList;
   9: import java.util.Iterator;
  10: import java.util.List;
  11: import kotlin.NoWhenBranchMatchedException;
  12: import one.me.android.initialization.AccountInitializer;
  13: import org.json.JSONObject;
  14: 
  15: /* JADX INFO: loaded from: classes.dex */
  16: public class pdc implements f84, snj, w95, yda, k6c, ek9, rl4 {
  17: public static pdc b;
--
 222: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th4);
 223: try {
 224: Iterator it7 = q1h.a.iterator();
 225: while (it7.hasNext()) {
 226: AccountInitializer accountInitializer = ((z6) it7.next()).a;
 227: try {
 228: f09.c0("Payload", "error while parse payload", th4);
 229: accountInitializer.c().j().d().a(str2, th4);
 230: } catch (Throwable th5) {
 231: f09.c0("Payload", "failed to collect exception", th5);
--
 232: }
 233: }
 234: int iG4 = s95.G(iqg.a);
--
 243: qp6Var = qp6Var;
 244: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
 245: it = q1h.a.iterator();
 246: while (it.hasNext()) {
 247: AccountInitializer accountInitializer2 = ((z6) it.next()).a;
 248: try {
 249: f09.c0("Payload", "error while parse payload", th);
 250: accountInitializer2.c().j().d().a(null, th);
 251: } catch (Throwable th7) {
 252: f09.c0("Payload", "failed to collect exception", th7);
--
 253: }
 254: }
 255: iG = s95.G(iqg.a);
--
~~~

### defpackage/ped.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import one.me.android.initialization.AccountInitializer;
   5: 
   6: /* JADX INFO: loaded from: classes2.dex */
   7: public abstract class ped {
   8: public static final nln a = new nln(16);
   9: 
--
  25: } catch (Throwable th) {
  26: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  27: Iterator it = q1h.a.iterator();
  28: while (it.hasNext()) {
  29: AccountInitializer accountInitializer = ((z6) it.next()).a;
  30: try {
  31: f09.c0("Payload", "error while parse payload", th);
  32: accountInitializer.c().j().d().a(null, th);
  33: } catch (Throwable th2) {
  34: f09.c0("Payload", "failed to collect exception", th2);
--
  35: }
  36: }
  37: int iG = s95.G(iqg.a);
--
  55: } catch (Throwable th3) {
  56: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  57: Iterator it2 = q1h.a.iterator();
  58: while (it2.hasNext()) {
  59: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  60: try {
  61: f09.c0("Payload", "error while parse payload", th3);
  62: accountInitializer2.c().j().d().a(null, th3);
  63: } catch (Throwable th4) {
  64: f09.c0("Payload", "failed to collect exception", th4);
--
  65: }
  66: }
  67: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/po.java
~~~text
   1: package defpackage;
   2: 
   3: import java.util.Iterator;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.android.initialization.AccountInitializer;
   6: 
   7: /* JADX INFO: loaded from: classes3.dex */
   8: public final class po {
   9: public final long a;
  10: public final long b;
--
  34: } catch (Throwable th) {
  35: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  36: Iterator it = q1h.a.iterator();
  37: while (it.hasNext()) {
  38: AccountInitializer accountInitializer = ((z6) it.next()).a;
  39: try {
  40: f09.c0("Payload", "error while parse payload", th);
  41: accountInitializer.c().j().d().a(null, th);
  42: } catch (Throwable th2) {
  43: f09.c0("Payload", "failed to collect exception", th2);
--
  44: }
  45: }
  46: int iG = s95.G(iqg.a);
--
  66: } catch (Throwable th3) {
  67: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  68: Iterator it2 = q1h.a.iterator();
  69: while (it2.hasNext()) {
  70: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  71: try {
  72: f09.c0("Payload", "error while parse payload", th3);
  73: accountInitializer2.c().j().d().a(null, th3);
  74: } catch (Throwable th4) {
  75: f09.c0("Payload", "failed to collect exception", th4);
--
  76: }
  77: }
  78: int iG2 = s95.G(iqg.a);
--
~~~

### defpackage/pom.java
~~~text
   4: import java.util.ArrayList;
   5: import java.util.Iterator;
   6: import kotlin.NoWhenBranchMatchedException;
   7: import kotlinx.serialization.SerializationException;
   8: import one.me.android.initialization.AccountInitializer;
   9: import org.json.JSONObject;
  10: 
  11: /* JADX INFO: loaded from: classes2.dex */
  12: public abstract class pom {
  13: public static final /* synthetic */ int a = 0;
--
  61: } catch (Throwable th) {
  62: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  63: Iterator it = q1h.a.iterator();
  64: while (it.hasNext()) {
  65: AccountInitializer accountInitializer = ((z6) it.next()).a;
  66: try {
  67: f09.c0("Payload", "error while parse payload", th);
  68: accountInitializer.c().j().d().a(null, th);
  69: } catch (Throwable th2) {
  70: f09.c0("Payload", "failed to collect exception", th2);
--
  71: }
  72: }
  73: int iG = s95.G(iqg.a);
--
  91: } catch (Throwable th3) {
  92: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
  93: Iterator it2 = q1h.a.iterator();
  94: while (it2.hasNext()) {
  95: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
  96: try {
  97: f09.c0("Payload", "error while parse payload", th3);
  98: accountInitializer2.c().j().d().a(null, th3);
  99: } catch (Throwable th4) {
 100: f09.c0("Payload", "failed to collect exception", th4);
--
 101: }
 102: }
 103: int iG2 = s95.G(iqg.a);
--
~~~

## network / handshake
Файлов с совпадениями (первые 85): 64

### androidx/media3/datasource/HttpDataSource$HttpDataSourceException.java
~~~text
  28: i2 = 1004;
  29: } else {
  30: i2 = (message == null \|\| !eug.b0(message).matches("cleartext.*not permitted.*")) ? 2001 : 2007;
  31: }
  32: return i2 == 2007 ? new HttpDataSource$CleartextNotPermittedException("Cleartext HTTP traffic not permitted. See https://developer.android.com/guide/topics/media/issues/cleartext-not-permitted", iOException, 2007) : new HttpDataSource$HttpDataSourceException(i2, i, iOException);
  33: }
  34: 
  35: public HttpDataSource$HttpDataSourceException(String str, int i) {
  36: super(str, i == 2000 ? 2001 : i);
  37: this.b = (byte) 1;
--
~~~

### com/google/android/gms/ads/identifier/zza.java
~~~text
  12: }
  13: 
  14: @Override // java.lang.Thread, java.lang.Runnable
  15: public final void run() {
  16: Uri.Builder builderBuildUpon = Uri.parse("https://pagead2.googlesyndication.com/pagead/gen_204?id=gmob-apps").buildUpon();
  17: Map map = this.zza;
  18: for (String str : map.keySet()) {
  19: builderBuildUpon.appendQueryParameter(str, (String) map.get(str));
  20: }
  21: zze.zza(builderBuildUpon.build().toString());
--
~~~

### com/google/android/gms/auth/api/signin/GoogleSignInOptions.java
~~~text
  46: Scope scope = new Scope(1, "profile");
  47: new Scope(1, "email");
  48: Scope scope2 = new Scope(1, "openid");
  49: l = scope2;
  50: Scope scope3 = new Scope(1, "https://www.googleapis.com/auth/games_lite");
  51: m = scope3;
  52: n = new Scope(1, "https://www.googleapis.com/auth/games");
  53: HashSet hashSet = new HashSet();
  54: HashMap map = new HashMap();
  55: hashSet.add(scope2);
--
  56: hashSet.add(scope);
  57: if (hashSet.contains(n)) {
--
~~~

### com/google/android/play/core/install/InstallException.java
~~~text
  20: Integer numValueOf2 = Integer.valueOf(i);
  21: if (map.containsKey(numValueOf2)) {
  22: HashMap map2 = ilm.b;
  23: if (map2.containsKey(numValueOf2)) {
  24: str = ((String) map.get(numValueOf2)) + " (https://developer.android.com/reference/com/google/android/play/core/install/model/InstallErrorCode#" + ((String) map2.get(numValueOf2)) + ")";
  25: } else {
  26: str = BuildConfig.FLAVOR;
  27: }
  28: } else {
  29: str = BuildConfig.FLAVOR;
--
~~~

### defpackage/acc.java
~~~text
  96: } else if (this.b.h.get() \|\| z3) {
  97: if (z3) {
  98: bcc bccVar2 = this.b;
  99: if (bccVar2.h.get()) {
 100: fldVar.b.c.f(new l6j("session.state", "SESSION_INIT already initialized", null));
 101: } else if (bccVar2.d(fldVar, d5h.class)) {
 102: fldVar.b.c.f(new l6j("session.state", "SESSION_INIT already requested", null));
 103: }
 104: f09.d0(this.b.a, "Double session init detected, skipping", new Object[0]);
 105: arrayList.add(fldVar);
--
 106: }
 107: if (fldVar.e) {
--
~~~

### defpackage/ahg.java
~~~text
 449: lshVar.e = 1;
 450: return ri7Var.b(obj21, lshVar) == ka5Var ? ka5Var : s1kVar;
 451: }
 452: if (k4iVar instanceof v0k) {
 453: k3g.o("This is a bug in DataStore. Please file a bug at: https://issuetracker.google.com/issues/new?component=907884&template=1466542");
 454: } else {
 455: k3g.l();
 456: }
 457: } else {
 458: if (i27 == 1) {
--
~~~

### defpackage/apm.java
~~~text
  73: }
  74: if (str.length() != 0 && (lastPathSegment = Uri.parse(str).getLastPathSegment()) != null) {
  75: str2 = lastPathSegment;
  76: }
  77: return "https://max.ru/joincall/".concat(str2);
  78: }
  79: }
--
~~~

### defpackage/ax9.java
~~~text
  15: int i = 1;
  16: if (str.length() >= 4) {
  17: if (zti.k0(str, ' ', 0, 6) >= 0) {
  18: i = 2;
  19: } else if (hui.Z(str, "https://", true) \|\| ((fi1Var.a && hui.Z(str, "http://", true)) \|\| (fi1Var.b && hui.Z(str, "max://", true)))) {
  20: i = (((Pattern) this.b.getValue()).matcher(str).matches() \|\| ((yx9) this.a.getValue()).d(str)) ? 0 : 3;
  21: } else {
  22: i = 4;
  23: }
  24: }
--
~~~

### defpackage/b07.java
~~~text
2622: String name = Thread.currentThread().getName();
2623: String name2 = looper.getThread().getName();
2624: String str = sgk.a;
2625: Locale locale = Locale.US;
2626: String strV = w7g.v("Player is accessed on the wrong thread.\nCurrent thread: '", name, "'\nExpected thread: '", name2, "'\nSee https://developer.android.com/guide/topics/media/issues/player-accessed-on-wrong-thread");
2627: if (this.g0) {
2628: k3g.o(strV);
2629: } else {
2630: i5a.i("ExoPlayerImpl", strV, this.h0 ? null : new IllegalStateException());
2631: this.h0 = true;
--
~~~

### defpackage/bh5.java
~~~text
 150: if (ywm.i(3, "CXCP")) {
 151: Log.d("CXCP", "Device is known to throw an exception while retrieving the value for CameraCharacteristics.CONTROL_ZOOM_RATIO_RANGE. CONTROL_ZOOM_RATIO_RANGE is not supported. [Manufacturer: " + Build.MANUFACTURER + ", Model: " + Build.MODEL + ", API Level: " + Build.VERSION.SDK_INT + "].");
 152: }
 153: } else if (ywm.i(6, "CXCP")) {
 154: Log.e("CXCP", "Exception thrown while retrieving the value for CameraCharacteristics.CONTROL_ZOOM_RATIO_RANGE on devices not known to throw exceptions during this operation. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: " + Build.MANUFACTURER + "
 155: }
 156: if (ywm.i(5, "CXCP")) {
 157: Log.w("CXCP", "AssertionError: failed to get CameraCharacteristics.CONTROL_ZOOM_RATIO_RANGE", e);
 158: }
 159: range = null;
--
~~~

### defpackage/bnb.java
~~~text
2847: if (jA != 0) {
2848: lastPathSegment = String.format(Locale.getDefault(), "c/%d", Long.valueOf(jA));
2849: if (!TextUtils.isEmpty(lastPathSegment)) {
2850: Locale.getDefault();
2851: string = yx9.b(j, "https://max.ru/" + lastPathSegment + "/").toString();
2852: }
2853: }
2854: } else if (!TextUtils.isEmpty(str2)) {
2855: lastPathSegment = Uri.parse(str2).getLastPathSegment();
2856: if (!TextUtils.isEmpty(lastPathSegment)) {
--
2857: Locale.getDefault();
2858: string = yx9.b(j, "https://max.ru/" + lastPathSegment + "/").toString();
2859: }
2860: }
2861: h74.a(k1(), string);
2862: if (h74.b()) {
2863: this.R2.e(new omh(new mdj(R.string.chat_screen_action_share_post_success_copied), Integer.valueOf(R.drawable.icon_check_round_fill), null, 4));
--
~~~

### defpackage/c5h.java
~~~text
  88: o1dVar.c(c6aVar, str3, "Invoked 'onSessionInitHandled', but traceId is null or empty!", null);
  89: }
  90: }
  91: } else {
  92: wud.h(s8a.i, "session_init_handled", 5, str2, false, null, null, 120);
  93: }
  94: if (strC == null \|\| strC.length() == 0) {
  95: return;
  96: }
  97: f09.p(this.f, "SessionInit: Send Login command");
--
~~~

### defpackage/cfj.java
~~~text
  25: 
  26: @Override // defpackage.phj
  27: public final mhj a(int i, int i2, int i3) {
  28: z3j z3jVar = qhj.a;
  29: StringBuilder sb = new StringBuilder("https://tiles.api-maps.yandex.ru/v1/tiles/?lang=ru_RU&l=map&projection=web_mercator&maptype=future_map&");
  30: int i4 = this.c;
  31: if (i4 != 1) {
  32: sb.append("scale=");
  33: sb.append(i4);
  34: sb.append('&');
--
~~~

### defpackage/cj0.java
~~~text
 385: if (str8 == null \|\| zti.n0(str8)) {
 386: str8 = null;
 387: }
 388: if (str8 == null) {
 389: str8 = "https://st.max.ru/emojis_sprites/emoji_sprite_";
 390: }
 391: jo6 jo6Var3 = (jo6) this.j;
 392: int i9 = ((on6) this.k).a;
 393: jo6Var3.getClass();
 394: String str9 = str8 + i9 + ".webp";
--
~~~

### defpackage/d2d.java
~~~text
 249: while (i11 > i10 && zti.b0(".,;:!?)]>}\"'", spannableD.charAt(i11 - 1))) {
 250: i11--;
 251: }
 252: if (i11 > i10) {
 253: if (d1d.c(spannableD, i10, i11, "http://") \|\| d1d.c(spannableD, i10, i11, "https://") \|\| d1d.c(spannableD, i10, i11, "rtsp://")) {
 254: String str7 = d1dVar2.b;
 255: o1d o1dVar2 = f09.g;
 256: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
 257: o1dVar2.c(c6aVar, str7, "isWebUrlCandidate: found web schema", null);
 258: }
--
~~~

### defpackage/d2l.java
~~~text
  49: case 6:
  50: u6a u6aVar2 = ick.a;
  51: return new mbi((n4h) j0g.r.getValue());
  52: default:
  53: return new URI("https://stats-dg.rustore.ru").resolve("/v1/send_custom_event_batch").toURL();
  54: }
  55: }
  56: 
  57: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  58: public /* synthetic */ d2l(int i2, byte b) {
--
~~~

### defpackage/df.java
~~~text
  85: ((jq) obj3).b.z((geg) obj, (ArrayList) obj2);
  86: return s1kVar;
  87: case 3:
  88: dy dyVar = (dy) obj3;
  89: a8g.w(new r(dyVar, (byte) 11), (Activity) obj2, ((yx) obj).a == 2 ? "https://play.google.com/store/apps/details?id=ru.oneme.app" : (String) dyVar.a.getValue());
  90: return s1kVar;
  91: case 4:
  92: u30 u30Var = (u30) obj2;
  93: List list = (List) obj;
  94: cb4.x0(list, new y20(lkh.O0((n00) obj3), null == true ? 1 : 0));
--
~~~

### defpackage/dp5.java
~~~text
 198: pl8 pl8Var = (pl8) obj2;
 199: return new sl8(pl8Var.a, pl8Var.c, pl8Var.e);
 200: case 27:
 201: int i3 = gm8.o;
 202: return Boolean.valueOf(((m66) ((gm8) obj2).c.getValue()).b(gm8.m, "api2.oneme.ru"));
 203: case 28:
 204: mt8 mt8Var = (mt8) obj2;
 205: lrh lrhVar = u34.j;
 206: lrhVar.f(mt8Var);
 207: Drawable drawableMutate = mt8Var.getContext().getDrawable(R.drawable.icon_cross).mutate();
--
~~~

### defpackage/dw9.java
~~~text
1246: qw4 qw4Var = (qw4) this.a.getValue();
1247: ye5 ye5Var = (ye5) this.p.getValue();
1248: yx9VarD.getClass();
1249: String string2 = uri4.toString();
1250: if (string2.equalsIgnoreCase("max.ru") \|\| string2.equalsIgnoreCase("http://max.ru") \|\| string2.equalsIgnoreCase("https://max.ru")) {
1251: obj = obj3;
1252: tx9Var = null;
1253: } else {
1254: String string3 = uri4.toString();
1255: if (string3.equalsIgnoreCase("max://max.ru") \|\| string3.equalsIgnoreCase("max://max.ru/")) {
--
1256: ku9Var = ku9Var;
1257: obj = obj3;
1258: qx9Var = new qx9(0L, 0L, 0L, 0L);
1259: } else if (uri4.toString().equalsIgnoreCase("https://max.ru/:share-self-out")) {
1260: ku9Var = ku9Var;
1261: obj = obj3;
1262: tx9Var = new rx9(0L, 0L, 0L, 0L);
1263: } else {
1264: String host = uri4.getHost();
--
~~~

### defpackage/er0.java
~~~text
 538: }
 539: }
 540: file = (File) o08Var.c();
 541: if (file != null \|\| !file.exists()) {
 542: str = "checkFilesDirAvailable: filesDir returns " + file + " which is not an existing directory. See https://issuetracker.google.com/issues/36918154";
 543: if (vc7Var != null) {
 544: return false;
 545: }
 546: vc7Var.a(str, new IllegalStateException(str));
 547: return false;
--
 622: }
 623: file = (File) o08Var.c();
 624: if (file != null) {
 625: }
 626: str = "checkFilesDirAvailable: filesDir returns " + file + " which is not an existing directory. See https://issuetracker.google.com/issues/36918154";
 627: if (vc7Var != null) {
 628: return false;
 629: }
 630: vc7Var.a(str, new IllegalStateException(str));
 631: return false;
--
~~~

### defpackage/ftm.java
~~~text
  23: jy7 jy7Var = c;
  24: Status status = Status.g;
  25: try {
  26: String str = this.a;
  27: HttpURLConnection httpURLConnection = (HttpURLConnection) new URL(str.length() != 0 ? "https://accounts.google.com/o/oauth2/revoke?token=".concat(str) : new String("https://accounts.google.com/o/oauth2/revoke?token=")).openConnection();
  28: httpURLConnection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
  29: int responseCode = httpURLConnection.getResponseCode();
  30: if (responseCode == 200) {
  31: status = Status.e;
  32: } else {
--
~~~

### defpackage/gom.java
~~~text
   7: import java.net.URL;
   8: 
   9: /* JADX INFO: loaded from: classes3.dex */
  10: public abstract class gom {
  11: public static final String[] a = {"http://play.google.com", "https://play.google.com", "http://market.android.com", "https://market.android.com", "https://appgallery.huawei.com/", "https://appgallery.cloud.huawei.com/", "market://", "samsungapps://", "appmarket://", "hiapplink://", "mimarket://", "https://apps.rustore.ru", "https://backap
  12: 
  13: public static boolean a(String str) {
  14: if (TextUtils.isEmpty(str)) {
  15: return false;
  16: }
--
~~~

### defpackage/hg7.java
~~~text
  51: }
  52: 
  53: public static URL a(String str) {
  54: try {
  55: return new URL("https://firebaseinstallations.googleapis.com/v1/".concat(str));
  56: } catch (MalformedURLException e2) {
  57: throw new FirebaseInstallationsException(e2.getMessage());
  58: }
  59: }
  60: 
--
~~~

### defpackage/j9e.java
~~~text
 770: this.v = g9eVar14;
 771: g9e g9eVar15 = new g9e(this, 0, true, false, luf.a(Integer.class), 1, v59Var, v59Var2);
 772: g9eVar15.b(zm9VarArr[14]);
 773: this.w = g9eVar15;
 774: g9e g9eVar16 = new g9e(this, "https://download.cdn.oneme.ru/android/patch/%vendor%/%abi%/%version%/%file%", false, false, luf.a(String.class), 1, v59Var, v59Var2);
 775: final byte b9 = 15;
 776: g9eVar16.b(zm9VarArr[15]);
 777: this.x = g9eVar16;
 778: g9e g9eVar17 = new g9e(this, null, true, false, luf.a(String.class), 1, v59Var, v59Var2);
 779: final byte b10 = 16;
--
 794: g9e g9eVar22 = new g9e(this, 2, false, false, luf.a(Integer.class), 1, v59Var, v59Var2);
 795: byte b11 = 21;
 796: g9eVar22.b(zm9VarArr[21]);
 797: this.D = g9eVar22;
 798: g9e g9eVar23 = new g9e(this, "https://max.ru", false, false, luf.a(String.class), 1, v59Var, v59Var2);
 799: g9eVar23.b(zm9VarArr[22]);
 800: this.E = g9eVar23;
 801: b54 b54VarA = luf.a(String.class);
 802: z3j z3jVarQ = xnm.q(new f9e(b11));
 803: String name = ((mg2) zm9VarArr[23]).getName();
--
1817: }), v59Var2);
1818: g9eVar85.b(zm9VarArr[91]);
1819: this.O0 = g9eVar85;
1820: final byte b22 = 23;
1821: g9e g9eVar86 = new g9e(this, "https://max.ru", false, false, luf.a(String.class), 2, xnm.q(new o08() { // from class: y8e
1822: @Override // defpackage.o08
1823: public final Object c() {
1824: switch (b22) {
1825: case 0:
1826: return "Мультизакрепы в личных чатах";
--
9743: this.C5 = g9eVar333;
9744: g9e g9eVar334 = new g9e(this, bool, false, false, luf.a(Boolean.class), 1, v59Var, v59Var2);
9745: g9eVar334.b(zm9VarArr[342]);
9746: this.D5 = g9eVar334;
9747: g9e g9eVar335 = new g9e(this, "https://vkvideo.ru/live", false, false, luf.a(String.class), 1, v59Var, v59Var2);
9748: g9eVar335.b(zm9VarArr[343]);
9749: this.E5 = g9eVar335;
9750: g9e g9eVar336 = new g9e(this, bool, false, false, luf.a(Boolean.class), 1, xnm.q(new o08() { // from class: d9e
9751: @Override // defpackage.o08
9752: public final Object c() {
--
13511: }
13512: }), v59Var2);
13513: g9eVar446.b(zm9VarArr[458]);
13514: this.L7 = g9eVar446;
13515: g9e g9eVar447 = new g9e(this, jfa.G(g4a.P("MEDICAL_PORTRAIT", "https://st.max.ru/images/disclaimers/medical_portrait.png"), g4a.P("MEDICAL_LANDSCAPE", "https://st.max.ru/images/disclaimers/medical_landscape.png"), g4a.P("DRUGS_PORTRAIT", "https://st.max.ru/images/disclaimers/drugs_portrait.png"), g4a.P("DRUGS_LANDSCAPE", "https://st.max.r
13516: @Override // defpackage.o08
13517: public final Object c() {
13518: switch (b133) {
13519: case 0:
13520: return "Мультизакрепы в личных чатах";
--
~~~

### defpackage/jam.java
~~~text
  31: this.f = host;
  32: int port = uri.getPort();
  33: this.g = port;
  34: try {
  35: URI uri2 = new URI("https://" + host + ":" + port);
  36: new HashMap();
  37: Optional.empty();
  38: j8c j8cVar = uamVar.g;
  39: j8cVar.getClass();
  40: int port2 = uri2.getPort();
--
~~~

### defpackage/jg7.java
~~~text
 236: 
 237: public final void f() {
 238: gg7 gg7Var = this.a;
 239: gg7Var.a();
 240: g4a.j(gg7Var.c.b, "Please set your Application ID. A valid Firebase App ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.");
 241: gg7Var.a();
 242: g4a.j(gg7Var.c.g, "Please set your Project ID. A valid Firebase Project ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.");
 243: gg7Var.a();
 244: g4a.j(gg7Var.c.a, "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.");
 245: gg7Var.a();
--
 246: String str = gg7Var.c.b;
 247: Pattern pattern = vgk.a;
--
 248: g4a.f("Please set your Application ID. A valid Firebase App ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.", str.contains(":"));
 249: gg7Var.a();
--
 250: g4a.f("Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.", vgk.a.matcher(gg7Var.c.a).matches());
 251: }
 252: 
 253: /* JADX WARN: Code duplicated, block: B:15:0x003d A[Catch: all -> 0x003f, DONT_GENERATE, TRY_ENTER, TryCatch #1 {all -> 0x003f, blocks: (B:10:0x002e, B:11:0x0030, B:15:0x003d, B:19:0x0041, B:20:0x0045, B:28:0x0054, B:12:0x0031, B:13:0x003a), top: B:35:0x002e, inners: #0 }] */
--
 254: /* JADX WARN: Code duplicated, block: B:19:0x0041 A[Catch: all -> 0x003f, TryCatch #1 {all -> 0x003f, blocks: (B:10:0x002e, B:11:0x0030, B:15:0x003d, B:19:0x0041, B:20:0x0045, B:28:0x0054, B:12:0x0031, B:13:0x003a), top: B:35:0x002e, inners: #0 }] */
 255: /* JADX WARN: Code duplicated, block: B:23:0x004c  */
--
~~~

### defpackage/jnj.java
~~~text
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final /* synthetic */ class jnj implements s7f {
   5: @Override // defpackage.s7f
   6: public final Object get() {
   7: return "https://sdk-api.apptracer.ru";
   8: }
   9: }
--
~~~

### defpackage/js7.java
~~~text
 231: } catch (SQLiteAccessPermException \| SQLiteCantOpenDatabaseException \| SQLiteConstraintException \| SQLiteDatabaseCorruptException \| SQLiteDatabaseLockedException \| SQLiteDiskIOException \| SQLiteFullException \| SQLiteTableLockedException e2) {
 232: int i = this.d + 1;
 233: this.d = i;
 234: if (i >= 3) {
 235: String str2 = lvm.a(context) ? "The file system on the device is in a bad state. WorkManager cannot access the app's internal data store." : "WorkManager can't be accessed from direct boot, because credential encrypted storage isn't accessible.\nDon't access or initialise WorkManager from directAware components. See https://developer.andr
 236: a08.x().s(str, str2, e2);
 237: IllegalStateException illegalStateException = new IllegalStateException(str2, e2);
 238: to4Var.getClass();
 239: throw illegalStateException;
 240: }
--
~~~

### defpackage/jt.java
~~~text
   4: import io.jsonwebtoken.JwtParser;
   5: 
   6: /* JADX INFO: loaded from: classes3.dex */
   7: public abstract class jt {
   8: public static final Uri a = Uri.parse("https://api2.ok.ru");
   9: 
  10: public static Uri a() {
  11: return a;
  12: }
  13: 
--
~~~

### defpackage/jy7.java
~~~text
 760: int iIndexOf = strY.indexOf("</DATA>");
 761: if (iIndexOf == -1) {
 762: i5a.h("FrameworkMediaDrm", "Could not find the </DATA> tag. Skipping LA_URL workaround.");
 763: }
 764: String str2 = strY.substring(0, iIndexOf) + "<LA_URL>https://x</LA_URL>" + strY.substring(iIndexOf);
 765: int i6 = iO + 52;
 766: ByteBuffer byteBufferAllocate = ByteBuffer.allocate(i6);
 767: byteBufferAllocate.order(ByteOrder.LITTLE_ENDIAN);
 768: byteBufferAllocate.putInt(i6);
 769: byteBufferAllocate.putShort(sQ);
--
 802: if (pd1.c.equals(uuid) && Build.VERSION.SDK_INT < 27) {
 803: data = sgk.s(data).replace('+', '-').replace('/', '_').getBytes(StandardCharsets.UTF_8);
 804: }
 805: String defaultUrl = keyRequest.getDefaultUrl();
 806: if ("<LA_URL>https://x</LA_URL>".equals(defaultUrl)) {
 807: defaultUrl = BuildConfig.FLAVOR;
 808: } else if (Build.VERSION.SDK_INT >= 33 && "https://default.url".equals(defaultUrl)) {
 809: String propertyString = mediaDrm.getPropertyString("version");
 810: if (Objects.equals(propertyString, "1.2") \|\| Objects.equals(propertyString, "aidl-1")) {
 811: defaultUrl = BuildConfig.FLAVOR;
--
 812: }
 813: }
--
~~~

### defpackage/jzm.java
~~~text
  53: } catch (IllegalArgumentException e) {
  54: if (!Build.MANUFACTURER.equals("motorola")) {
  55: throw e;
  56: }
  57: i5a.e("MediaSessionLegacyStub", "caught IllegalArgumentException on a motorola device when attempting to set the media button broadcast receiver. See https://github.com/androidx/media/issues/1730 for details.", e);
  58: }
  59: }
  60: }
--
~~~

### defpackage/kr6.java
~~~text
 177: int i2 = Build.VERSION.SDK_INT;
 178: if (i2 >= 31) {
 179: str = ", SOC: " + Build.SOC_MODEL;
 180: }
 181: ywm.e("VideoTimebaseConverter", String.format("Detected camera timebase inconsistent. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Model: %s, Hardware: %s, API Level: %d%s].\nCamera timebase is inconsistent. The timebase reported by the came
 182: }
 183: gijVar = gijVar2;
 184: qxaVar.e = gijVar;
 185: }
 186: int iOrdinal = gijVar.ordinal();
--
~~~

### defpackage/mw6.java
~~~text
  37: str.getClass();
  38: switch (str) {
  39: case "urn:scte:scte35:2014:bin":
  40: return h;
  41: case "https://aomedia.org/emsg/ID3":
  42: case "https://developer.apple.com/streaming/emsg-id3":
  43: return g;
  44: default:
  45: return null;
  46: }
--
  47: }
--
~~~

### defpackage/mxl.java
~~~text
  52: int i2 = lxlVar.f;
  53: b55 b55Var = null;
  54: if (i2 == 0) {
  55: xnm.y(objI0);
  56: String str = "https://geocode-maps.yandex.ru/v1?lang=ru_RU&results=1&format=json&geocode=" + d2 + ',' + d + "&apikey=" + this.b;
  57: ly lyVar = new ly();
  58: lyVar.c("GET", null);
  59: lyVar.f(str);
  60: o0g o0gVarA = lyVar.a();
  61: z95 z95VarD = ((vxc) this.a).d();
--
~~~

### defpackage/n95.java
~~~text
  22: 
  23: public final String b() {
  24: lqh lqhVar = this.a;
  25: if (lqhVar == null) {
  26: return "https://sdk-api.apptracer.ru";
  27: }
  28: try {
  29: Object obj = lqhVar.a;
  30: if (obj != null) {
  31: return (String) obj;
--
  32: }
  33: throw new IllegalArgumentException("Required value was null.");
  34: } catch (Exception unused) {
  35: return "https://sdk-api.apptracer.ru";
  36: }
  37: }
  38: }
--
~~~

### defpackage/nxg.java
~~~text
  30: if (o1dVar.b(c6aVar)) {
  31: o1dVar.c(c6aVar, str2, "SessionInit.recoveryUrl is empty, try use default", null);
  32: }
  33: }
  34: return a(Uri.parse("https://go.max.ru/recovery"), i);
  35: }
  36: try {
  37: n4gVar = Uri.parse(str);
  38: } catch (Throwable th) {
  39: n4gVar = new n4g(th);
--
  48: if (o1dVar2.b(c6aVar2)) {
  49: o1dVar2.c(c6aVar2, str2, "Parsing sessionInit.recoveryUrl:" + str + " returns error:" + p4g.a(n4gVar) + ".", null);
  50: }
  51: }
  52: return a(Uri.parse("https://go.max.ru/recovery"), i);
  53: }
  54: }
--
~~~

### defpackage/o4m.java
~~~text
 605: az7.j("AttributionHandler: attribution has already been received");
 606: return;
 607: }
 608: try {
 609: String queryParameter = Uri.parse("https://tracker-api.vk-analytics.ru/?" + URLDecoder.decode(str, "UTF-8")).getQueryParameter("mt_deeplink");
 610: if (TextUtils.isEmpty(queryParameter)) {
 611: az7.j("AttributionHandler: deeplink is empty");
 612: } else {
 613: wt8Var.g(new JSONObject().put("deeplink", queryParameter));
 614: }
--
~~~

### defpackage/o57.java
~~~text
  41: n3a n3aVar2 = dleVar.a;
  42: String strU = n3aVar.U();
  43: if (strU == null) {
  44: yx9Var.getClass();
  45: strU = "api2.oneme.ru";
  46: } else {
  47: strU = strU.length() <= 0 ? null : strU;
  48: if (strU == null) {
  49: yx9Var.getClass();
  50: strU = "api2.oneme.ru";
--
  51: }
  52: }
  53: String strV = n3aVar2.V();
  54: if (strV == null) {
  55: yx9Var.getClass();
--
~~~

### defpackage/qjn.java
~~~text
  18: if (ywm.i(3, "CXCP")) {
  19: Log.d("CXCP", "Device is known to throw an exception while checking flash availability. Flash is not available. [Manufacturer: " + Build.MANUFACTURER + ", Model: " + Build.MODEL + ", API Level: " + Build.VERSION.SDK_INT + "].");
  20: }
  21: } else if (ywm.i(6, "CXCP")) {
  22: Log.e("CXCP", "Exception thrown while checking for flash availability on device not known to throw exceptions during this check. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: " + Build.MANUFACTURER + ", Model: " + Build.MODEL + ", API Level: " + 
  23: }
  24: bool = Boolean.FALSE;
  25: }
  26: if (bool == null && ywm.i(5, "CXCP")) {
  27: Log.w("CXCP", "Characteristics did not contain key FLASH_INFO_AVAILABLE. Flash is not available.");
--
~~~

### defpackage/rk.java
~~~text
 203: }
 204: xnm.y(obj);
 205: str = (String) this.j;
 206: ((yx9) mm8Var.d.getValue()).getClass();
 207: zC = g4a.c(str, "api2.oneme.ru");
 208: if (zC && ((c6h) rp9Var.getValue()).isConnected()) {
 209: i2 = 0;
 210: if (zC \|\| !((c6h) rp9Var.getValue()).isConnected()) {
 211: jm8 jm8Var = new jm8(mm8Var, str, b55Var, b4);
 212: this.l = str;
--
~~~

### defpackage/rlh.java
~~~text
  38: LatLng latLng2 = wlhVarS2.c;
  39: double d = latLng2.a;
  40: double d2 = latLng2.b;
  41: String str = y99.a;
  42: List<u36> listI0 = wa4.i0(new u36(y99.n(context, Uri.parse("yandexmaps://maps.yandex.ru/?rtext=~" + d + "," + d2)), "yandex_maps", "ru.yandex.yandexmaps", 8), new u36(y99.n(context, Uri.parse("yandexnavi://build_route_on_map/?lat_to=" + d + "&lon_to=" + d2)), "yandex_navigator", "ru.yandex.yandexnavi", 8), new u36(Uri.parse("dgis://2gis.r
  43: ArrayList arrayList = new ArrayList();
  44: for (u36 u36Var : listI0) {
  45: Intent intent = new Intent("android.intent.action.VIEW", u36Var.a);
  46: intent.setPackage(u36Var.c);
  47: t36 t36Var = intent.resolveActivity(context.getPackageManager()) != null ? new t36(intent, u36Var.b) : null;
--
~~~

### defpackage/s80.java
~~~text
2651: int i3 = (int) (jA >> 32);
2652: int i4 = (int) (jA & 4294967295L);
2653: double d5 = n4aVar.b;
2654: double d6 = n4aVar.a;
2655: StringBuilder sbR = pq0.r("https://static-maps.yandex.ru/v1?lang=ru_RU&maptype=future_map&scale=1.5&size=", i3, ",", i4, "&z=");
2656: sbR.append(iH);
2657: sbR.append("&ll=");
2658: sbR.append(d5);
2659: sbR.append(",");
2660: sbR.append(d6);
--
2704: int i5 = (int) (jA >> 32);
2705: int i6 = (int) (jA & 4294967295L);
2706: double d7 = n4aVar.b;
2707: double d8 = n4aVar.a;
2708: StringBuilder sbR2 = pq0.r("https://static-maps.yandex.ru/v1?lang=ru_RU&maptype=future_map&scale=1.5&size=", i5, ",", i6, "&z=");
2709: sbR2.append(iH);
2710: sbR2.append("&ll=");
2711: sbR2.append(d7);
2712: sbR2.append(",");
2713: sbR2.append(d8);
--
~~~

### defpackage/sx3.java
~~~text
 378: ((yx9) gm8Var2.d.getValue()).getClass();
 379: f09.p(((gm8) this.j).b, "checking oneMe host...");
 380: jElapsedRealtime2 = SystemClock.elapsedRealtime();
 381: dp5 dp5Var = new dp5((gm8) this.j, (byte) 27);
 382: str2 = "api2.oneme.ru";
 383: this.i = "api2.oneme.ru";
 384: this.k = null;
 385: this.h = i;
 386: this.g = jElapsedRealtime2;
 387: this.f = (byte) 2;
--
 388: objE2 = qo9.E(jp6Var, dp5Var, this);
--
 457: ((yx9) gm8Var4.d.getValue()).getClass();
 458: f09.p(((gm8) this.j).b, "checking oneMe host...");
 459: jElapsedRealtime2 = SystemClock.elapsedRealtime();
 460: dp5 dp5Var2 = new dp5((gm8) this.j, (byte) 27);
 461: str2 = "api2.oneme.ru";
 462: this.i = "api2.oneme.ru";
 463: this.k = null;
 464: this.h = i;
 465: this.g = jElapsedRealtime2;
 466: this.f = (byte) 2;
--
 467: objE2 = qo9.E(jp6Var, dp5Var2, this);
--
~~~

### defpackage/tdd.java
~~~text
 210: h = new tdd("RECONNECT", s5, s6);
 211: short s7 = 5;
 212: i = new tdd("LOG", s6, s7);
 213: short s8 = 6;
 214: j = new tdd("SESSION_INIT", 4, s8);
 215: k = new tdd("PROFILE", s7, (short) 16);
 216: l = new tdd("AUTH_REQUEST", s8, (short) 17);
 217: short s9 = 27;
 218: G = new tdd("ASSETS_GET", s9, (short) 26);
 219: short s10 = 28;
--
~~~

### defpackage/uhm.java
~~~text
  58: } else {
  59: String str2 = y99.a;
  60: Context context = ((u2f) u06Var.b).d;
  61: try {
  62: ResolveInfo resolveInfoResolveActivity = context.getPackageManager().resolveActivity(new Intent("android.intent.action.VIEW", Uri.parse("https://example.com")), 65536);
  63: n4gVar = Boolean.valueOf(g4a.c((resolveInfoResolveActivity == null \|\| (activityInfo = resolveInfoResolveActivity.activityInfo) == null) ? null : activityInfo.packageName, "com.yandex.browser"));
  64: } catch (Throwable th) {
  65: n4gVar = new n4g(th);
  66: }
  67: Throwable thA = p4g.a(n4gVar);
--
~~~

### defpackage/v99.java
~~~text
  27: }
  28: long jLongValue = l.longValue();
  29: ByteBuffer byteBufferAllocate = ByteBuffer.allocate(8);
  30: byteBufferAllocate.putLong(jLongValue);
  31: return CallsSdkInitializer.INSTANCE.initializeSessionSeed(this.a, byteBufferAllocate.array(), this.b.a().getBytes(o53.a));
  32: }
  33: }
--
~~~

### defpackage/vm8.java
~~~text
  21: this.c = rp9Var2;
  22: this.d = rp9Var3;
  23: this.e = rp9Var;
  24: this.f = context.getSharedPreferences("dev_tools", 0);
  25: List listI0 = wa4.i0("api2.oneme.ru", "api-test.oneme.ru", "api-tg.oneme.ru", "api-test2.oneme.ru", "api-test3.oneme.ru");
  26: ArrayList arrayList = new ArrayList(listI0.size());
  27: arrayList.addAll(listI0);
  28: cb4.u0(arrayList, new String[0]);
  29: this.g = arrayList;
  30: this.h = az7.c(c1());
--
~~~

### defpackage/vz8.java
~~~text
  89: Linkify.addLinks(spannable, 4);
  90: }
  91: ArrayList<kx9> arrayList = new ArrayList();
  92: if ((i4 & 1) != 0) {
  93: hsd.e(arrayList, spannable, tpd.b, new String[]{"http://", "https://", "rtsp://"}, Linkify.sUrlMatchFilter);
  94: }
  95: if ((i4 & 2) != 0) {
  96: hsd.e(arrayList, spannable, tpd.c, new String[]{"mailto:"}, null);
  97: }
  98: if ((i4 & 8) != 0) {
--
~~~

### defpackage/wy8.java
~~~text
  50: }
  51: Locale locale = Locale.getDefault();
  52: HashMap map = klm.a;
  53: if (map.containsKey(-1)) {
  54: str = ((String) map.get(-1)) + " (https://developer.android.com/reference/com/google/android/play/core/review/model/ReviewErrorCode.html#" + ((String) klm.b.get(-1)) + ")";
  55: } else {
  56: str = BuildConfig.FLAVOR;
  57: }
  58: alnVarE = zv2.e(new ReviewException(new Status(-1, String.format(locale, "Review Error(%d): %s", -1, str), null, null)));
  59: } else {
--
~~~

### defpackage/x4f.java
~~~text
  31: @Override // defpackage.mg2
  32: /* JADX INFO: renamed from: f, reason: merged with bridge method [inline-methods] */
  33: public final zm9 getReflected() {
  34: if (this.a) {
  35: m00.i("Kotlin reflection is not yet supported for synthetic Java properties. Please follow/upvote https://youtrack.jetbrains.com/issue/KT-55980");
  36: return null;
  37: }
  38: qm9 qm9VarCompute = compute();
  39: if (qm9VarCompute != this) {
  40: return (zm9) qm9VarCompute;
--
~~~

### defpackage/yh6.java
~~~text
  82: }
  83: ka0 ka0VarU2 = p9bVar.u();
  84: String str2 = ka0VarU2 != null ? ka0VarU2.b : null;
  85: if (str2 != null && str2.length() != 0 && (ka0VarU = p9bVar.u()) != null && (str = ka0VarU.b) != null) {
  86: String strV0 = zti.v0(zti.v0(str, "http://"), "https://");
  87: if7 if7VarQ = j0h.Q(j0h.I(new q00(listB, (byte) 1), new l15((byte) 21)), new l15((byte) 22));
  88: boolean z3 = zti.a0(string, strV0, true) \|\| zti.a0(string, str, false);
  89: hf7 hf7Var = new hf7(if7VarQ);
  90: while (true) {
  91: if (!hf7Var.hasNext()) {
--
  94: }
  95: break;
  96: }
  97: String str3 = (String) hf7Var.next();
  98: if (hui.V(str3, str, true) \|\| hui.V(str3, strV0, true) \|\| zti.v0(zti.v0(str3, "http://"), "https://").equalsIgnoreCase(strV0)) {
  99: }
 100: z2 = false;
 101: break;
 102: }
 103: }
--
~~~

### defpackage/yr0.java
~~~text
 156: t5a.i(t5aVar, "HOST_REACHABILITY", "GET_HOST_REACHABILITY", deaVar.b(), 8);
 157: return s1kVar;
 158: pw5 pw5VarB = nm9.b(ja5Var, (lx6) z3jVar.getValue(), 0, new r25(mm8Var, b55Var, (byte) 14), 2);
 159: ((yx9) mm8Var.d.getValue()).getClass();
 160: List listI0 = wa4.i0("api2.oneme.ru", (String) om8.b.getValue(), (String) om8.f.getValue(), (String) om8.h.getValue(), (String) om8.d.getValue());
 161: x95 x95Var = (lx6) z3jVar.getValue();
 162: if (x95Var == null) {
 163: x95Var = this.b;
 164: }
 165: t45 t45VarA = fa5.a(x95Var);
--
~~~

### defpackage/yx9.java
~~~text
  78: if (!TextUtils.isEmpty(str) && (uri = Uri.parse(str)) != null) {
  79: List<String> pathSegments = uri.getPathSegments();
  80: if (!TextUtils.isEmpty(uri.getScheme())) {
  81: String host = uri.getHost();
  82: if (!uri.getScheme().equalsIgnoreCase("max") ? !(TextUtils.isEmpty(host) \|\| pathSegments.size() <= 0 \|\| (!host.equalsIgnoreCase("max.ru") && !host.equalsIgnoreCase("api-test.oneme.ru") && !host.equalsIgnoreCase("api-tg.oneme.ru"))) : !(TextUtils.isEmpty(host) \|\| pathSegments.size() <= 0 \|\| (!host.equalsIgnoreCase("chat") && !host.
  83: return true;
  84: }
  85: } else if (!pathSegments.isEmpty()) {
  86: String str2 = pathSegments.get(0);
  87: if (!TextUtils.isEmpty(str2) && pathSegments.size() > 1 && (str2.equalsIgnoreCase("max.ru") \|\| str2.equalsIgnoreCase("api-test.oneme.ru") \|\| str2.equalsIgnoreCase("api-tg.oneme.ru"))) {
--
  88: return true;
  89: }
  90: }
  91: }
  92: return false;
--
 100: if (host == null && TextUtils.isEmpty(uri.getScheme())) {
 101: List<String> pathSegments = uri.getPathSegments();
 102: host = pathSegments.isEmpty() ? null : pathSegments.get(0);
 103: }
 104: if (host != null && (host.equalsIgnoreCase("max.ru") \|\| host.equalsIgnoreCase("api-test.oneme.ru") \|\| host.equalsIgnoreCase("api-tg.oneme.ru"))) {
 105: if (string.endsWith("/")) {
 106: string = string.substring(0, string.length() - 1);
 107: }
 108: }
 109: } else if (string.endsWith("/") && string.length() > 1) {
--
 115: if (string.startsWith("@")) {
 116: return uri;
 117: }
 118: if (!string.contains("://") && TextUtils.isEmpty(uri.getScheme())) {
 119: return Uri.parse("https://".concat(string));
 120: }
 121: return Uri.parse(string);
 122: }
 123: }
--
~~~

### defpackage/zx.java
~~~text
  24: rp9 rp9Var = this.b;
  25: switch (b) {
  26: case 0:
  27: ((nvc) rp9Var.getValue()).getClass();
  28: return "https://download.max.ru/#android?version=26.35.1";
  29: case 1:
  30: return (job) ((lob) rp9Var.getValue()).d.getValue();
  31: case 2:
  32: return Boolean.valueOf(((ae3) rp9Var.getValue()).c());
  33: case 3:
--
~~~

### io/jsonwebtoken/SignatureAlgorithm.java
~~~text
 108: sb3.append(" class's 'secretKeyFor(SignatureAlgorithm.");
 109: sb3.append(name());
 110: sb3.append(")' method to create a key guaranteed to be secure enough for ");
 111: sb3.append(name());
 112: sb3.append(".  See https://tools.ietf.org/html/rfc7518#section-3.2 for more information.");
 113: throw new WeakKeyException(sb3.toString());
 114: }
 115: if (z && !(key instanceof PrivateKey)) {
 116: throw new InvalidKeyException(w7g.w(new StringBuilder(), this.familyName, " signing keys must be PrivateKey instances."));
 117: }
--
 138: sb5.append(" class's 'keyPairFor(SignatureAlgorithm.");
 139: sb5.append(name());
 140: sb5.append(")' method to create a key pair guaranteed to be secure enough for ");
 141: sb5.append(name());
 142: sb5.append(".  See https://tools.ietf.org/html/rfc7518#section-3.4 for more information.");
 143: throw new WeakKeyException(sb5.toString());
 144: }
 145: if (!(key instanceof RSAKey)) {
 146: StringBuilder sb6 = new StringBuilder();
 147: sb6.append(this.familyName);
--
 165: sb7.append(" class's 'keyPairFor(SignatureAlgorithm.");
 166: sb7.append(name());
 167: sb7.append(")' method to create a key pair guaranteed to be secure enough for ");
 168: sb7.append(name());
 169: sb7.append(".  See https://tools.ietf.org/html/rfc7518#section-");
 170: sb7.append(str);
 171: sb7.append(" for more information.");
 172: throw new WeakKeyException(sb7.toString());
 173: }
 174: }
--
 196: if (length >= signatureAlgorithm.minKeyLength) {
 197: return signatureAlgorithm;
 198: }
 199: }
 200: throw new WeakKeyException(vg9.v(length, "The specified SecretKey is not strong enough to be used with JWT HMAC signature algorithms.  The JWT specification requires HMAC keys to be >= 256 bits long.  The specified key is ", " bits.  See https://tools.ietf.org/html/rfc7518#section-3.2 for more information."));
 201: }
 202: if (!(key instanceof RSAKey)) {
 203: int iBitLength = ((ECKey) key).getParams().getOrder().bitLength();
 204: for (SignatureAlgorithm signatureAlgorithm2 : PREFERRED_EC_ALGS) {
 205: if (iBitLength >= signatureAlgorithm2.minKeyLength) {
--
 206: signatureAlgorithm2.assertValidSigningKey(key);
 207: return signatureAlgorithm2;
 208: }
 209: }
 210: throw new WeakKeyException(vg9.v(iBitLength, "The specified Elliptic Curve signing key is not strong enough to be used with JWT ECDSA signature algorithms.  The JWT specification requires ECDSA keys to be >= 256 bits long.  The specified ECDSA key is ", " bits.  See https://tools.ietf.org/html/rfc7518#section-3.4 for more information."));
 211: }
 212: int iBitLength2 = ((RSAKey) key).getModulus().bitLength();
 213: if (iBitLength2 >= 4096) {
 214: SignatureAlgorithm signatureAlgorithm3 = RS512;
 215: signatureAlgorithm3.assertValidSigningKey(key);
--
~~~

### io/jsonwebtoken/impl/DefaultClaims.java
~~~text
   6: import java.util.Map;
   7: 
   8: /* JADX INFO: loaded from: classes2.dex */
   9: public class DefaultClaims extends JwtMap implements Claims {
  10: private static final String CONVERSION_ERROR_MSG = "Cannot convert existing claim value of type '%s' to desired type '%s'. JJWT only converts simple String, Date, Long, Integer, Short and Byte types automatically. Anything more complex is expected to be already converted to your desired type by the JSON Deserializer implementation. You ma
  11: 
  12: public DefaultClaims() {
  13: }
  14: 
  15: private <T> T castClaimValue(Object obj, Class<T> cls) {
--
  25: }
  26: if (cls.isInstance(obj)) {
  27: return cls.cast(obj);
  28: }
  29: throw new RequiredTypeException("Cannot convert existing claim value of type '" + obj.getClass() + "' to desired type '" + cls + "'. JJWT only converts simple String, Date, Long, Integer, Short and Byte types automatically. Anything more complex is expected to be already converted to your desired type by the JSON Deserializer implementati
  30: }
  31: 
  32: private static boolean isSpecDate(String str) {
  33: return Claims.EXPIRATION.equals(str) \|\| Claims.ISSUED_AT.equals(str) \|\| Claims.NOT_BEFORE.equals(str);
  34: }
--
~~~

### io/jsonwebtoken/impl/crypto/EllipticCurveProvider.java
~~~text
  56: int iBitLength = (((ECKey) key).getParams().getOrder().bitLength() + 7) / 8;
  57: if (iBitLength * 2 == signatureByteArrayLength) {
  58: return;
  59: }
  60: throw new InvalidKeyException("EllipticCurve key has a field size of " + byteSizeString(iBitLength) + ", but " + signatureAlgorithm.name() + " requires a field size of " + byteSizeString(i) + " per [RFC 7518, Section 3.4 (validation)](https://datatracker.ietf.org/doc/html/rfc7518#section-3.4).");
  61: }
  62: 
  63: public static String byteSizeString(int i) {
  64: return i + " bytes (" + (i * 8) + " bits)";
  65: }
--
~~~

### io/jsonwebtoken/impl/crypto/EllipticCurveSignatureValidator.java
~~~text
  44: }
  45: return false;
  46: }
  47: if (bArr2[0] != 48 \|\| !"true".equalsIgnoreCase(System.getProperty(DER_ENCODING_SYS_PROPERTY_NAME))) {
  48: throw new io.jsonwebtoken.security.SignatureException("Provided signature is " + EllipticCurveProvider.byteSizeString(bArr2.length) + " but " + this.alg.name() + " signatures must be exactly " + EllipticCurveProvider.byteSizeString(signatureByteArrayLength) + " per [RFC 7518, Section 3.4 (validation)](https://datatracker.ietf.org/doc/html
  49: }
  50: return doVerify(signatureCreateSignatureInstance, publicKey, bArr, bArr2);
  51: } catch (Exception e) {
  52: kzd.g("Unable to verify Elliptic Curve signature using configured ECPublicKey. ", e.getMessage(), e);
  53: return false;
--
~~~

### io/jsonwebtoken/security/Keys.java
~~~text
  92: }
  93: }
  94: StringBuilder sbT = a15.t(length, "The specified key byte array is ", " bits which is not secure enough for any JWT HMAC-SHA algorithm.  The JWT JWA Specification (RFC 7518, Section 3.2) states that keys used with HMAC-SHA algorithms MUST have a size >= 256 bits (the key size must be greater than or equal to the hash output size).  Consid
  95: sbT.append(Keys.class.getName());
  96: sbT.append("#secretKeyFor(SignatureAlgorithm) method to create a key guaranteed to be secure enough for your preferred HMAC-SHA algorithm.  See https://tools.ietf.org/html/rfc7518#section-3.2 for more information.");
  97: throw new WeakKeyException(sbT.toString());
  98: }
  99: 
 100: public static KeyPair keyPairFor(SignatureAlgorithm signatureAlgorithm) throws IllegalArgumentException {
 101: Assert.notNull(signatureAlgorithm, "SignatureAlgorithm cannot be null.");
--
~~~

### io/reactivex/rxjava3/exceptions/OnErrorNotImplementedException.java
~~~text
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class OnErrorNotImplementedException extends RuntimeException {
   5: public OnErrorNotImplementedException(Throwable th) {
   6: super("The exception was not handled due to missing onError handler in the subscribe() method call. Further reading: https://github.com/ReactiveX/RxJava/wiki/Error-Handling \| " + th, th == null ? new NullPointerException() : th);
   7: }
   8: }
--
~~~

### io/reactivex/rxjava3/exceptions/UndeliverableException.java
~~~text
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class UndeliverableException extends IllegalStateException {
   5: public UndeliverableException(Throwable th) {
   6: super("The exception could not be delivered to the consumer because it has already canceled/disposed the flow or the exception has nowhere to go to begin with. Further reading: https://github.com/ReactiveX/RxJava/wiki/What's-different-in-2.0#error-handling \| " + th, th);
   7: }
   8: }
--
~~~

### one/me/callssdk/CallsSdkInitializer.java
~~~text
  18: import kotlin.collections.a;
  19: import me.leolin.shortcutbadger.BuildConfig;
  20: 
  21: /* JADX INFO: loaded from: classes.dex */
  22: @Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u0012\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÁ\u0002\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J
  23: public final class CallsSdkInitializer {
  24: public static final CallsSdkInitializer INSTANCE = new CallsSdkInitializer();
  25: 
  26: private CallsSdkInitializer() {
  27: }
--
  96: } while (i2 < i);
  97: return bArr;
  98: }
  99: 
 100: public final native byte[] initializeSessionSeed(Context context, byte[] seed, byte[] deviceId);
 101: }
--
~~~

### one/me/stories/edit/link/AddStoryLinkBottomSheet.java
~~~text
 407: }
 408: if (((ax9) ycVarH1.c.getValue()).a(str3, yc.g).equals(yw9.a)) {
 409: ycVarH1.d1(str3);
 410: } else {
 411: ycVarH1.d1("https://");
 412: }
 413: }
 414: xc xcVar = (xc) H1().e.a.getValue();
 415: G1().r(xcVar.a);
 416: zm9 zm9Var4 = zm9VarArr[5];
--
~~~

### ru/ok/tracer/lite/crash/report/TracerCrashReportLite.java
~~~text
 243: Collection collectionD = ((qd6) rb5Var.a.getDropHolder().a.getValue()).d();
 244: Collection collection = !collectionD.isEmpty() ? collectionD : null;
 245: String string4 = collection != null ? khn.d(collection).toString() : null;
 246: jnj jnjVar = tracerLite.getConfiguration().a;
 247: Uri.Builder builderAppendQueryParameter = Uri.parse("https://sdk-api.apptracer.ru").buildUpon().appendEncodedPath("api/crash/upload").appendQueryParameter("crashToken", libToken);
 248: if (str4 != null) {
 249: builderAppendQueryParameter.appendQueryParameter("crashHostAppToken", str4);
 250: }
 251: String string5 = builderAppendQueryParameter.toString();
 252: xo8 xo8Var = new xo8();
--
~~~

