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

## Углублённое изучение обработчика и его зависимостей

### `defpackage/dol.java`

```java
Total lines: 240. Examined: 100–240.
  100:         ka5 ka5Var = ka5.a;
  101:         int i2 = colVar2.i;
  102:         if (i2 != 0) {
  103:             if (i2 == 1) {
  104:                 zikVar = colVar2.d;
  105:                 xnm.y(objC);
  106:             } else {
  107:                 if (i2 == 2) {
  108:                     bolVar = colVar2.f;
  109:                     golVar = colVar2.e;
  110:                     zikVar2 = colVar2.d;
  111:                     xnm.y(objC);
  112:                     bol bolVar2 = bolVar;
  113:                     golVar2 = golVar;
  114:                     zik zikVar3 = zikVar2;
  115:                     b55 b55Var = null;
  116:                     a8l a8lVar = new a8l((Object) golVar2, (Object) this, (Object) zikVar3, b55Var, (byte) 16);
  117:                     colVar2.d = null;
  118:                     colVar2.e = golVar2;
  119:                     colVar2.f = null;
  120:                     colVar2.i = 3;
  121:                     objC = bolVar2.c(a8lVar, colVar2);
  122:                     r4 = b55Var;
  123:                     if (objC != ka5Var) {
  124:                     }
  125:                 }
  126:                 if (i2 != 3) {
  127:                     if (i2 == 4) {
  128:                         xnm.y(objC);
  129:                         return s1kVar;
  130:                     }
  131:                     k3g.o("call to 'resume' before 'invoke' with coroutine");
  132:                     return null;
  133:                 }
  134:                 golVar2 = colVar2.e;
  135:                 xnm.y(objC);
  136:                 r4 = 0;
  137:             }
  138:             qrk qrkVar = new qrk(this, golVar2, r4, (byte) 17);
  139:             colVar2.d = r4;
  140:             colVar2.e = r4;
  141:             colVar2.f = r4;
  142:             colVar2.i = 4;
  143:             return ((aj9) objC).d(qrkVar, colVar2) == ka5Var ? ka5Var : s1kVar;
  144:         }
  145:         xnm.y(objC);
  146:         zik zikVar4 = zik.a;
  147:         mj9 mj9Var = this.a;
  148:         qi4 qi4Var = (qi4) this.b.getValue();
  149:         bb1 bb1Var2 = this.d;
  150:         gj9 gj9Var = new gj9(new jj9("json_decode_error", 2));
  151:         try {
  152:             mj9Var.getClass();
  153:             objA = mj9Var.a(gol.Companion.serializer(), str);
  154:             zikVar2 = zikVar4;
  155:         } catch (IllegalArgumentException e) {
  156:             String name = mj9Var.getClass().getName();
  157:             WebAppJsonException webAppJsonException = new WebAppJsonException(e);
  158:             o1d o1dVar = f09.g;
  159:             if (o1dVar != null) {
  160:                 c6a c6aVar = c6a.f;
  161:                 if (o1dVar.b(c6aVar)) {
  162:                     o1dVar.c(c6aVar, name, "json parse error at: " + zikVar4, webAppJsonException);
  163:                 }
  164:             }
  165:             colVar2.d = zikVar4;
  166:             colVar2.e = null;
  167:             colVar2.f = null;
  168:             colVar2.i = 1;
  169:             if (qi4Var.a(bb1Var2, gj9Var, zikVar4, null, colVar2) != ka5Var) {
  170:                 zikVar = zikVar4;
  171:                 zikVar2 = zikVar;
  172:                 objA = null;
  173:             }
  174:         }
  175:         golVar = (gol) objA;
  176:         if (golVar != null) {
  177:             bolVar = new bol(golVar.b);
  178:             bb1Var = this.d;
  179:             colVar2.d = zikVar2;
  180:             colVar2.e = golVar;
  181:             colVar2.f = bolVar;
  182:             colVar2.i = 2;
  183:             if (bb1Var.b(colVar2, bolVar) != ka5Var) {
  184:                 bol bolVar3 = bolVar;
  185:                 golVar2 = golVar;
  186:                 zik zikVar5 = zikVar2;
  187:                 b55 b55Var2 = null;
  188:                 a8l a8lVar2 = new a8l((Object) golVar2, (Object) this, (Object) zikVar5, b55Var2, (byte) 16);
  189:                 colVar2.d = null;
  190:                 colVar2.e = golVar2;
  191:                 colVar2.f = null;
  192:                 colVar2.i = 3;
  193:                 objC = bolVar3.c(a8lVar2, colVar2);
  194:                 r4 = b55Var2;
  195:                 if (objC != ka5Var) {
  196:                     qrk qrkVar2 = new qrk(this, golVar2, r4, (byte) 17);
  197:                     colVar2.d = r4;
  198:                     colVar2.e = r4;
  199:                     colVar2.f = r4;
  200:                     colVar2.i = 4;
  201:                     if (((aj9) objC).d(qrkVar2, colVar2) == ka5Var) {
  202:                     }
  203:                 }
  204:             }
  205:         }
  206:         zikVar2 = zikVar;
  207:         objA = null;
  208:         golVar = (gol) objA;
  209:         if (golVar != null) {
  210:             bolVar = new bol(golVar.b);
  211:             bb1Var = this.d;
  212:             colVar2.d = zikVar2;
  213:             colVar2.e = golVar;
  214:             colVar2.f = bolVar;
  215:             colVar2.i = 2;
  216:             if (bb1Var.b(colVar2, bolVar) != ka5Var) {
  217:                 bol bolVar4 = bolVar;
  218:                 golVar2 = golVar;
  219:                 zik zikVar6 = zikVar2;
  220:                 b55 b55Var3 = null;
  221:                 a8l a8lVar3 = new a8l((Object) golVar2, (Object) this, (Object) zikVar6, b55Var3, (byte) 16);
  222:                 colVar2.d = null;
  223:                 colVar2.e = golVar2;
  224:                 colVar2.f = null;
  225:                 colVar2.i = 3;
  226:                 objC = bolVar4.c(a8lVar3, colVar2);
  227:                 r4 = b55Var3;
  228:                 if (objC != ka5Var) {
  229:                     qrk qrkVar3 = new qrk(this, golVar2, r4, (byte) 17);
  230:                     colVar2.d = r4;
  231:                     colVar2.e = r4;
  232:                     colVar2.f = r4;
  233:                     colVar2.i = 4;
  234:                     if (((aj9) objC).d(qrkVar3, colVar2) == ka5Var) {
  235:                     }
  236:                 }
  237:             }
  238:         }
  239:     }
  240: }
```

### `defpackage/gol.java`

```java
Total lines: 37. Examined: 1–37.
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: @x0h
    5: public final class gol {
    6:     public static final fol Companion = new fol();
    7:     public final String a;
    8:     public final String b;
    9: 
   10:     public /* synthetic */ gol(int i, String str, String str2) {
   11:         if (3 != (i & 3)) {
   12:             az7.S(i, 3, eol.a.d());
   13:             throw null;
   14:         }
   15:         this.a = str;
   16:         this.b = str2;
   17:     }
   18: 
   19:     public final boolean equals(Object obj) {
   20:         if (this == obj) {
   21:             return true;
   22:         }
   23:         if (!(obj instanceof gol)) {
   24:             return false;
   25:         }
   26:         gol golVar = (gol) obj;
   27:         return g4a.c(this.a, golVar.a) && g4a.c(this.b, golVar.b);
   28:     }
   29: 
   30:     public final int hashCode() {
   31:         return this.b.hashCode() + (this.a.hashCode() * 31);
   32:     }
   33: 
   34:     public final String toString() {
   35:         return w7g.v("WebAppVerifyMobileIdRequest(requestId=", this.a, ", url=", this.b, ")");
   36:     }
   37: }
```

### `defpackage/hol.java`

```java
Total lines: 83. Examined: 1–83.
    1: package defpackage;
    2: 
    3: import java.util.Map;
    4: 
    5: /* JADX INFO: loaded from: classes3.dex */
    6: public final /* synthetic */ class hol implements c58 {
    7:     public static final hol a;
    8:     private static final q0h descriptor;
    9: 
   10:     static {
   11:         hol holVar = new hol();
   12:         a = holVar;
   13:         x8e x8eVar = new x8e("one.me.webapp.domain.jsbridge.delegates.private.WebAppVerifyMobileIdResponse", holVar, 4);
   14:         x8eVar.k("requestId", false);
   15:         x8eVar.k("statusCode", false);
   16:         x8eVar.k("headers", false);
   17:         x8eVar.k("data", false);
   18:         descriptor = x8eVar;
   19:     }
   20: 
   21:     /* JADX WARN: Multi-variable type inference failed */
   22:     @Override // defpackage.c58
   23:     public final an9[] a() {
   24:         rp9[] rp9VarArr = jol.e;
   25:         vti vtiVar = vti.a;
   26:         return new an9[]{vtiVar, n99.a, rp9VarArr[2].getValue(), vtiVar};
   27:     }
   28: 
   29:     @Override // defpackage.an9
   30:     public final Object b(km5 km5Var) {
   31:         q0h q0hVar = descriptor;
   32:         em4 em4VarB = km5Var.b(q0hVar);
   33:         rp9[] rp9VarArr = jol.e;
   34:         boolean z = true;
   35:         int i = 0;
   36:         int iR = 0;
   37:         String strL = null;
   38:         Map map = null;
   39:         String strL2 = null;
   40:         while (z) {
   41:             int iH = em4VarB.h(q0hVar);
   42:             if (iH == -1) {
   43:                 z = false;
   44:             } else if (iH == 0) {
   45:                 strL = em4VarB.l(q0hVar, 0);
   46:                 i |= 1;
   47:             } else if (iH == 1) {
   48:                 iR = em4VarB.r(q0hVar, 1);
   49:                 i |= 2;
   50:             } else if (iH == 2) {
   51:                 map = (Map) em4VarB.q(q0hVar, 2, (an9) rp9VarArr[2].getValue(), map);
   52:                 i |= 4;
   53:             } else {
   54:                 if (iH != 3) {
   55:                     kw7.e(iH);
   56:                     return null;
   57:                 }
   58:                 strL2 = em4VarB.l(q0hVar, 3);
   59:                 i |= 8;
   60:             }
   61:         }
   62:         em4VarB.o(q0hVar);
   63:         return new jol(i, strL, iR, map, strL2);
   64:     }
   65: 
   66:     @Override // defpackage.an9
   67:     public final void c(vq6 vq6Var, Object obj) {
   68:         jol jolVar = (jol) obj;
   69:         q0h q0hVar = descriptor;
   70:         gm4 gm4VarB = vq6Var.b(q0hVar);
   71:         rp9[] rp9VarArr = jol.e;
   72:         gm4VarB.u(q0hVar, 0, jolVar.a);
   73:         gm4VarB.t(1, jolVar.b, q0hVar);
   74:         gm4VarB.m(q0hVar, 2, (an9) rp9VarArr[2].getValue(), jolVar.c);
   75:         gm4VarB.u(q0hVar, 3, jolVar.d);
   76:         gm4VarB.e();
   77:     }
   78: 
   79:     @Override // defpackage.an9
   80:     public final q0h d() {
   81:         return descriptor;
   82:     }
   83: }
```

### `defpackage/eol.java`

```java
Total lines: 65. Examined: 1–65.
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: public final /* synthetic */ class eol implements c58 {
    5:     public static final eol a;
    6:     private static final q0h descriptor;
    7: 
    8:     static {
    9:         eol eolVar = new eol();
   10:         a = eolVar;
   11:         x8e x8eVar = new x8e("one.me.webapp.domain.jsbridge.delegates.private.WebAppVerifyMobileIdRequest", eolVar, 2);
   12:         x8eVar.k("requestId", false);
   13:         x8eVar.k("url", false);
   14:         descriptor = x8eVar;
   15:     }
   16: 
   17:     @Override // defpackage.c58
   18:     public final an9[] a() {
   19:         vti vtiVar = vti.a;
   20:         return new an9[]{vtiVar, vtiVar};
   21:     }
   22: 
   23:     @Override // defpackage.an9
   24:     public final Object b(km5 km5Var) {
   25:         q0h q0hVar = descriptor;
   26:         em4 em4VarB = km5Var.b(q0hVar);
   27:         boolean z = true;
   28:         int i = 0;
   29:         String strL = null;
   30:         String strL2 = null;
   31:         while (z) {
   32:             int iH = em4VarB.h(q0hVar);
   33:             if (iH == -1) {
   34:                 z = false;
   35:             } else if (iH == 0) {
   36:                 strL = em4VarB.l(q0hVar, 0);
   37:                 i |= 1;
   38:             } else {
   39:                 if (iH != 1) {
   40:                     kw7.e(iH);
   41:                     return null;
   42:                 }
   43:                 strL2 = em4VarB.l(q0hVar, 1);
   44:                 i |= 2;
   45:             }
   46:         }
   47:         em4VarB.o(q0hVar);
   48:         return new gol(i, strL, strL2);
   49:     }
   50: 
   51:     @Override // defpackage.an9
   52:     public final void c(vq6 vq6Var, Object obj) {
   53:         gol golVar = (gol) obj;
   54:         q0h q0hVar = descriptor;
   55:         gm4 gm4VarB = vq6Var.b(q0hVar);
   56:         gm4VarB.u(q0hVar, 0, golVar.a);
   57:         gm4VarB.u(q0hVar, 1, golVar.b);
   58:         gm4VarB.e();
   59:     }
   60: 
   61:     @Override // defpackage.an9
   62:     public final q0h d() {
   63:         return descriptor;
   64:     }
   65: }
```

### `defpackage/zik.java`

```java
Total lines: 35. Examined: 1–35.
    1: package defpackage;
    2: 
    3: /* JADX WARN: $VALUES field not found */
    4: /* JADX WARN: Failed to restore enum class, 'enum' modifier and super class removed */
    5: /* JADX INFO: loaded from: classes3.dex */
    6: public final class zik implements xcl {
    7:     public static final zik a;
    8:     public static final /* synthetic */ ut6 b;
    9: 
   10:     static {
   11:         zik zikVar = new zik("VERIFY_MOBILE_ID", 0);
   12:         a = zikVar;
   13:         b = new ut6(new zik[]{zikVar});
   14:     }
   15: 
   16:     @Override // defpackage.xcl
   17:     public final Integer a() {
   18:         return null;
   19:     }
   20: 
   21:     @Override // defpackage.xcl
   22:     public final String c() {
   23:         return "WebAppVerifyMobileId";
   24:     }
   25: 
   26:     @Override // defpackage.xcl
   27:     public final String h() {
   28:         return "verify_mobile_id";
   29:     }
   30: 
   31:     @Override // defpackage.xcl
   32:     public final boolean i() {
   33:         return true;
   34:     }
   35: }
```

### `defpackage/ajk.java`

```java
Total lines: 40. Examined: 1–40.
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

### `defpackage/col.java`

```java
Total lines: 24. Examined: 1–24.
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: public final class col extends d55 {
    5:     public zik d;
    6:     public gol e;
    7:     public bol f;
    8:     public /* synthetic */ Object g;
    9:     public final /* synthetic */ dol h;
   10:     public int i;
   11: 
   12:     /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   13:     public col(dol dolVar, d55 d55Var) {
   14:         super(d55Var);
   15:         this.h = dolVar;
   16:     }
   17: 
   18:     @Override // defpackage.hv0
   19:     public final Object w(Object obj) {
   20:         this.g = obj;
   21:         this.i |= Integer.MIN_VALUE;
   22:         return this.h.f(null, this);
   23:     }
   24: }
```

### `defpackage/ekl.java`

```java
Total lines: 820. Examined: 1–160.
    1: package defpackage;
    2: 
    3: import android.content.ContentResolver;
    4: import android.content.ContentValues;
    5: import android.content.Context;
    6: import android.media.MediaScannerConnection;
    7: import android.net.ConnectivityManager;
    8: import android.net.NetworkRequest;
    9: import android.net.Uri;
   10: import android.os.Build;
   11: import android.os.Environment;
   12: import android.provider.MediaStore;
   13: import android.webkit.MimeTypeMap;
   14: import io.jsonwebtoken.JwtParser;
   15: import java.io.File;
   16: import java.io.IOException;
   17: import java.io.OutputStream;
   18: import java.util.ArrayList;
   19: import java.util.HashSet;
   20: import java.util.Iterator;
   21: import java.util.List;
   22: import java.util.Locale;
   23: import java.util.concurrent.ConcurrentHashMap;
   24: import java.util.concurrent.atomic.AtomicBoolean;
   25: import kotlin.collections.a;
   26: import me.leolin.shortcutbadger.BuildConfig;
   27: 
   28: /* JADX INFO: loaded from: classes3.dex */
   29: public final class ekl extends oyk {
   30:     public static final /* synthetic */ zm9[] Q1 = {new c4c(ekl.class, "reloadWebAppJob", "getReloadWebAppJob()Lkotlinx/coroutines/Job;"), a15.f(luf.a, ekl.class, "openInternalLinkJob", "getOpenInternalLinkJob()Lkotlinx/coroutines/Job;"), new c4c(ekl.class, "sharingMaxJob", "getSharingMaxJob()Lkotlinx/coroutines/Job;"), new c4c(ekl.class, "verifyMobileIdJob", "getVerifyMobileId
   31:     public static final String[] R1 = {"image/*", "video/*"};
   32:     public static final HashSet S1;
   33:     public final rp9 A;
   34:     public final z3j A1;
   35:     public final rp9 B;
   36:     public final rp9 B1;
   37:     public final String C;
   38:     public final r4i C1;
   39:     public u5l D;
   40:     public final dmf D1;
   41:     public final z9g E;
   42:     public aj9 E1;
   43:     public final z9g F;
   44:     public m9l F1;
   45:     public final fj9 G;
   46:     public rll G1;
   47:     public final AtomicBoolean H;
   48:     public qll H1;
   49:     public final r4i I;
   50:     public y8l I1;
   51:     public final r4i J;
   52:     public aj9 J1;
   53:     public final ConcurrentHashMap K1;
   54:     public g0i L1;
   55:     public final ConcurrentHashMap M1;
   56:     public final z3j N1;
   57:     public final z9g O1;
   58:     public long P1;
   59:     public final r4i X;
   60:     public final r4i Y;
   61:     public final boolean Z;
   62:     public final long c;
   63:     public final zy c1;
   64:     public final l5l d;
   65:     public final r4i d1;
   66:     public final Long e;
   67:     public boolean e1;
   68:     public final String f;
   69:     public volatile boolean f1;
   70:     public final kkl g;
   71:     public boolean g1;
   72:     public final spl h;
   73:     public volatile String h1;
   74:     public final pol i;
   75:     public volatile String i1;
   76:     public final c74 j;
   77:     public final z9g j1;
   78:     public final pb5 k;
   79:     public final z9g k1;
   80:     public final c88 l;
   81:     public final r4i l1;
   82:     public final k97 m;
   83:     public final c30 m1;
   84:     public final rp9 n;
   85:     public final dmf n1;
   86:     public final rp9 o;
   87:     public final dmf o1;
   88:     public final rp9 p;
   89:     public final dmf p1;
   90:     public final rp9 q;
   91:     public final nih q1;
   92:     public final rp9 r;
   93:     public final xeg r1;
   94:     public final rp9 s;
   95:     public final vv6 s1;
   96:     public final rp9 t;
   97:     public final z3j t1;
   98:     public final rp9 u;
   99:     public final rp9 u1;
  100:     public final rp9 v;
  101:     public final z3j v1;
  102:     public final rp9 w;
  103:     public final rp9 w1;
  104:     public final z3j x;
  105:     public final z3j x1;
  106:     public final rp9 y;
  107:     public final z3j y1;
  108:     public final rp9 z;
  109:     public volatile oil z1;
  110: 
  111:     static {
  112:         HashSet hashSet = new HashSet(jfa.F(5));
  113:         a.j0(new String[]{"WebAppMaxShare", "WebAppShare", "WebAppDownloadFile", "WebAppOpenLink", "WebAppOpenMaxLink"}, hashSet);
  114:         S1 = hashSet;
  115:     }
  116: 
  117:     /* JADX WARN: Code duplicated, block: B:41:0x0354  */
  118:     public ekl(long j, l5l l5lVar, Long l, String str, kkl kklVar, String str2, z3j z3jVar, spl splVar, pol polVar, c74 c74Var, pb5 pb5Var, c88 c88Var, k97 k97Var, rp9 rp9Var, ej9 ej9Var, final rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9, final rp9 rp9Var10, rp9 rp9Var11, final rp9 rp9Var12, final rp9 rp9Var13, final rp
  119:         boolean z;
  120:         String str3;
  121:         this.c = j;
  122:         this.d = l5lVar;
  123:         this.e = l;
  124:         this.f = str;
  125:         this.g = kklVar;
  126:         this.h = splVar;
  127:         this.i = polVar;
  128:         this.j = c74Var;
  129:         this.k = pb5Var;
  130:         this.l = c88Var;
  131:         this.m = k97Var;
  132:         this.n = rp9Var;
  133:         this.o = rp9Var2;
  134:         this.p = rp9Var3;
  135:         this.q = rp9Var5;
  136:         this.r = rp9Var6;
  137:         this.s = rp9Var8;
  138:         this.t = rp9Var9;
  139:         this.u = rp9Var10;
  140:         this.v = rp9Var11;
  141:         this.w = rp9Var12;
  142:         this.x = z3jVar;
  143:         this.y = xnm.p(3, new mlf(rp9Var7, (byte) 16));
  144:         this.z = rp9Var16;
  145:         this.A = rp9Var17;
  146:         this.B = rp9Var19;
  147:         String name = ekl.class.getName();
  148:         this.C = name;
  149:         this.E = c45.Q();
  150:         this.F = c45.Q();
  151:         t45 t45Var = this.b;
  152:         k6j k6jVar = (k6j) ej9Var.a.getValue();
  153:         List list = ej9Var.b;
  154:         aol aolVar = ej9Var.c;
  155:         rp9 rp9Var20 = ej9Var.d;
  156:         fj9 fj9Var = new fj9();
  157:         fj9Var.a = t45Var;
  158:         fj9Var.b = k6jVar;
  159:         fj9Var.c = list;
  160:         fj9Var.d = aolVar;
```

### `defpackage/j01.java`

```java
Total lines: 234. Examined: 1–110.
    1: package defpackage;
    2: 
    3: import kotlin.Metadata;
    4: import me.leolin.shortcutbadger.BuildConfig;
    5: import one.video.calls.sdk.net.signaling.wt.nal.internal.WebTransportSocket;
    6: 
    7: /* JADX INFO: loaded from: classes3.dex */
    8: [long Kotlin metadata/codegen omitted]
    9: public final /* data */ class j01 {
   10: 
   11:     /* JADX INFO: renamed from: a, reason: from kotlin metadata */
   12:     public final long batteryPercent;
   13: 
   14:     /* JADX INFO: renamed from: b, reason: from kotlin metadata */
   15:     public final long cpuTicks;
   16: 
   17:     /* JADX INFO: renamed from: c, reason: from kotlin metadata */
   18:     public final long mobileRxBytes;
   19: 
   20:     /* JADX INFO: renamed from: d, reason: from kotlin metadata */
   21:     public final long mobileTxBytes;
   22: 
   23:     /* JADX INFO: renamed from: e, reason: from kotlin metadata */
   24:     public final long mobileIdleMs;
   25: 
   26:     /* JADX INFO: renamed from: f, reason: from kotlin metadata */
   27:     public final long wifiRxBytes;
   28: 
   29:     /* JADX INFO: renamed from: g, reason: from kotlin metadata */
   30:     public final long wifiTxBytes;
   31: 
   32:     /* JADX INFO: renamed from: h, reason: from kotlin metadata */
   33:     public final long wifiIdleMs;
   34: 
   35:     /* JADX INFO: renamed from: i, reason: from kotlin metadata */
   36:     public final long processes;
   37: 
   38:     /* JADX INFO: renamed from: j, reason: from kotlin metadata */
   39:     public final int networkSourceMask;
   40: 
   41:     /* JADX INFO: renamed from: k, reason: from kotlin metadata */
   42:     public final long maxTemperature;
   43: 
   44:     /* JADX INFO: renamed from: l, reason: from kotlin metadata */
   45:     public final boolean wasBatteryOptimizationsEnabled;
   46: 
   47:     /* JADX INFO: renamed from: m, reason: from kotlin metadata */
   48:     public final boolean wasBackgroundActivityDisabled;
   49: 
   50:     public /* synthetic */ j01(long j, long j2, long j3, long j4, long j5, long j6, long j7, long j8, long j9, int i, long j10, boolean z, boolean z2, int i2, hq5 hq5Var) {
   51:         this((i2 & 1) != 0 ? 0L : j, (i2 & 2) != 0 ? 0L : j2, (i2 & 4) != 0 ? 0L : j3, (i2 & 8) != 0 ? 0L : j4, (i2 & 16) != 0 ? 0L : j5, (i2 & 32) != 0 ? 0L : j6, (i2 & 64) != 0 ? 0L : j7, (i2 & 128) != 0 ? 0L : j8, (i2 & 256) != 0 ? zoe.INSTANCE.a(0L) : j9, (i2 & 512) != 0 ? 0 : i, (i2 & WebTransportSocket.INITIAL_MESSAGE_SIZE) != 0 ? 0L : j10, (i2 & 2048) != 0 ? false : z, (
   52:     }
   53: 
   54:     /* JADX INFO: renamed from: A, reason: from getter */
   55:     public final long getWifiRxBytes() {
   56:         return this.wifiRxBytes;
   57:     }
   58: 
   59:     /* JADX INFO: renamed from: B, reason: from getter */
   60:     public final long getWifiTxBytes() {
   61:         return this.wifiTxBytes;
   62:     }
   63: 
   64:     /* JADX INFO: renamed from: a, reason: from getter */
   65:     public final long getBatteryPercent() {
   66:         return this.batteryPercent;
   67:     }
   68: 
   69:     /* JADX INFO: renamed from: b, reason: from getter */
   70:     public final int getNetworkSourceMask() {
   71:         return this.networkSourceMask;
   72:     }
   73: 
   74:     /* JADX INFO: renamed from: c, reason: from getter */
   75:     public final long getMaxTemperature() {
   76:         return this.maxTemperature;
   77:     }
   78: 
   79:     /* JADX INFO: renamed from: d, reason: from getter */
   80:     public final boolean getWasBatteryOptimizationsEnabled() {
   81:         return this.wasBatteryOptimizationsEnabled;
   82:     }
   83: 
   84:     /* JADX INFO: renamed from: e, reason: from getter */
   85:     public final boolean getWasBackgroundActivityDisabled() {
   86:         return this.wasBackgroundActivityDisabled;
   87:     }
   88: 
   89:     public boolean equals(Object other) {
   90:         if (this == other) {
   91:             return true;
   92:         }
   93:         if (!(other instanceof j01)) {
   94:             return false;
   95:         }
   96:         j01 j01Var = (j01) other;
   97: [long Kotlin metadata/codegen omitted]
   98:     }
   99: 
  100:     /* JADX INFO: renamed from: f, reason: from getter */
  101:     public final long getCpuTicks() {
  102:         return this.cpuTicks;
  103:     }
  104: 
  105:     /* JADX INFO: renamed from: g, reason: from getter */
  106:     public final long getMobileRxBytes() {
  107:         return this.mobileRxBytes;
  108:     }
  109: 
  110:     /* JADX INFO: renamed from: h, reason: from getter */
```

## Применение результатов

Этот отчёт предназначен для ручной проверки того, какие поля, обработчики и результаты связаны с вызовом мини-приложения.
Он не содержит исполняемых рекомендаций по подмене Mobile ID или серверного подтверждения.
Наличие класса не доказывает, что конкретный запуск мини-приложения использовал данный путь.
