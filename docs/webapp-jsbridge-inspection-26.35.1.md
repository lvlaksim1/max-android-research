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
36:         f09.d0(dol.class.getName(), "Unknown method with name = " + str + " in JsDelegate: " + this, new Object[0]);
37:         return s1kVar;
38:     }
39: 
40:     @Override // defpackage.kj9
41:     public final boolean b(String str) {
42:         if (str.equals("WebAppVerifyMobileId")) {
43:             return true;
44:         }
45:         f09.d0(dol.class.getName(), "Unknown method with name = " + str + " in JsDelegate: " + this, new Object[0]);
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
