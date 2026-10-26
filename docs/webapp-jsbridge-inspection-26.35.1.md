# Android MAX 26.35.1 — структура JS bridge (read-only)

APK sha256: `e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc`.
Анализ: исходники JADX; `WebAppVerifyMobileId` и `no_cellular` без вызовов сервера.

## Индекс классов

- `defpackage/a8l.java`: строк 705, совпадений 1.
- `defpackage/dol.java`: строк 240, совпадений 4.
- `defpackage/eol.java`: строк 65, совпадений 1.
- `defpackage/gol.java`: строк 37, совпадений 1.
- `defpackage/hol.java`: строк 83, совпадений 1.
- `defpackage/jol.java`: строк 56, совпадений 1.
- `defpackage/jql.java`: строк 24, совпадений 4.
- `defpackage/kfl.java`: строк 33, совпадений 2.
- `defpackage/koe.java`: строк 17, совпадений 3.
- `defpackage/pil.java`: строк 170, совпадений 3.
- `defpackage/zik.java`: строк 35, совпадений 1.
- `one/me/webapp/domain/jsbridge/WebAppJsonException.java`: строк 13, совпадений 2.
- `one/me/webapp/rootscreen/WebAppRootScreen.java`: строк 1179, совпадений 3.
- `one/me/webapp/util/WebAppHttpClient$WebAppNoNetworkException.java`: строк 8, совпадений 2.
- `org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java`: строк 67, совпадений 3.

## Основные места внедрения JavascriptInterface/JS API

### `defpackage/a8l.java`

```java
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
658:                     abl ablVar = new abl(((xal) this.i).a, String.valueOf(nzkVar.a), String.valueOf(nzkVar.b));
```

### `defpackage/dol.java`

```java
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
```

### `defpackage/eol.java`

```java
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
```

### `defpackage/gol.java`

```java
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
```

### `defpackage/jol.java`

```java
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

### `defpackage/jql.java`

```java
1: package defpackage;
2: 
3: import android.webkit.JavascriptInterface;
4: 
5: /* JADX INFO: loaded from: classes3.dex */
6: public final class jql {
7:     public final ekl a;
8: 
9:     public jql(ekl eklVar) {
10:         this.a = eklVar;
11:     }
12: 
13:     @JavascriptInterface
14:     public final void postEvent(String str, String str2) {
15:         this.a.j1(str, str2, false);
16:     }
17: 
18:     @JavascriptInterface
19:     public final void resolveShare(String str, byte[] bArr, String str2, String str3) {
20:         ekl eklVar = this.a;
21:         eklVar.getClass();
22:         oyk.Z0(eklVar, null, new m60(eklVar, str, bArr, str2, str3, null, (byte) 14), 3);
23:     }
24: }
```

### `defpackage/kfl.java`

```java
1: package defpackage;
2: 
3: import android.webkit.JavascriptInterface;
4: 
5: /* JADX INFO: loaded from: classes3.dex */
6: public final class kfl {
7:     public final pol a;
8: 
9:     public kfl(pol polVar) {
10:         this.a = polVar;
11:     }
12: 
13:     @JavascriptInterface
14:     public final void trackFcp(long j) {
15:         pol polVar = this.a;
16:         String str = polVar.g;
17:         lmj lmjVar = str != null ? new lmj(str) : null;
18:         String str2 = lmjVar != null ? lmjVar.a : null;
19:         if (str2 != null && str2.length() != 0) {
20:             polVar.f(str2, new vld("fcp", Long.valueOf(j)));
21:             return;
22:         }
23:         String str3 = polVar.b;
24:         o1d o1dVar = f09.g;
25:         if (o1dVar == null) {
26:             return;
27:         }
28:         c6a c6aVar = c6a.f;
29:         if (o1dVar.b(c6aVar)) {
30:             o1dVar.c(c6aVar, str3, "Invoked 'fcp', but traceId is null or empty!", null);
31:         }
32:     }
33: }
```

### `defpackage/koe.java`

```java
1: package defpackage;
2: 
3: import android.webkit.JavascriptInterface;
4: 
5: /* JADX INFO: loaded from: classes3.dex */
6: public final class koe {
7:     public final ekl a;
8: 
9:     public koe(ekl eklVar) {
10:         this.a = eklVar;
11:     }
12: 
13:     @JavascriptInterface
14:     public final void postEvent(String str, String str2) {
15:         this.a.j1(str, str2, true);
16:     }
17: }
```

### `defpackage/pil.java`

```java
112:                 }
113:                 if (((Boolean) webAppRootScreen.L1().M().i()).booleanValue()) {
114:                     Bundle bundle = webAppRootScreen.E;
115:                     if (bundle != null) {
116:                         cngVar.restoreState(bundle);
117:                     }
118:                 } else {
119:                     webAppRootScreen.setRetainViewMode(j55.b);
120:                 }
121:                 til tilVar = webAppRootScreen.r;
122:                 if (tilVar != null) {
123:                     cngVar.postVisualStateCallback(99991L, tilVar);
124:                 }
125:                 cngVar.setWebViewClient(new pad(webAppRootScreen.m.getAccessor().d(11), new ypl(webAppRootScreen.N1(), new hsb(context, (byte) 18), webAppRootScreen.n)));
126:                 cngVar.setWebChromeClient(new nad(new x5b(webAppRootScreen.N1(), (byte) 17), new lql(webAppRootScreen.n), ((Boolean) webAppRootScreen.L1().C().i()).booleanValue()));
127:                 cngVar.addJavascriptInterface(new jql(webAppRootScreen.N1()), "WebViewHandler");
128:                 cngVar.addJavascriptInterface(new kfl(webAppRootScreen.n), "AndroidPerf");
129:                 if (webAppRootScreen.N1().Z) {
130:                     cngVar.addJavascriptInterface(new koe(webAppRootScreen.N1()), "PrivateWebViewHandler");
131:                 }
132:                 g4d g4dVar = new g4d(frameLayout.getContext());
133:                 g4dVar.setId(R.id.webapp_root_progressbar);
134:                 g4dVar.setLayoutParams(new FrameLayout.LayoutParams(-2, -2, 17));
135:                 g4dVar.l(v3d.a);
136:                 yyc yycVar = new yyc(frameLayout.getContext());
137:                 yycVar.setId(R.id.webapp_root_error_container);
138:                 FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(-1, -2, 17);
139:                 layoutParams.setMarginStart(nb6.t(i36.d().getDisplayMetrics().density * r7));
140:                 layoutParams.setMarginEnd(nb6.t(i36.d().getDisplayMetrics().density * 20.0f));
141:                 yycVar.setLayoutParams(layoutParams);
142:                 yycVar.j(R.drawable.icon_warning);
143:                 yycVar.m(new mdj(R.string.technical_problems));
144:                 yycVar.l(new mdj(R.string.wait_and_retry));
145:                 yycVar.k(c45.D(R.string.retry, webAppRootScreen.getContext()), new y3k(webAppRootScreen, (byte) 8));
146:                 frameLayout.addView(cngVar);
147:                 e0c.M(new dk7(nm9.n(new c30(webAppRootScreen.N1().p1, (byte) 12), webAppRootScreen.getViewLifecycleOwner().f(), nr9.d), new l1c((b55) null, webAppRootScreen, cngVar, frameLayout, yycVar, g4dVar), (byte) 3), webAppRootScreen.getViewLifecycleScope());
148:                 linearLayout.addView(frameLayout);
149:                 return s1k.a;
150:             case 1:
151:                 WebAppRootScreen webAppRootScreen2 = this.b;
```

### `defpackage/qrk.java`

```java
707:                     if (!z18) {
708:                         k3g.o("call to 'resume' before 'invoke' with coroutine");
709:                         return null;
710:                     }
711:                     xnm.y(obj);
712:                 }
713:                 knlVar2.k(fnlVar2.a);
714:                 return s1k.a;
715:             case 17:
716:                 dol dolVar = (dol) this.h;
717:                 Throwable th7 = (Throwable) this.g;
718:                 ka5 ka5Var18 = ka5.a;
719:                 boolean z19 = this.f;
720:                 if (!z19) {
721:                     xnm.y(obj);
722:                     ij9 gj9Var2 = th7 instanceof CancellationException ? new gj9(new jj9("cancelled", 0)) : th7 instanceof WebAppHttpClient$WebAppNoNetworkException ? new gj9(new jj9("no_cellular", 1)) : hj9.d;
723:                     qi4 qi4Var3 = (qi4) dolVar.b.getValue();
724:                     bb1 bb1Var11 = dolVar.d;
725:                     zik zikVar = zik.a;
726:                     String str19 = ((gol) this.i).a;
727:                     this.g = null;
728:                     this.f = true;
729:                     if (qi4Var3.a(bb1Var11, gj9Var2, zikVar, str19, this) == ka5Var18) {
730:                         return ka5Var18;
731:                     }
732:                 } else {
733:                     if (!z19) {
734:                         k3g.o("call to 'resume' before 'invoke' with coroutine");
735:                         return null;
736:                     }
737:                     xnm.y(obj);
738:                 }
739:                 return s1k.a;
740:             case 18:
741:                 Object obj3 = this.g;
742:                 ka5 ka5Var19 = ka5.a;
743:                 boolean z20 = this.f;
```

### `defpackage/zik.java`

```java
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

### `one/me/webapp/rootscreen/WebAppRootScreen.java`

```java
875:         t5l t5lVar = (t5l) eklVarN2.q.getValue();
876:         u5l u5lVar = eklVarN2.D;
877:         if (u5lVar != null) {
878:             t5lVar.a(2, u5lVar.a, u5lVar.b, u5lVar.c, u5lVar.d);
879:         }
880:     }
881: 
882:     @Override // com.bluelinelabs.conductor.Controller
883:     public final void onDestroyView(View view) {
884:         super.onDestroyView(view);
885:         ekl eklVarN1 = N1();
886:         if (eklVarN1.A1.d()) {
887:             ((adl) eklVarN1.A1.getValue()).b();
888:         }
889:         this.r = null;
890:         O1().removeJavascriptInterface("WebViewHandler");
891:         if (N1().Z) {
892:             O1().removeJavascriptInterface("PrivateWebViewHandler");
893:         }
894:         O1().removeJavascriptInterface("AndroidPerf");
895:         this.C.b = wt0.j;
896:         this.u = null;
897:     }
898: 
899:     @Override // com.bluelinelabs.conductor.Controller
900:     public final void onDetach(View view) {
901:         super.onDetach(view);
902:         N1().z1 = null;
903:         ekl eklVarN1 = N1();
904:         if (eklVarN1.A1.d()) {
905:             ((adl) eklVarN1.A1.getValue()).a();
906:         }
907:         N1().c1.e();
908:         getRouter().M(this.s);
909:         N1().f1 = false;
910:     }
911: 
912:     @Override // defpackage.k45
913:     public final void onDismiss() {
914:         zm9[] zm9VarArr = H;
915:         zm9 zm9Var = zm9VarArr[8];
```

### `org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java`

```java
12: import java.util.LinkedHashMap;
13: import java.util.List;
14: import java.util.function.BiConsumer;
15: import java.util.function.Consumer;
16: 
17: /* JADX INFO: loaded from: classes3.dex */
18: public interface WebViewBuilderBoundaryInterface {
19: 
20:     @Retention(RetentionPolicy.SOURCE)
21:     public @interface Baseline {
22:         public static final int DEFAULT = 0;
23:     }
24: 
25:     public static class Config implements Consumer<BiConsumer<Integer, Object>> {
26:         public String profileName;
27:         public boolean restrictJavascriptInterface;
28:         public int baseline = 0;
29:         public final ArrayList a = new ArrayList();
30:         public final LinkedHashMap b = new LinkedHashMap();
31:         public final ArrayList c = new ArrayList();
32: 
33:         @Override // java.util.function.Consumer
34:         public void accept(BiConsumer<Integer, Object> biConsumer) {
35:             biConsumer.accept(0, Integer.valueOf(this.baseline));
36:             biConsumer.accept(2, Boolean.valueOf(this.restrictJavascriptInterface));
37:             biConsumer.accept(1, new Object[]{this.a, new ArrayList(this.b.keySet()), this.c});
38:             if (this.profileName != null) {
39:                 biConsumer.accept(3, this.profileName);
40:             }
41:         }
42: 
43:         public void addJavascriptInterface(Object obj, String str, List<String> list) {
44:             LinkedHashMap linkedHashMap = this.b;
45:             if (linkedHashMap.containsKey(str)) {
46:                 k3g.t(vg9.y("A duplicate JavaScript interface was provided for \"", str, "\""));
47:                 return;
48:             }
49:             this.a.add(obj);
50:             linkedHashMap.put(str, Boolean.TRUE);
51:             this.c.add(list);
52:         }
53:     }
54: 
55:     @Target({ElementType.TYPE_USE})
56:     @Retention(RetentionPolicy.SOURCE)
57:     public @interface ConfigField {
58:         public static final int BASELINE = 0;
59:         public static final int JAVASCRIPT_INTERFACE = 1;
60:         public static final int PROFILE_NAME = 3;
61:         public static final int RESTRICT_JAVASCRIPT_INTERFACE = 2;
62:     }
63: 
64:     void applyTo(WebView webView, Consumer<BiConsumer<Integer, Object>> consumer);
```

## Exact client-error serialization structures

### `gu6.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: @x0h
5: public final class gu6 {
6:     public static final cu6 Companion = new cu6();
7:     public final String a;
8:     public final fu6 b;
9: 
10:     public /* synthetic */ gu6(int i, String str, fu6 fu6Var) {
11:         if (3 != (i & 3)) {
12:             az7.S(i, 3, bu6.a.d());
13:             throw null;
14:         }
15:         this.a = str;
16:         this.b = fu6Var;
17:     }
18: 
19:     public final boolean equals(Object obj) {
20:         if (this == obj) {
21:             return true;
22:         }
23:         if (!(obj instanceof gu6)) {
24:             return false;
25:         }
26:         gu6 gu6Var = (gu6) obj;
27:         return g4a.c(this.a, gu6Var.a) && g4a.c(this.b, gu6Var.b);
28:     }
29: 
30:     public final int hashCode() {
31:         return this.b.hashCode() + (this.a.hashCode() * 31);
32:     }
33: 
34:     public final String toString() {
35:         return "ErrorResponse(requestId=" + this.a + ", error=" + this.b + ")";
36:     }
37: 
38:     public gu6(String str, fu6 fu6Var) {
39:         this.a = str;
40:         this.b = fu6Var;
41:     }
42: }
```

### `fu6.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: @x0h
5: public final class fu6 {
6:     public static final eu6 Companion = new eu6();
7:     public final String a;
8: 
9:     public /* synthetic */ fu6(int i, String str) {
10:         if (1 == (i & 1)) {
11:             this.a = str;
12:         } else {
13:             az7.S(i, 1, du6.a.d());
14:             throw null;
15:         }
16:     }
17: 
18:     public fu6(String str) {
19:         this.a = str;
20:     }
21: }
```

### `jj9.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: public final class jj9 {
5:     public final String a;
6:     public final int b;
7: 
8:     public jj9(String str, int i) {
9:         this.a = str;
10:         this.b = i;
11:     }
12: 
13:     public final boolean equals(Object obj) {
14:         if (this == obj) {
15:             return true;
16:         }
17:         if (!(obj instanceof jj9)) {
18:             return false;
19:         }
20:         jj9 jj9Var = (jj9) obj;
21:         return this.a.equals(jj9Var.a) && this.b == jj9Var.b;
22:     }
23: 
24:     public final int hashCode() {
25:         return Integer.hashCode(this.b) + (this.a.hashCode() * 31);
26:     }
27: 
28:     public final String toString() {
29:         return vg9.w(this.b, "JsBridgeMethodErrorReason(title=", this.a, ", code=", ")");
30:     }
31: }
```

### `gj9.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: public final class gj9 extends ij9 {
5:     public final jj9 d;
6: 
7:     public gj9(jj9 jj9Var) {
8:         super("client", 1, jj9Var);
9:         this.d = jj9Var;
10:     }
11: 
12:     @Override // defpackage.ij9
13:     public final jj9 b() {
14:         return this.d;
15:     }
16: 
17:     public final boolean equals(Object obj) {
18:         if (this == obj) {
19:             return true;
20:         }
21:         return (obj instanceof gj9) && this.d.equals(((gj9) obj).d);
22:     }
23: 
24:     public final int hashCode() {
25:         return this.d.hashCode();
26:     }
27: 
28:     public final String toString() {
29:         return "ClientError(reason=" + this.d + ")";
30:     }
31: }
```

### `hj9.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: public final class hj9 extends ij9 {
5:     public static final hj9 d = new hj9("unknown", 6, null);
6: 
7:     public final boolean equals(Object obj) {
8:         return this == obj || (obj instanceof hj9);
9:     }
10: 
11:     public final int hashCode() {
12:         return -745687876;
13:     }
14: 
15:     public final String toString() {
16:         return "UnknownError";
17:     }
18: }
```

### `ij9.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: public abstract class ij9 {
5:     public final String a;
6:     public final byte b;
7:     public final jj9 c;
8: 
9:     /* JADX WARN: Multi-variable type inference failed */
10:     public ij9(String str, int i, jj9 jj9Var) {
11:         this.a = str;
12:         this.b = i;
13:         this.c = jj9Var;
14:     }
15: 
16:     public final String a(String str) {
17:         StringBuilder sb = new StringBuilder(this.a.concat("."));
18:         sb.append(str);
19:         jj9 jj9VarB = b();
20:         if (jj9VarB != null) {
21:             sb.append(".".concat(jj9VarB.a));
22:         }
23:         return sb.toString();
24:     }
25: 
26:     public jj9 b() {
27:         return this.c;
28:     }
29: }
```

### `qi4.java`

```java
1: package defpackage;
2: 
3: /* JADX INFO: loaded from: classes3.dex */
4: public final class qi4 {
5:     public final mj9 a;
6:     public final rp9 b;
7:     public u5l c;
8: 
9:     public qi4(mj9 mj9Var, rp9 rp9Var) {
10:         this.a = mj9Var;
11:         this.b = rp9Var;
12:     }
13: 
14:     /* JADX WARN: Code duplicated, block: B:7:0x001b  */
15:     public final Object a(b13 b13Var, ij9 ij9Var, xcl xclVar, String str, b55 b55Var) {
16:         pi4 pi4Var;
17:         String str2;
18:         xcl xclVar2;
19:         ij9 ij9Var2 = ij9Var;
20:         if (b55Var instanceof pi4) {
21:             pi4Var = (pi4) b55Var;
22:             int i = pi4Var.i;
23:             if ((i & Integer.MIN_VALUE) != 0) {
24:                 pi4Var.i = i - Integer.MIN_VALUE;
25:             } else {
26:                 pi4Var = new pi4(this, b55Var);
27:             }
28:         } else {
29:             pi4Var = new pi4(this, b55Var);
30:         }
31:         Object obj = pi4Var.g;
32:         int i2 = pi4Var.i;
33:         s1k s1kVar = s1k.a;
34:         if (i2 == 0) {
35:             xnm.y(obj);
36:             f09.p(qi4.class.getName(), "Error in method: " + xclVar.c() + " - " + ij9Var2.a(xclVar.h()));
37:             if (str == null) {
38:                 f09.f0(qi4.class.getName(), "No request id or wrong type");
39:                 return s1kVar;
40:             }
41:             String strC = xclVar.c();
42:             gu6 gu6Var = new gu6(str, new fu6(ij9Var2.a(xclVar.h())));
43:             mj9 mj9Var = this.a;
44:             mj9Var.getClass();
45:             Object bj9Var = new bj9(strC, mj9Var.b(gu6.Companion.serializer(), gu6Var), xclVar.i());
46:             pi4Var.d = ij9Var2;
47:             pi4Var.e = xclVar;
48:             pi4Var.f = strC;
49:             pi4Var.i = 1;
50:             Object objB = b13Var.b(pi4Var, bj9Var);
51:             Object obj2 = ka5.a;
52:             if (objB == obj2) {
53:                 return obj2;
54:             }
55:             str2 = strC;
56:             xclVar2 = xclVar;
57:         } else {
58:             if (i2 != 1) {
59:                 k3g.o("call to 'resume' before 'invoke' with coroutine");
60:                 return null;
61:             }
62:             String str3 = pi4Var.f;
63:             xclVar2 = pi4Var.e;
64:             ij9 ij9Var3 = pi4Var.d;
65:             xnm.y(obj);
66:             str2 = str3;
67:             ij9Var2 = ij9Var3;
68:         }
69:         byte b = ij9Var2.b;
70:         Integer numA = xclVar2.a();
71:         jj9 jj9VarB = ij9Var2.b();
72:         Integer num = jj9VarB != null ? new Integer(jj9VarB.b) : null;
73:         u5l u5lVar = this.c;
74:         if (u5lVar != null) {
75:             o8l.a((o8l) this.b.getValue(), str2, u5lVar.a, u5lVar.b, false, b, numA, num, 128);
76:         }
77:         return s1kVar;
78:     }
79: }
```

### `jql.java`

```java
1: package defpackage;
2: 
3: import android.webkit.JavascriptInterface;
4: 
5: /* JADX INFO: loaded from: classes3.dex */
6: public final class jql {
7:     public final ekl a;
8: 
9:     public jql(ekl eklVar) {
10:         this.a = eklVar;
11:     }
12: 
13:     @JavascriptInterface
14:     public final void postEvent(String str, String str2) {
15:         this.a.j1(str, str2, false);
16:     }
17: 
18:     @JavascriptInterface
19:     public final void resolveShare(String str, byte[] bArr, String str2, String str3) {
20:         ekl eklVar = this.a;
21:         eklVar.getClass();
22:         oyk.Z0(eklVar, null, new m60(eklVar, str, bArr, str2, str3, null, (byte) 14), 3);
23:     }
24: }
```

### `koe.java`

```java
1: package defpackage;
2: 
3: import android.webkit.JavascriptInterface;
4: 
5: /* JADX INFO: loaded from: classes3.dex */
6: public final class koe {
7:     public final ekl a;
8: 
9:     public koe(ekl eklVar) {
10:         this.a = eklVar;
11:     }
12: 
13:     @JavascriptInterface
14:     public final void postEvent(String str, String str2) {
15:         this.a.j1(str, str2, true);
16:     }
17: }
```

### `ypl.java`

```java
1: package defpackage;
2: 
3: import android.content.ActivityNotFoundException;
4: import android.content.Context;
5: import android.content.Intent;
6: import android.content.SharedPreferences;
7: import android.content.res.ColorStateList;
8: import android.graphics.Rect;
9: import android.graphics.drawable.Drawable;
10: import android.graphics.drawable.LayerDrawable;
11: import android.graphics.drawable.ShapeDrawable;
12: import android.graphics.drawable.shapes.OvalShape;
13: import android.hardware.camera2.CameraCharacteristics;
14: import android.hardware.camera2.CaptureRequest;
15: import android.media.metrics.LogSessionId;
16: import android.net.Uri;
17: import android.os.Build;
18: import android.os.Handler;
19: import android.text.TextUtils;
20: import android.util.Log;
21: import android.view.Surface;
22: import android.view.View;
23: import android.webkit.URLUtil;
24: import androidx.camera.video.internal.encoder.EncodeException;
25: import com.vk.push.pushsdk.receiver.OneTimePushReceiveHelper$SyncTimeoutExceededException;
26: import java.io.BufferedReader;
27: import java.io.IOException;
28: import java.lang.ref.WeakReference;
29: import java.net.CookieManager;
30: import java.net.HttpURLConnection;
31: import java.net.URI;
32: import java.util.ArrayDeque;
33: import java.util.ArrayList;
34: import java.util.Collection;
35: import java.util.Collections;
36: import java.util.HashMap;
37: import java.util.Iterator;
38: import java.util.List;
39: import java.util.Locale;
40: import java.util.Map;
41: import java.util.concurrent.CountDownLatch;
42: import java.util.concurrent.ScheduledThreadPoolExecutor;
43: import java.util.concurrent.TimeUnit;
44: import java.util.concurrent.atomic.AtomicBoolean;
45: import me.leolin.shortcutbadger.BuildConfig;
46: import one.me.calls.ui.ui.call.panels.VpnPanelWidget;
47: import one.me.sdk.transfer.exceptions.HttpUrlExpiredException;
48: import one.video.upload.exceptions.UploadUrlExpiredException;
49: 
50: /* JADX INFO: loaded from: classes3.dex */
51: public final class ypl implements xpl, h84, sk4, pxl, di, u7k, y18, xq6, g3j {
52:     public Object a;
53:     public Object b;
54:     public Object c;
55: 
56:     public ypl(b07 b07Var, Context context) {
57:         this.c = b07Var;
58:         this.a = new WeakReference(context);
59:         hn3 hn3Var = new hn3(this, (byte) 1);
60:         this.b = hn3Var;
61:         context.registerDeviceIdChangeListener(new a07(((d4j) b07Var.w).a(b07Var.u, null), (byte) 0), hn3Var);
62:     }
63: 
64:     /* JADX WARN: Code duplicated, block: B:28:0x0059  */
65:     public static vgm G(HttpURLConnection httpURLConnection, int i) {
66:         String headerField = httpURLConnection.getHeaderField("Location");
67:         if (headerField == null || headerField.isEmpty()) {
68:             return new vgm(2, i, null, "empty redirection");
69:         }
70:         try {
71:             String string = httpURLConnection.getURL().toURI().resolve(new URI(headerField)).toString();
72:             boolean z = Build.VERSION.SDK_INT < 28 || URLUtil.isHttpsUrl(string);
73:             if (!TextUtils.isEmpty(string)) {
74:                 for (int i2 = 0; i2 < 13; i2++) {
75:                     if (!string.startsWith(gom.a[i2])) {
76:                     }
77:                 }
78:                 if (!z) {
79:                     return new vgm(2, i, null, pq0.i("cleartext redirect blocked: ", string));
80:                 }
81:             } else if (!z) {
82:                 return new vgm(2, i, null, pq0.i("cleartext redirect blocked: ", string));
83:             }
84:             return new vgm(1, i, string, null);
85:         } catch (Throwable unused) {
86:             return new vgm(0, i, headerField, null);
87:         }
88:     }
89: 
90:     public static void J(ypl yplVar) {
91:         Context context = (Context) ((WeakReference) yplVar.a).get();
92:         if (context == null) {
93:             return;
94:         }
95:         context.unregisterDeviceIdChangeListener((hn3) yplVar.b);
96:     }
97: 
98:     public static ypl N(SharedPreferences sharedPreferences, ScheduledThreadPoolExecutor scheduledThreadPoolExecutor) {
99:         ypl yplVar = new ypl();
100:         yplVar.b = new ArrayDeque();
101:         yplVar.a = sharedPreferences;
102:         yplVar.c = scheduledThreadPoolExecutor;
103:         synchronized (((ArrayDeque) yplVar.b)) {
104:             try {
105:                 ((ArrayDeque) yplVar.b).clear();
106:                 String string = ((SharedPreferences) yplVar.a).getString("topic_operation_queue", BuildConfig.FLAVOR);
107:                 if (!TextUtils.isEmpty(string) && string.contains(",")) {
108:                     String[] strArrSplit = string.split(",", -1);
109:                     if (strArrSplit.length == 0) {
110:                         Log.e("FirebaseMessaging", "Corrupted queue. Please check the queue contents and item separator provided");
111:                     }
112:                     for (String str : strArrSplit) {
113:                         if (!TextUtils.isEmpty(str)) {
114:                             ((ArrayDeque) yplVar.b).add(str);
115:                         }
116:                     }
117:                     return yplVar;
118:                 }
119:                 return yplVar;
120:             } catch (Throwable th) {
121:                 throw th;
122:             }
123:         }
124:     }
125: 
126:     @Override // defpackage.pxl
127:     public ow5 A(hbk hbkVar) {
128:         return hbkVar.h(Collections.singletonList(CaptureRequest.SCALER_CROP_REGION));
129:     }
130: 
131:     @Override // defpackage.xpl
132:     public void B(String str) {
133:         pol polVar = (pol) this.c;
134:         String str2 = polVar.g;
135:         lmj lmjVar = str2 != null ? new lmj(str2) : null;
136:         String str3 = lmjVar != null ? lmjVar.a : null;
137:         if (str3 == null || str3.length() == 0) {
138:             String str4 = polVar.b;
139:             o1d o1dVar = f09.g;
140:             if (o1dVar != null) {
141:                 c6a c6aVar = c6a.f;
142:                 if (o1dVar.b(c6aVar)) {
143:                     o1dVar.c(c6aVar, str4, "Invoked 'webapp_nav_start', but traceId is null or empty!", null);
144:                 }
145:             }
146:         } else {
147:             wud.h(polVar, "nav_start", 2, str3, false, null, null, 120);
148:         }
149:         ((ekl) this.a).o1(str, false);
150:     }
151: 
152:     @Override // defpackage.pxl
153:     public ow5 C(float f, hbk hbkVar) {
154:         Rect rect = (Rect) this.c;
155:         if (Math.abs(f) < ((double) Math.ulp(Math.abs(f))) * 2.0d) {
156:             if (ywm.i(5, "CXCP")) {
157:                 Log.w("CXCP", "ZoomCompat: Invalid zoom ratio of 0.0f passed in, defaulting to 1.0f");
158:             }
159:             f = 1.0f;
160:         }
161:         float fWidth = rect.width() / f;
162:         float fHeight = rect.height() / f;
163:         float fWidth2 = (rect.width() - fWidth) / 2.0f;
164:         float fHeight2 = (rect.height() - fHeight) / 2.0f;
165:         Rect rect2 = new Rect((int) fWidth2, (int) fHeight2, (int) (fWidth2 + fWidth), (int) (fHeight2 + fHeight));
166:         this.b = rect2;
167:         return hbkVar.k(Collections.singletonMap(CaptureRequest.SCALER_CROP_REGION, rect2), fbk.b);
168:     }
169: 
170:     @Override // defpackage.xq6
171:     public void D(v93 v93Var) {
172:         ((wsf) this.c).I = v93Var;
173:     }
174: 
175:     @Override // defpackage.di
176:     public synchronized int E() {
177:         ((ys5) this.c).c.getClass();
178:         return 65536;
179:     }
180: 
181:     /* JADX WARN: Code duplicated, block: B:7:0x0013  */
182:     public Object F(String str, d55 d55Var) {
183:         fcm fcmVar;
184:         if (d55Var instanceof fcm) {
185:             fcmVar = (fcm) d55Var;
186:             int i = fcmVar.f;
187:             if ((i & Integer.MIN_VALUE) != 0) {
188:                 fcmVar.f = i - Integer.MIN_VALUE;
189:             } else {
190:                 fcmVar = new fcm(this, d55Var);
```
