# MAX 26.35.1 — трассировка WebAppVerifyMobileId (статический анализ)

SHA256 исходного APK: `e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc`; обнаружено Java-файлов с признаками: 15.
Контент получен из JADX, не из сетевых ответов. Ошибки декомпилятора и обфускация могут скрывать отдельные пути.

## Файлы с признаками Mobile ID

| Путь | Совпавшие маркеры |
|---|---|
| `defpackage/a8l.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/ajk.java` | VerifyMobileIdResponseInfo, MobileId |
| `defpackage/dol.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/e11.java` | MobileId |
| `defpackage/ekl.java` | verifyMobileId, MobileId |
| `defpackage/eol.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/ey2.java` | getSimOperator() |
| `defpackage/gol.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/hol.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/j01.java` | MobileId |
| `defpackage/jol.java` | WebAppVerifyMobileId, MobileId |
| `defpackage/lb6.java` | getNetworkOperator() |
| `defpackage/t5a.java` | getNetworkOperator() |
| `defpackage/yr0.java` | getNetworkOperator() |
| `defpackage/zik.java` | WebAppVerifyMobileId, MobileId |

## Ключевые классы и фрагменты исполнения

### `defpackage/a8l.java`

```java
File lines: 705, matched locations: 2.
Lines 607–657:
  607:                     qi4 qi4VarG9 = knlVar2.g();
  608:                     bb1 bb1Var14 = knlVar2.e;
  609:                     fnl fnlVar2 = (fnl) this.g;
  610:                     String str17 = ((nnl) this.h).b;
  611:                     this.j = null;
  612:                     this.f = true;
  613:                     if (qi4VarG9.a(bb1Var14, ij9VarF11, fnlVar2, str17, this) == ka5Var16) {
  614:                         return ka5Var16;
  615:                     }
  616:                 } else {
  617:                     if (!z16) {
  618:                         k3g.o("call to 'resume' before 'invoke' with coroutine");
  619:                         return null;
  620:                     }
  621:                     xnm.y(obj);
  622:                 }
  623:                 return s1k.a;
  624:             case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
  625:                 zik zikVar = (zik) this.h;
  626:                 dol dolVar = (dol) this.g;
  627:                 ajk ajkVar = (ajk) this.j;
  628:                 ka5 ka5Var17 = ka5.a;
  629:                 boolean z17 = this.f;
  630:                 if (!z17) {
  631:                     xnm.y(obj);
  632:                     jol jolVar = new jol(((gol) this.i).a, ajkVar.a, ajkVar.b, ajkVar.c);
  633:                     bb1 bb1Var15 = dolVar.d;
  634:                     zikVar.getClass();
  635:                     mj9 mj9Var4 = dolVar.a;
  636:                     mj9Var4.getClass();
  637:                     bj9 bj9Var4 = new bj9("WebAppVerifyMobileId", mj9Var4.b(jol.Companion.serializer(), jolVar), true);
  638:                     this.j = null;
  639:                     this.f = true;
  640:                     if (bb1Var15.b(this, bj9Var4) == ka5Var17) {
  641:                         return ka5Var17;
  642:                     }
  643:                 } else {
  644:                     if (!z17) {
  645:                         k3g.o("call to 'resume' before 'invoke' with coroutine");
  646:                         return null;
  647:                     }
  648:                     xnm.y(obj);
  649:                 }
  650:                 return s1k.a;
  651:             default:
  652:                 nol nolVar = (nol) this.g;
  653:                 nzk nzkVar = (nzk) this.j;
  654:                 ka5 ka5Var18 = ka5.a;
  655:                 boolean z18 = this.f;
  656:                 if (!z18) {
  657:                     xnm.y(obj);
```

### `defpackage/dol.java`

```java
File lines: 240, matched locations: 4.
Lines 1–101:
    1: package defpackage;
    2: 
    3: import java.util.ArrayList;
    4: import java.util.Set;
    5: import one.me.webapp.domain.jsbridge.WebAppJsonException;
    6: 
    7: /* JADX INFO: loaded from: classes3.dex */
    8: public final class dol implements kj9 {
    9:     public final mj9 a;
   10:     public final rp9 b;
   11:     public final Set c;
   12:     public final bb1 d;
   13: 
   14:     public dol(mj9 mj9Var, rp9 rp9Var) {
   15:         this.a = mj9Var;
   16:         this.b = rp9Var;
   17:         ut6 ut6Var = zik.b;
   18:         ArrayList arrayList = new ArrayList(xa4.p0(ut6Var, 10));
   19:         j2 j2Var = new j2(ut6Var, (byte) 0);
   20:         while (j2Var.hasNext()) {
   21:             ((zik) j2Var.next()).getClass();
   22:             arrayList.add("WebAppVerifyMobileId");
   23:         }
   24:         this.c = va4.v1(arrayList);
   25:         this.d = az7.b(0, 0, null, 7);
   26:     }
   27: 
   28:     @Override // defpackage.kj9
   29:     public final Object a(String str, String str2, b55 b55Var) {
   30:         Object objF;
   31:         boolean zContains = this.c.contains(str);
   32:         s1k s1kVar = s1k.a;
   33:         if (zContains) {
   34:             return (str.equals("WebAppVerifyMobileId") && (objF = f(str2, (d55) b55Var)) == ka5.a) ? objF : s1kVar;
   35:         }
   36:         f09.f0(dol.class.getName(), "Unknown method with name = " + str + " in JsDelegate: " + this);
   37:         return s1kVar;
   38:     }
   39: 
   40:     @Override // defpackage.kj9
   41:     public final boolean b(String str) {
   42:         if (str.equals("WebAppVerifyMobileId")) {
   43:             return true;
   44:         }
   45:         f09.f0(dol.class.getName(), "Unknown method with name = " + str + " in JsDelegate: " + this);
   46:         return false;
   47:     }
   48: 
   49:     @Override // defpackage.kj9
   50:     public final bb1 c() {
   51:         return this.d;
   52:     }
   53: 
   54:     @Override // defpackage.kj9
   55:     public final Set d() {
   56:         return this.c;
   57:     }
   58: 
   59:     @Override // defpackage.kj9
   60:     public final void e(u5l u5lVar) {
   61:     }
   62: 
   63:     /* JADX WARN: Code duplicated, block: B:21:0x0051 A[PHI: r1 r3 r4
   64:       0x0051: PHI (r1v10 bol) = (r1v8 bol), (r1v19 bol) binds: [B:42:0x00f0, B:20:0x0048] A[DONT_GENERATE, DONT_INLINE]
   65:       0x0051: PHI (r3v3 gol) = (r3v2 gol), (r3v7 gol) binds: [B:42:0x00f0, B:20:0x0048] A[DONT_GENERATE, DONT_INLINE]
   66:       0x0051: PHI (r4v6 zik) = (r4v4 zik), (r4v9 zik) binds: [B:42:0x00f0, B:20:0x0048] A[DONT_GENERATE, DONT_INLINE]] */
   67:     /* JADX WARN: Code duplicated, block: B:41:0x00da  */
   68:     /* JADX WARN: Code duplicated, block: B:47:0x010b A[PHI: r0 r1 r4
   69:       0x010b: PHI (r0v19 java.lang.Object) = (r0v18 java.lang.Object), (r0v1 java.lang.Object) binds: [B:45:0x0108, B:19:0x0040] A[DONT_GENERATE, DONT_INLINE]
   70:       0x010b: PHI (r1v12 gol) = (r1v11 gol), (r1v20 gol) binds: [B:45:0x0108, B:19:0x0040] A[DONT_GENERATE, DONT_INLINE]
   71:       0x010b: PHI (r4v8 ??) = (r4v11 ??), (r4v10 ??) binds: [B:45:0x0108, B:19:0x0040] A[DONT_GENERATE, DONT_INLINE]] */
   72:     /* JADX WARN: Code duplicated, block: B:8:0x001a  */
   73:     /* JADX WARN: Type inference failed for: r4v10 */
   74:     /* JADX WARN: Type inference failed for: r4v11 */
   75:     /* JADX WARN: Type inference failed for: r4v8, types: [b55, bol, gol, zik] */
   76:     public final Object f(String str, d55 d55Var) {
   77:         col colVar;
   78:         zik zikVar;
   79:         Object objA;
   80:         zik zikVar2;
   81:         gol golVar;
   82:         bol bolVar;
   83:         bb1 bb1Var;
   84:         gol golVar2;
   85:         ?? r4;
   86:         s1k s1kVar = s1k.a;
   87:         if (d55Var instanceof col) {
   88:             colVar = (col) d55Var;
   89:             int i = colVar.i;
   90:             if ((i & Integer.MIN_VALUE) != 0) {
   91:                 colVar.i = i - Integer.MIN_VALUE;
   92:             } else {
   93:                 colVar = new col(this, d55Var);
   94:             }
   95:         } else {
   96:             colVar = new col(this, d55Var);
   97:         }
   98:         col colVar2 = colVar;
   99:         Object objC = colVar2.g;
  100:         ka5 ka5Var = ka5.a;
  101:         int i2 = colVar2.i;
```

### `defpackage/jol.java`

```java
File lines: 56, matched locations: 8.
Lines 1–56:
    1: package defpackage;
    2: 
    3: import java.util.Map;
    4: 
    5: /* JADX INFO: loaded from: classes3.dex */
    6: @x0h
    7: public final class jol {
    8:     public static final iol Companion = new iol();
    9:     public static final rp9[] e = {null, null, xnm.p(2, new mbl((byte) 15)), null};
   10:     public final String a;
   11:     public final int b;
   12:     public final Map c;
   13:     public final String d;
   14: 
   15:     public /* synthetic */ jol(int i, String str, int i2, Map map, String str2) {
   16:         if (15 != (i & 15)) {
   17:             az7.S(i, 15, hol.a.d());
   18:             throw null;
   19:         }
   20:         this.a = str;
   21:         this.b = i2;
   22:         this.c = map;
   23:         this.d = str2;
   24:     }
   25: 
   26:     public final boolean equals(Object obj) {
   27:         if (this == obj) {
   28:             return true;
   29:         }
   30:         if (!(obj instanceof jol)) {
   31:             return false;
   32:         }
   33:         jol jolVar = (jol) obj;
   34:         return g4a.c(this.a, jolVar.a) && this.b == jolVar.b && g4a.c(this.c, jolVar.c) && g4a.c(this.d, jolVar.d);
   35:     }
   36: 
   37:     public final int hashCode() {
   38:         return this.d.hashCode() + rmi.d(this.c, a15.d(this.b, this.a.hashCode() * 31, 31), 31);
   39:     }
   40: 
   41:     public final String toString() {
   42:         StringBuilder sbA = vg9.A(this.b, "WebAppVerifyMobileIdResponse(requestId=", this.a, ", statusCode=", ", headers=");
   43:         sbA.append(this.c);
   44:         sbA.append(", data=");
   45:         sbA.append(this.d);
   46:         sbA.append(")");
   47:         return sbA.toString();
   48:     }
   49: 
   50:     public jol(String str, int i, Map map, String str2) {
   51:         this.a = str;
   52:         this.b = i;
   53:         this.c = map;
   54:         this.d = str2;
   55:     }
   56: }
```

### `defpackage/ajk.java`

```java
File lines: 40, matched locations: 5.
Lines 1–40:
    1: package defpackage;
    2: 
    3: import java.util.Map;
    4: 
    5: /* JADX INFO: loaded from: classes3.dex */
    6: public final class ajk {
    7:     public final int a;
    8:     public final Map b;
    9:     public final String c;
   10: 
   11:     public ajk(int i, String str, Map map) {
   12:         this.a = i;
   13:         this.b = map;
   14:         this.c = str;
   15:     }
   16: 
   17:     public final boolean equals(Object obj) {
   18:         if (this == obj) {
   19:             return true;
   20:         }
   21:         if (!(obj instanceof ajk)) {
   22:             return false;
   23:         }
   24:         ajk ajkVar = (ajk) obj;
   25:         return this.a == ajkVar.a && this.b.equals(ajkVar.b) && this.c.equals(ajkVar.c);
   26:     }
   27: 
   28:     public final int hashCode() {
   29:         return this.c.hashCode() + rmi.d(this.b, Integer.hashCode(this.a) * 31, 31);
   30:     }
   31: 
   32:     public final String toString() {
   33:         StringBuilder sb = new StringBuilder("VerifyMobileIdResponseInfo(code=");
   34:         sb.append(this.a);
   35:         sb.append(", headers=");
   36:         sb.append(this.b);
   37:         sb.append(", data=");
   38:         return w7g.w(sb, this.c, ")");
   39:     }
   40: }
```

### `defpackage/bj9.java`

```java
File lines: 33, matched locations: 5.
Lines 1–33:
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: public final class bj9 implements dj9 {
    5:     public final String a;
    6:     public final String b;
    7:     public final boolean c;
    8: 
    9:     public bj9(String str, String str2, boolean z) {
   10:         this.a = str;
   11:         this.b = str2;
   12:         this.c = z;
   13:     }
   14: 
   15:     public final boolean equals(Object obj) {
   16:         if (this == obj) {
   17:             return true;
   18:         }
   19:         if (!(obj instanceof bj9)) {
   20:             return false;
   21:         }
   22:         bj9 bj9Var = (bj9) obj;
   23:         return g4a.c(this.a, bj9Var.a) && g4a.c(this.b, bj9Var.b) && this.c == bj9Var.c;
   24:     }
   25: 
   26:     public final int hashCode() {
   27:         return Boolean.hashCode(this.c) + a15.e(this.a.hashCode() * 31, 31, this.b);
   28:     }
   29: 
   30:     public final String toString() {
   31:         return s95.r(pq0.s("JsEvent(name=", this.a, ", data=", this.b, ", isPrivateEvent="), this.c, ")");
   32:     }
   33: }
```

### `defpackage/mj9.java`

```java
File lines: 53, matched locations: 2.
Lines 1–42:
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes.dex */
    4: public abstract class mj9 {
    5:     public static final lj9 d = new lj9(new wj9(false, false, false, true, "    ", false, "type", true, 3), c45.c);
    6:     public final wj9 a;
    7:     public final wdc b;
    8:     public final mxf c = new mxf((byte) 5);
    9: 
   10:     public mj9(wj9 wj9Var, wdc wdcVar) {
   11:         this.a = wj9Var;
   12:         this.b = wdcVar;
   13:     }
   14: 
   15:     public final Object a(an9 an9Var, String str) {
   16:         uoj uojVar = new uoj(str);
   17:         Object objF = new fti(this, dxl.c, uojVar, an9Var.d()).f(an9Var);
   18:         if (uojVar.e() == 10) {
   19:             return objF;
   20:         }
   21:         uoj.m(uojVar, "Expected EOF after parsing, but had " + str.charAt(uojVar.b - 1) + " instead", 0, null, 6);
   22:         throw null;
   23:     }
   24: 
   25:     public final String b(an9 an9Var, Object obj) {
   26:         char[] cArr;
   27:         mv mvVar = new mv((byte) 4);
   28:         v43 v43Var = v43.c;
   29:         synchronized (v43Var) {
   30:             vz vzVar = v43Var.a;
   31:             cArr = null;
   32:             char[] cArr2 = (char[]) (vzVar.isEmpty() ? null : vzVar.removeLast());
   33:             if (cArr2 != null) {
   34:                 v43Var.b -= cArr2.length;
   35:                 cArr = cArr2;
   36:             }
   37:         }
   38:         if (cArr == null) {
   39:             cArr = new char[128];
   40:         }
   41:         mvVar.c = cArr;
   42:         try {
```

### `defpackage/s1k.java`

```java
File lines: 10, matched locations: 1.
Lines 1–10:
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes.dex */
    4: public final class s1k {
    5:     public static final s1k a = new s1k();
    6: 
    7:     public final String toString() {
    8:         return "kotlin.Unit";
    9:     }
   10: }
```

## Применение результатов

Этот отчёт предназначен для ручной проверки того, какие поля, обработчики и результаты связаны с вызовом мини-приложения.
Он не содержит исполняемых рекомендаций по подмене Mobile ID или серверного подтверждения.
Наличие класса не доказывает, что конкретный запуск мини-приложения использовал данный путь.
