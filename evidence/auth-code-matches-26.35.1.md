# MAX 26.35.1: ссылки на участки кода

Автоматические совпадения строк в выводе JADX. Возможны ошибки декомпиляции.
SHA-256: e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc

## defpackage/rkg.java (приоритет 81)
- Строка 12; AUTH_OTP: AUTH_OTP(52),
- Строка 15; AUTH_CALL_OUT: AUTH_CALL_OUT(55),
- Строка 138; AUTH_2FA: AUTH_2FA_PASSWORD_CREATE(760),
- Строка 139; AUTH_2FA: AUTH_2FA_SUGGEST(761),
- Строка 140; AUTH_2FA: AUTH_2FA_EMAIL(762),
- Строка 141; AUTH_2FA: AUTH_2FA_EMAIL_CODE(763),
- Строка 142; AUTH_2FA: AUTH_2FA_SUCCESS(764),
- Строка 143; AUTH_2FA: AUTH_2FA_PASSWORD_INPUT(765),
- Строка 144; AUTH_2FA: AUTH_2FA_START(766),

## one/me/settings/twofa/creation/TwoFACreationScreen.java (приоритет 75)
- Строка 119; AUTH_2FA: return rkg.AUTH_2FA_PASSWORD_CREATE;
- Строка 122; AUTH_2FA: return rkg.AUTH_2FA_SUGGEST;
- Строка 125; AUTH_2FA: return rkg.AUTH_2FA_EMAIL;
- Строка 128; AUTH_2FA: return rkg.AUTH_2FA_EMAIL_CODE;
- Строка 188; AUTH_2FA: return rkg.AUTH_2FA_PASSWORD_CREATE;
- Строка 191; AUTH_2FA: return rkg.AUTH_2FA_SUGGEST;
- Строка 194; AUTH_2FA: return rkg.AUTH_2FA_EMAIL;
- Строка 197; AUTH_2FA: return rkg.AUTH_2FA_EMAIL_CODE;

## defpackage/tdd.java (приоритет 45)
- Строка 72; AUTH_CHECK_PASSWORD: public static final tdd w = new tdd("AUTH_CHECK_PASSWORD", 17, 113, lrh.d);
- Строка 81; AUTH_2FA: public static final tdd F = new tdd("AUTH_2FA_DETAILS", 26, 104, nt6.c);
- Строка 255; AUTH_QR_APPROVE: H3 = new tdd("AUTH_QR_APPROVE", 169, (short) 290, cg6Var);
- Строка 257; AUTH_BY_TRACK: J3 = new tdd("AUTH_BY_TRACK", 171, (short) 291, df7.c);
- Строка 258; AUTH_CHECK_CALL: K3 = new tdd("AUTH_CHECK_CALL", 172, (short) 294, ih0.b);

## one/me/login/inputphone/InputPhoneScreen.java (приоритет 33)
- Строка 101; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 107; InputPhoneScreen: @Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\b\u0001\u0018\u00002\u00020\u00012\u00020\u00022\u00020\u0003B\u000f\u0012\u0006\u0010\u0005\u001a\u00020\u0004¢\u0006\u0004\b\u0006\u0010\u0007B\u001b\b\u0016\u0012\u0006\u0010\t\u001a\u00020\b\
- Строка 108; InputPhoneScreen: public final class InputPhoneScreen extends Widget implements cb5 {
- Строка 109; InputPhoneScreen: public static final /* synthetic */ zm9[] w = {new c4c(InputPhoneScreen.class, "phone", "getPhone()Ljava/lang/String;"), vg9.s(luf.a, InputPhoneScreen.class, "isAddAccountLogin", "isAddAccountLogin()Z", 0), new v4f(InputPhoneScreen.class, "gradientBgView", "getGradientBgView()Landroid/view/View;", 0), new v4f(InputPhoneScreen.class, "continueButton", "getContinueButton()Lone/me/sdk/uikit/common/bu
- Строка 133; InputPhoneScreen: public InputPhoneScreen(Bundle bundle) {
- Строка 136; InputPhoneScreen: this.b = InputPhoneScreen.class.getName();
- Строка 227; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen b;
- Строка 237; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.b;
- Строка 238; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;

## one/me/settings/twofa/password/TwoFACheckPassScreen.java (приоритет 30)
- Строка 121; AUTH_2FA: return rkg.AUTH_2FA_PASSWORD_INPUT;
- Строка 158; AUTH_2FA: return rkg.AUTH_2FA_PASSWORD_INPUT;
- Строка 199; AUTH_2FA: return rkg.AUTH_2FA_PASSWORD_INPUT;

## defpackage/hb3.java (приоритет 27)
- Строка 17; accessToken: sbS.append(", chatAccessToken=true");
- Строка 29; accessToken: sbS.append(", chatAccessToken=true");
- Строка 41; accessToken: sbS.append(", chatAccessToken=true");

## one/me/login/confirm/ConfirmPhoneScreen.java (приоритет 22)
- Строка 118; ConfirmPhoneScreen: @Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0001\u0018\u00002\u00020\u00012\u00020\u00022\u00020\u00032\u00020\u0004B\u000f\u0012\u0006\u0010\u0006\u001
- Строка 119; ConfirmPhoneScreen: public final class ConfirmPhoneScreen extends Widget implements qq4, ar4 {
- Строка 120; ConfirmPhoneScreen: public static final /* synthetic */ zm9[] z = {new v4f(ConfirmPhoneScreen.class, "verifyToken", "getVerifyToken()Ljava/lang/String;", 0), vg9.s(luf.a, ConfirmPhoneScreen.class, "phone", "getPhone()Ljava/lang/String;", 0), new v4f(ConfirmPhoneScreen.class, "countryNameCode", "getCountryNameCode()Ljava/lang/String;", 0), new v4f(ConfirmPhoneScreen.class, "codeLength", "getCodeLength()I", 0), new v4f
- Строка 147; ConfirmPhoneScreen: public ConfirmPhoneScreen(Bundle bundle) {
- Строка 256; ConfirmPhoneScreen: o1dVar.c(c6aVar, "ConfirmPhoneScreen", "handleBack", null);
- Строка 265; ConfirmPhoneScreen: o1dVar2.c(c6aVar, "ConfirmPhoneScreen", "handleBack, skip", null);
- Строка 423; ConfirmPhoneScreen: e0c.M(new dk7(w1().o, new f60(2, this, ConfirmPhoneScreen.class, "processSmsEvent", "processSmsEvent(Lone/me/login/confirm/SmsCodeResultEvent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", 0, (byte) 13), (byte) 3), getViewLifecycleScope());
- Строка 611; ConfirmPhoneScreen: o1dVar.c(c6aVar, "ConfirmPhoneScreen", "Early return in processSmsEvent " + ((bvh) dvhVar).a + " because view is null", null);
- Строка 678; ConfirmPhoneScreen: public ConfirmPhoneScreen(String str, String str2, int i, long j, String str3, nkg nkgVar) {

## one/me/login/confirmcallout/ConfirmPhoneCallOutScreen.java (приоритет 22)
- Строка 91; AUTH_CALL_OUT: this.b = fa5.e(this, rkg.AUTH_CALL_OUT);

## defpackage/k79.java (приоритет 20)
- Строка 8; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 16; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen g;
- Строка 19; InputPhoneScreen: public /* synthetic */ k79(b55 b55Var, InputPhoneScreen inputPhoneScreen, byte b) {
- Строка 22; InputPhoneScreen: this.g = inputPhoneScreen;
- Строка 55; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.g;
- Строка 58; InputPhoneScreen: k79 k79Var = new k79(inputPhoneScreen, b55Var, (byte) 0);
- Строка 62; InputPhoneScreen: k79 k79Var2 = new k79(b55Var, inputPhoneScreen, (byte) 1);
- Строка 66; InputPhoneScreen: k79 k79Var3 = new k79(b55Var, inputPhoneScreen, (byte) 2);
- Строка 70; InputPhoneScreen: k79 k79Var4 = new k79(b55Var, inputPhoneScreen, (byte) 3);

## defpackage/n79.java (приоритет 20)
- Строка 6; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 14; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen h;
- Строка 17; InputPhoneScreen: public /* synthetic */ n79(InputPhoneScreen inputPhoneScreen, b55 b55Var, byte b) {
- Строка 20; InputPhoneScreen: this.h = inputPhoneScreen;
- Строка 27; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.h;
- Строка 33; InputPhoneScreen: n79 n79Var = new n79(inputPhoneScreen, b55Var, (byte) 0);
- Строка 39; InputPhoneScreen: n79 n79Var2 = new n79(inputPhoneScreen, b55Var, (byte) 1);
- Строка 55; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.h;
- Строка 56; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;

## defpackage/sv2.java (приоритет 20)
- Строка 11; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 125; ConfirmPhoneScreen: 0x0760: PHI (r3v26 one.me.login.confirm.ConfirmPhoneScreen) = (r3v23 one.me.login.confirm.ConfirmPhoneScreen), (r3v28 one.me.login.confirm.ConfirmPhoneScreen) binds: [B:357:0x089f, B:333:0x0753] A[DONT_GENERATE, DONT_INLINE]] */
- Строка 181; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen;
- Строка 185; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen2;
- Строка 343; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen3 = (ConfirmPhoneScreen) this.j;
- Строка 348; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;
- Строка 349; ConfirmPhoneScreen: confirmPhoneScreen3.t1().animate().setDuration(800L).alpha(0.0f).start();
- Строка 350; ConfirmPhoneScreen: confirmPhoneScreen3.v1().animate().setDuration(800L).alpha(0.0f).start();
- Строка 353; ConfirmPhoneScreen: ViewGroup viewGroup = (ViewGroup) confirmPhoneScreen3.getView();

## defpackage/vp4.java (приоритет 20)
- Строка 3; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 9; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen b;
- Строка 11; ConfirmPhoneScreen: public /* synthetic */ vp4(ConfirmPhoneScreen confirmPhoneScreen, byte b) {
- Строка 13; ConfirmPhoneScreen: this.b = confirmPhoneScreen;
- Строка 19; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = this.b;
- Строка 22; ConfirmPhoneScreen: eq4 eq4Var = (eq4) confirmPhoneScreen.h.getAccessor().c(855);
- Строка 23; ConfirmPhoneScreen: rz rzVar = confirmPhoneScreen.f;
- Строка 24; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;
- Строка 26; ConfirmPhoneScreen: int iIntValue = ((Number) rzVar.a(confirmPhoneScreen)).intValue();

## defpackage/yp4.java (приоритет 20)
- Строка 4; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 11; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen g;
- Строка 14; ConfirmPhoneScreen: public yp4(b55 b55Var, ConfirmPhoneScreen confirmPhoneScreen) {
- Строка 17; ConfirmPhoneScreen: this.g = confirmPhoneScreen;
- Строка 41; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = this.g;
- Строка 44; ConfirmPhoneScreen: yp4 yp4Var = new yp4(b55Var, confirmPhoneScreen);
- Строка 48; ConfirmPhoneScreen: yp4 yp4Var2 = new yp4(confirmPhoneScreen, b55Var, (byte) 1);
- Строка 52; ConfirmPhoneScreen: yp4 yp4Var3 = new yp4(confirmPhoneScreen, b55Var, (byte) 2);
- Строка 62; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = this.g;

## com/vk/push/authsdk/ipc/AuthService.java (приоритет 19)
- Строка 19; AuthService: public final class AuthService extends Service {

## defpackage/kz.java (приоритет 18)
- Строка 6; AuthService: import com.vk.push.authsdk.ipc.AuthService;
- Строка 53; AuthService: return new kj0((g68) nt6.a().x.getValue(), new d68(nt6.a().c, (pi0) nt6.a().r.getValue(), (lb5) nt6.a().i.getValue()), (h1l) nt6.a().p.getValue(), (pi0) nt6.a().r.getValue(), ((AuthService) this.c).a, (ei0) nt6.a().n.getValue(), (ri) nt6.a().m.getValue());

## defpackage/ojm.java (приоритет 18)
- Строка 31; refreshToken: bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);
- Строка 34; tokenRefresh, accessToken: bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);

## defpackage/oq6.java (приоритет 18)
- Строка 5; AuthService: import com.vk.push.authsdk.ipc.AuthService;
- Строка 18; AuthService: context.getPackageManager().setComponentEnabledSetting(new ComponentName(context, (Class<?>) AuthService.class), 1, 1);

## defpackage/oxj.java (приоритет 18)
- Строка 24; AUTH_2FA: return rkg.AUTH_2FA_START;
- Строка 27; AUTH_2FA: return rkg.AUTH_2FA_SUCCESS;

## defpackage/wpc.java (приоритет 18)
- Строка 132; refreshToken: jSONObject.put("RefreshToken", gn0Var.d);
- Строка 218; refreshToken: String strOptString3 = jSONObject.optString("RefreshToken", null);

## defpackage/x36.java (приоритет 18)
- Строка 5; AuthService: import com.vk.push.authsdk.ipc.AuthService;
- Строка 19; AuthService: context.getPackageManager().setComponentEnabledSetting(new ComponentName(context, (Class<?>) AuthService.class), 2, 1);

## defpackage/y1l.java (приоритет 18)
- Строка 103; AuthService: return new ComponentName((String) obj, "com.vk.push.authsdk.ipc.AuthService");
- Строка 107; AuthService: return new ComponentName((String) obj, "com.vk.push.authsdk.ipc.AuthService");

## defpackage/i79.java (приоритет 15)
- Строка 6; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 13; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen b;
- Строка 15; InputPhoneScreen: public /* synthetic */ i79(InputPhoneScreen inputPhoneScreen, byte b) {
- Строка 17; InputPhoneScreen: this.b = inputPhoneScreen;
- Строка 23; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.b;
- Строка 26; InputPhoneScreen: v79 v79Var = (v79) inputPhoneScreen.e.getAccessor().c(857);
- Строка 30; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 31; InputPhoneScreen: inputPhoneScreen.getContext();
- Строка 34; InputPhoneScreen: zm9[] zm9VarArr2 = InputPhoneScreen.w;

## ru/ok/android/externcalls/sdk/AuthRequiredException.java (приоритет 14)
- Строка 7; Authorization: return "Authorization required";

## defpackage/l79.java (приоритет 12)
- Строка 5; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 11; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen g;
- Строка 14; InputPhoneScreen: public /* synthetic */ l79(InputPhoneScreen inputPhoneScreen, b55 b55Var, byte b) {
- Строка 17; InputPhoneScreen: this.g = inputPhoneScreen;
- Строка 24; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.g;
- Строка 27; InputPhoneScreen: l79 l79Var = new l79(inputPhoneScreen, (b55) obj3, (byte) 0);
- Строка 32; InputPhoneScreen: l79 l79Var2 = new l79(inputPhoneScreen, (b55) obj3, (byte) 1);
- Строка 44; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.g;
- Строка 49; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;

## defpackage/o79.java (приоритет 12)
- Строка 5; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 10; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen b;
- Строка 12; InputPhoneScreen: public o79(InputPhoneScreen inputPhoneScreen) {
- Строка 13; InputPhoneScreen: this.b = inputPhoneScreen;
- Строка 30; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 31; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.b;
- Строка 32; InputPhoneScreen: u79 u79VarU1 = inputPhoneScreen.u1();
- Строка 36; InputPhoneScreen: rz rzVar = inputPhoneScreen.f;
- Строка 37; InputPhoneScreen: zm9 zm9Var = InputPhoneScreen.w[0];

## defpackage/wi3.java (приоритет 12)
- Строка 10; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 84; ConfirmPhoneScreen: zm9[] zm9VarArr3 = ConfirmPhoneScreen.z;
- Строка 88; ConfirmPhoneScreen: zm9[] zm9VarArr4 = ConfirmPhoneScreen.z;
- Строка 89; AUTH_OTP: return rkg.AUTH_OTP;

## defpackage/bwb.java (приоритет 10)
- Строка 1012; AuthRequest: ij4Var.c(863, "one.me.login.usecases.AuthRequestUseCase");
- Строка 1017; AuthApi: ij4Var.c(122, "one.me.sdk.api.auth.AuthApi");

## defpackage/m79.java (приоритет 10)
- Строка 9; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 14; InputPhoneScreen: public final /* synthetic */ InputPhoneScreen a;
- Строка 17; InputPhoneScreen: public m79(InputPhoneScreen inputPhoneScreen, String str) {
- Строка 18; InputPhoneScreen: this.a = inputPhoneScreen;
- Строка 24; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = this.a;
- Строка 25; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 30; InputPhoneScreen: inputPhoneScreen.startActivity(intent);
- Строка 32; InputPhoneScreen: f09.d0(inputPhoneScreen.b, "open web link with terms is failed, no activity found", new Object[0]);
- Строка 33; InputPhoneScreen: v5d v5dVar = new v5d(inputPhoneScreen);

## defpackage/wbi.java (приоритет 10)
- Строка 133; refreshToken: jSONObject2.put("forceCodeForRefreshToken", googleSignInOptions.f);
- Строка 134; AuthRequest: jSONObject2.put("serverAuthRequested", googleSignInOptions.e);

## com/google/android/gms/auth/api/signin/GoogleSignInOptions.java (приоритет 9)
- Строка 104; refreshToken, AuthRequest: return new GoogleSignInOptions(3, new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), jSONObject.has("serverClientId") ? jSONObject.optString("serverClientId") : null, jSONObject.has("hostedDomain") ? jSON

## defpackage/gn0.java (приоритет 9)
- Строка 119; refreshToken: sb.append(", refreshToken=");

## defpackage/hg7.java (приоритет 9)
- Строка 120; refreshToken: } else if (strNextName.equals("refreshToken")) {

## defpackage/p0b.java (приоритет 9)
- Строка 254; api/v3/ws: String string = new Uri.Builder().scheme(zl8Var.w()).encodedAuthority(emcVar != null ? emcVar.b : zl8Var.x()).path("api/v3/ws").appendQueryParameter("push_tokens", va4.S0(concurrentLinkedDeque, ",", null, null, null, 62)).build().toString();

## defpackage/p73.java (приоритет 9)
- Строка 512; accessToken: h("chatAccessToken", str);

## defpackage/qzb.java (приоритет 9)
- Строка 17; accessToken: case "chatAccessToken":

## defpackage/sm0.java (приоритет 9)
- Строка 90; refreshToken: sb.append(", refreshToken=");

## defpackage/tp4.java (приоритет 9)
- Строка 4; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 9; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen b;
- Строка 11; ConfirmPhoneScreen: public /* synthetic */ tp4(ConfirmPhoneScreen confirmPhoneScreen, byte b) {
- Строка 13; ConfirmPhoneScreen: this.b = confirmPhoneScreen;
- Строка 19; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = this.b;
- Строка 22; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;
- Строка 23; ConfirmPhoneScreen: dq4 dq4VarW1 = confirmPhoneScreen.w1();
- Строка 28; ConfirmPhoneScreen: zm9[] zm9VarArr2 = ConfirmPhoneScreen.z;
- Строка 29; ConfirmPhoneScreen: dq4 dq4VarW2 = confirmPhoneScreen.w1();

## defpackage/ug9.java (приоритет 9)
- Строка 74; accessToken: f09.d0(ug9.class.getName(), "link or chatAccessToken must not be null", new Object[0]);

## defpackage/up4.java (приоритет 9)
- Строка 3; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 8; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen b;
- Строка 10; ConfirmPhoneScreen: public /* synthetic */ up4(ConfirmPhoneScreen confirmPhoneScreen, byte b) {
- Строка 12; ConfirmPhoneScreen: this.b = confirmPhoneScreen;
- Строка 19; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = this.b;
- Строка 23; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;
- Строка 25; ConfirmPhoneScreen: r4i r4iVar = confirmPhoneScreen.w1().t;
- Строка 32; ConfirmPhoneScreen: zm9[] zm9VarArr2 = ConfirmPhoneScreen.z;
- Строка 33; ConfirmPhoneScreen: xqc onBackPressedDispatcher = confirmPhoneScreen.getOnBackPressedDispatcher();

## defpackage/zjn.java (приоритет 9)
- Строка 78; refreshToken: String strD3 = wbi.a(context).d("refreshToken");

## defpackage/ty3.java (приоритет 8)
- Строка 5; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 27; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = (InputPhoneScreen) obj;
- Строка 28; InputPhoneScreen: zm9[] zm9VarArr2 = InputPhoneScreen.w;
- Строка 29; InputPhoneScreen: if (inputPhoneScreen.getView() != null) {
- Строка 30; InputPhoneScreen: u79 u79VarU1 = inputPhoneScreen.u1();
- Строка 31; InputPhoneScreen: g0i g0iVar = (g0i) u79VarU1.c.a(u79VarU1.b, ((vxc) ((k6j) u79VarU1.f.getValue())).b(), 2, new yr0(inputPhoneScreen.t1().a(), String.valueOf(inputPhoneScreen.t1().i.getText()), u79VarU1, null, (byte) 11));
- Строка 36; InputPhoneScreen: u79 u79VarU2 = inputPhoneScreen.u1();
- Строка 41; InputPhoneScreen: svc svcVarR1 = inputPhoneScreen.r1();

## one/me/location/map/pick/PickLocationScreen.java (приоритет 7)
- Строка 88; requestCode: @Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\t\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\u0018\u00002\u00020\u00012\u00060\u0002j\u0002'\u00032\u00060\u0004
- Строка 90; requestCode: public static final /* synthetic */ zm9[] p = {new v4f(PickLocationScreen.class, "chatId", "getChatId()J", 0), vg9.s(luf.a, PickLocationScreen.class, "requestCode", "getRequestCode()I", 0), new v4f(PickLocationScreen.class, "chatScopeId", "getChatScopeId()Lone/me/sdk/arch/store/ScopeId;", 0), new v4f(PickLocationScreen.class, "mapView", "getMapView()Lone/me/geo/view/OneMeMapView;", 0), new v4f(Pic
- Строка 119; requestCode: this.c = new rz("LocationMapScreen.requestCode", Integer.class);
- Строка 380; requestCode: this(e0c.d(new vld(Widget.ARG_ACCOUNT_ID_OVERRIDE, Integer.valueOf(q1aVar.a)), new vld("LocationMapScreen.chatId", Long.valueOf(j)), new vld("LocationMapScreen.requestCode", Integer.valueOf(i)), new vld("LocationMapScreen.arg_key_chat_scope_id", nkgVar)));

## defpackage/eb1.java (приоритет 6)
- Строка 8; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 22; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = (InputPhoneScreen) this.a;
- Строка 24; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 25; InputPhoneScreen: mxd mxdVar = (mxd) inputPhoneScreen.o.getValue();
- Строка 27; InputPhoneScreen: int i = ((ab5) inputPhoneScreen.u1().w.a.getValue()).b;
- Строка 28; InputPhoneScreen: inputPhoneScreen.u1().d.getClass();

## defpackage/aq4.java (приоритет 5)
- Строка 3; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 7; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen a;
- Строка 9; ConfirmPhoneScreen: public aq4(ConfirmPhoneScreen confirmPhoneScreen) {
- Строка 10; ConfirmPhoneScreen: this.a = confirmPhoneScreen;
- Строка 16; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;

## defpackage/u9m.java (приоритет 5)
- Строка 208; Authorization: u9mVar.c.e("Request of user's authorization is failed", thA);
- Строка 321; Authorization: u9mVar.c.e("Request of user's authorization is failed", thA);
- Строка 466; Authorization: u9mVar.c.e("Request of user's authorization is failed", thA);
- Строка 580; Authorization: u9mVar.c.e("Request of user's authorization is failed", thA);
- Строка 648; Authorization: u9mVar.c.e("Request of user's authorization is failed", thA);

## defpackage/wp4.java (приоритет 5)
- Строка 4; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 12; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen h;
- Строка 16; ConfirmPhoneScreen: public wp4(ConfirmPhoneScreen confirmPhoneScreen, d55 d55Var) {
- Строка 18; ConfirmPhoneScreen: this.h = confirmPhoneScreen;
- Строка 25; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;

## defpackage/zp4.java (приоритет 5)
- Строка 3; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 9; ConfirmPhoneScreen: public final /* synthetic */ ConfirmPhoneScreen f;
- Строка 13; ConfirmPhoneScreen: public zp4(b55 b55Var, ConfirmPhoneScreen confirmPhoneScreen) {
- Строка 15; ConfirmPhoneScreen: this.f = confirmPhoneScreen;
- Строка 22; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;

## one/me/chats/picker/contacts/ContactsPickerScreen.java (приоритет 5)
- Строка 72; requestCode: @Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0001\u0018\u00002\b\u0012\u0004\u0012\u00020\u00020\u00012\u00020\u00032\u00020\u00042\u00020\u0005B\u00
- Строка 74; requestCode: public static final /* synthetic */ zm9[] o = {new v4f(ContactsPickerScreen.class, "requestCode", "getRequestCode()I", 0), vg9.s(luf.a, ContactsPickerScreen.class, "chatId", "getChatId()J", 0), new v4f(ContactsPickerScreen.class, "chatScopeId", "getChatScopeId()Lone/me/sdk/arch/store/ScopeId;", 0)};

## one/me/sdk/permissionhost/PermissionBottomSheet.java (приоритет 5)
- Строка 42; requestCode: @Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0004\b\u0000\u0018\u00002\u00020\u0001B\u0007¢\u0006\u0004\b\u0002\u0010\u0003BG\b\u0016\u0012\f\u0010\u0006\u001a\b\u0012\u0004\u0012\u00020\u0
- Строка 44; requestCode: public static final /* synthetic */ zm9[] Z = {new c4c(PermissionBottomSheet.class, "settingsMode", "getSettingsMode()Z"), a15.f(luf.a, PermissionBottomSheet.class, "showCancelButton", "getShowCancelButton()Z"), new c4c(PermissionBottomSheet.class, "customSettingsIntent", "getCustomSettingsIntent()Landroid/content/Intent;"), new c4c(PermissionBottomSheet.class, "titleId", "getTitleId()I"), new c4c

## one/me/webapp/rootscreen/WebAppRootScreen.java (приоритет 5)
- Строка 182; requestCode: @Metadata(d1 = {"\u0000V\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\t\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0010\b\n\u0000\n\u0002\u00
- Строка 184; requestCode: public static final /* synthetic */ zm9[] H = {new c4c(WebAppRootScreen.class, "sourceId", "getSourceId()Ljava/lang/Long;"), a15.f(luf.a, WebAppRootScreen.class, "botId", "getBotId()J"), new c4c(WebAppRootScreen.class, "rawEntryPoint", "getRawEntryPoint()Ljava/lang/String;"), new c4c(WebAppRootScreen.class, "startParam", "getStartParam()Ljava/lang/String;"), new c4c(WebAppRootScreen.class, "isFull

## defpackage/dr.java (приоритет 4)
- Строка 14; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 160; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = (InputPhoneScreen) this.b;
- Строка 161; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 163; InputPhoneScreen: inputPhoneScreen.requireActivity().reportFullyDrawn();

## defpackage/f60.java (приоритет 4)
- Строка 12; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 207; ConfirmPhoneScreen: ConfirmPhoneScreen confirmPhoneScreen = (ConfirmPhoneScreen) this.receiver;
- Строка 208; ConfirmPhoneScreen: zm9[] zm9VarArr = ConfirmPhoneScreen.z;
- Строка 209; ConfirmPhoneScreen: return confirmPhoneScreen.x1((dvh) obj, (b55) obj2);

## defpackage/ka9.java (приоритет 4)
- Строка 11; ConfirmPhoneScreen: import one.me.login.confirm.ConfirmPhoneScreen;
- Строка 55; InputPhoneScreen: if (g4a.c(zbgVar.b, "InputPhoneScreen")) {
- Строка 68; InputPhoneScreen: } while (!g4a.c(((zbg) objPrevious).b, "InputPhoneScreen"));
- Строка 89; ConfirmPhoneScreen: c(nb6.e(new ConfirmPhoneScreen(str, str2, i, j, str3, this.b), null, null), "ConfirmPhoneScreen");

## defpackage/so.java (приоритет 4)
- Строка 12; InputPhoneScreen: import one.me.login.inputphone.InputPhoneScreen;
- Строка 107; InputPhoneScreen: InputPhoneScreen inputPhoneScreen = (InputPhoneScreen) this.c;
- Строка 108; InputPhoneScreen: zm9[] zm9VarArr = InputPhoneScreen.w;
- Строка 110; InputPhoneScreen: inputPhoneScreen.u1().l.e(m8a.b.l());

## defpackage/sx3.java (приоритет 4)
- Строка 382; api2.oneme.ru: str2 = "api2.oneme.ru";
- Строка 383; api2.oneme.ru: this.i = "api2.oneme.ru";
- Строка 461; api2.oneme.ru: str2 = "api2.oneme.ru";
- Строка 462; api2.oneme.ru: this.i = "api2.oneme.ru";

## one/me/calls/ui/ui/incoming/CallIncomingScreen.java (приоритет 4)
- Строка 218; requestCode: StringBuilder sbT = a15.t(i, "incoming call permission: requestCode=", " permissions=");

## one/me/informer/ui/InformerBottomSheet.java (приоритет 4)
- Строка 152; requestCode: String strR = w7g.r(i, "onActivityResult fail! unknown requestCode=");


## Участки исходного кода для ручной проверки цепочки входа

Нумерация строк соответствует результатам декомпиляции; длинные строки усечены.
Публичный отчёт не содержит личных данных или рабочих токенов.


### one/me/login/inputphone/InputPhoneScreen.java
Строки 120–160:
```java
  120: public final ulf k;
  121: public final ulf l;
  122: public final ulf m;
  123: public final ulf n;
  124: public final rp9 o;
  125: public bb9 p;
  126: public final rp9 q;
  127: public final rp9 r;
  128: public final rp9 s;
  129: public LocaleBottomSheet t;
  130: public final rp9 u;
  131: public final o79 v;
  132: 
  133: public InputPhoneScreen(Bundle bundle) {
  134: super(bundle);
  135: this.a = new qzd((byte) 19);
  136: this.b = InputPhoneScreen.class.getName();
  137: this.c = new o89(0, 0, 0, new s71(3, 3, false), 7);
  138: this.d = fa5.f(this, new wz7((byte) 4));
  139: wj2 wj2Var = new wj2(mo17getAccountScopeuqN4xOY());
  140: this.e = wj2Var;
  141: this.f = new rz(String.class, BuildConfig.FLAVOR, "screen:input_phone:phone");
  142: this.g = new rz(Boolean.class, Boolean.FALSE, "screen:input_phone:is_add_account_login");
  143: this.h = createViewModelLazy(u79.class, new wu3(new i79(this, (byte) 0), (byte) 8));
  144: this.i = xnm.p(3, new i79(this, (byte) 1));
  145: u79 u79VarU1 = u1();
  146: b79 b79Var = u79VarU1.d;
  147: t45 t45Var = u79VarU1.b;
  148: b79Var.e(t45Var, Collections.singletonList(null));
  149: this.j = viewBinding(R.id.oneme_login_input_gradient_bg);
  150: this.k = viewBinding(R.id.oneme_login_input_continue_button);
  151: this.l = viewBinding(R.id.oneme_login_input_phone_number_input);
  152: this.m = viewBinding(R.id.oneme_login_input_input_description);
  153: this.n = viewBinding(R.id.oneme_login_input_help_button);
  154: this.o = wj2Var.getAccessor().d(391);
  155: this.q = xnm.p(3, new i79(this, (byte) 2));
  156: owd.a.a();
  157: this.r = wj2Var.a();
  158: this.s = wj2Var.getAccessor().d(89);
  159: this.u = wj2Var.getAccessor().d(92);
  160: this.v = new o79(this);
```
Строки 260–330:
```java
  260: 
  261: @Override // defpackage.q08
  262: public final Object d(Object obj) {
  263: byte b3 = b;
  264: s1k s1kVar = s1k.a;
  265: InputPhoneScreen inputPhoneScreen = this.b;
  266: zm9[] zm9VarArr = InputPhoneScreen.w;
  267: switch (b3) {
  268: case 0:
  269: nom.h(inputPhoneScreen);
  270: xqc xqcVarH = inputPhoneScreen.getRouter().h();
  271: if (xqcVarH != null) {
  272: xqcVarH.d();
  273: }
  274: break;
  275: default:
  276: nom.h(inputPhoneScreen);
  277: inputPhoneScreen.u1().l.e(d79.b);
  278: break;
  279: }
  280: return s1kVar;
  281: }
  282: }, 14)));
  283: hadVar.B(new r9d(null, new aad(R.drawable.icon_question, null, null, null, new so(hadVar, this, (byte) 7), 110), null));
  284: ((nvc) this.s.getValue()).getClass();
  285: a08.c(hadVar, new o89(0, 3, 0, null, 13), null);
  286: lu4Var.addView(hadVar);
  287: View dr9Var = new dr9(lu4Var.getContext());
  288: dr9Var.setId(R.id.oneme_login_input_logo);
  289: ju4 ju4Var3 = new ju4(-1, 0);
  290: ju4Var3.i = 0;
  291: ju4Var3.t = 0;
  292: ju4Var3.v = 0;
  293: ju4Var3.l = R.id.oneme_login_input_toolbar;
  294: dr9Var.setLayoutParams(ju4Var3);
  295: a08.c(dr9Var, new o89(0, 3, 0, null, 13), null);
  296: lu4Var.addView(dr9Var);
  297: TextView textView = new TextView(lu4Var.getContext());
  298: textView.setId(R.id.oneme_login_input_title);
  299: fej fejVar = tzj.a;
  300: tzj.a(tzj.c, textView);
  301: textView.setText(R.string.oneme_login_input_title);
  302: ju4 ju4Var4 = new ju4(0, -2);
  303: ju4Var4.setMargins(nb6.t(i36.d().getDisplayMetrics().density * 28.0f), nb6.t(i36.d().getDisplayMetrics().density * 24.0f), nb6.t(i36.d().getDisplayMetrics().density * 28.0f), 0);
  304: ju4Var4.j = R.id.oneme_login_input_toolbar;
  305: ju4Var4.t = 0;
  306: ju4Var4.v = 0;
  307: textView.setGravity(17);
  308: textView.setLayoutParams(ju4Var4);
  309: byte b3 = 3;
  310: c45.J(new k1j((int) b3, b55Var, (byte) 11), textView);
  311: lu4Var.addView(textView);
  312: f3d f3dVar = new f3d(lu4Var.getContext());
  313: f3dVar.setId(R.id.oneme_login_input_phone_number_input);
  314: ju4 ju4Var5 = new ju4(0, -2);
  315: ju4Var5.setMargins(nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 24.0f), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 24.0f));
  316: ju4Var5.j = R.id.oneme_login_input_title;
  317: ju4Var5.t = 0;
  318: ju4Var5.v = 0;
  319: f3dVar.setLayoutParams(ju4Var5);
  320: f3dVar.a = new eb1(this, f3dVar);
  321: ty3 ty3Var = new ty3(new i79(this, b3), (byte) 4);
  322: f3dVar.f.setOnClickListener(ty3Var);
  323: f3dVar.g.setOnClickListener(ty3Var);
  324: f3dVar.h.setOnClickListener(ty3Var);
  325: lu4Var.addView(f3dVar);
  326: TextView textView2 = new TextView(lu4Var.getContext());
  327: textView2.setId(R.id.oneme_login_input_input_description);
  328: fej fejVar2 = tzj.i;
  329: tzj.a(fejVar2, textView2);
  330: textView2.setText(u1().u.b(textView2.getContext()));
```
Строки 400–472:
```java
  400: byte b3 = 1;
  401: r1().setEnabled(str.length() > 0);
  402: g4a.G(r1(), 300L, new ty3(this, b3));
  403: t1().i.addTextChangedListener(this.v);
  404: e0c.M(new dk7(u1().l, new k79(this, b55Var, b2), (byte) 3), getViewLifecycleScope());
  405: qad.a(view, new dr(view, this, (byte) 8));
  406: cmf cmfVar = u1().o;
  407: is9 is9VarF = getViewLifecycleOwner().f();
  408: nr9 nr9Var = nr9.d;
  409: e0c.M(new dk7(nm9.n(cmfVar, is9VarF, nr9Var), new k79(b55Var, this, b3), (byte) 3), getViewLifecycleScope());
  410: e0c.M(new dk7(u1().q, new k79(this, b55Var, (byte) 4), (byte) 3), getViewLifecycleScope());
  411: e0c.M(new dk7(nm9.n(u1().v, getViewLifecycleOwner().f(), nr9Var), new k79(b55Var, this, b), (byte) 3), getViewLifecycleScope());
  412: e0c.M(new dk7(nm9.n(u1().n, getViewLifecycleOwner().f(), nr9Var), new k79(b55Var, this, (byte) 3), (byte) 3), getViewLifecycleScope());
  413: e0c.M(new dk7(nm9.n(u1().w, getViewLifecycleOwner().f(), nr9Var), new k79(b55Var, this, (byte) 5), (byte) 3), getViewLifecycleScope());
  414: }
  415: 
  416: public final svc r1() {
  417: return (svc) this.k.s(this, w[3]);
  418: }
  419: 
  420: public final TextView s1() {
  421: return (TextView) this.m.s(this, w[5]);
  422: }
  423: 
  424: public final f3d t1() {
  425: return (f3d) this.l.s(this, w[4]);
  426: }
  427: 
  428: public final u79 u1() {
  429: return (u79) this.h.getValue();
  430: }
  431: 
  432: public final void v1(String str, String str2, SpannableString spannableString, m79 m79Var, a9d a9dVar) {
  433: int iL0 = zti.l0(str, str2, 0, false, 6);
  434: if (iL0 != -1) {
  435: int length = str2.length() + iL0;
  436: spannableString.setSpan(m79Var, iL0, length, 33);
  437: spannableString.setSpan(new ForegroundColorSpan(a9dVar.getText().a), iL0, length, 33);
  438: return;
  439: }
  440: a aVar = new a(vg9.y("text=", str2, " not found in source text"), null, 2, null);
  441: String str3 = this.b;
  442: o1d o1dVar = f09.g;
  443: if (o1dVar == null) {
  444: return;
  445: }
  446: c6a c6aVar = c6a.f;
  447: if (o1dVar.b(c6aVar)) {
  448: o1dVar.c(c6aVar, str3, pq0.i("locale=", ((hog) ((c74) this.u.getValue())).l()), aVar);
  449: }
  450: }
  451: 
  452: public final void w1(CharSequence charSequence) {
  453: if (charSequence == null) {
  454: charSequence = u1().u.b(getContext());
  455: }
  456: s1().setText(charSequence);
  457: TextView textViewS1 = s1();
  458: a9d a9dVarF = u34.j.f(s1());
  459: boolean z = u1().t;
  460: t8d text = a9dVarF.getText();
  461: textViewS1.setTextColor(z ? text.i : text.d);
  462: s1().setVisibility((charSequence == null \|\| charSequence.length() == 0) ? 8 : 0);
  463: }
  464: 
  465: public InputPhoneScreen(nkg nkgVar, boolean z) {
  466: this(e0c.d(new vld(Widget.ARG_SCOPE_ID, nkgVar), new vld("screen:input_phone:is_add_account_login", Boolean.valueOf(z))));
  467: }
  468: 
  469: public /* synthetic */ InputPhoneScreen(nkg nkgVar, boolean z, int i, hq5 hq5Var) {
  470: this(nkgVar, (i & 2) != 0 ? false : z);
  471: }
  472: }
```

### one/me/login/confirm/ConfirmPhoneScreen.java
Строки 118–205:
```java
  118: @Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0001\u0018\u00002\u00020\u00012\u00020\u00022\u00020\u00032\u00020\u0004B\u000f\u0012\u0006\u0010\u0006\u001
  119: public final class ConfirmPhoneScreen extends Widget implements qq4, ar4 {
  120: public static final /* synthetic */ zm9[] z = {new v4f(ConfirmPhoneScreen.class, "verifyToken", "getVerifyToken()Ljava/lang/String;", 0), vg9.s(luf.a, ConfirmPhoneScreen.class, "phone", "getPhone()Ljava/lang/String;", 0), new v4f(ConfirmPhoneScreen.class, "countryNameCode", "getCountryNameCode()Ljava/lang/String;", 0), new v4f(ConfirmPhoneScreen.class, "codeLength", "getCodeLength()I", 0), new v4f
  121: public final /* synthetic */ qzd a;
  122: public final o89 b;
  123: public final rz c;
  124: public final rz d;
  125: public final rz e;
  126: public final rz f;
  127: public final rz g;
  128: public final wj2 h;
  129: public final l90 i;
  130: public final rp9 j;
  131: public final rp9 k;
  132: public final rp9 l;
  133: public final n9d m;
  134: public s9d n;
  135: public final ulf o;
  136: public final ulf p;
  137: public final ulf q;
  138: public final ulf r;
  139: public svc s;
  140: public final rp9 t;
  141: public final ulf u;
  142: public TextView v;
  143: public final rp9 w;
  144: public AppCompatTextView x;
  145: public final z9g y;
  146: 
  147: public ConfirmPhoneScreen(Bundle bundle) {
  148: super(bundle);
  149: this.a = new qzd((byte) 19);
  150: this.b = o89.f;
  151: Class<String> cls = String.class;
  152: this.c = new rz("screen:confirm_phone:verify_token", cls);
  153: this.d = new rz("screen:confirm_phone:phone", cls);
  154: this.e = new rz("screen:confirm_phone:country_name_code", cls);
  155: this.f = new rz("screen:confirm_phone:code_length", Integer.class);
  156: this.g = new rz("screen:confirm_phone:code_resend", Long.class);
  157: wj2 wj2Var = new wj2(mo17getAccountScopeuqN4xOY());
  158: this.h = wj2Var;
  159: this.i = fa5.f(this, new wi3((byte) 17));
  160: this.j = createViewModelLazy(dq4.class, new no3(new vp4(this, (byte) 0), (byte) 10));
  161: this.k = xnm.p(3, new vp4(this, (byte) 1));
  162: this.l = wj2Var.a();
  163: n9d n9dVar = new n9d(null, new up4(this, (byte) 1));
  164: this.m = n9dVar;
  165: this.n = n9dVar;
  166: this.o = viewBinding(R.id.oneme_login_confirm_toolbar);
  167: this.p = viewBinding(R.id.oneme_login_confirm_description);
  168: this.q = viewBinding(R.id.oneme_login_confirm_timer);
  169: this.r = viewBinding(R.id.oneme_login_confirm_resend_code);
  170: this.t = xnm.p(3, new vp4(this, (byte) 2));
  171: this.u = viewBinding(R.id.oneme_login_confirm_sms_input);
  172: this.w = xnm.p(3, new vp4(this, (byte) 3));
  173: this.y = c45.Q();
  174: }
  175: 
  176: public final void A1(rdj rdjVar) {
  177: ViewPropertyAnimator viewPropertyAnimatorAnimate;
  178: ViewPropertyAnimator duration;
  179: ViewPropertyAnimator viewPropertyAnimatorAlpha;
  180: TextView textView = this.v;
  181: if (textView == null && rdjVar != null) {
  182: int iIndexOfChild = ((ViewGroup) getView()).indexOfChild(u1());
  183: TextView textView2 = new TextView(getContext());
  184: fej fejVar = tzj.a;
  185: tzj.a(tzj.i, textView2);
  186: textView2.setTextColor(u34.j.f(textView2).getText().i);
  187: LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(-1, -2);
  188: layoutParams.setMargins(nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(16.0f * i36.d().getDisplayMetrics().density), nb6.t(12.0f * i36.d().getDisplayMetrics().density), 0);
  189: textView2.setLayoutParams(layoutParams);
  190: textView2.setGravity(17);
  191: textView2.setAlpha(0.0f);
  192: View view = getView();
  193: ViewGroup viewGroup = view instanceof ViewGroup ? (ViewGroup) view : null;
  194: if (viewGroup != null) {
  195: viewGroup.addView(textView2, iIndexOfChild + 1);
  196: }
  197: this.v = textView2;
  198: textView = textView2;
  199: }
  200: float f = rdjVar != null ? 1.0f : 0.0f;
  201: if (textView != null) {
  202: textView.setText(rdjVar != null ? rdjVar.b(getContext()) : null);
  203: }
  204: TextView textView3 = this.v;
  205: if (textView3 == null \|\| (viewPropertyAnimatorAnimate = textView3.animate()) == null \|\| (duration = viewPropertyAnimatorAnimate.setDuration(200L)) == null \|\| (viewPropertyAnimatorAlpha = duration.alpha(f)) == null) {
```
Строки 440–520:
```java
  440: }
  441: } else {
  442: wp4Var = new wp4(this, d55Var);
  443: }
  444: Object obj = wp4Var.g;
  445: int i3 = wp4Var.i;
  446: s1k s1kVar = s1k.a;
  447: ka5 ka5Var = ka5.a;
  448: if (i3 == 0) {
  449: xnm.y(obj);
  450: textView.setText(i);
  451: textView.setAlpha(0.0f);
  452: textView.animate().alpha(1.0f).setDuration(800L).start();
  453: wp4Var.d = textView;
  454: wp4Var.e = i;
  455: wp4Var.f = z2;
  456: wp4Var.i = 1;
  457: if (usc.n(2800L, wp4Var) != ka5Var) {
  458: }
  459: return ka5Var;
  460: }
  461: if (i3 != 1) {
  462: if (i3 == 2) {
  463: xnm.y(obj);
  464: return s1kVar;
  465: }
  466: k3g.o("call to 'resume' before 'invoke' with coroutine");
  467: return null;
  468: }
  469: z2 = wp4Var.f;
  470: i = wp4Var.e;
  471: textView = wp4Var.d;
  472: xnm.y(obj);
  473: if (!z2) {
  474: textView.animate().alpha(0.0f).setDuration(800L).start();
  475: wp4Var.d = null;
  476: wp4Var.e = i;
  477: wp4Var.f = z2;
  478: wp4Var.i = 2;
  479: if (usc.n(800L, wp4Var) == ka5Var) {
  480: return ka5Var;
  481: }
  482: }
  483: return s1kVar;
  484: }
  485: 
  486: public final String s1() {
  487: zm9 zm9Var = z[1];
  488: return (String) this.d.a(this);
  489: }
  490: 
  491: public final svc t1() {
  492: return (svc) this.r.s(this, z[8]);
  493: }
  494: 
  495: public final uq4 u1() {
  496: return (uq4) this.u.s(this, z[9]);
  497: }
  498: 
  499: public final TextView v1() {
  500: return (TextView) this.q.s(this, z[7]);
  501: }
  502: 
  503: public final dq4 w1() {
  504: return (dq4) this.j.getValue();
  505: }
  506: 
  507: /* JADX WARN: Code duplicated, block: B:7:0x0015  */
  508: /* JADX WARN: Code restructure failed: missing block: B:52:0x0110, code lost:
  509: 
  510: if (defpackage.usc.n(1000, r1) == r2) goto L58;
  511: */
  512: /* JADX WARN: Code restructure failed: missing block: B:57:0x0131, code lost:
  513: 
  514: if (defpackage.usc.n(300, r1) == r2) goto L58;
  515: */
  516: /*
  517: Code decompiled incorrectly, please refer to instructions dump.
  518: */
  519: public final Object x1(dvh dvhVar, b55 b55Var) {
  520: zp4 zp4Var;
```
Строки 560–681:
```java
  560: ((bi0) this.l.getValue()).a(new zh0(((y7a) bvhVar.a).e));
  561: y7a y7aVar = (y7a) bvhVar.a;
  562: hu6 hu6Var = new hu6(y7aVar.c, y7aVar.d, null);
  563: this.a.getClass();
  564: qzd.j(this, hu6Var);
  565: } else if (z7aVar instanceof s7a) {
  566: A1(((s7a) z7aVar).c);
  567: } else if (z7aVar instanceof q7a) {
  568: A1(((q7a) z7aVar).c);
  569: } else if ((z7aVar instanceof u7a) \|\| (z7aVar instanceof t7a)) {
  570: A1(((x7a) z7aVar).c);
  571: zp4Var.d = bvhVar;
  572: zp4Var.g = 2;
  573: } else {
  574: if (z7aVar instanceof v7a) {
  575: bjn.b(this);
  576: return s1kVar;
  577: }
  578: if (!(z7aVar instanceof r7a) && !(z7aVar instanceof w7a)) {
  579: k3g.l();
  580: return null;
  581: }
  582: }
  583: zp4Var.d = null;
  584: zp4Var.g = 3;
  585: }
  586: return ka5Var;
  587: }
  588: if (i2 == 1) {
  589: xnm.y(obj);
  590: return s1kVar;
  591: }
  592: if (i2 != 2) {
  593: if (i2 != 3) {
  594: k3g.o("call to 'resume' before 'invoke' with coroutine");
  595: return null;
  596: }
  597: xnm.y(obj);
  598: A1(null);
  599: u1().R0(rq4.d);
  600: return s1kVar;
  601: }
  602: dvhVar = zp4Var.d;
  603: xnm.y(obj);
  604: View view = getView();
  605: LinearLayout linearLayout = view instanceof LinearLayout ? (LinearLayout) view : null;
  606: if (linearLayout == null) {
  607: o1d o1dVar = f09.g;
  608: if (o1dVar != null) {
  609: c6a c6aVar = c6a.f;
  610: if (o1dVar.b(c6aVar)) {
  611: o1dVar.c(c6aVar, "ConfirmPhoneScreen", "Early return in processSmsEvent " + ((bvh) dvhVar).a + " because view is null", null);
  612: return s1kVar;
  613: }
  614: }
  615: } else {
  616: t1().setVisibility(8);
  617: v1().setVisibility(8);
  618: if (((bvh) dvhVar).a instanceof u7a) {
  619: if (this.s == null) {
  620: svc svcVar = new svc(getContext());
  621: svcVar.setId(R.id.oneme_login_confirm_restore_access);
  622: svcVar.q(c45.D(R.string.oneme_login_restore_access, getContext()));
  623: svcVar.i(pvc.l);
  624: svcVar.p(qvc.g);
  625: LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(-1, -2);
  626: layoutParams.setMargins(nb6.t(i36.d().getDisplayMetrics().density * 12.0f), 0, nb6.t(12.0f * i36.d().getDisplayMetrics().density), nb6.t(16.0f * i36.d().getDisplayMetrics().density));
  627: svcVar.setLayoutParams(layoutParams);
  628: g4a.G(svcVar, 300L, new tp4(this, b));
  629: this.s = svcVar;
  630: linearLayout.addView(svcVar, linearLayout.getChildCount());
  631: }
  632: svc svcVar2 = this.s;
  633: if (svcVar2 != null) {
  634: svcVar2.setVisibility(0);
  635: }
  636: }
  637: uq4 uq4VarU1 = u1();
  638: int childCount = uq4VarU1.getChildCount();
  639: for (int i3 = 0; i3 < childCount; i3++) {
  640: zuh zuhVarO0 = uq4VarU1.O0(i3);
  641: if (zuhVarO0 != null) {
  642: zuhVarO0.w.setText((CharSequence) null);
  643: }
  644: }
  645: }
  646: return s1kVar;
  647: }
  648: 
  649: public final void y1(String str) {
  650: boolean z2 = str != null;
  651: t1().setVisibility(!z2 ? 0 : 8);
  652: v1().setVisibility(z2 ? 0 : 8);
  653: t1().setAlpha(z2 ? 0.0f : 1.0f);
  654: v1().setAlpha(z2 ? 1.0f : 0.0f);
  655: if (str != null) {
  656: v1().setText(((String) this.w.getValue()) + " " + str);
  657: }
  658: }
  659: 
  660: public final void z1() {
  661: zm9[] zm9VarArr = z;
  662: zm9 zm9Var = zm9VarArr[10];
  663: z9g z9gVar = this.y;
  664: kf9 kf9Var = (kf9) z9gVar.s(this, zm9Var);
  665: if (kf9Var != null) {
  666: kf9Var.m(null);
  667: }
  668: z9gVar.y(this, zm9VarArr[10], null);
  669: View view = getView();
  670: ViewGroup viewGroup = view instanceof ViewGroup ? (ViewGroup) view : null;
  671: if (viewGroup != null) {
  672: viewGroup.removeView(this.x);
  673: }
  674: this.x = null;
  675: y1((String) w1().r.a.getValue());
  676: }
  677: 
  678: public ConfirmPhoneScreen(String str, String str2, int i, long j, String str3, nkg nkgVar) {
  679: this(e0c.d(new vld("screen:confirm_phone:verify_token", str), new vld("screen:confirm_phone:phone", str2), new vld("screen:confirm_phone:code_length", Integer.valueOf(i)), new vld("screen:confirm_phone:code_resend", Long.valueOf(j)), new vld("screen:confirm_phone:country_name_code", str3), new vld(Widget.ARG_SCOPE_ID, nkgVar)));
  680: }
  681: }
```

### one/me/login/confirmcallout/ConfirmPhoneCallOutScreen.java
Строки 75–165:
```java
   75: public final rz f;
   76: public final rz g;
   77: public final rz h;
   78: public final rz i;
   79: public Bundle j;
   80: public final rp9 k;
   81: public final rp9 l;
   82: public final ulf m;
   83: public final ulf n;
   84: public final ulf o;
   85: public final ulf p;
   86: public final rp9 q;
   87: 
   88: public ConfirmPhoneCallOutScreen(Bundle bundle) {
   89: super(bundle);
   90: this.a = new qzd((byte) 19);
   91: this.b = fa5.e(this, rkg.AUTH_CALL_OUT);
   92: this.c = new wj2(mo17getAccountScopeuqN4xOY());
   93: this.d = o89.f;
   94: Class<String> cls = String.class;
   95: this.e = new rz("screen:confirm_call_out:phone", cls);
   96: this.f = new rz("screen:confirm_call_out:track_id", cls);
   97: this.g = new rz("screen:confirm_call_out:time_out", Long.class);
   98: this.h = new rz("screen:confirm_call_out:call_number", cls);
   99: this.i = new rz("screen:confirm_call_out:polling_interval", Integer.class);
  100: this.k = createViewModelLazy(lp4.class, new no3(new gp4(this, (byte) 0), (byte) 9));
  101: this.l = xnm.p(3, new gp4(this, (byte) 1));
  102: this.m = viewBinding(R.id.oneme_login_confirm_callout_title);
  103: this.n = viewBinding(R.id.oneme_login_confirm_callout_description);
  104: this.o = viewBinding(R.id.oneme_login_confirm_callout_hint);
  105: this.p = viewBinding(R.id.oneme_login_confirm_callout_button);
  106: this.q = xnm.p(3, new gp4(this, (byte) 2));
  107: }
  108: 
  109: @Override // one.me.sdk.arch.Widget
  110: /* JADX INFO: renamed from: getInsetsConfig, reason: from getter */
  111: public final o89 getB() {
  112: return this.d;
  113: }
  114: 
  115: @Override // one.me.sdk.arch.Widget
  116: /* JADX INFO: renamed from: getScreenDelegate */
  117: public final vkg getU() {
  118: return this.b;
  119: }
  120: 
  121: @Override // com.bluelinelabs.conductor.Controller
  122: public final void onActivityStarted(Activity activity) {
  123: super.onActivityStarted(activity);
  124: vld vldVarU1 = u1();
  125: t1().g1((q12) vldVarU1.a, s1(), (String) vldVarU1.b);
  126: }
  127: 
  128: @Override // com.bluelinelabs.conductor.Controller
  129: public final void onActivityStopped(Activity activity) {
  130: super.onActivityStopped(activity);
  131: Activity activity2 = getActivity();
  132: tv7 tv7Var = activity2 instanceof tv7 ? (tv7) activity2 : null;
  133: if (tv7Var != null) {
  134: tv7Var.a.f((zr9) this.q.getValue());
  135: }
  136: lp4 lp4VarT1 = t1();
  137: kf9 kf9VarF1 = lp4VarT1.f1();
  138: if (kf9VarF1 != null) {
  139: kf9VarF1.m(null);
  140: }
  141: z9g z9gVar = lp4VarT1.u;
  142: zm9[] zm9VarArr = lp4.x;
  143: kf9 kf9Var = (kf9) z9gVar.s(lp4VarT1, zm9VarArr[0]);
  144: if (kf9Var != null) {
  145: kf9Var.m(null);
  146: }
  147: kf9 kf9Var2 = (kf9) lp4VarT1.v.s(lp4VarT1, zm9VarArr[1]);
  148: if (kf9Var2 != null) {
  149: kf9Var2.m(null);
  150: }
  151: }
  152: 
  153: @Override // com.bluelinelabs.conductor.Controller
  154: public final View onCreateView(LayoutInflater layoutInflater, ViewGroup viewGroup, Bundle bundle) {
  155: LinearLayout linearLayout = new LinearLayout(getContext());
  156: linearLayout.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
  157: linearLayout.setOrientation(1);
  158: linearLayout.setGravity(1);
  159: had hadVar = new had(linearLayout.getContext());
  160: hadVar.setId(R.id.oneme_login_confirm_callout_toolbar);
  161: hadVar.z(x9d.b);
  162: hadVar.A(new n9d(null, new sq2(this, (byte) 19)));
  163: linearLayout.setGravity(17);
  164: linearLayout.addView(hadVar);
  165: TextView textView = new TextView(linearLayout.getContext());
```

### one/me/login/LoginScreen.java
Строки 1–116:
```java
    1: package one.me.login;
    2: 
    3: import android.os.Bundle;
    4: import android.view.LayoutInflater;
    5: import android.view.View;
    6: import android.view.ViewGroup;
    7: import android.widget.FrameLayout;
    8: import defpackage.a9a;
    9: import defpackage.b55;
   10: import defpackage.c74;
   11: import defpackage.dk7;
   12: import defpackage.e0c;
   13: import defpackage.f09;
   14: import defpackage.lkg;
   15: import defpackage.luf;
   16: import defpackage.n3a;
   17: import defpackage.nkg;
   18: import defpackage.nm9;
   19: import defpackage.nr9;
   20: import defpackage.p7;
   21: import defpackage.pz2;
   22: import defpackage.r25;
   23: import defpackage.r4i;
   24: import defpackage.rp9;
   25: import defpackage.t2g;
   26: import defpackage.tul;
   27: import defpackage.ulf;
   28: import defpackage.v4f;
   29: import defpackage.v8a;
   30: import defpackage.wj2;
   31: import defpackage.wt0;
   32: import defpackage.wu3;
   33: import defpackage.xnm;
   34: import defpackage.yj3;
   35: import defpackage.z8a;
   36: import defpackage.zm9;
   37: import kotlin.Metadata;
   38: import me.leolin.shortcutbadger.BuildConfig;
   39: import one.me.sdk.arch.Widget;
   40: import ru.oneme.app.R;
   41: 
   42: /* JADX INFO: loaded from: classes.dex */
   43: @Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\b\u0001\u0018\u00002\u00020\u00012\u00020\u0002B\u000f\u0012\u0006\u0010\u0004\u001a\u00020\u0003¢\u0006\u0004\b\u0005\u0010\u0006¨\u0006\u0007"}, d2 = {"Lone/me/login/LoginScreen;", "Lone/me/sdk/arch/Widget;", BuildConfig.FLAVOR, "Landroid/os/Bundle;", "args", "<init>", "(
   44: public final class LoginScreen extends Widget {
   45: public static final /* synthetic */ zm9[] h;
   46: public final String a;
   47: public final ulf b;
   48: public final nkg c;
   49: public final rp9 d;
   50: public final wj2 e;
   51: public final t2g f;
   52: public final rp9 g;
   53: 
   54: static {
   55: v4f v4fVar = new v4f(LoginScreen.class, "loginRouter", "getLoginRouter()Lcom/bluelinelabs/conductor/Router;", 0);
   56: luf.a.getClass();
   57: h = new zm9[]{v4fVar};
   58: }
   59: 
   60: public LoginScreen(Bundle bundle) {
   61: super(bundle);
   62: this.a = LoginScreen.class.getName();
   63: this.b = Widget.childRouter$default(this, R.id.oneme_login_conductor, null, 2, null);
   64: this.c = nkg.a(super.getC(), 0, 2);
   65: this.d = xnm.p(3, new wu3(this, (byte) 9));
   66: this.e = new wj2(mo17getAccountScopeuqN4xOY());
   67: this.f = tul.i0(new v8a(this, (byte) 0));
   68: this.g = createViewModelLazy(z8a.class, new wu3(new v8a(this, (byte) 1), (byte) 10));
   69: }
   70: 
   71: @Override // one.me.sdk.arch.Widget
   72: /* JADX INFO: renamed from: getAccountScope-uqN4xOY, reason: not valid java name */
   73: public final lkg mo17getAccountScopeuqN4xOY() {
   74: return ((p7) this.d.getValue()).a;
   75: }
   76: 
   77: @Override // one.me.sdk.arch.Widget
   78: /* JADX INFO: renamed from: getScopeId, reason: from getter */
   79: public final nkg getC() {
   80: return this.c;
   81: }
   82: 
   83: @Override // com.bluelinelabs.conductor.Controller
   84: public final View onCreateView(LayoutInflater layoutInflater, ViewGroup viewGroup, Bundle bundle) {
   85: pz2 pz2Var = new pz2(getContext());
   86: pz2Var.setId(R.id.oneme_login_conductor);
   87: pz2Var.setLayoutParams(new FrameLayout.LayoutParams(-1, -1));
   88: return pz2Var;
   89: }
   90: 
   91: @Override // com.bluelinelabs.conductor.Controller
   92: public final void onDestroyView(View view) {
   93: super.onDestroyView(view);
   94: this.f.b = wt0.j;
   95: }
   96: 
   97: @Override // one.me.sdk.arch.Widget
   98: public final void onViewCreated(View view) {
   99: super.onViewCreated(view);
  100: rp9 rp9Var = this.g;
  101: z8a z8aVar = (z8a) rp9Var.getValue();
  102: r4i r4iVar = z8aVar.g;
  103: n3a n3aVar = (n3a) ((c74) z8aVar.d.getValue());
  104: b55 b55Var = null;
  105: if (((Boolean) n3aVar.f1.s(n3aVar, n3a.g1[52])).booleanValue()) {
  106: f09.c0(z8a.class.getName(), "Logout not fully completed", new a("Logout not fully completed"));
  107: r4iVar.getClass();
  108: r4iVar.j(null, a9a.b);
  109: nm9.J(z8aVar.b, null, 0, new r25(z8aVar, b55Var, (byte) 24), 3);
  110: } else {
  111: r4iVar.getClass();
  112: r4iVar.j(null, a9a.c);
  113: }
  114: e0c.M(new dk7(nm9.n(((z8a) rp9Var.getValue()).h, getViewLifecycleOwner().f(), nr9.d), new yj3(null, this), (byte) 3), getViewLifecycleScope());
  115: }
  116: }
```

### defpackage/ty3.java
Строки 1–76:
```java
    1: package defpackage;
    2: 
    3: import android.view.View;
    4: import one.me.chats.list.ChatsListWidget;
    5: import one.me.login.inputphone.InputPhoneScreen;
    6: 
    7: /* JADX INFO: loaded from: classes.dex */
    8: public final /* synthetic */ class ty3 implements View.OnClickListener {
    9: public final /* synthetic */ byte a;
   10: public final /* synthetic */ Object b;
   11: 
   12: public /* synthetic */ ty3(Object obj, byte b) {
   13: this.a = b;
   14: this.b = obj;
   15: }
   16: 
   17: @Override // android.view.View.OnClickListener
   18: public final void onClick(View view) {
   19: byte b = this.a;
   20: Object obj = this.b;
   21: switch (b) {
   22: case 0:
   23: zm9[] zm9VarArr = ChatsListWidget.Z;
   24: a04.b.r(((ChatsListWidget) obj).e);
   25: break;
   26: case 1:
   27: InputPhoneScreen inputPhoneScreen = (InputPhoneScreen) obj;
   28: zm9[] zm9VarArr2 = InputPhoneScreen.w;
   29: if (inputPhoneScreen.getView() != null) {
   30: u79 u79VarU1 = inputPhoneScreen.u1();
   31: g0i g0iVar = (g0i) u79VarU1.c.a(u79VarU1.b, ((vxc) ((k6j) u79VarU1.f.getValue())).b(), 2, new yr0(inputPhoneScreen.t1().a(), String.valueOf(inputPhoneScreen.t1().i.getText()), u79VarU1, null, (byte) 11));
   32: z9g z9gVar = u79VarU1.r;
   33: zm9[] zm9VarArr3 = u79.x;
   34: boolean z = false;
   35: z9gVar.y(u79VarU1, zm9VarArr3[0], g0iVar);
   36: u79 u79VarU2 = inputPhoneScreen.u1();
   37: kf9 kf9Var = (kf9) u79VarU2.r.s(u79VarU2, zm9VarArr3[0]);
   38: if (kf9Var != null && kf9Var.a()) {
   39: z = true;
   40: }
   41: svc svcVarR1 = inputPhoneScreen.r1();
   42: svcVarR1.o(z);
   43: svcVarR1.setClickable(!z);
   44: }
   45: break;
   46: case 2:
   47: ((xrc) obj).c();
   48: break;
   49: case 3:
   50: ((xrc) obj).c();
   51: break;
   52: case 4:
   53: ((o08) obj).c();
   54: break;
   55: case 5:
   56: ((h5d) obj).d();
   57: break;
   58: case 6:
   59: m7d m7dVar = (m7d) obj;
   60: q08 q08Var = m7dVar.j;
   61: if (q08Var != null) {
   62: q08Var.d(m7dVar.b());
   63: }
   64: break;
   65: case 7:
   66: o08 o08Var = ((ndi) obj).j;
   67: if (o08Var != null) {
   68: o08Var.c();
   69: }
   70: break;
   71: default:
   72: ((aad) obj).g.d(view);
   73: break;
   74: }
   75: }
   76: }
```

### defpackage/yr0.java
Строки 200–480:
```java
  200: return ka5Var;
  201: }
  202: 
  203: /* JADX WARN: Code duplicated, block: B:31:0x00c9  */
  204: /* JADX WARN: Code duplicated, block: B:34:0x010d  */
  205: /* JADX WARN: Code duplicated, block: B:37:0x0111 A[RETURN] */
  206: /* JADX WARN: Code duplicated, block: B:38:0x0112  */
  207: private final Object B(Object obj) {
  208: Object objG;
  209: String str;
  210: String str2;
  211: Object objA;
  212: String str3;
  213: bj0 bj0Var;
  214: String str4;
  215: c cVar;
  216: Object objD;
  217: u79 u79Var = (u79) this.k;
  218: b79 b79Var = u79Var.d;
  219: byte b = this.f;
  220: s1k s1kVar = s1k.a;
  221: ka5 ka5Var = ka5.a;
  222: if (b == 0) {
  223: xnm.y(obj);
  224: String strY = vg9.y((String) this.i, " ", (String) this.j);
  225: String strC = b79Var.i.c(strY, BuildConfig.FLAVOR);
  226: d2c d2cVar = (d2c) u79Var.h.getValue();
  227: this.g = strY;
  228: this.h = strC;
  229: this.f = (byte) 1;
  230: objG = d2cVar.g(strC, this);
  231: if (objG != ka5Var) {
  232: str = strY;
  233: str2 = strC;
  234: }
  235: return ka5Var;
  236: }
  237: if (b == 1) {
  238: str2 = (String) this.h;
  239: str = (String) this.g;
  240: xnm.y(obj);
  241: objG = obj;
  242: } else {
  243: if (b == 2) {
  244: xnm.y(obj);
  245: return s1kVar;
  246: }
  247: if (b != 3) {
  248: if (b == 4) {
  249: xnm.y(obj);
  250: return s1kVar;
  251: }
  252: k3g.o("call to 'resume' before 'invoke' with coroutine");
  253: return null;
  254: }
  255: String str5 = (String) this.g;
  256: xnm.y(obj);
  257: str3 = str5;
  258: objA = obj;
  259: }
  260: bj0Var = (bj0) objA;
  261: str4 = ((fyc) b79Var.e.getValue()).a;
  262: cVar = bj0Var.h;
  263: if (cVar != null) {
  264: u79Var.l.e(new h79(bj0Var.d, bj0Var.e, bj0Var.c, str3, str4));
  265: return s1kVar;
  266: }
  267: this.g = null;
  268: this.h = null;
  269: this.f = (byte) 4;
  270: long jF = ((hog) ((c74) u79Var.k.getValue())).f() + ((long) cVar.c);
  271: objD = ((ph0) u79Var.i.getValue()).a(jF, az7.U(cVar.d, me6.d), cVar.b).d(new q79(u79Var, cVar, str3, jF), this);
  272: if (objD != ka5Var) {
  273: objD = s1kVar;
  274: }
  275: if (objD != ka5Var) {
  276: return ka5Var;
  277: }
  278: return s1kVar;
  279: if (((Boolean) objG).booleanValue()) {
  280: nih nihVar = u79Var.m;
  281: q7a q7aVar = new q7a(new mdj(R.string.oneme_login_already_in_this_profile));
  282: this.g = null;
  283: this.h = null;
  284: this.f = (byte) 2;
  285: if (nihVar.b(q7aVar, this) != ka5Var) {
  286: return s1kVar;
  287: }
  288: } else {
  289: zm9[] zm9VarArr = u79.x;
  290: ej0 ej0Var = (ej0) u79Var.e.getValue();
  291: this.g = str;
  292: this.h = null;
  293: this.f = (byte) 3;
  294: objA = ej0Var.a(str2, 1, this);
  295: if (objA != ka5Var) {
  296: str3 = str;
  297: bj0Var = (bj0) objA;
  298: str4 = ((fyc) b79Var.e.getValue()).a;
  299: cVar = bj0Var.h;
  300: if (cVar != null) {
  301: u79Var.l.e(new h79(bj0Var.d, bj0Var.e, bj0Var.c, str3, str4));
  302: return s1kVar;
  303: }
  304: this.g = null;
  305: this.h = null;
  306: this.f = (byte) 4;
  307: long jF2 = ((hog) ((c74) u79Var.k.getValue())).f() + ((long) cVar.c);
  308: objD = ((ph0) u79Var.i.getValue()).a(jF2, az7.U(cVar.d, me6.d), cVar.b).d(new q79(u79Var, cVar, str3, jF2), this);
  309: if (objD != ka5Var) {
  310: objD = s1kVar;
  311: }
  312: if (objD != ka5Var) {
  313: return s1kVar;
  314: }
  315: }
  316: }
  317: return ka5Var;
  318: }
  319: 
  320: /* JADX WARN: Code duplicated, block: B:25:0x008a  */
  321: /* JADX WARN: Code duplicated, block: B:29:0x00a9  */
  322: /* JADX WARN: Code duplicated, block: B:33:0x00d7  */
  323: private final Object C(Object obj) {
  324: a0h a0hVar;
  325: a0h a0hVar2;
  326: ArrayList arrayList;
  327: Object objG;
  328: a0h a0hVar3;
  329: ArrayList arrayList2;
  330: Collection collection;
  331: Object objG2;
  332: Collection collection2;
  333: z05 z05Var;
  334: q29 q29Var;
  335: ArrayList arrayList3;
  336: k40 k40Var = (k40) this.k;
  337: byte b = this.f;
  338: ka5 ka5Var = ka5.a;
  339: if (b == 0) {
  340: xnm.y(obj);
  341: this.f = (byte) 1;
  342: obj = k40Var.e(this);
  343: if (obj != ka5Var) {
  344: }
  345: return ka5Var;
  346: }
  347: if (b == 1) {
  348: xnm.y(obj);
  349: } else {
  350: if (b == 2) {
  351: a0hVar = (a0h) this.g;
  352: xnm.y(obj);
  353: a0hVar2 = (a0h) obj;
  354: arrayList = new ArrayList();
  355: List listT = j0h.T(a0hVar);
  356: this.g = null;
  357: this.h = a0hVar2;
  358: this.i = arrayList;
  359: this.f = (byte) 3;
  360: objG = jd0.g(listT, this);
  361: if (objG != ka5Var) {
  362: a0hVar3 = a0hVar2;
  363: obj = objG;
  364: arrayList2 = arrayList;
  365: collection = (Collection) obj;
  366: List listT2 = j0h.T(a0hVar3);
  367: this.g = null;
  368: this.h = null;
  369: this.i = arrayList2;
  370: this.j = collection;
  371: this.f = (byte) 4;
  372: objG2 = jd0.g(listT2, this);
  373: if (objG2 != ka5Var) {
  374: collection2 = collection;
  375: obj = objG2;
  376: va4.I0(va4.a1((Iterable) obj, collection2), arrayList2);
  377: z05Var = (z05) ((rp9) k40Var.g).getValue();
  378: q29Var = new q29((byte) 23);
  379: this.g = null;
  380: this.h = null;
  381: this.i = arrayList2;
  382: this.j = null;
  383: this.f = (byte) 5;
  384: if (z05Var.b(arrayList2, q29Var, this) != ka5Var) {
  385: arrayList3 = arrayList2;
  386: }
  387: }
  388: }
  389: return ka5Var;
  390: }
  391: if (b == 3) {
  392: arrayList2 = (ArrayList) this.i;
  393: a0hVar3 = (a0h) this.h;
  394: xnm.y(obj);
  395: collection = (Collection) obj;
  396: List listT3 = j0h.T(a0hVar3);
  397: this.g = null;
  398: this.h = null;
  399: this.i = arrayList2;
  400: this.j = collection;
  401: this.f = (byte) 4;
  402: objG2 = jd0.g(listT3, this);
  403: if (objG2 != ka5Var) {
  404: collection2 = collection;
  405: obj = objG2;
  406: va4.I0(va4.a1((Iterable) obj, collection2), arrayList2);
  407: z05Var = (z05) ((rp9) k40Var.g).getValue();
  408: q29Var = new q29((byte) 23);
  409: this.g = null;
  410: this.h = null;
  411: this.i = arrayList2;
  412: this.j = null;
  413: this.f = (byte) 5;
  414: if (z05Var.b(arrayList2, q29Var, this) != ka5Var) {
  415: arrayList3 = arrayList2;
  416: }
  417: }
  418: return ka5Var;
  419: }
  420: if (b == 4) {
  421: Collection collection3 = (Collection) this.j;
  422: ArrayList arrayList4 = (ArrayList) this.i;
  423: xnm.y(obj);
  424: collection2 = collection3;
  425: arrayList2 = arrayList4;
  426: va4.I0(va4.a1((Iterable) obj, collection2), arrayList2);
  427: z05Var = (z05) ((rp9) k40Var.g).getValue();
  428: q29Var = new q29((byte) 23);
  429: this.g = null;
  430: this.h = null;
  431: this.i = arrayList2;
  432: this.j = null;
  433: this.f = (byte) 5;
  434: if (z05Var.b(arrayList2, q29Var, this) != ka5Var) {
  435: arrayList3 = arrayList2;
  436: }
  437: return ka5Var;
  438: }
  439: if (b != 5) {
  440: k3g.o("call to 'resume' before 'invoke' with coroutine");
  441: return null;
  442: }
  443: arrayList3 = (ArrayList) this.i;
  444: xnm.y(obj);
  445: }
  446: arrayList3.removeIf(new i7(new y20(new n3c(arrayList3.size()), (byte) 2), (byte) 10));
  447: r4i r4iVar = (r4i) k40Var.j;
  448: r4iVar.getClass();
  449: r4iVar.j(null, arrayList3);
  450: ((AtomicBoolean) k40Var.e).set(false);
  451: return s1k.a;
  452: a0hVar = (a0h) obj;
  453: this.g = a0hVar;
  454: this.f = (byte) 2;
  455: obj = k40Var.f(this);
  456: if (obj != ka5Var) {
  457: a0hVar2 = (a0h) obj;
  458: arrayList = new ArrayList();
  459: List listT4 = j0h.T(a0hVar);
  460: this.g = null;
  461: this.h = a0hVar2;
  462: this.i = arrayList;
  463: this.f = (byte) 3;
  464: objG = jd0.g(listT4, this);
  465: if (objG != ka5Var) {
  466: a0hVar3 = a0hVar2;
  467: obj = objG;
  468: arrayList2 = arrayList;
  469: collection = (Collection) obj;
  470: List listT5 = j0h.T(a0hVar3);
  471: this.g = null;
  472: this.h = null;
  473: this.i = arrayList2;
  474: this.j = collection;
  475: this.f = (byte) 4;
  476: objG2 = jd0.g(listT5, this);
  477: if (objG2 != ka5Var) {
  478: collection2 = collection;
  479: obj = objG2;
  480: va4.I0(va4.a1((Iterable) obj, collection2), arrayList2);
```

### defpackage/u79.java
Строки 1–156:
```java
    1: package defpackage;
    2: 
    3: import me.leolin.shortcutbadger.BuildConfig;
    4: import ru.oneme.app.R;
    5: 
    6: /* JADX INFO: loaded from: classes.dex */
    7: public final class u79 extends oyk implements fs4 {
    8: public static final /* synthetic */ zm9[] x = {new c4c(u79.class, "authJob", "getAuthJob()Lkotlinx/coroutines/Job;"), a15.f(luf.a, u79.class, "jobPhoneValidation", "getJobPhoneValidation()Lkotlinx/coroutines/Job;")};
    9: public final /* synthetic */ qyk c;
   10: public final b79 d;
   11: public final rp9 e;
   12: public final rp9 f;
   13: public final rp9 g;
   14: public final rp9 h;
   15: public final rp9 i;
   16: public final rp9 j;
   17: public final rp9 k;
   18: public final vv6 l;
   19: public final nih m;
   20: public final vv6 n;
   21: public final cmf o;
   22: public final String p;
   23: public final dk7 q;
   24: public final z9g r;
   25: public final z9g s;
   26: public volatile boolean t;
   27: public final mdj u;
   28: public final qi7 v;
   29: public final dmf w;
   30: 
   31: public u79(b79 b79Var, rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9) {
   32: byte b = 12;
   33: qyk qykVar = new qyk(rp9Var3, new vo4(b));
   34: this.c = qykVar;
   35: this.d = b79Var;
   36: this.e = rp9Var;
   37: this.f = rp9Var2;
   38: this.g = rp9Var5;
   39: this.h = rp9Var6;
   40: this.i = rp9Var7;
   41: this.j = rp9Var9;
   42: this.k = rp9Var8;
   43: b55 b55Var = null;
   44: this.l = new vv6(null);
   45: nih nihVarC = fa5.c(0, 0, 7);
   46: this.m = nihVarC;
   47: this.n = new vv6(null);
   48: this.o = b79Var.h;
   49: this.p = u79.class.getName();
   50: qi7[] qi7VarArr = {nihVarC, new c30(qykVar.d, (byte) 12)};
   51: byte b2 = 3;
   52: dk7 dk7Var = new dk7(xk7.d(qi7VarArr), new yj3(this, b55Var, b), b2);
   53: this.q = dk7Var;
   54: this.r = c45.Q();
   55: this.s = c45.Q();
   56: this.u = new mdj(R.string.oneme_login_input_select_country_info);
   57: this.v = b79Var.a(new r79(2, b55Var, (byte) 0));
   58: this.w = b79Var.b(this.b);
   59: e0c.M(h6c.p(new dk7(dk7Var, new pk3((Object) this, (Object) rp9Var4, b55Var, (byte) 5), b2), ((vxc) ((k6j) rp9Var2.getValue())).a()), this.b);
   60: e0c.M(qo9.c(new fw8(this, b55Var, (byte) 1)), this.b);
   61: }
   62: 
   63: @Override // defpackage.oyk
   64: public final void a1() {
   65: zm9[] zm9VarArr = x;
   66: zm9 zm9Var = zm9VarArr[0];
   67: z9g z9gVar = this.r;
   68: kf9 kf9Var = (kf9) z9gVar.s(this, zm9Var);
   69: if (kf9Var != null) {
   70: kf9Var.m(null);
   71: }
   72: z9gVar.y(this, zm9VarArr[0], null);
   73: zm9 zm9Var2 = zm9VarArr[1];
   74: z9g z9gVar2 = this.s;
   75: kf9 kf9Var2 = (kf9) z9gVar2.s(this, zm9Var2);
   76: if (kf9Var2 != null) {
   77: kf9Var2.m(null);
   78: }
   79: z9gVar2.y(this, zm9VarArr[1], null);
   80: }
   81: 
   82: /* JADX WARN: Code duplicated, block: B:7:0x0019  */
   83: public final Object c1(c cVar, String str, d55 d55Var) {
   84: s79 s79Var;
   85: String str2 = str;
   86: if (d55Var instanceof s79) {
   87: s79Var = (s79) d55Var;
   88: int i = s79Var.g;
   89: if ((i & Integer.MIN_VALUE) != 0) {
   90: s79Var.g = i - Integer.MIN_VALUE;
   91: } else {
   92: s79Var = new s79(this, d55Var);
   93: }
   94: } else {
   95: s79Var = new s79(this, d55Var);
   96: }
   97: Object objA = s79Var.e;
   98: ka5 ka5Var = ka5.a;
   99: int i2 = s79Var.g;
  100: if (i2 == 0) {
  101: xnm.y(objA);
  102: fh0 fh0Var = (fh0) this.j.getValue();
  103: String strB = cVar.b();
  104: s79Var.d = str2;
  105: s79Var.g = 1;
  106: objA = fh0Var.a(strB, str2, s79Var);
  107: if (objA == ka5Var) {
  108: return ka5Var;
  109: }
  110: } else {
  111: if (i2 != 1) {
  112: k3g.o("call to 'resume' before 'invoke' with coroutine");
  113: return null;
  114: }
  115: str2 = s79Var.d;
  116: xnm.y(objA);
  117: }
  118: String str3 = str2;
  119: eh0 eh0Var = (eh0) objA;
  120: if (eh0Var instanceof dh0) {
  121: azc azcVarA = ((dh0) eh0Var).a();
  122: ii0 ii0VarE = azcVarA != null ? azcVarA.E() : ii0.e;
  123: m8a m8aVar = m8a.b;
  124: String strL = azcVarA != null ? azcVarA.L() : null;
  125: String str4 = strL == null ? BuildConfig.FLAVOR : strL;
  126: String strG = azcVarA != null ? azcVarA.G() : null;
  127: String str5 = strG == null ? BuildConfig.FLAVOR : strG;
  128: String strF = azcVarA != null ? azcVarA.F() : null;
  129: this.l.e(m8aVar.m(str4, str5, strF == null ? BuildConfig.FLAVOR : strF, str3, ii0VarE.c(), ii0VarE.b(), ii0VarE.a()));
  130: } else if (g4a.c(eh0Var, ah0.a)) {
  131: this.l.e(f79.b);
  132: } else if (eh0Var instanceof ch0) {
  133: ch0 ch0Var = (ch0) eh0Var;
  134: this.l.e(new g79(ch0Var.b(), ch0Var.a()));
  135: } else {
  136: if (!g4a.c(eh0Var, bh0.a)) {
  137: k3g.l();
  138: return null;
  139: }
  140: String name = u79.class.getName();
  141: o1d o1dVar = f09.g;
  142: if (o1dVar != null) {
  143: c6a c6aVar = c6a.f;
  144: if (o1dVar.b(c6aVar)) {
  145: o1dVar.c(c6aVar, name, "authByTrackUseCase execute: return None", null);
  146: }
  147: }
  148: }
  149: return s1k.a;
  150: }
  151: 
  152: @Override // defpackage.fs4
  153: public final cmf f0() {
  154: return this.c.d;
  155: }
  156: }
```

### defpackage/v79.java
Строки 1–28:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes.dex */
    4: public final class v79 {
    5: public final rp9 a;
    6: public final b79 b;
    7: public final rp9 c;
    8: public final rp9 d;
    9: public final rp9 e;
   10: public final rp9 f;
   11: public final rp9 g;
   12: public final rp9 h;
   13: public final rp9 i;
   14: public final rp9 j;
   15: 
   16: public v79(rp9 rp9Var, b79 b79Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9, rp9 rp9Var10) {
   17: this.a = rp9Var;
   18: this.b = b79Var;
   19: this.c = rp9Var2;
   20: this.d = rp9Var3;
   21: this.e = rp9Var4;
   22: this.f = rp9Var5;
   23: this.g = rp9Var7;
   24: this.h = rp9Var8;
   25: this.i = rp9Var9;
   26: this.j = rp9Var10;
   27: }
   28: }
```

### defpackage/dq4.java
Строки 1–88:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class dq4 extends oyk implements fs4 {
    5: public static final /* synthetic */ zm9[] y;
    6: public static final String z;
    7: public final /* synthetic */ qyk c;
    8: public final int d;
    9: public String e;
   10: public final String f;
   11: public final rp9 g;
   12: public final rp9 h;
   13: public final rp9 i;
   14: public final rp9 j;
   15: public final rp9 k;
   16: public final rp9 l;
   17: public final z3j m;
   18: public final nih n;
   19: public final h13 o;
   20: public final vv6 p;
   21: public final r4i q;
   22: public final dmf r;
   23: public final cmf s;
   24: public final r4i t;
   25: public final r4i u;
   26: public volatile String v;
   27: public g0i w;
   28: public final z9g x;
   29: 
   30: static {
   31: c4c c4cVar = new c4c(dq4.class, "loginJob", "getLoginJob()Lkotlinx/coroutines/Job;");
   32: luf.a.getClass();
   33: y = new zm9[]{c4cVar};
   34: z = dq4.class.getName();
   35: }
   36: 
   37: public dq4(int i, String str, String str2, long j, rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9) {
   38: qyk qykVar = new qyk(rp9Var6, new u23((byte) 27));
   39: this.c = qykVar;
   40: this.d = i;
   41: this.e = str;
   42: this.f = str2;
   43: this.g = rp9Var;
   44: this.h = rp9Var2;
   45: this.i = rp9Var3;
   46: this.j = rp9Var4;
   47: this.k = rp9Var5;
   48: this.l = rp9Var8;
   49: this.m = new z3j(new ka2(rp9Var9, this, (byte) 29));
   50: nih nihVarC = fa5.c(0, 1, 1);
   51: this.n = nihVarC;
   52: h13 h13VarD = xk7.d(nihVarC, new a63(new c30(qykVar.d, (byte) 12), (byte) 4));
   53: this.o = h13VarD;
   54: this.p = new vv6(null);
   55: r4i r4iVarC = az7.c(Long.valueOf(fe6.w(j, me6.e)));
   56: this.q = r4iVarC;
   57: byte b = 3;
   58: this.r = tul.l0(new qt0(r4iVarC, b), this.b, hjh.a, null);
   59: this.s = ((tb8) rp9Var8.getValue()).c;
   60: Boolean bool = Boolean.FALSE;
   61: this.t = az7.c(bool);
   62: this.u = az7.c(bool);
   63: this.x = c45.Q();
   64: e0c.M(h6c.p(new dk7(h13VarD, new xfg((Object) this, (Object) rp9Var7, (b55) null, (byte) 18), b), ((vxc) ((k6j) rp9Var5.getValue())).a()), this.b);
   65: }
   66: 
   67: @Override // defpackage.oyk
   68: public final void a1() {
   69: g0i g0iVar = this.w;
   70: if (g0iVar != null) {
   71: g0iVar.m(null);
   72: }
   73: this.w = null;
   74: zm9[] zm9VarArr = y;
   75: zm9 zm9Var = zm9VarArr[0];
   76: z9g z9gVar = this.x;
   77: kf9 kf9Var = (kf9) z9gVar.s(this, zm9Var);
   78: if (kf9Var != null) {
   79: kf9Var.m(null);
   80: }
   81: z9gVar.y(this, zm9VarArr[0], null);
   82: }
   83: 
   84: @Override // defpackage.fs4
   85: public final cmf f0() {
   86: return this.c.d;
   87: }
   88: }
```

### defpackage/ka9.java
Строки 1–99:
```java
    1: package defpackage;
    2: 
    3: import android.os.Bundle;
    4: import com.bluelinelabs.conductor.Controller;
    5: import com.bluelinelabs.conductor.j;
    6: import java.util.ArrayList;
    7: import java.util.HashSet;
    8: import java.util.Iterator;
    9: import java.util.ListIterator;
   10: import me.leolin.shortcutbadger.BuildConfig;
   11: import one.me.login.confirm.ConfirmPhoneScreen;
   12: import one.me.login.confirmcallout.ConfirmPhoneCallOutScreen;
   13: import one.me.login.inputname.InputNameScreen;
   14: 
   15: /* JADX INFO: loaded from: classes2.dex */
   16: public final class ka9 {
   17: public final j a;
   18: public final nkg b;
   19: 
   20: public ka9(j jVar, nkg nkgVar) {
   21: this.a = jVar;
   22: this.b = nkgVar;
   23: }
   24: 
   25: /* JADX WARN: Type inference fix 'apply assigned field type' failed
   26: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
   27: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
   28: at jadx.core.dex.attributes.nodes.ClassTypeVarsAttr.getTypeVarsMapFor(ClassTypeVarsAttr.java:35)
   29: at jadx.core.dex.nodes.utils.TypeUtils.replaceClassGenerics(TypeUtils.java:177)
   30: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.insertExplicitUseCast(FixTypesVisitor.java:397)
   31: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryFieldTypeWithNewCasts(FixTypesVisitor.java:359)
   32: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.applyFieldType(FixTypesVisitor.java:309)
   33: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
   34: */
   35: public final void a(boolean z, boolean z2) {
   36: Bundle bundle;
   37: Object objPrevious;
   38: Controller controller;
   39: if (z) {
   40: bundle = new Bundle();
   41: bundle.putString("screen:input_phone:phone", BuildConfig.FLAVOR);
   42: } else {
   43: bundle = null;
   44: }
   45: j jVar = this.a;
   46: ArrayList arrayListE = jVar.e();
   47: HashSet hashSet = new HashSet();
   48: Iterator it = new a6g(jVar.e()).iterator();
   49: while (true) {
   50: ListIterator listIterator = ((z5g) it).b;
   51: if (!listIterator.hasPrevious()) {
   52: break;
   53: }
   54: zbg zbgVar = (zbg) listIterator.previous();
   55: if (g4a.c(zbgVar.b, "InputPhoneScreen")) {
   56: break;
   57: } else {
   58: hashSet.add(zbgVar);
   59: }
   60: }
   61: ListIterator listIterator2 = arrayListE.listIterator(arrayListE.size());
   62: do {
   63: if (!listIterator2.hasPrevious()) {
   64: objPrevious = null;
   65: break;
   66: }
   67: objPrevious = listIterator2.previous();
   68: } while (!g4a.c(((zbg) objPrevious).b, "InputPhoneScreen"));
   69: zbg zbgVar2 = (zbg) objPrevious;
   70: if (zbgVar2 == null \|\| (controller = zbgVar2.a) == null) {
   71: f09.d0(ka9.class.getName(), "Early return in goBackTo cuz of newBackStack.findLast { it.tag() == tag }?.controller is null", new Object[0]);
   72: return;
   73: }
   74: if (bundle != null) {
   75: controller.getArgs().putAll(bundle);
   76: }
   77: arrayListE.removeAll(hashSet);
   78: jVar.R(arrayListE, z2 ? new kl8(0) : null);
   79: }
   80: 
   81: public final void c(zbg zbgVar, String str) {
   82: zbgVar.e(str);
   83: zbgVar.c(new kl8(0));
   84: zbgVar.a(new kl8(0));
   85: this.a.I(zbgVar);
   86: }
   87: 
   88: public final void d(int i, long j, String str, String str2, String str3) {
   89: c(nb6.e(new ConfirmPhoneScreen(str, str2, i, j, str3, this.b), null, null), "ConfirmPhoneScreen");
   90: }
   91: 
   92: public final void e(int i, long j, String str, String str2, String str3) {
   93: c(nb6.e(new ConfirmPhoneCallOutScreen(str, str2, j, str3, i, this.b), null, null), "ConfirmPhoneCallOutScreen");
   94: }
   95: 
   96: public final void f(String str, String str2, kme kmeVar) {
   97: c(nb6.e(new InputNameScreen(str, str2, kmeVar, this.b), null, null), "InputNameScreen");
   98: }
   99: }
```

### defpackage/wi3.java
Строки 1–120:
```java
    1: package defpackage;
    2: 
    3: import android.media.MediaCodecInfo;
    4: import android.media.MediaCodecList;
    5: import android.os.Build;
    6: import java.util.ArrayList;
    7: import kotlin.collections.a;
    8: import one.me.chats.search.ChatsListSearchScreen;
    9: import one.me.chatscreen.ChatScreen;
   10: import one.me.login.confirm.ConfirmPhoneScreen;
   11: import one.me.profile.screens.members.ChatMembersScreen;
   12: import org.webrtc.PeerConnectionFactory;
   13: import ru.oneme.app.R;
   14: 
   15: /* JADX INFO: loaded from: classes2.dex */
   16: public final /* synthetic */ class wi3 implements o08 {
   17: public final /* synthetic */ byte a;
   18: 
   19: @Override // defpackage.o08
   20: public final Object c() {
   21: int maxSupportedInstances = 0;
   22: switch (this.a) {
   23: case 0:
   24: return new g45(R.id.profile_members_list_action_delete_from_admin, new mdj(R.string.profile_members_list_action_delete_from_admin), Integer.valueOf(R.attr.text_negative), Integer.valueOf(R.drawable.icon_delete), Integer.valueOf(R.attr.icon_negative), 32);
   25: case 1:
   26: zm9[] zm9VarArr = ChatMembersScreen.k;
   27: return rkg.CHAT_INFO_ALL_PARTICIPANTS;
   28: case 2:
   29: return wa4.i0(new yq4(R.id.chat_preview__confirm_mute_1_hour, new mdj(R.string.oneme_chat_notifications_disable_1_hour), 3, 56), new yq4(R.id.chat_preview__confirm_mute_4_hour, new mdj(R.string.oneme_chat_notifications_disable_4_hour), 3, 56), new yq4(R.id.chat_preview__confirm_mute_1_day, new mdj(R.string.oneme_chat_notifications_disable_1_day), 3, 56), new yq4(R.id.chat_preview__confirm_mute_inf
   30: case 3:
   31: return new sre();
   32: case 4:
   33: ran ranVar = ChatScreen.I1;
   34: return new nge();
   35: case 5:
   36: ran ranVar2 = ChatScreen.I1;
   37: return new kva();
   38: case 6:
   39: ran ranVar3 = ChatScreen.I1;
   40: return new oc();
   41: case 7:
   42: ran ranVar4 = ChatScreen.I1;
   43: return new q0c();
   44: case 8:
   45: zm9[] zm9VarArr2 = ChatsListSearchScreen.F;
   46: return Boolean.FALSE;
   47: case 9:
   48: return new aw3();
   49: case 10:
   50: return new aw3();
   51: case 11:
   52: return new xuf("^(http[s]?://www\\.\|http[s]?://\|www\\.)");
   53: case 12:
   54: if (Build.VERSION.SDK_INT >= 29) {
   55: MediaCodecInfo[] codecInfos = new MediaCodecList(0).getCodecInfos();
   56: codecInfos.getClass();
   57: ArrayList arrayList = new ArrayList();
   58: for (MediaCodecInfo mediaCodecInfo : codecInfos) {
   59: String[] supportedTypes = mediaCodecInfo.getSupportedTypes();
   60: supportedTypes.getClass();
   61: if (a.L(supportedTypes, "video/avc") && !mediaCodecInfo.isEncoder() && mediaCodecInfo.isHardwareAccelerated()) {
   62: arrayList.add(mediaCodecInfo);
   63: }
   64: }
   65: int size = arrayList.size();
   66: int i = 0;
   67: while (i < size) {
   68: Object obj = arrayList.get(i);
   69: i++;
   70: MediaCodecInfo.CodecCapabilities capabilitiesForType = ((MediaCodecInfo) obj).getCapabilitiesForType("video/avc");
   71: if (capabilitiesForType.getMaxSupportedInstances() > 0) {
   72: maxSupportedInstances = capabilitiesForType.getMaxSupportedInstances();
   73: }
   74: }
   75: }
   76: return Integer.valueOf(nm9.h(maxSupportedInstances - 5, 4, 10));
   77: case 13:
   78: return new qwe(R.string.oneme_profile_section_common_chats, null, 14);
   79: case 14:
   80: return new brh(false);
   81: case 15:
   82: return new brh(true);
   83: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
   84: zm9[] zm9VarArr3 = ConfirmPhoneScreen.z;
   85: int i2 = rn9.a;
   86: return Boolean.valueOf(rn9.b(rn9.c));
   87: case 17:
   88: zm9[] zm9VarArr4 = ConfirmPhoneScreen.z;
   89: return rkg.AUTH_OTP;
   90: case 18:
   91: return "connect";
   92: case 19:
   93: return "registerRead";
   94: case 20:
   95: return "readyForReadPayload";
   96: case 21:
   97: return "readyForWritePayload";
   98: case 22:
   99: return "disableWriteInterest";
  100: case 23:
  101: return "close";
  102: case 24:
  103: return "onConnected";
  104: case 25:
  105: return "registerConnect";
  106: case 26:
  107: return "readyForWrite";
  108: case 27:
  109: return "enableWriteInterest";
  110: case 28:
  111: return "readyForRead";
  112: default:
  113: return "registerWrite";
  114: }
  115: }
  116: 
  117: public /* synthetic */ wi3(byte b) {
  118: this.a = b;
  119: }
  120: }
```

### defpackage/k79.java
Строки 1–120:
```java
    1: package defpackage;
    2: 
    3: import android.widget.EditText;
    4: import com.bluelinelabs.conductor.Controller;
    5: import com.bluelinelabs.conductor.j;
    6: import me.leolin.shortcutbadger.BuildConfig;
    7: import one.me.android.root.RootController;
    8: import one.me.login.inputphone.InputPhoneScreen;
    9: import one.me.sdk.bottomsheet.BottomSheetWidget;
   10: import one.me.settings.multilang.LocaleBottomSheet;
   11: 
   12: /* JADX INFO: loaded from: classes.dex */
   13: public final class k79 extends x1j implements e18 {
   14: public final /* synthetic */ byte e;
   15: public /* synthetic */ Object f;
   16: public final /* synthetic */ InputPhoneScreen g;
   17: 
   18: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   19: public /* synthetic */ k79(b55 b55Var, InputPhoneScreen inputPhoneScreen, byte b) {
   20: super(2, b55Var);
   21: this.e = b;
   22: this.g = inputPhoneScreen;
   23: }
   24: 
   25: @Override // defpackage.e18
   26: public final Object invoke(Object obj, Object obj2) {
   27: byte b = this.e;
   28: s1k s1kVar = s1k.a;
   29: switch (b) {
   30: case 0:
   31: ((k79) u((b55) obj2, (y6c) obj)).w(s1kVar);
   32: break;
   33: case 1:
   34: ((k79) u((b55) obj2, obj)).w(s1kVar);
   35: break;
   36: case 2:
   37: ((k79) u((b55) obj2, obj)).w(s1kVar);
   38: break;
   39: case 3:
   40: ((k79) u((b55) obj2, obj)).w(s1kVar);
   41: break;
   42: case 4:
   43: ((k79) u((b55) obj2, (z7a) obj)).w(s1kVar);
   44: break;
   45: default:
   46: ((k79) u((b55) obj2, obj)).w(s1kVar);
   47: break;
   48: }
   49: return s1kVar;
   50: }
   51: 
   52: @Override // defpackage.hv0
   53: public final b55 u(b55 b55Var, Object obj) {
   54: byte b = this.e;
   55: InputPhoneScreen inputPhoneScreen = this.g;
   56: switch (b) {
   57: case 0:
   58: k79 k79Var = new k79(inputPhoneScreen, b55Var, (byte) 0);
   59: k79Var.f = obj;
   60: return k79Var;
   61: case 1:
   62: k79 k79Var2 = new k79(b55Var, inputPhoneScreen, (byte) 1);
   63: k79Var2.f = obj;
   64: return k79Var2;
   65: case 2:
   66: k79 k79Var3 = new k79(b55Var, inputPhoneScreen, (byte) 2);
   67: k79Var3.f = obj;
   68: return k79Var3;
   69: case 3:
   70: k79 k79Var4 = new k79(b55Var, inputPhoneScreen, (byte) 3);
   71: k79Var4.f = obj;
   72: return k79Var4;
   73: case 4:
   74: k79 k79Var5 = new k79(inputPhoneScreen, b55Var, (byte) 4);
   75: k79Var5.f = obj;
   76: return k79Var5;
   77: default:
   78: k79 k79Var6 = new k79(b55Var, inputPhoneScreen, (byte) 5);
   79: k79Var6.f = obj;
   80: return k79Var6;
   81: }
   82: }
   83: 
   84: /* JADX WARN: Type inference fix 'apply assigned field type' failed
   85: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
   86: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
   87: at jadx.core.dex.attributes.nodes.ClassTypeVarsAttr.getTypeVarsMapFor(ClassTypeVarsAttr.java:35)
   88: at jadx.core.dex.nodes.utils.TypeUtils.replaceClassGenerics(TypeUtils.java:177)
   89: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.insertExplicitUseCast(FixTypesVisitor.java:397)
   90: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryFieldTypeWithNewCasts(FixTypesVisitor.java:359)
   91: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.applyFieldType(FixTypesVisitor.java:309)
   92: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
   93: */
   94: @Override // defpackage.hv0
   95: public final Object w(Object obj) {
   96: byte b = this.e;
   97: CharSequence charSequence = BuildConfig.FLAVOR;
   98: s1k s1kVar = s1k.a;
   99: InputPhoneScreen inputPhoneScreen = this.g;
  100: switch (b) {
  101: case 0:
  102: rp9 rp9Var = inputPhoneScreen.q;
  103: y6c y6cVar = (y6c) this.f;
  104: xnm.y(obj);
  105: if (y6cVar instanceof h79) {
  106: zm9[] zm9VarArr = InputPhoneScreen.w;
  107: h79 h79Var = (h79) y6cVar;
  108: ((ka9) rp9Var.getValue()).d(h79Var.a(), h79Var.b(), h79Var.e(), h79Var.d(), h79Var.c());
  109: } else if (y6cVar instanceof d79) {
  110: LocaleBottomSheet localeBottomSheet = new LocaleBottomSheet(inputPhoneScreen.getB().b());
  111: z46 z46Var = new z46(localeBottomSheet, new x49(inputPhoneScreen, (byte) 1));
  112: if (localeBottomSheet.getRouter() != null) {
  113: localeBottomSheet.getRouter().a(z46Var);
  114: } else {
  115: localeBottomSheet.addLifecycleListener(new ac(localeBottomSheet, z46Var, (byte) 8));
  116: }
  117: inputPhoneScreen.t = localeBottomSheet;
  118: zm9[] zm9VarArr2 = BottomSheetWidget.t;
  119: localeBottomSheet.setTargetController(inputPhoneScreen);
  120: Controller parentController = inputPhoneScreen;
```

### defpackage/bwb.java
Строки 995–1033:
```java
  995: ij4Var.c(749, "one.me.sdk.transfer.upload.network.ConnectionFactory");
  996: ij4Var.c(117, "ru.ok.tamtam.logout.LogoutUseCase");
  997: ij4Var.c(744, "one.me.sdk.upload.videomsg.preparation.VideoMessagePrepareStepConvert");
  998: ij4Var.c(264, "one.me.sdk.statistics.calls.CallsStats");
  999: ij4Var.c(1134, "one.me.webapp.settings.WebAppsSettingViewModelFactory");
 1000: ij4Var.c(1179, "one.me.sdk.media.fresco.core.ImageNetworkFetcher");
 1001: ij4Var.c(785, "one.me.calls.api.service.CallIntentActionDepended");
 1002: ij4Var.c(886, "one.me.chatmediabar.mediatypepicker.MediaTypePickerViewModelFactory");
 1003: ij4Var.c(853, "one.me.sdk.dynamicfont.OneMeDynamicFont");
 1004: ij4Var.c(377, "ru.ok.tamtam.events.NotifBannerEvents");
 1005: ij4Var.c(286, "one.me.features.media.autosave.usecase.AwaitAndSaveVideoToGalleryUseCase");
 1006: ij4Var.c(1199, "one.me.android.notifications.BadgeCountUpdater");
 1007: ij4Var.c(931, "one.me.settings.ProfileEvents");
 1008: ij4Var.c(319, "one.me.stories.core.domain.StoryPublishingController");
 1009: ij4Var.c(653, "one.me.sdk.stickers.StickerCreateLogic");
 1010: ij4Var.c(184, "ru.ok.tamtam.android.prefs.SdkClientPrefs");
 1011: ij4Var.c(549, "ru.ok.tamtam.chats.usecases.ChatUnpinMessageUseCase");
 1012: ij4Var.c(863, "one.me.login.usecases.AuthRequestUseCase");
 1013: ij4Var.c(701, "one.me.sdk.contacts.UndoBlockContactUseCase");
 1014: ij4Var.c(68, "one.me.calls.api.core.CallsCoroutineScope");
 1015: ij4Var.c(668, "ru.ok.tamtam.GetChatInfoUseCase");
 1016: ij4Var.c(1175, "com.facebook.imagepipeline.core.ImagePipelineConfig$Builder");
 1017: ij4Var.c(122, "one.me.sdk.api.auth.AuthApi");
 1018: ij4Var.c(1116, "one.me.chatscreen.drafts.RestoreDraftUseCase");
 1019: ij4Var.c(1161, "one.me.profile.screens.joinrequests.JoinRequestsViewModelFactory");
 1020: ij4Var.c(1096, "one.me.folders.FolderNavigationComponent");
 1021: ij4Var.c(1072, "one.me.chats.list.ChatMetaDump");
 1022: ij4Var.c(255, "one.me.webview.WebViewJsErrorHandler");
 1023: ij4Var.c(884, "one.me.profileedit.screens.adminpermissions.ProfileAdminPermissionsBuilder");
 1024: ij4Var.c(287, "one.me.features.media.autosave.usecase.AwaitAndSavePhotoToGalleryUseCase");
 1025: ij4Var.c(1008, "com.facebook.imagepipeline.memory.BitmapPool");
 1026: ij4Var.c(1049, "one.me.stories.edit.export.SplitStoryVideoUseCase");
 1027: ij4Var.c(345, "one.me.incrementalupdate.download.MupdFileDownloader");
 1028: ij4Var.c(39, "one.me.statistics.androidperf.memory.MemoryRegistrar");
 1029: ij4Var.c(841, "one.me.videomessage.VideoMessageUtil");
 1030: ij4Var.c(1051, "one.me.chats.list.ChatsListViewModelFactory");
 1031: ij4Var.c(772, "one.me.calls.api.repository.CallChatRepository");
 1032: ij4Var.c(524, "ru.ok.tamtam.VisibilityLogic");
 1033: ij4Var.c(695, "ru.ok.tamtam.events.NotifTranscriptionEvents");
```
Строки 130–155:
```java
  130: ij4Var.c(329, "one.me.stories.core.domain.StoryFilesRenderer");
  131: ij4Var.c(468, "ru.ok.tamtam.android.video.converter.VideoConversionsDao");
  132: ij4Var.c(475, "androidx.work.impl.model.WorkersQueueDao");
  133: ij4Var.c(281, "ru.ok.tamtam.notifications.FileLoadingNotifications");
  134: ij4Var.c(686, "one.me.sdk.chats.UpdateChatAfterMessageSendUseCase");
  135: ij4Var.c(193, "one.me.multiaccount.statistics.MultiaccountStat");
  136: ij4Var.c(480, "one.me.chats.pins.ChatPinsStateDao");
  137: ij4Var.c(685, "ru.ok.tamtam.chats.usecases.SyncChatHistoryOnNotifMessageUseCase");
  138: ij4Var.c(75, "android.app.Application");
  139: ij4Var.c(1107, "one.me.calllist.event.CallHistoryEvents");
  140: ij4Var.c(461, "ru.ok.tamtam.android.calls.CallHistoryDao");
  141: ij4Var.c(4, "one.me.metric.sdk.datasource.EventDataSource");
  142: ij4Var.c(62, "one.me.calls.api.listeners.CallsListenersWrapper");
  143: ij4Var.c(628, "ru.ok.tamtam.android.notifications.messages.newpush.repos.data.FcmChatNotificationsDataRepository");
  144: ij4Var.c(154, "one.me.sdk.media.MediaCacheRepositoryContract");
  145: ij4Var.c(48, "one.me.statistics.androidperf.AndroidPerfDependenciesProvider");
  146: ij4Var.c(849, "ru.ok.tamtam.messages.ForwardAttachMessageUseCase");
  147: ij4Var.c(1083, "ru.ok.tamtam.initialdata.InitialDataMainExecutorWrapper");
  148: ij4Var.c(1186, "one.me.android.initialization.CustomWorkerFactory");
  149: ij4Var.c(279, "one.me.sdk.transfer.HttpFileDownloader");
  150: ij4Var.c(437, "one.me.settings.twofa.creation.TwoFACreationViewModelFactory");
  151: ij4Var.c(309, "one.me.stories.core.repository.StoriesPublishRepository");
  152: ij4Var.c(988, "one.me.pinbars.player.PlayerComposerFactory");
  153: ij4Var.c(1157, "one.me.profile.screens.members.ChatAdminsViewModelFactory");
  154: ij4Var.c(45, "one.me.statistics.androidperf.battery.BatteryRegistrar");
  155: ij4Var.c(476, "ru.ok.tamtam.android.chat.ChatsDao");
```

### defpackage/tdd.java
Строки 1–300:
```java
    1: package defpackage;
    2: 
    3: import java.util.HashMap;
    4: import java.util.Iterator;
    5: 
    6: /* JADX WARN: $VALUES field not found */
    7: /* JADX WARN: Failed to restore enum class, 'enum' modifier and super class removed */
    8: /* JADX INFO: loaded from: classes.dex */
    9: public final class tdd {
   10: public static final tdd A1;
   11: public static final tdd G;
   12: public static final tdd G1;
   13: public static final tdd H;
   14: public static final tdd H3;
   15: public static final tdd I;
   16: public static final tdd I3;
   17: public static final tdd J3;
   18: public static final tdd K3;
   19: public static final tdd L3;
   20: public static final tdd M3;
   21: public static final tdd N3;
   22: public static final tdd O3;
   23: public static final tdd P3;
   24: public static final tdd Q3;
   25: public static final tdd R3;
   26: public static final tdd S3;
   27: public static final tdd T3;
   28: public static final tdd U3;
   29: public static final tdd V3;
   30: public static final tdd W3;
   31: public static final tdd X3;
   32: public static final tdd Y3;
   33: public static final tdd Z;
   34: public static final /* synthetic */ ut6 Z3;
   35: public static final cp5 c;
   36: public static final HashMap d;
   37: public static final HashMap e;
   38: public static final tdd f;
   39: public static final tdd f1;
   40: public static final tdd g;
   41: public static final tdd h;
   42: public static final tdd i;
   43: public static final tdd i1;
   44: public static final tdd j;
   45: public static final tdd j1;
   46: public static final tdd k;
   47: public static final tdd k1;
   48: public static final tdd l;
   49: public static final tdd l1;
   50: public static final tdd m1;
   51: public static final tdd n1;
   52: public static final tdd p1;
   53: public static final tdd r1;
   54: public static final tdd s1;
   55: public static final tdd t1;
   56: public static final tdd u1;
   57: public static final tdd v1;
   58: public static final tdd w1;
   59: public static final tdd y1;
   60: public final short a;
   61: public final f84 b;
   62: public static final tdd m = new tdd("AUTH", 7, 18);
   63: public static final tdd n = new tdd("LOGIN", 8, 19, f0c.f);
   64: public static final tdd o = new tdd("LOGIN2", 9, 8, bwb.f);
   65: public static final tdd p = new tdd("GET_PROMOTED_CONTENT", 10, 9, df7.g);
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
   76: public static final tdd A = new tdd("AUTH_VALIDATE_PASSWORD", 21, 107, fj0.c);
   77: public static final tdd B = new tdd("AUTH_VALIDATE_HINT", 22, 108, fj0.b);
   78: public static final tdd C = new tdd("AUTH_VERIFY_EMAIL", 23, 109, f0c.b);
   79: public static final tdd D = new tdd("AUTH_CHECK_EMAIL", 24, 110, qzd.c);
   80: public static final tdd E = new tdd("AUTH_SET_2FA", 25, 111, fj0.a);
   81: public static final tdd F = new tdd("AUTH_2FA_DETAILS", 26, 104, nt6.c);
   82: public static final tdd J = new tdd("ASSETS_LIST_MODIFY", 30, 261);
   83: public static final tdd X = new tdd("ASSETS_REMOVE", 31, 259);
   84: public static final tdd Y = new tdd("ASSETS_MOVE", 32, 260);
   85: public static final tdd c1 = new tdd("PRESET_AVATARS", 34, 25, tdc.i);
   86: public static final tdd d1 = new tdd("CONTACT_INFO", 35, 32, cg6.d);
   87: public static final tdd e1 = new tdd("CONTACT_INFO_BY_PHONE", 36, 46, cp5.e);
   88: public static final tdd g1 = new tdd("CONTACT_UPDATE", 38, 34);
   89: public static final tdd h1 = new tdd("CONTACT_PRESENCE", 39, 35, bwb.d);
   90: public static final tdd o1 = new tdd("CHAT_INFO", 46, 48);
   91: public static final tdd q1 = new tdd("CHAT_MARK", 48, 50, cg6.c);
   92: public static final tdd x1 = new tdd("CHAT_JOIN", 55, 57, lrh.e);
   93: public static final tdd z1 = new tdd("CHAT_MEMBERS", 57, 59, bwb.c);
   94: public static final tdd B1 = new tdd("CHAT_PERSONAL_CONFIG", 59, 61, f0c.c);
   95: public static final tdd C1 = new tdd("REACTIONS_SETTINGS_GET_BY_CHAT_ID", 60, 258, qzd.d);
   96: public static final tdd D1 = new tdd("CHAT_REACTIONS_SETTINGS_SET", 61, 257, pdc.d);
   97: public static final tdd E1 = new tdd("CHAT_CHECK_ESIA", 62, 307, fj0.d);
   98: public static final tdd F1 = new tdd("ENTITY_ORG_INFO", 63, 308, nt6.b);
   99: public static final tdd H1 = new tdd("MSG_TYPING", 65, 65);
  100: public static final tdd I1 = new tdd("MSG_DELETE", 66, 66);
  101: public static final tdd J1 = new tdd("MSG_EDIT", 67, 67);
  102: public static final tdd K1 = new tdd("GET_COMMENTS_UPDATES", 68, 91, wt0.g);
  103: public static final tdd L1 = new tdd("MSG_DELETE_RANGE", 69, 92);
  104: public static final tdd M1 = new tdd("MSG_REACTION", 70, 178, nt6.i);
  105: public static final tdd N1 = new tdd("MSG_CANCEL_REACTION", 71, 179, tdc.g);
  106: public static final tdd O1 = new tdd("MSG_GET_REACTIONS", 72, 180, wt0.h);
  107: public static final tdd P1 = new tdd("MSG_GET_DETAILED_REACTIONS", 73, 181);
  108: public static final tdd Q1 = new tdd("STORIES_LIST", 74, 208, wt0.k);
  109: public static final tdd R1 = new tdd("STORIES_LIST_BY_OWNER_ID", 75, 209, ih0.k);
  110: public static final tdd S1 = new tdd("STORIES_GET_BY_OWNER_ID", 76, 210, f0c.i);
  111: public static final tdd T1 = new tdd("STORIES_GET_STATS", 77, 211, wdc.j);
  112: public static final tdd U1 = new tdd("STORIES_GET_DETAILED_STATS", 78, 212, tdc.j);
  113: public static final tdd V1 = new tdd("STORIES_REACT", 79, 213, df7.k);
  114: public static final tdd W1 = new tdd("STORIES_MARK", 80, 214, nt6.l);
  115: public static final tdd X1 = new tdd("STORIES_SEND", 81, 215, qzd.i);
  116: public static final tdd Y1 = new tdd("NOTIF_STORIES_UPDATE", 82, 216, wt0.i);
  117: public static final tdd Z1 = new tdd("STORIES_EDIT", 83, 217, bwb.i);
  118: public static final tdd a2 = new tdd("STORIES_DELETE", 84, 218, cg6.j);
  119: public static final tdd b2 = new tdd("STORIES_GET_BY_STORY_ID", 85, 220, pdc.i);
  120: public static final tdd c2 = new tdd("STORIES_HISTORY_GET_BY_OWNER_ID", 86, 219, kwm.j);
  121: public static final tdd d2 = new tdd("GET_PINNED_MESSAGE_STATES", 87, 240, nt6.h);
  122: public static final tdd e2 = new tdd("PINNED_MESSAGES_GET", 88, 241, cg6.i);
  123: public static final tdd f2 = new tdd("PINNED_MESSAGE_UPDATE", 89, 242, cp5.i);
  124: public static final tdd g2 = new tdd("NOTIF_CHAT_MESSAGE_PINNED", 90, 243, f0c.g);
  125: public static final tdd h2 = new tdd("CHAT_SEARCH", 91, 68);
  126: public static final tdd i2 = new tdd("MSG_SHARE_PREVIEW", 92, 70);
  127: public static final tdd j2 = new tdd("MSG_GET", 93, 71, kwm.g);
  128: public static final tdd k2 = new tdd("MSG_SEARCH_TOUCH", 94, 72);
  129: public static final tdd l2 = new tdd("MSG_SEARCH", 95, 73);
  130: public static final tdd m2 = new tdd("MSG_GET_STAT", 96, 74);
  131: public static final tdd n2 = new tdd("CHAT_SUBSCRIBE", 97, 75);
  132: public static final tdd o2 = new tdd("VIDEO_CHAT_START", 98, 76, nt6.d);
  133: public static final tdd p2 = new tdd("VIDEO_CHAT_START_ACTIVE", 99, 78, wt0.l);
  134: public static final tdd q2 = new tdd("VIDEO_CHAT_JOIN", 100, 166, ih0.l);
  135: public static final tdd r2 = new tdd("VIDEO_CHAT_HANGUP", 101, 167, kwm.k);
  136: public static final tdd s2 = new tdd("CHAT_MEMBERS_UPDATE", 102, 77);
  137: public static final tdd t2 = new tdd("VIDEO_CHAT_HISTORY", 103, 79);
  138: public static final tdd u2 = new tdd("PHOTO_UPLOAD", 104, 80, qzd.b);
  139: public static final tdd v2 = new tdd("STICKER_UPLOAD", 105, 81);
  140: public static final tdd w2 = new tdd("VIDEO_UPLOAD", 106, 82, nt6.m);
  141: public static final tdd x2 = new tdd("VIDEO_PLAY", 107, 83);
  142: public static final tdd y2 = new tdd("VIDEO_CHAT_CREATE_JOIN_LINK", 108, 84, wdc.c);
  143: public static final tdd z2 = new tdd("CHAT_PIN_SET_VISIBILITY", 109, 86);
  144: public static final tdd A2 = new tdd("FILE_UPLOAD", 110, 87);
  145: public static final tdd B2 = new tdd("FILE_DOWNLOAD", 111, 88, bwb.e);
  146: public static final tdd C2 = new tdd("LINK_INFO", 112, 89, cp5.g);
  147: public static final tdd D2 = new tdd("SESSIONS_INFO", 113, 96);
  148: public static final tdd E2 = new tdd("SESSIONS_CLOSE", 114, 97);
  149: public static final tdd F2 = new tdd("PHONE_BIND_REQUEST", 115, 98);
  150: public static final tdd G2 = new tdd("PHONE_BIND_CONFIRM", 116, 99);
  151: public static final tdd H2 = new tdd("GET_INBOUND_CALLS", 117, 103);
  152: public static final tdd I2 = new tdd("EXTERNAL_CALLBACK", 118, 105, cp5.f);
  153: public static final tdd J2 = new tdd("PHONE_WEBAPP_SHARE", 119, 106, r74.j);
  154: public static final tdd K2 = new tdd("OK_TOKEN", 120, 158, nt6.j);
  155: public static final tdd L2 = new tdd("CHAT_COMPLAIN", 121, 117);
  156: public static final tdd M2 = new tdd("MSG_SEND_CALLBACK", 122, 118);
  157: public static final tdd N2 = new tdd("SUSPEND_BOT", 123, 119);
  158: public static final tdd O2 = new tdd("LOCATION_STOP", 124, 124);
  159: public static final tdd P2 = new tdd("LOCATION_SEND", 125, 125);
  160: public static final tdd Q2 = new tdd("LOCATION_REQUEST", 126, 126);
  161: public static final tdd R2 = new tdd("GET_LAST_MENTIONS", 127, 127);
  162: public static final tdd S2 = new tdd("STICKER_CREATE", 128, 193);
  163: public static final tdd T2 = new tdd("STICKER_SUGGEST", 129, 194);
  164: public static final tdd U2 = new tdd("VIDEO_CHAT_MEMBERS", 130, 195);
  165: public static final tdd V2 = new tdd("NOTIF_MESSAGE", 131, 128, lgc.a);
  166: public static final tdd W2 = new tdd("NOTIF_TYPING", 132, 129);
  167: public static final tdd X2 = new tdd("NOTIF_MARK", 133, 130, tdc.h);
  168: public static final tdd Y2 = new tdd("NOTIF_CONTACT", 134, 131);
  169: public static final tdd Z2 = new tdd("NOTIF_PRESENCE", 135, 132);
  170: public static final tdd a3 = new tdd("NOTIF_CONFIG", 136, 134);
  171: public static final tdd b3 = new tdd("NOTIF_CHAT", 137, 135);
  172: public static final tdd c3 = new tdd("NOTIF_ATTACH", 138, 136, cp5.h);
  173: public static final tdd d3 = new tdd("NOTIF_CALL_START", 139, 137);
  174: public static final tdd e3 = new tdd("NOTIF_CONTACT_SORT", 140, 139);
  175: public static final tdd f3 = new tdd("NOTIF_MSG_DELETE_RANGE", 141, 140);
  176: public static final tdd g3 = new tdd("NOTIF_MSG_DELETE", 142, 142, kwm.h);
  177: public static final tdd h3 = new tdd("NOTIF_MSG_REACTIONS_CHANGED", 143, 155);
  178: public static final tdd i3 = new tdd("NOTIF_MSG_YOU_REACTED", 144, 156);
  179: public static final tdd j3 = new tdd("NOTIF_CALLBACK_ANSWER", 145, 143);
  180: public static final tdd k3 = new tdd("CHAT_BOT_COMMANDS", 146, 144);
  181: public static final tdd l3 = new tdd("BOT_INFO", 147, 145, tdc.c);
  182: public static final tdd m3 = new tdd("NOTIF_LOCATION", 148, 147);
  183: public static final tdd n3 = new tdd("NOTIF_LOCATION_REQUEST", 149, 148);
  184: public static final tdd o3 = new tdd("NOTIF_ASSETS_UPDATE", 150, 150);
  185: public static final tdd p3 = new tdd("CHAT_HIDE", 151, 196);
  186: public static final tdd q3 = new tdd("CHAT_SEARCH_COMMON_PARTICIPANTS", 152, 198);
  187: public static final tdd r3 = new tdd("NOTIF_MSG_DELAYED", 153, 154, wdc.h);
  188: public static final tdd s3 = new tdd("NOTIF_PROFILE", 154, 159, ih0.i);
  189: public static final tdd t3 = new tdd("PROFILE_DELETE", 155, 199, wdc.i);
  190: public static final tdd u3 = new tdd("PROFILE_DELETE_TIME", 156, 200, kwm.i);
  191: public static final tdd v3 = new tdd("WEB_APP_INIT_DATA", 157, 160, qzd.j);
  192: public static final tdd w3 = new tdd("COMPLAIN", 158, 161, wdc.d);
  193: public static final tdd x3 = new tdd("COMPLAIN_REASONS_GET", 159, 162, kwm.c);
  194: public static final tdd y3 = new tdd("CALL_HISTORY", 160, 163, ih0.d);
  195: public static final tdd z3 = new tdd("CALL_HISTORY_CLEAR", 161, 164, kwm.b);
  196: public static final tdd A3 = new tdd("NOTIF_CALL_HISTORY", 162, 165, bwb.g);
  197: public static final tdd B3 = new tdd("FOLDERS_GET", 163, 272, tdc.f);
  198: public static final tdd C3 = new tdd("FOLDERS_GET_BY_ID", 164, 273, pdc.e);
  199: public static final tdd D3 = new tdd("FOLDERS_UPDATE", 165, 274, kwm.f);
  200: public static final tdd E3 = new tdd("FOLDERS_REORDER", 166, 275, wdc.f);
  201: public static final tdd F3 = new tdd("FOLDERS_DELETE", 167, 276, f0c.e);
  202: public static final tdd G3 = new tdd("NOTIF_FOLDERS", 168, 277, pdc.g);
  203: 
  204: static {
  205: short s4 = 1;
  206: f = new tdd("PING", 0, s4);
  207: short s5 = 2;
  208: g = new tdd("DEBUG", s4, s5);
  209: short s6 = 3;
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
  220: H = new tdd("ASSETS_UPDATE", s10, s9);
  221: short s11 = 29;
  222: I = new tdd("ASSETS_GET_BY_IDS", s11, s10);
  223: short s12 = 33;
  224: Z = new tdd("ASSETS_ADD", s12, s11);
  225: short s13 = 37;
  226: f1 = new tdd("CONTACT_ADD", s13, s12);
  227: short s14 = 40;
  228: i1 = new tdd("CONTACT_LIST", s14, (short) 36);
  229: j1 = new tdd("CONTACT_SEARCH", 41, s13);
  230: short s15 = 42;
  231: k1 = new tdd("CONTACT_PHOTOS", s15, (short) 39);
  232: short s16 = 43;
  233: l1 = new tdd("CONTACT_SORT", s16, s14);
  234: m1 = new tdd("CONTACT_VERIFY", 44, s15);
  235: n1 = new tdd("REMOVE_CONTACT_PHOTO", 45, s16);
  236: short s17 = 49;
  237: p1 = new tdd("CHAT_HISTORY", 47, s17);
  238: short s18 = 51;
  239: r1 = new tdd("CHAT_MEDIA", s17, s18);
  240: short s19 = 52;
  241: s1 = new tdd("CHAT_DELETE", 50, s19);
  242: short s20 = 53;
  243: t1 = new tdd("CHATS_LIST", s18, s20);
  244: short s21 = 54;
  245: u1 = new tdd("CHAT_CLEAR", s19, s21);
  246: v1 = new tdd("CHAT_UPDATE", s20, (short) 55);
  247: short s22 = 56;
  248: w1 = new tdd("CHAT_CHECK_LINK", s21, s22);
  249: short s23 = 58;
  250: y1 = new tdd("CHAT_LEAVE", s22, s23);
  251: A1 = new tdd("PUBLIC_SEARCH", s23, (short) 60);
  252: short s24 = 64;
  253: G1 = new tdd("MSG_SEND", s24, s24);
  254: cg6 cg6Var = cg6.h;
  255: H3 = new tdd("AUTH_QR_APPROVE", 169, (short) 290, cg6Var);
  256: I3 = new tdd("NOTIF_BANNERS", 170, (short) 292, cg6Var);
  257: J3 = new tdd("AUTH_BY_TRACK", 171, (short) 291, df7.c);
  258: K3 = new tdd("AUTH_CHECK_CALL", 172, (short) 294, ih0.b);
  259: L3 = new tdd("BANNERS_GET", 173, (short) 302, wt0.b);
  260: M3 = new tdd("CHAT_SUGGEST", 174, (short) 300, tdc.d);
  261: N3 = new tdd("AUDIO_PLAY", 175, (short) 301, wt0.c);
  262: O3 = new tdd("MSG_DELIVERY", 176, (short) 303, fj0.e);
  263: P3 = new tdd("SEND_VOTE", 177, (short) 304, f0c.h);
  264: Q3 = new tdd("VOTERS_LIST_BY_ANSWER", 178, (short) 305, pdc.h);
  265: R3 = new tdd("GET_POLL_UPDATES", 179, (short) 306, ih0.h);
  266: S3 = new tdd("TRANSCRIBE_MEDIA", 180, (short) 202, rqj.a);
  267: T3 = new tdd("NOTIF_TRANSCRIPTION", 181, (short) 293, ehc.a);
  268: U3 = new tdd("ORG_INFO", 182, (short) 256, lrh.j);
  269: V3 = new tdd("CHAT_LIVESTREAM_INFO", 183, (short) 62, cp5.d);
  270: W3 = new tdd("PHOTO_URL_REFRESH", 184, (short) 203, r74.g);
  271: X3 = new tdd("MSG_DELETE_USER", 185, (short) 94, wdc.g);
  272: Y3 = new tdd("CHAT_LINKS_LIST", 186, (short) 221, r74.c);
  273: ut6 ut6VarH0 = lkh.h0(new tdd[]{f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, X, Y, Z, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, q1, r1, s1, t1, u1, v1, w1, x1, y1, z1, A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, L1, M1, N1, O1, P1, Q1, R1, S1, T1, U1, V1, W1, X1, Y1, Z1, a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2, l2, m2, n2, o2, p2, q2
  274: Z3 = ut6VarH0;
  275: c = new cp5((byte) 16);
  276: d = new HashMap();
  277: e = new HashMap();
  278: Iterator it = ut6VarH0.iterator();
  279: while (true) {
  280: j2 j2Var = (j2) it;
  281: if (!j2Var.hasNext()) {
  282: return;
  283: }
  284: tdd tddVar = (tdd) j2Var.next();
  285: d.put(Short.valueOf(tddVar.a), tddVar.name());
  286: HashMap map = e;
  287: Short shValueOf = Short.valueOf(tddVar.a);
  288: String strName = tddVar.name();
  289: cp5 cp5Var = c;
  290: short s25 = tddVar.a;
  291: cp5Var.getClass();
  292: map.put(shValueOf, strName + "(0x" + Integer.toHexString(s25 & 65535) + ")");
  293: }
  294: }
  295: 
  296: public tdd(String str, int i4, short s4, f84 f84Var) {
  297: super(str, i4);
  298: this.a = s4;
  299: this.b = f84Var;
  300: }
```

### defpackage/ej0.java
Строки 1–18:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class ej0 {
    5: public final rp9 a;
    6: public final rp9 b;
    7: public final rp9 c;
    8: 
    9: public ej0(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3) {
   10: this.a = rp9Var;
   11: this.b = rp9Var2;
   12: this.c = rp9Var3;
   13: }
   14: 
   15: public final Object a(String str, int i, x1j x1jVar) {
   16: return hzj.R(new u3(new xeg(new cj0((Object) this, str, i, (b55) null, (byte) 0)), new dj0(4, null), (byte) 15), x1jVar);
   17: }
   18: }
```

### defpackage/cj0.java
Строки 1–385:
```java
    1: package defpackage;
    2: 
    3: import android.graphics.Bitmap;
    4: import android.graphics.BitmapFactory;
    5: import android.webkit.PermissionRequest;
    6: import java.io.File;
    7: import java.util.List;
    8: import java.util.ListIterator;
    9: import java.util.concurrent.CancellationException;
   10: import one.me.search.usecase.InvalidSearchResultMarkerException;
   11: import ru.ok.tamtam.errors.TamErrorException;
   12: import ru.oneme.app.R;
   13: 
   14: /* JADX INFO: loaded from: classes3.dex */
   15: public final class cj0 extends x1j implements e18 {
   16: public final /* synthetic */ byte e;
   17: public Object f;
   18: public int g;
   19: public byte h;
   20: public Object i;
   21: public Object j;
   22: public final /* synthetic */ Object k;
   23: 
   24: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   25: public cj0(String str, aqg aqgVar, int i, Long l, b55 b55Var) {
   26: super(2, b55Var);
   27: this.e = (byte) 5;
   28: this.k = str;
   29: this.i = aqgVar;
   30: this.g = i;
   31: this.j = l;
   32: }
   33: 
   34: /* JADX WARN: Failed to calculate best type for var: r7v6 ??
   35: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r7v6 ??, new type: boolean
   36: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
   37: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
   38: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
   39: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
   40: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
   41: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
   42: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
   43: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
   44: Caused by: java.lang.NullPointerException
   45: */
   46: /*  JADX ERROR: Types fix failed
   47: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r7v4 ??, new type: boolean
   48: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
   49: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
   50: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryPossibleTypes(FixTypesVisitor.java:186)
   51: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:245)
   52: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
   53: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
   54: Caused by: java.lang.NullPointerException
   55: */
   56: private final java.lang.Object y(java.lang.Object r61) {
   57: /*
   58: Method dump skipped, instruction units count: 1167
   59: To view this dump add '--comments-level debug' option
   60: */
   61: throw new UnsupportedOperationException("Method not decompiled: defpackage.cj0.y(java.lang.Object):java.lang.Object");
   62: }
   63: 
   64: @Override // defpackage.e18
   65: public final Object invoke(Object obj, Object obj2) {
   66: byte b = this.e;
   67: s1k s1kVar = s1k.a;
   68: switch (b) {
   69: case 0:
   70: return ((cj0) u((b55) obj2, (ri7) obj)).w(s1kVar);
   71: case 1:
   72: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   73: case 2:
   74: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   75: case 3:
   76: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   77: case 4:
   78: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   79: case 5:
   80: return ((cj0) u((b55) obj2, (ri7) obj)).w(s1kVar);
   81: case 6:
   82: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   83: default:
   84: return ((cj0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   85: }
   86: }
   87: 
   88: @Override // defpackage.hv0
   89: public final b55 u(b55 b55Var, Object obj) {
   90: byte b = this.e;
   91: Object obj2 = this.k;
   92: switch (b) {
   93: case 0:
   94: cj0 cj0Var = new cj0(this.j, (String) obj2, this.g, b55Var, (byte) 0);
   95: cj0Var.f = obj;
   96: return cj0Var;
   97: case 1:
   98: cj0 cj0Var2 = new cj0((kz2) this.j, (p73) obj2, b55Var, (byte) 1);
   99: cj0Var2.i = obj;
  100: return cj0Var2;
  101: case 2:
  102: return new cj0((jo6) this.j, (on6) obj2, b55Var, (byte) 2);
  103: case 3:
  104: cj0 cj0Var3 = new cj0((fq7) this.j, (pm7) obj2, b55Var, (byte) 3);
  105: cj0Var3.i = obj;
  106: return cj0Var3;
  107: case 4:
  108: cj0 cj0Var4 = new cj0(this.j, (String) obj2, this.g, b55Var, (byte) 4);
  109: cj0Var4.i = obj;
  110: return cj0Var4;
  111: case 5:
  112: cj0 cj0Var5 = new cj0((String) obj2, (aqg) this.i, this.g, (Long) this.j, b55Var);
  113: cj0Var5.f = obj;
  114: return cj0Var5;
  115: case 6:
  116: return new cj0((xdh) obj2, b55Var);
  117: default:
  118: cj0 cj0Var6 = new cj0((PermissionRequest) this.j, (ekl) obj2, b55Var, (byte) 7);
  119: cj0Var6.f = obj;
  120: return cj0Var6;
  121: }
  122: }
  123: 
  124: /* JADX WARN: Code duplicated, block: B:100:0x020f  */
  125: /* JADX WARN: Code duplicated, block: B:182:0x03ed  */
  126: /* JADX WARN: Code duplicated, block: B:253:0x055b A[PHI: r0 r15
  127: 0x055b: PHI (r0v61 int) = (r0v49 int), (r0v76 int) binds: [B:245:0x0525, B:250:0x0556] A[DONT_GENERATE, DONT_INLINE]
  128: 0x055b: PHI (r15v1 java.io.File) = (r15v0 java.io.File), (r15v3 java.io.File) binds: [B:245:0x0525, B:250:0x0556] A[DONT_GENERATE, DONT_INLINE]] */
  129: /* JADX WARN: Code duplicated, block: B:256:0x0560  */
  130: /* JADX WARN: Code duplicated, block: B:262:0x0593  */
  131: /* JADX WARN: Code duplicated, block: B:264:0x05a1  */
  132: /* JADX WARN: Code duplicated, block: B:272:0x05c7 A[Catch: all -> 0x05cc, TryCatch #8 {all -> 0x05cc, blocks: (B:270:0x05c1, B:272:0x05c7, B:275:0x05ce), top: B:368:0x05c1 }] */
  133: /* JADX WARN: Code duplicated, block: B:280:0x05df  */
  134: /* JADX WARN: Code duplicated, block: B:282:0x05e3  */
  135: /* JADX WARN: Code duplicated, block: B:285:0x05fe  */
  136: /* JADX WARN: Code duplicated, block: B:36:0x00bd A[Catch: all -> 0x00e2, TryCatch #2 {all -> 0x00e2, blocks: (B:34:0x00b3, B:36:0x00bd, B:38:0x00c1, B:41:0x00c8, B:43:0x00d0, B:46:0x00e4, B:47:0x00e5, B:50:0x00ec, B:33:0x00ad, B:18:0x0048), top: B:358:0x0019 }] */
  137: /* JADX WARN: Code duplicated, block: B:38:0x00c1 A[Catch: all -> 0x00e2, TryCatch #2 {all -> 0x00e2, blocks: (B:34:0x00b3, B:36:0x00bd, B:38:0x00c1, B:41:0x00c8, B:43:0x00d0, B:46:0x00e4, B:47:0x00e5, B:50:0x00ec, B:33:0x00ad, B:18:0x0048), top: B:358:0x0019 }] */
  138: /* JADX WARN: Code duplicated, block: B:40:0x00c7  */
  139: /* JADX WARN: Code duplicated, block: B:41:0x00c8 A[Catch: all -> 0x00e2, TryCatch #2 {all -> 0x00e2, blocks: (B:34:0x00b3, B:36:0x00bd, B:38:0x00c1, B:41:0x00c8, B:43:0x00d0, B:46:0x00e4, B:47:0x00e5, B:50:0x00ec, B:33:0x00ad, B:18:0x0048), top: B:358:0x0019 }] */
  140: /* JADX WARN: Code duplicated, block: B:43:0x00d0 A[Catch: all -> 0x00e2, TryCatch #2 {all -> 0x00e2, blocks: (B:34:0x00b3, B:36:0x00bd, B:38:0x00c1, B:41:0x00c8, B:43:0x00d0, B:46:0x00e4, B:47:0x00e5, B:50:0x00ec, B:33:0x00ad, B:18:0x0048), top: B:358:0x0019 }] */
  141: /* JADX WARN: Code duplicated, block: B:46:0x00e4 A[Catch: all -> 0x00e2, TryCatch #2 {all -> 0x00e2, blocks: (B:34:0x00b3, B:36:0x00bd, B:38:0x00c1, B:41:0x00c8, B:43:0x00d0, B:46:0x00e4, B:47:0x00e5, B:50:0x00ec, B:33:0x00ad, B:18:0x0048), top: B:358:0x0019 }] */
  142: /* JADX WARN: Code duplicated, block: B:49:0x00eb  */
  143: /* JADX WARN: Code duplicated, block: B:53:0x00f8 A[Catch: all -> 0x0100, TRY_ENTER, TryCatch #1 {all -> 0x0100, blocks: (B:53:0x00f8, B:56:0x0103), top: B:356:0x00f6 }] */
  144: /* JADX WARN: Code duplicated, block: B:56:0x0103 A[Catch: all -> 0x0100, TRY_LEAVE, TryCatch #1 {all -> 0x0100, blocks: (B:53:0x00f8, B:56:0x0103), top: B:356:0x00f6 }] */
  145: /* JADX WARN: Code restructure failed: missing block: B:102:0x0223, code lost:
  146: 
  147: if (r11.b(r5, r33) == r12) goto L106;
  148: */
  149: /* JADX WARN: Code restructure failed: missing block: B:105:0x0235, code lost:
  150: 
  151: if (r11.b(r2, r33) == r12) goto L106;
  152: */
  153: /* JADX WARN: Code restructure failed: missing block: B:124:0x0288, code lost:
  154: 
  155: if (r0 == r4) goto L156;
  156: */
  157: /* JADX WARN: Code restructure failed: missing block: B:155:0x0325, code lost:
  158: 
  159: if (r0 == r4) goto L156;
  160: */
  161: /* JADX WARN: Code restructure failed: missing block: B:183:0x03ee, code lost:
  162: 
  163: if (r0 == r5) goto L192;
  164: */
  165: /* JADX WARN: Code restructure failed: missing block: B:191:0x041c, code lost:
  166: 
  167: if (defpackage.nm9.i0(((defpackage.vxc) r4.d).c(), new defpackage.eq7(r4, r13, 1), r33) == r5) goto L192;
  168: */
  169: /* JADX WARN: Code restructure failed: missing block: B:247:0x054c, code lost:
  170: 
  171: if (r4 == r3) goto L284;
  172: */
  173: /* JADX WARN: Code restructure failed: missing block: B:315:0x0678, code lost:
  174: 
  175: if (r7.E((defpackage.ys3) r0, r33) == r4) goto L325;
  176: */
  177: /* JADX WARN: Code restructure failed: missing block: B:324:0x0699, code lost:
  178: 
  179: if (r3.F(r0, r33) == r4) goto L325;
  180: */
  181: /* JADX WARN: Code restructure failed: missing block: B:349:0x073a, code lost:
  182: 
  183: if (r0.b(r2, r33) == r3) goto L350;
  184: */
  185: /* JADX WARN: Code restructure failed: missing block: B:383:?, code lost:
  186: 
  187: return r4;
  188: */
  189: /* JADX WARN: Code restructure failed: missing block: B:385:?, code lost:
  190: 
  191: return r5;
  192: */
  193: /* JADX WARN: Instruction removed from duplicated block: B:43:0x00d0, please report this as an issue */
  194: @Override // defpackage.hv0
  195: /*
  196: Code decompiled incorrectly, please refer to instructions dump.
  197: */
  198: public final Object w(Object obj) throws Throwable {
  199: Object objB;
  200: Object n4gVar;
  201: Object objE0;
  202: kz2 kz2Var;
  203: int i;
  204: File file;
  205: Object n4gVar2;
  206: int i2;
  207: Object objI0;
  208: boolean z;
  209: Bitmap bitmapDecodeFile;
  210: jo6 jo6Var;
  211: j41 j41Var;
  212: int i3;
  213: String str;
  214: on6 on6Var;
  215: o1d o1dVar;
  216: Object n4gVar3;
  217: Boolean bool;
  218: boolean z2;
  219: Object obj2;
  220: String str2;
  221: on6 on6Var2;
  222: o1d o1dVar2;
  223: b55 b55Var;
  224: Object n4gVar4;
  225: Object objI1;
  226: Object n4gVar5;
  227: Object objI2;
  228: rdj qdjVar;
  229: long j;
  230: Object objG0;
  231: z8f z8fVar;
  232: String str3;
  233: int i4;
  234: Long l;
  235: o1d o1dVar3;
  236: Long l2;
  237: Long l3;
  238: int i5;
  239: Object objI3;
  240: Object n4gVar6;
  241: ekl eklVar;
  242: Throwable thA;
  243: Boolean bool2;
  244: boolean zBooleanValue;
  245: PermissionRequest permissionRequest;
  246: String str4;
  247: o1d o1dVar4;
  248: c6a c6aVar;
  249: int iNextIndex = -1;
  250: z = false;
  251: boolean z3 = false;
  252: int i6 = 0;
  253: byte b = 1;
  254: b55 b55Var2 = null;
  255: switch (this.e) {
  256: case 0:
  257: ri7 ri7Var = (ri7) this.f;
  258: ka5 ka5Var = ka5.a;
  259: byte b2 = this.h;
  260: if (b2 != 0) {
  261: if (b2 == 1) {
  262: ri7Var = (ri7) this.i;
  263: xnm.y(obj);
  264: objB = obj;
  265: } else {
  266: if (b2 != 2) {
  267: k3g.o("call to 'resume' before 'invoke' with coroutine");
  268: return null;
  269: }
  270: xnm.y(obj);
  271: }
  272: return s1k.a;
  273: }
  274: xnm.y(obj);
  275: ej0 ej0Var = (ej0) this.j;
  276: String str5 = (String) this.k;
  277: int i7 = this.g;
  278: this.f = null;
  279: this.i = ri7Var;
  280: this.h = (byte) 1;
  281: bcc bccVar = (bcc) ((z6j) ej0Var.b.getValue()).i.get();
  282: iNextIndex = bccVar != null ? bccVar.l.get() : -1;
  283: v99 v99Var = (v99) ej0Var.c.getValue();
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
  294: this.h = (byte) 2;
  295: break;
  296: case 1:
  297: s1k s1kVar = s1k.a;
  298: kz2 kz2Var2 = (kz2) this.j;
  299: ka5 ka5Var2 = ka5.a;
  300: byte b3 = this.h;
  301: try {
  302: if (b3 == 0) {
  303: xnm.y(obj);
  304: p73 p73Var = (p73) this.k;
  305: zsc zscVarB = kz2Var2.b();
  306: String str6 = kz2Var2.g;
  307: a2h a2hVar = kz2Var2.a;
  308: if (a2hVar == null) {
  309: a2hVar = null;
  310: }
  311: yw6 yw6Var = (yw6) a2hVar.p.getValue();
  312: this.i = null;
  313: this.f = kz2Var2;
  314: this.g = 0;
  315: this.h = (byte) 1;
  316: objE0 = hzj.e0(zscVarB, p73Var, str6, yw6Var, this);
  317: if (objE0 != ka5Var2) {
  318: kz2Var = kz2Var2;
  319: i = 0;
  320: }
  321: return ka5Var2;
  322: }
  323: if (b3 != 1) {
  324: if (b3 == 2) {
  325: xnm.y(obj);
  326: n4gVar = s1kVar;
  327: Throwable thA2 = p4g.a(n4gVar);
  328: if (thA2 != null) {
  329: if (thA2 instanceof CancellationException) {
  330: throw thA2;
  331: }
  332: this.i = null;
  333: this.f = n4gVar;
  334: this.g = 0;
  335: this.h = (byte) 3;
  336: }
  337: } else {
  338: if (b3 != 3) {
  339: k3g.o("call to 'resume' before 'invoke' with coroutine");
  340: return null;
  341: }
  342: xnm.y(obj);
  343: }
  344: break;
  345: } else {
  346: int i8 = this.g;
  347: kz2 kz2Var3 = (kz2) this.f;
  348: xnm.y(obj);
  349: kz2Var = kz2Var3;
  350: i = i8;
  351: objE0 = obj;
  352: }
  353: return s1kVar;
  354: this.i = null;
  355: this.f = null;
  356: this.g = i;
  357: this.h = (byte) 2;
  358: } catch (Throwable th) {
  359: n4gVar = new n4g(th);
  360: }
  361: break;
  362: case 2:
  363: c6a c6aVar2 = c6a.f;
  364: ka5 ka5Var3 = ka5.a;
  365: byte b4 = this.h;
  366: if (b4 == 0) {
  367: xnm.y(obj);
  368: dp6 dp6Var = (dp6) ((jo6) this.j).h.get();
  369: jo6 jo6Var2 = (jo6) this.j;
  370: if (dp6Var == null) {
  371: String str7 = jo6Var2.e;
  372: on6 on6Var3 = (on6) this.k;
  373: o1d o1dVar5 = f09.g;
  374: if (o1dVar5 == null \|\| !o1dVar5.b(c6aVar2)) {
  375: return null;
  376: }
  377: o1dVar5.c(c6aVar2, str7, "Can't start extracting sprite by location:" + on6Var3 + " because config is null", null);
  378: return null;
  379: }
  380: Bitmap bitmap = (Bitmap) jo6Var2.a.b.c(new Integer(((on6) this.k).a));
  381: if (bitmap != null && !bitmap.isRecycled()) {
  382: return bitmap;
  383: }
  384: String str8 = dp6Var.b;
  385: if (str8 == null \|\| zti.n0(str8)) {
```

### defpackage/aj0.java
Строки 1–35:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: public final class aj0 extends u6j {
    5: public final int c;
    6: 
    7: public aj0(int i, int i2, String str, byte[] bArr) {
    8: String str2;
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
   19: }
   20: h("type", str2);
   21: if (bArr != null) {
   22: this.a.put("mode", bArr);
   23: }
   24: }
   25: 
   26: @Override // defpackage.u6j
   27: public final boolean o() {
   28: return false;
   29: }
   30: 
   31: @Override // defpackage.u6j
   32: public final int p() {
   33: return this.c;
   34: }
   35: }
```

### defpackage/ctc.java
Строки 1–16:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes.dex */
    4: public final class ctc {
    5: public final rp9 a;
    6: public final rp9 b;
    7: 
    8: public ctc(rp9 rp9Var, rp9 rp9Var2) {
    9: this.a = rp9Var;
   10: this.b = rp9Var2;
   11: }
   12: 
   13: public final f7j a() {
   14: return (f7j) this.a.getValue();
   15: }
   16: }
```

### defpackage/v99.java
Строки 1–33:
```java
    1: package defpackage;
    2: 
    3: import android.content.Context;
    4: import java.nio.ByteBuffer;
    5: import one.me.callssdk.CallsSdkInitializer;
    6: 
    7: /* JADX INFO: loaded from: classes.dex */
    8: public final class v99 {
    9: public final Context a;
   10: public final h16 b;
   11: public final sn4 c;
   12: public final z3j d = new z3j(new o2(this, (byte) 27));
   13: 
   14: public v99(Context context, h16 h16Var, sn4 sn4Var) {
   15: this.a = context;
   16: this.b = h16Var;
   17: this.c = sn4Var;
   18: }
   19: 
   20: public final byte[] a(Long l) {
   21: byte[] bArr = (byte[]) this.d.getValue();
   22: if (bArr != null) {
   23: return bArr;
   24: }
   25: if (l == null) {
   26: return null;
   27: }
   28: long jLongValue = l.longValue();
   29: ByteBuffer byteBufferAllocate = ByteBuffer.allocate(8);
   30: byteBufferAllocate.putLong(jLongValue);
   31: return CallsSdkInitializer.INSTANCE.initializeSessionSeed(this.a, byteBufferAllocate.array(), this.b.a().getBytes(o53.a));
   32: }
   33: }
```

### defpackage/beb.java
Строки 1–250:
```java
    1: package defpackage;
    2: 
    3: import java.io.Closeable;
    4: import java.io.IOException;
    5: import java.math.BigInteger;
    6: import java.nio.ByteBuffer;
    7: import java.nio.CharBuffer;
    8: import java.nio.charset.CharacterCodingException;
    9: import java.nio.charset.CharsetDecoder;
   10: import java.nio.charset.CoderResult;
   11: import java.nio.charset.CodingErrorAction;
   12: import me.leolin.shortcutbadger.BuildConfig;
   13: import org.msgpack.core.MessageFormatException;
   14: import org.msgpack.core.MessageInsufficientBufferException;
   15: import org.msgpack.core.MessageIntegerOverflowException;
   16: import org.msgpack.core.MessageNeverUsedFormatException;
   17: import org.msgpack.core.MessagePackException;
   18: import org.msgpack.core.MessageSizeException;
   19: import org.msgpack.core.MessageStringCodingException;
   20: import org.msgpack.core.MessageTypeException;
   21: import org.msgpack.core.buffer.ArrayBufferInput;
   22: import org.msgpack.core.buffer.MessageBuffer;
   23: import org.webrtc.PeerConnectionFactory;
   24: 
   25: /* JADX INFO: loaded from: classes.dex */
   26: public final class beb implements Closeable {
   27: public static final MessageBuffer m = MessageBuffer.wrap(new byte[0]);
   28: public final CodingErrorAction a;
   29: public final CodingErrorAction b;
   30: public final int c;
   31: public final short d;
   32: public final ArrayBufferInput e;
   33: public int g;
   34: public int i;
   35: public StringBuilder j;
   36: public CharsetDecoder k;
   37: public CharBuffer l;
   38: public MessageBuffer f = m;
   39: public final MessageBuffer h = MessageBuffer.allocate(8);
   40: 
   41: public beb(ArrayBufferInput arrayBufferInput, qcb qcbVar) {
   42: this.e = arrayBufferInput;
   43: this.a = qcbVar.a;
   44: this.b = qcbVar.b;
   45: this.c = qcbVar.c;
   46: this.d = qcbVar.e;
   47: }
   48: 
   49: public static MessagePackException R(byte b, String str) {
   50: qab qabVar = qab.Y[b & 255];
   51: if (qabVar == qab.g) {
   52: return new MessageNeverUsedFormatException(vg9.y("Expected ", str, ", but encountered 0xC1 \"NEVER_USED\" byte"));
   53: }
   54: String strL = ihk.l(qabVar.a());
   55: return new MessageTypeException(String.format("Expected %s, but got %s (%02x)", str, strL.substring(0, 1) + strL.substring(1).toLowerCase(), Byte.valueOf(b)));
   56: }
   57: 
   58: public static MessageIntegerOverflowException w(int i) {
   59: return new MessageIntegerOverflowException(BigInteger.valueOf(((long) (i & Integer.MAX_VALUE)) + 2147483648L));
   60: }
   61: 
   62: public static MessageIntegerOverflowException y(long j) {
   63: return new MessageIntegerOverflowException(BigInteger.valueOf(j - Long.MIN_VALUE).setBit(63));
   64: }
   65: 
   66: public final long A0() {
   67: byte b = readByte();
   68: if (usc.y(b)) {
   69: return b;
   70: }
   71: switch (b) {
   72: case -52:
   73: return readByte() & 255;
   74: case -51:
   75: return readShort() & 65535;
   76: case -50:
   77: int i = readInt();
   78: return i < 0 ? ((long) (i & Integer.MAX_VALUE)) + 2147483648L : i;
   79: case -49:
   80: long j = readLong();
   81: if (j >= 0) {
   82: return j;
   83: }
   84: throw y(j);
   85: case -48:
   86: return readByte();
   87: case -47:
   88: return readShort();
   89: case -46:
   90: return readInt();
   91: case -45:
   92: return readLong();
   93: default:
   94: throw R(b, "Integer");
   95: }
   96: }
   97: 
   98: public final MessageBuffer D(int i) throws IOException {
   99: int size = this.f.size();
  100: int i2 = this.g;
  101: int i3 = size - i2;
  102: if (i3 >= i) {
  103: this.i = i2;
  104: this.g = i2 + i;
  105: return this.f;
  106: }
  107: MessageBuffer messageBuffer = this.h;
  108: if (i3 > 0) {
  109: messageBuffer.putMessageBuffer(0, this.f, i2, i3);
  110: i -= i3;
  111: } else {
  112: i3 = 0;
  113: }
  114: while (true) {
  115: u();
  116: int size2 = this.f.size();
  117: MessageBuffer messageBuffer2 = this.f;
  118: if (size2 >= i) {
  119: messageBuffer.putMessageBuffer(i3, messageBuffer2, 0, i);
  120: this.g = i;
  121: this.i = 0;
  122: return messageBuffer;
  123: }
  124: messageBuffer.putMessageBuffer(i3, messageBuffer2, 0, size2);
  125: i -= size2;
  126: i3 += size2;
  127: }
  128: }
  129: 
  130: public final int E() {
  131: return readShort() & 65535;
  132: }
  133: 
  134: public final int F0() {
  135: byte b = readByte();
  136: if ((b & (-16)) == -128) {
  137: return b & 15;
  138: }
  139: if (b == -34) {
  140: return E();
  141: }
  142: if (b == -33) {
  143: return I();
  144: }
  145: throw R(b, "Map");
  146: }
  147: 
  148: public final int I() {
  149: int i = readInt();
  150: if (i >= 0) {
  151: return i;
  152: }
  153: throw new MessageSizeException();
  154: }
  155: 
  156: public final int J0() {
  157: int iE;
  158: byte b = readByte();
  159: if ((b & (-32)) == -96) {
  160: return b & 31;
  161: }
  162: int iE2 = -1;
  163: switch (b) {
  164: case -39:
  165: iE = readByte() & 255;
  166: break;
  167: case -38:
  168: iE = E();
  169: break;
  170: case -37:
  171: iE = I();
  172: break;
  173: default:
  174: iE = -1;
  175: break;
  176: }
  177: if (iE >= 0) {
  178: return iE;
  179: }
  180: switch (b) {
  181: case -60:
  182: iE2 = readByte() & 255;
  183: break;
  184: case -59:
  185: iE2 = E();
  186: break;
  187: case -58:
  188: iE2 = I();
  189: break;
  190: }
  191: if (iE2 >= 0) {
  192: return iE2;
  193: }
  194: throw R(b, "String");
  195: }
  196: 
  197: public final String K0() {
  198: int iRemaining;
  199: MessageBuffer messageBuffer;
  200: int iJ0 = J0();
  201: if (iJ0 == 0) {
  202: return BuildConfig.FLAVOR;
  203: }
  204: int i = this.c;
  205: if (iJ0 > i) {
  206: throw new MessageSizeException(String.format("cannot unpack a String of size larger than %,d: %,d", Integer.valueOf(i), Integer.valueOf(iJ0)));
  207: }
  208: CharsetDecoder charsetDecoder = this.k;
  209: if (charsetDecoder == null) {
  210: this.l = CharBuffer.allocate(this.d);
  211: this.k = rcb.a.newDecoder().onMalformedInput(this.a).onUnmappableCharacter(this.b);
  212: } else {
  213: charsetDecoder.reset();
  214: }
  215: StringBuilder sb = this.j;
  216: if (sb == null) {
  217: this.j = new StringBuilder();
  218: } else {
  219: sb.setLength(0);
  220: }
  221: if (this.f.size() - this.g >= iJ0) {
  222: return a(iJ0);
  223: }
  224: while (iJ0 > 0) {
  225: try {
  226: int size = this.f.size();
  227: int i2 = this.g;
  228: int i3 = size - i2;
  229: if (i3 >= iJ0) {
  230: this.j.append(a(iJ0));
  231: break;
  232: }
  233: if (i3 == 0) {
  234: u();
  235: } else {
  236: ByteBuffer byteBufferSliceAsByteBuffer = this.f.sliceAsByteBuffer(i2, i3);
  237: int iPosition = byteBufferSliceAsByteBuffer.position();
  238: this.l.clear();
  239: CoderResult coderResultDecode = this.k.decode(byteBufferSliceAsByteBuffer, this.l, false);
  240: int iPosition2 = byteBufferSliceAsByteBuffer.position() - iPosition;
  241: this.g += iPosition2;
  242: iJ0 -= iPosition2;
  243: this.j.append(this.l.flip());
  244: if (coderResultDecode.isError()) {
  245: q(coderResultDecode);
  246: }
  247: if (coderResultDecode.isUnderflow() && iPosition2 < i3) {
  248: ByteBuffer byteBufferAllocate = ByteBuffer.allocate(Integer.numberOfLeadingZeros((~(this.f.getByte(this.g) & 255)) << 24));
  249: MessageBuffer messageBuffer2 = this.f;
  250: messageBuffer2.getBytes(this.g, messageBuffer2.size() - this.g, byteBufferAllocate);
```

### defpackage/bcc.java
Строки 1–280:
```java
    1: package defpackage;
    2: 
    3: import java.io.IOException;
    4: import java.util.ArrayList;
    5: import java.util.Iterator;
    6: import java.util.Locale;
    7: import java.util.Map;
    8: import java.util.concurrent.ConcurrentHashMap;
    9: import java.util.concurrent.atomic.AtomicBoolean;
   10: import java.util.concurrent.atomic.AtomicInteger;
   11: import java.util.concurrent.atomic.AtomicLong;
   12: import java.util.concurrent.locks.Lock;
   13: import java.util.concurrent.locks.ReentrantLock;
   14: import me.leolin.shortcutbadger.BuildConfig;
   15: 
   16: /* JADX INFO: loaded from: classes.dex */
   17: public final class bcc {
   18: public static final AtomicInteger N = new AtomicInteger(0);
   19: public static final AtomicInteger O = new AtomicInteger(0);
   20: public boolean A;
   21: public final boolean B;
   22: public final boolean C;
   23: public final boolean D;
   24: public final boolean E;
   25: public final ruc F;
   26: public final q7c G;
   27: public final j6h H;
   28: public final z3j I;
   29: public final o57 J;
   30: public volatile xr4 K;
   31: public volatile aj4 L;
   32: public final Object M;
   33: public final String a;
   34: public final int m;
   35: public final o57 p;
   36: public final vng q;
   37: public final kuc r;
   38: public final f6h s;
   39: public final st5 t;
   40: public final ArrayList v;
   41: public final am4 x;
   42: public final am4 y;
   43: public final int z;
   44: public final AtomicInteger b = new AtomicInteger(0);
   45: public final AtomicInteger c = new AtomicInteger(0);
   46: public volatile Long d = null;
   47: public final AtomicLong e = new AtomicLong(0);
   48: public final AtomicBoolean f = new AtomicBoolean(false);
   49: public final AtomicBoolean g = new AtomicBoolean();
   50: public final AtomicBoolean h = new AtomicBoolean(false);
   51: public final AtomicInteger i = new AtomicInteger(0);
   52: public final AtomicLong j = new AtomicLong(0);
   53: public final AtomicBoolean k = new AtomicBoolean(false);
   54: public final AtomicInteger l = new AtomicInteger(0);
   55: public final AtomicLong n = new AtomicLong(Long.MIN_VALUE);
   56: public final AtomicBoolean o = new AtomicBoolean(false);
   57: public final ConcurrentHashMap u = new ConcurrentHashMap();
   58: public final Object w = new Object();
   59: 
   60: public bcc(ccc cccVar) {
   61: Object reentrantLock = null;
   62: new AtomicInteger();
   63: O.incrementAndGet();
   64: this.I = cccVar.i;
   65: int iIncrementAndGet = N.incrementAndGet();
   66: this.m = iIncrementAndGet;
   67: this.q = cccVar.c;
   68: this.r = cccVar.f;
   69: String strR = w7g.r(iIncrementAndGet, "Session#");
   70: this.a = strR;
   71: this.p = cccVar.a;
   72: this.s = cccVar.e;
   73: this.t = cccVar.d;
   74: this.F = cccVar.g;
   75: this.G = cccVar.h;
   76: int iMax = Math.max(0, 0);
   77: this.z = iMax;
   78: this.B = cccVar.l;
   79: this.C = cccVar.n;
   80: this.D = cccVar.j;
   81: this.E = cccVar.k;
   82: f09.o(strR, "init, sendLimitIfNoSession=%d", Integer.valueOf(iMax));
   83: this.x = new am4((byte) 4);
   84: this.y = new am4((byte) 4);
   85: j6h j6hVar = cccVar.b;
   86: this.H = j6hVar;
   87: this.v = new ArrayList();
   88: j6hVar.a(new o4h(this), "session-conn-handler").start();
   89: o1d o1dVar = f09.g;
   90: if (o1dVar != null) {
   91: c6a c6aVar = c6a.d;
   92: if (o1dVar.b(c6aVar)) {
   93: o1dVar.c(c6aVar, strR, "init, completed=".concat(String.valueOf(this)), null);
   94: }
   95: }
   96: this.J = cccVar.o;
   97: this.K = new cg6((byte) 15);
   98: boolean z = this.B;
   99: if (z && cccVar.m) {
  100: reentrantLock = new duf();
  101: } else if (z) {
  102: reentrantLock = new ReentrantLock();
  103: }
  104: this.M = reentrantLock;
  105: }
  106: 
  107: public static String h(int i) {
  108: if (i == 0) {
  109: return "DISCONNECTED";
  110: }
  111: if (i != 1) {
  112: return i != 2 ? "<UNKNOWN>" : "LOGGED_IN";
  113: }
  114: return "CONNECTED";
  115: }
  116: 
  117: public static final void v(euf eufVar, bcc bccVar, int i) {
  118: eufVar.a = bccVar.u(i);
  119: }
  120: 
  121: public final void a(long j) {
  122: f09.o(this.a, "cancelRequest(): %d", Long.valueOf(j));
  123: synchronized (this.w) {
  124: try {
  125: for (fld fldVar : this.v) {
  126: eld eldVar = fldVar.b;
  127: if (eldVar != null && eldVar.c.p() == j) {
  128: String str = this.a;
  129: short sK = fldVar.b.a.k();
  130: tdd.c.getClass();
  131: f09.o(str, "cancelRequest(): remove task from mPacketSenderTasks, opcode=%s, requestId=%s", cp5.l(sK), Long.valueOf(fldVar.b.c.p()));
  132: this.v.remove(fldVar);
  133: break;
  134: }
  135: }
  136: } catch (Throwable th) {
  137: throw th;
  138: }
  139: }
  140: for (Map.Entry entry : this.u.entrySet()) {
  141: if (((dld) entry.getValue()).a.p() == j) {
  142: f09.o(this.a, "cancelRequest(): remove task from mPacketReaderTasks, seq=%s, requestId=%s", entry.getKey(), Long.valueOf(((dld) entry.getValue()).a.p()));
  143: this.u.remove(entry.getKey());
  144: return;
  145: }
  146: }
  147: }
  148: 
  149: public final void b(boolean z) {
  150: boolean z2 = false;
  151: boolean zCompareAndSet = this.g.compareAndSet(false, true);
  152: String str = this.a;
  153: if (!zCompareAndSet) {
  154: f09.d0(str, vg9.y("close, ", String.valueOf(this), " has ALREADY been CLOSED, skip re-closing"), new Object[0]);
  155: return;
  156: }
  157: o1d o1dVar = f09.g;
  158: if (o1dVar != null) {
  159: c6a c6aVar = c6a.d;
  160: if (o1dVar.b(c6aVar)) {
  161: o1dVar.c(c6aVar, str, "close, closing the ".concat(String.valueOf(this)), null);
  162: }
  163: }
  164: w(false);
  165: this.x.l();
  166: this.y.l();
  167: if (!this.o.get() && !k()) {
  168: z2 = true;
  169: }
  170: if (this.K.close()) {
  171: e(true, z, e46.l);
  172: }
  173: this.p.getClass();
  174: if (z2) {
  175: this.s.b(Integer.toString(this.m), e46.k);
  176: }
  177: O.decrementAndGet();
  178: f09.p(this.a, "close, " + String.valueOf(this) + " closed");
  179: }
  180: 
  181: public final void c() {
  182: if (!this.o.get() \|\| this.g.get()) {
  183: return;
  184: }
  185: f09.d0(this.a, "closeSessionIfMarkedToDestroy, closing ".concat(String.valueOf(this)), new Object[0]);
  186: b(true);
  187: }
  188: 
  189: public final boolean d(fld fldVar, Class cls) {
  190: eld eldVar = fldVar.b;
  191: if (eldVar == null \|\| !cls.isInstance(eldVar.a)) {
  192: k3g.o("wrong usage of method 'containsInPacketReader'");
  193: return false;
  194: }
  195: Iterator it = this.u.entrySet().iterator();
  196: while (it.hasNext()) {
  197: eld eldVar2 = ((dld) ((Map.Entry) it.next()).getValue()).b.b;
  198: if (eldVar2 != null && cls.isInstance(eldVar2.a)) {
  199: return true;
  200: }
  201: }
  202: return false;
  203: }
  204: 
  205: public final void e(boolean z, boolean z2, e46 e46Var) {
  206: ArrayList arrayList;
  207: f09.o(this.a, "disconnect: clearSenderTasks %b, reason=%s", Boolean.valueOf(z), e46Var);
  208: t(0);
  209: if (!this.o.get()) {
  210: r(e46Var);
  211: }
  212: g6j g6jVar = new g6j("disconnect");
  213: Iterator it = this.u.entrySet().iterator();
  214: while (it.hasNext()) {
  215: ((dld) ((Map.Entry) it.next()).getValue()).a.f(g6jVar);
  216: }
  217: this.u.clear();
  218: if (z) {
  219: Object obj = this.w;
  220: if (z2) {
  221: synchronized (obj) {
  222: this.v.clear();
  223: }
  224: return;
  225: }
  226: synchronized (obj) {
  227: try {
  228: arrayList = null;
  229: for (fld fldVar : this.v) {
  230: if (fldVar.b != null) {
  231: if (arrayList == null) {
  232: arrayList = new ArrayList(1);
  233: }
  234: arrayList.add(fldVar);
  235: }
  236: }
  237: this.v.clear();
  238: } catch (Throwable th) {
  239: throw th;
  240: }
  241: }
  242: if (arrayList != null) {
  243: Iterator it2 = arrayList.iterator();
  244: while (it2.hasNext()) {
  245: ((fld) it2.next()).b.c.f(g6jVar);
  246: }
  247: }
  248: }
  249: }
  250: 
  251: public final void f(cld cldVar) {
  252: synchronized (this.w) {
  253: ArrayList arrayList = this.v;
  254: qzd qzdVar = fe6.b;
  255: arrayList.add(new fld(2, null, az7.V(System.currentTimeMillis(), me6.d), cldVar));
  256: }
  257: this.y.l();
  258: }
  259: 
  260: public final void g(u6j u6jVar, boolean z, long j, e6j e6jVar) {
  261: if (u6jVar instanceof d9a) {
  262: f09.p(this.a, "Received LogoutCmd, clearing all tasks");
  263: this.u.clear();
  264: synchronized (this.w) {
  265: this.v.clear();
  266: }
  267: }
  268: ArrayList arrayList = null;
  269: if (u6jVar.i()) {
  270: String str = this.a;
  271: short sK = u6jVar.k();
  272: tdd.c.getClass();
  273: f09.o(str, "clearPreviousDuplicatedTasks() opCode=%s", cp5.l(sK));
  274: synchronized (this.w) {
  275: try {
  276: for (fld fldVar : this.v) {
  277: eld eldVar = fldVar.b;
  278: if (eldVar != null && eldVar.a.k() == u6jVar.k() && fldVar.b.a.l() == u6jVar.l()) {
  279: if (arrayList == null) {
  280: arrayList = new ArrayList();
```

### defpackage/f0c.java
Строки 1–230:
```java
    1: package defpackage;
    2: 
    3: import android.content.Context;
    4: import android.net.Uri;
    5: import java.io.File;
    6: import java.util.ArrayList;
    7: import java.util.HashMap;
    8: import java.util.Iterator;
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
   19: public static final f0c b = new f0c((byte) 1);
   20: public static final f0c c = new f0c((byte) 2);
   21: public static final /* synthetic */ f0c d = new f0c((byte) 3);
   22: public static final f0c e = new f0c((byte) 4);
   23: public static final f0c f = new f0c((byte) 5);
   24: public static final f0c g = new f0c((byte) 6);
   25: public static final f0c h = new f0c((byte) 7);
   26: public static final f0c i = new f0c((byte) 8);
   27: public final /* synthetic */ byte a;
   28: 
   29: public f0c(Set set) {
   30: this.a = (byte) 0;
   31: new HashMap();
   32: new HashMap();
   33: Iterator it = set.iterator();
   34: if (it.hasNext()) {
   35: s95.D(it.next());
   36: throw null;
   37: }
   38: }
   39: 
   40: public static ArrayList c(List list) {
   41: ArrayList arrayList = new ArrayList();
   42: for (Object obj : list) {
   43: if (((o5f) obj) != o5f.b) {
   44: arrayList.add(obj);
   45: }
   46: }
   47: ArrayList arrayList2 = new ArrayList(xa4.p0(arrayList, 10));
   48: Iterator it = arrayList.iterator();
   49: while (it.hasNext()) {
   50: arrayList2.add(((o5f) it.next()).a);
   51: }
   52: return arrayList2;
   53: }
   54: 
   55: public static byte[] e(List list) {
   56: x91 x91Var = new x91();
   57: for (String str : c(list)) {
   58: x91Var.R(str.length());
   59: x91Var.m0(0, str.length(), str);
   60: }
   61: return x91Var.w(x91Var.b);
   62: }
   63: 
   64: /* JADX WARN: Code duplicated, block: B:10:0x001e A[RETURN] */
   65: /* JADX WARN: Code duplicated, block: B:11:0x001f A[RETURN] */
   66: public static dx5 f(f0c f0cVar, Number number) {
   67: dx5 dx5Var = dx5.REGULAR;
   68: f0cVar.getClass();
   69: byte bByteValue = number.byteValue();
   70: for (dx5 dx5Var2 : dx5.values()) {
   71: if (dx5Var2.a == bByteValue) {
   72: if (dx5Var2 == null) {
   73: return dx5Var;
   74: }
   75: return dx5Var2;
   76: }
   77: }
   78: dx5Var2 = null;
   79: if (dx5Var2 == null) {
   80: return dx5Var;
   81: }
   82: return dx5Var2;
   83: }
   84: 
   85: public static File g(Context context, c0c c0cVar) {
   86: File fileJ = j(context);
   87: yl5.w(fileJ);
   88: return ef7.d0(fileJ, c0cVar.b + "_" + System.currentTimeMillis() + ".bin");
   89: }
   90: 
   91: public static int h(int i2) {
   92: if (i2 >= nb6.t(200.0f * i36.d().getDisplayMetrics().density)) {
   93: return nb6.t(90.0f * i36.d().getDisplayMetrics().density);
   94: }
   95: if (i2 >= nb6.t(72.0f * i36.d().getDisplayMetrics().density)) {
   96: return nb6.t(36.0f * i36.d().getDisplayMetrics().density);
   97: }
   98: if (i2 >= nb6.t(64.0f * i36.d().getDisplayMetrics().density)) {
   99: return nb6.t(32.0f * i36.d().getDisplayMetrics().density);
  100: }
  101: if (i2 >= nb6.t(48.0f * i36.d().getDisplayMetrics().density)) {
  102: return nb6.t(28.0f * i36.d().getDisplayMetrics().density);
  103: }
  104: if (i2 >= nb6.t(36.0f * i36.d().getDisplayMetrics().density)) {
  105: return nb6.t(24.0f * i36.d().getDisplayMetrics().density);
  106: }
  107: if (i2 >= nb6.t(32.0f * i36.d().getDisplayMetrics().density)) {
  108: return nb6.t(20.0f * i36.d().getDisplayMetrics().density);
  109: }
  110: return i2 >= 28 ? nb6.t(16.0f * i36.d().getDisplayMetrics().density) : nb6.t(12.0f * i36.d().getDisplayMetrics().density);
  111: }
  112: 
  113: public static File j(Context context) {
  114: String str;
  115: String strL = xnm.l();
  116: if (strL.equals(context.getPackageName())) {
  117: str = "tracer";
  118: } else {
  119: str = "tracer-" + ((Object) Uri.encode(hui.X(strL, ':', '-', false)));
  120: }
  121: return new File(context.getCacheDir(), str);
  122: }
  123: 
  124: public static boolean k() {
  125: return "Dalvik".equals(System.getProperty("java.vm.name"));
  126: }
  127: 
  128: private final x6j l(beb bebVar) {
  129: int iP0;
  130: String strS0;
  131: if (!bebVar.m()) {
  132: return null;
  133: }
  134: try {
  135: iP0 = e0c.p0(bebVar);
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
  146: }
  147: }
  148: int iG = s95.G(iqg.a);
  149: if (iG != 0) {
  150: if (iG == 1) {
  151: throw th;
  152: }
  153: k3g.l();
  154: return null;
  155: }
  156: iP0 = 0;
  157: }
  158: r53 r53VarC = null;
  159: for (int i2 = 0; i2 < iP0; i2++) {
  160: try {
  161: strS0 = e0c.s0(bebVar, null);
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
  172: }
  173: }
  174: int iG2 = s95.G(iqg.a);
  175: if (iG2 != 0) {
  176: if (iG2 != 1) {
  177: throw new NoWhenBranchMatchedException();
  178: }
  179: throw th3;
  180: }
  181: strS0 = null;
  182: }
  183: if (strS0 != null) {
  184: try {
  185: if (strS0.equals("chat")) {
  186: r53VarC = r53.c(bebVar);
  187: } else {
  188: try {
  189: bebVar.N();
  190: } catch (Throwable th5) {
  191: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
  192: Iterator it3 = q1h.a.iterator();
  193: while (it3.hasNext()) {
  194: AccountInitializer accountInitializer3 = ((z6) it3.next()).a;
  195: try {
  196: f09.c0("Payload", "error while parse payload", th5);
  197: accountInitializer3.c().j().d().a(null, th5);
  198: } catch (Throwable th6) {
  199: f09.c0("Payload", "failed to collect exception", th6);
  200: }
  201: }
  202: int iG3 = s95.G(iqg.a);
  203: if (iG3 != 0) {
  204: if (iG3 != 1) {
  205: throw new NoWhenBranchMatchedException();
  206: }
  207: throw th5;
  208: }
  209: }
  210: }
  211: } catch (Throwable th7) {
  212: try {
  213: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th7);
  214: Iterator it4 = q1h.a.iterator();
  215: while (it4.hasNext()) {
  216: AccountInitializer accountInitializer4 = ((z6) it4.next()).a;
  217: try {
  218: f09.c0("Payload", "error while parse payload", th7);
  219: accountInitializer4.c().j().d().a(null, th7);
  220: } catch (Throwable th8) {
  221: f09.c0("Payload", "failed to collect exception", th8);
  222: }
  223: }
  224: int iG4 = s95.G(iqg.a);
  225: if (iG4 != 0) {
  226: if (iG4 != 1) {
  227: throw new NoWhenBranchMatchedException();
  228: }
  229: throw th7;
  230: }
```

### defpackage/zl8.java
Строки 1–8:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public interface zl8 {
    5: String w();
    6: 
    7: String x();
    8: }
```

### defpackage/dj0.java
Строки 1–26:
```java
    1: package defpackage;
    2: 
    3: import ru.ok.tamtam.errors.TamErrorException;
    4: 
    5: /* JADX INFO: loaded from: classes2.dex */
    6: public final class dj0 extends x1j implements j18 {
    7: public /* synthetic */ Throwable e;
    8: public /* synthetic */ long f;
    9: 
   10: @Override // defpackage.j18
   11: public final Object m(Object obj, Object obj2, Object obj3, Object obj4) {
   12: long jLongValue = ((Number) obj3).longValue();
   13: dj0 dj0Var = new dj0(4, (b55) obj4);
   14: dj0Var.e = (Throwable) obj2;
   15: dj0Var.f = jLongValue;
   16: return dj0Var.w(s1k.a);
   17: }
   18: 
   19: @Override // defpackage.hv0
   20: public final Object w(Object obj) {
   21: Throwable th = this.e;
   22: long j = this.f;
   23: xnm.y(obj);
   24: return Boolean.valueOf((th instanceof TamErrorException) && g4a.c(((TamErrorException) th).a.b, "session.sequence") && j < 3);
   25: }
   26: }
```

### defpackage/oh0.java
Строки 1–90:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class oh0 extends x1j implements e18 {
    5: public final /* synthetic */ byte e = 1;
    6: public byte f;
    7: public final /* synthetic */ long g;
    8: public final /* synthetic */ String h;
    9: public final /* synthetic */ long i;
   10: public /* synthetic */ Object j;
   11: public final /* synthetic */ Object k;
   12: 
   13: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   14: public oh0(oe3 oe3Var, long j, String str, t76 t76Var, long j2, b55 b55Var) {
   15: super(2, b55Var);
   16: this.j = oe3Var;
   17: this.g = j;
   18: this.h = str;
   19: this.k = t76Var;
   20: this.i = j2;
   21: }
   22: 
   23: @Override // defpackage.e18
   24: public final Object invoke(Object obj, Object obj2) {
   25: byte b = this.e;
   26: s1k s1kVar = s1k.a;
   27: switch (b) {
   28: case 0:
   29: return ((oh0) u((b55) obj2, (ri7) obj)).w(s1kVar);
   30: default:
   31: return ((oh0) u((b55) obj2, (ja5) obj)).w(s1kVar);
   32: }
   33: }
   34: 
   35: @Override // defpackage.hv0
   36: public final b55 u(b55 b55Var, Object obj) {
   37: byte b = this.e;
   38: Object obj2 = this.k;
   39: switch (b) {
   40: case 0:
   41: oh0 oh0Var = new oh0((ph0) obj2, this.g, this.h, this.i, b55Var);
   42: oh0Var.j = obj;
   43: return oh0Var;
   44: default:
   45: long j = this.i;
   46: return new oh0((oe3) this.j, this.g, this.h, (t76) obj2, j, b55Var);
   47: }
   48: }
   49: 
   50: /* JADX WARN: Code duplicated, block: B:114:0x0219  */
   51: /* JADX WARN: Code duplicated, block: B:116:0x022b  */
   52: /* JADX WARN: Code duplicated, block: B:119:0x0238  */
   53: /* JADX WARN: Code duplicated, block: B:124:0x0271  */
   54: /* JADX WARN: Code duplicated, block: B:125:0x0273  */
   55: /* JADX WARN: Code duplicated, block: B:127:0x0276 A[DONT_INVERT] */
   56: /* JADX WARN: Code duplicated, block: B:128:0x0278  */
   57: /* JADX WARN: Code duplicated, block: B:129:0x027a  */
   58: /* JADX WARN: Code duplicated, block: B:130:0x027f  */
   59: /* JADX WARN: Code duplicated, block: B:131:0x0282  */
   60: /* JADX WARN: Code duplicated, block: B:133:0x0285  */
   61: /* JADX WARN: Code duplicated, block: B:134:0x028b  */
   62: /* JADX WARN: Code duplicated, block: B:151:? A[RETURN, SYNTHETIC] */
   63: /* JADX WARN: Code duplicated, block: B:152:? A[RETURN, SYNTHETIC] */
   64: /* JADX WARN: Code duplicated, block: B:153:? A[RETURN, SYNTHETIC] */
   65: /* JADX WARN: Code duplicated, block: B:154:? A[RETURN, SYNTHETIC] */
   66: /* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:139:0x02a1 -> B:112:0x0211). Please report as a decompilation issue!!! */
   67: /*  JADX ERROR: JadxOverflowException in pass: RegionMakerVisitor
   68: jadx.core.utils.exceptions.JadxOverflowException: Regions stack size limit reached
   69: at jadx.core.utils.ErrorsCounter.addError(ErrorsCounter.java:59)
   70: at jadx.core.utils.ErrorsCounter.error(ErrorsCounter.java:31)
   71: at jadx.core.dex.attributes.nodes.NotificationAttrNode.addError(NotificationAttrNode.java:19)
   72: */
   73: @Override // defpackage.hv0
   74: public final java.lang.Object w(java.lang.Object r23) {
   75: /*
   76: Method dump skipped, instruction units count: 684
   77: To view this dump add '--comments-level debug' option
   78: */
   79: throw new UnsupportedOperationException("Method not decompiled: defpackage.oh0.w(java.lang.Object):java.lang.Object");
   80: }
   81: 
   82: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   83: public oh0(ph0 ph0Var, long j, String str, long j2, b55 b55Var) {
   84: super(2, b55Var);
   85: this.k = ph0Var;
   86: this.g = j;
   87: this.h = str;
   88: this.i = j2;
   89: }
   90: }
```

### defpackage/cq3.java
Строки 1–310:
```java
    1: package defpackage;
    2: 
    3: import android.content.Context;
    4: import android.content.res.Resources;
    5: import android.graphics.Bitmap;
    6: import android.graphics.BitmapFactory;
    7: import android.net.Uri;
    8: import android.view.View;
    9: import java.io.File;
   10: import java.io.InputStream;
   11: import java.io.Serializable;
   12: import java.nio.file.Path;
   13: import java.util.ArrayList;
   14: import java.util.Collection;
   15: import java.util.Iterator;
   16: import java.util.List;
   17: import java.util.Map;
   18: import java.util.concurrent.CancellationException;
   19: import kotlinx.coroutines.flow.internal.AbortFlowException;
   20: import one.me.chats.tab.ChatsTabWidget;
   21: import one.me.messages.list.loader.MessageModel;
   22: import org.webrtc.PeerConnectionFactory;
   23: import ru.oneme.app.R;
   24: 
   25: /* JADX INFO: loaded from: classes2.dex */
   26: public final class cq3 extends x1j implements e18 {
   27: public final /* synthetic */ byte e;
   28: public boolean f;
   29: public /* synthetic */ Object g;
   30: public Object h;
   31: public final /* synthetic */ Object i;
   32: 
   33: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   34: public cq3(List list, xx4 xx4Var, b55 b55Var) {
   35: super(2, b55Var);
   36: this.e = (byte) 14;
   37: this.i = list;
   38: this.g = xx4Var;
   39: }
   40: 
   41: private final Object y(Object obj) {
   42: s48 s48Var = (s48) this.i;
   43: boolean z = this.f;
   44: s1k s1kVar = s1k.a;
   45: b55 b55Var = null;
   46: if (!z) {
   47: xnm.y(obj);
   48: z28 z28Var = (z28) this.h;
   49: if (z28Var != null) {
   50: e09 e09Var = s48Var.f;
   51: y28 y28Var = z28Var.a;
   52: int i = s48Var.q.b;
   53: this.f = true;
   54: z95 z95VarB = ((vxc) e09Var.d).b();
   55: aa5 aa5Var = e09Var.c;
   56: z95VarB.getClass();
   57: Object objI0 = nm9.i0(xnm.s(z95VarB, aa5Var), new agd((Object) e09Var, (Object) y28Var, i, b55Var, (byte) 6), this);
   58: ka5 ka5Var = ka5.a;
   59: if (objI0 != ka5Var) {
   60: objI0 = s1kVar;
   61: }
   62: if (objI0 == ka5Var) {
   63: return ka5Var;
   64: }
   65: }
   66: } else {
   67: if (!z) {
   68: k3g.o("call to 'resume' before 'invoke' with coroutine");
   69: return null;
   70: }
   71: xnm.y(obj);
   72: }
   73: z28 z28Var2 = (z28) this.g;
   74: z95 z95VarF = ((vxc) s48Var.d1()).f();
   75: aa5 aa5Var2 = s48Var.g;
   76: z95VarF.getClass();
   77: s48Var.z = oyk.Z0(s48Var, xnm.s(z95VarF, aa5Var2), new wi((Object) s48Var, (Object) z28Var2, b55Var, (byte) 28), 2);
   78: return s1kVar;
   79: }
   80: 
   81: private final Object z(Object obj) {
   82: h39 h39Var = h39.a;
   83: Object obj2 = this.g;
   84: ka5 ka5Var = ka5.a;
   85: boolean z = this.f;
   86: if (!z) {
   87: xnm.y(obj);
   88: e49 e49Var = (e49) obj2;
   89: if (e49Var instanceof a49) {
   90: Uri uri = ((a49) e49Var).a;
   91: ob7 ob7Var = uri != null ? new ob7(uri, (byte) 7) : null;
   92: z49 z49Var = (z49) this.h;
   93: z49Var.m = ob7Var;
   94: z49Var.k.e(h39Var);
   95: } else if (e49Var instanceof c49) {
   96: c49 c49Var = (c49) e49Var;
   97: ((z49) this.h).k.e(new j39(c49Var.a, c49Var.c, c49Var.b));
   98: } else if (e49Var instanceof d49) {
   99: File file = ((d49) e49Var).a;
  100: ((z49) this.h).l.set(file);
  101: if (!((z49) this.h).c1(130) && !((z49) this.h).d1()) {
  102: String str = ((z49) this.h).f;
  103: o1d o1dVar = f09.g;
  104: if (o1dVar != null) {
  105: c6a c6aVar = c6a.d;
  106: if (o1dVar.b(c6aVar)) {
  107: o1dVar.c(c6aVar, str, "update: downloadedFile=" + file, null);
  108: }
  109: }
  110: z49 z49Var2 = (z49) this.h;
  111: if (file == null) {
  112: String str2 = z49Var2.f;
  113: o1d o1dVar2 = f09.g;
  114: if (o1dVar2 != null) {
  115: c6a c6aVar2 = c6a.f;
  116: if (o1dVar2.b(c6aVar2)) {
  117: o1dVar2.c(c6aVar2, str2, "Can't update app from informer because file is null", null);
  118: }
  119: }
  120: } else {
  121: z49Var2.m = null;
  122: z49Var2.k.e(h39Var);
  123: ((z49) this.h).e.f();
  124: unf unfVar = (unf) ((rp9) this.i).getValue();
  125: v89 v89Var = v89.f;
  126: this.g = null;
  127: this.f = true;
  128: if (unfVar.D(file, v89Var, this) == ka5Var) {
  129: return ka5Var;
  130: }
  131: }
  132: }
  133: } else if (!(e49Var instanceof b49)) {
  134: k3g.l();
  135: return null;
  136: }
  137: } else {
  138: if (!z) {
  139: k3g.o("call to 'resume' before 'invoke' with coroutine");
  140: return null;
  141: }
  142: xnm.y(obj);
  143: }
  144: return s1k.a;
  145: }
  146: 
  147: @Override // defpackage.e18
  148: public final Object invoke(Object obj, Object obj2) throws Throwable {
  149: byte b = this.e;
  150: s1k s1kVar = s1k.a;
  151: switch (b) {
  152: case 0:
  153: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  154: case 1:
  155: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  156: case 2:
  157: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  158: case 3:
  159: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  160: case 4:
  161: return ((cq3) u((b55) obj2, (ri7) obj)).w(s1kVar);
  162: case 5:
  163: ((cq3) u((b55) obj2, (q83) obj)).w(s1kVar);
  164: return s1kVar;
  165: case 6:
  166: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  167: case 7:
  168: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  169: case 8:
  170: return ((cq3) u((b55) obj2, (oab) obj)).w(s1kVar);
  171: case 9:
  172: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  173: case 10:
  174: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  175: case 11:
  176: return ((cq3) u((b55) obj2, (ri7) obj)).w(s1kVar);
  177: case 12:
  178: return ((cq3) u((b55) obj2, (ri7) obj)).w(s1kVar);
  179: case 13:
  180: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  181: case 14:
  182: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  183: case 15:
  184: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  185: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
  186: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  187: case 17:
  188: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  189: case 18:
  190: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  191: case 19:
  192: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  193: case 20:
  194: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  195: case 21:
  196: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  197: case 22:
  198: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  199: case 23:
  200: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  201: case 24:
  202: return ((cq3) u((b55) obj2, (ri7) obj)).w(s1kVar);
  203: case 25:
  204: return ((cq3) u((b55) obj2, (ri7) obj)).w(s1kVar);
  205: case 26:
  206: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  207: case 27:
  208: return ((cq3) u((b55) obj2, (ja5) obj)).w(s1kVar);
  209: case 28:
  210: return ((cq3) u((b55) obj2, obj)).w(s1kVar);
  211: default:
  212: return ((cq3) u((b55) obj2, (wpe) obj)).w(s1kVar);
  213: }
  214: }
  215: 
  216: @Override // defpackage.hv0
  217: public final b55 u(b55 b55Var, Object obj) {
  218: byte b = this.e;
  219: Object obj2 = this.i;
  220: switch (b) {
  221: case 0:
  222: cq3 cq3Var = new cq3(obj2, b55Var, (byte) 0);
  223: cq3Var.g = obj;
  224: return cq3Var;
  225: case 1:
  226: cq3 cq3Var2 = new cq3(this.h, obj2, b55Var, (byte) 1);
  227: cq3Var2.g = obj;
  228: return cq3Var2;
  229: case 2:
  230: return new cq3(this.h, obj2, this.g, b55Var, (byte) 2);
  231: case 3:
  232: return new cq3(this.h, obj2, this.g, b55Var, (byte) 3);
  233: case 4:
  234: cq3 cq3Var3 = new cq3((c30) obj2, b55Var, (vq3) this.h);
  235: cq3Var3.g = obj;
  236: return cq3Var3;
  237: case 5:
  238: cq3 cq3Var4 = new cq3((String) this.h, this.f, (kt3) obj2, b55Var);
  239: cq3Var4.g = obj;
  240: return cq3Var4;
  241: case 6:
  242: cq3 cq3Var5 = new cq3(this.h, obj2, b55Var, (byte) 6);
  243: cq3Var5.g = obj;
  244: return cq3Var5;
  245: case 7:
  246: return new cq3(this.h, obj2, this.g, b55Var, (byte) 7);
  247: case 8:
  248: cq3 cq3Var6 = new cq3(obj2, b55Var, (byte) 8);
  249: cq3Var6.g = obj;
  250: return cq3Var6;
  251: case 9:
  252: cq3 cq3Var7 = new cq3(this.h, obj2, b55Var, (byte) 9);
  253: cq3Var7.g = obj;
  254: return cq3Var7;
  255: case 10:
  256: return new cq3(this.h, obj2, this.g, b55Var, (byte) 10);
  257: case 11:
  258: cq3 cq3Var8 = new cq3((c30) this.h, b55Var, obj2, (byte) 11);
  259: cq3Var8.g = obj;
  260: return cq3Var8;
  261: case 12:
  262: cq3 cq3Var9 = new cq3((c30) this.h, b55Var, obj2, (byte) 12);
  263: cq3Var9.g = obj;
  264: return cq3Var9;
  265: case 13:
  266: cq3 cq3Var10 = new cq3(obj2, b55Var, (byte) 13);
  267: cq3Var10.g = obj;
  268: return cq3Var10;
  269: case 14:
  270: return new cq3((List) obj2, (xx4) this.g, b55Var);
  271: case 15:
  272: return new cq3((byte) 15, b55Var, obj2, this.g, false);
  273: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
  274: return new cq3(this.h, obj2, this.g, b55Var, (byte) 16);
  275: case 17:
  276: return new cq3((ww5) this.h, b55Var, obj2, this.g, (byte) 17);
  277: case 18:
  278: return new cq3((ww5) this.h, b55Var, obj2, this.g, (byte) 18);
  279: case 19:
  280: return new cq3(this.h, obj2, this.g, b55Var, (byte) 19);
  281: case 20:
  282: return new cq3(this.h, obj2, this.g, b55Var, (byte) 20);
  283: case 21:
  284: return new cq3(this.h, obj2, this.g, b55Var, (byte) 21);
  285: case 22:
  286: return new cq3((byte) 22, b55Var, obj2, this.g, false);
  287: case 23:
  288: cq3 cq3Var11 = new cq3(this.h, obj2, b55Var, (byte) 23);
  289: cq3Var11.g = obj;
  290: return cq3Var11;
  291: case 24:
  292: cq3 cq3Var12 = new cq3(this.h, obj2, b55Var, (byte) 24);
  293: cq3Var12.g = obj;
  294: return cq3Var12;
  295: case 25:
  296: cq3 cq3Var13 = new cq3(this.h, obj2, b55Var, (byte) 25);
  297: cq3Var13.g = obj;
  298: return cq3Var13;
  299: case 26:
  300: cq3 cq3Var14 = new cq3(this.h, obj2, b55Var, (byte) 26);
  301: cq3Var14.g = obj;
  302: return cq3Var14;
  303: case 27:
  304: return new cq3(this.h, obj2, this.g, b55Var, (byte) 27);
  305: case 28:
  306: cq3 cq3Var15 = new cq3(b55Var, (z49) this.h, (rp9) obj2);
  307: cq3Var15.g = obj;
  308: return cq3Var15;
  309: default:
  310: cq3 cq3Var16 = new cq3(this.h, obj2, b55Var, (byte) 29);
```

### defpackage/ii0.java
Строки 1–50:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class ii0 {
    5: public static final ii0 e;
    6: public final /* synthetic */ byte a;
    7: public int b;
    8: public int c;
    9: public int d;
   10: 
   11: static {
   12: int i = Integer.MAX_VALUE;
   13: e = new ii0(1, i, i, (byte) 0);
   14: }
   15: 
   16: public /* synthetic */ ii0(byte b, boolean z) {
   17: this.a = b;
   18: this.b = 0;
   19: this.c = 0;
   20: this.d = 0;
   21: }
   22: 
   23: public int a() {
   24: return this.d;
   25: }
   26: 
   27: public int b() {
   28: return this.c;
   29: }
   30: 
   31: public int c() {
   32: return this.b;
   33: }
   34: 
   35: public String toString() {
   36: switch (this.a) {
   37: case 0:
   38: return pq0.h(this.d, ")", pq0.r("Config(pminl=", this.b, ",pml=", this.c, ",hml="));
   39: default:
   40: return super.toString();
   41: }
   42: }
   43: 
   44: public /* synthetic */ ii0(int i, int i2, int i3, byte b) {
   45: this.a = b;
   46: this.b = i;
   47: this.c = i2;
   48: this.d = i3;
   49: }
   50: }
```

### defpackage/kh0.java
Строки 1–25:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class kh0 implements nh0 {
    5: public final String a;
    6: 
    7: public kh0(String str) {
    8: this.a = str;
    9: }
   10: 
   11: public final boolean equals(Object obj) {
   12: if (this == obj) {
   13: return true;
   14: }
   15: return (obj instanceof kh0) && g4a.c(this.a, ((kh0) obj).a);
   16: }
   17: 
   18: public final int hashCode() {
   19: return this.a.hashCode();
   20: }
   21: 
   22: public final String toString() {
   23: return vg9.y("NumberAssigned(callNumber=", this.a, ")");
   24: }
   25: }
```

### defpackage/lh0.java
Строки 1–18:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class lh0 implements nh0 {
    5: public static final lh0 a = new lh0();
    6: 
    7: public final boolean equals(Object obj) {
    8: return this == obj \|\| (obj instanceof lh0);
    9: }
   10: 
   11: public final int hashCode() {
   12: return -993235639;
   13: }
   14: 
   15: public final String toString() {
   16: return "VerificationPassed";
   17: }
   18: }
```

### defpackage/mh0.java
Строки 1–18:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class mh0 implements nh0 {
    5: public static final mh0 a = new mh0();
    6: 
    7: public final boolean equals(Object obj) {
    8: return this == obj \|\| (obj instanceof mh0);
    9: }
   10: 
   11: public final int hashCode() {
   12: return -1247401048;
   13: }
   14: 
   15: public final String toString() {
   16: return "VerificationTimeout";
   17: }
   18: }
```

### defpackage/bj0.java
Строки 1–590:
```java
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
   11: public final long e;
   12: public final long f;
   13: public final int g;
   14: public final c h;
   15: 
   16: public bj0(String str, int i, long j, long j2, int i2, c cVar) {
   17: this.c = str;
   18: this.d = i;
   19: this.e = j;
   20: this.f = j2;
   21: this.g = i2;
   22: this.h = cVar;
   23: }
   24: 
   25: /* JADX WARN: Code duplicated, block: B:390:0x0342 A[EXC_TOP_SPLITTER, SYNTHETIC] */
   26: /* JADX WARN: Code duplicated, block: B:93:0x0167 A[PHI: r19 r21
   27: 0x0167: PHI (r19v2 long) = (r19v1 long), (r19v1 long), (r19v1 long), (r19v1 long), (r19v5 long), (r19v6 long) binds: [B:46:0x00b7, B:115:0x01c6, B:99:0x0183, B:92:0x0165, B:71:0x0114, B:54:0x00ce] A[DONT_GENERATE, DONT_INLINE]
   28: 0x0167: PHI (r21v2 int) = (r21v1 int), (r21v5 int), (r21v6 int), (r21v1 int), (r21v1 int), (r21v1 int) binds: [B:46:0x00b7, B:115:0x01c6, B:99:0x0183, B:92:0x0165, B:71:0x0114, B:54:0x00ce] A[DONT_GENERATE, DONT_INLINE]] */
   29: /* JADX WARN: Multi-variable type inference failed */
   30: /* JADX WARN: Type inference failed for: r0v109, types: [pb5] */
   31: /* JADX WARN: Type inference failed for: r0v123, types: [pb5] */
   32: /* JADX WARN: Type inference failed for: r0v137, types: [pb5] */
   33: /* JADX WARN: Type inference failed for: r0v151, types: [pb5] */
   34: /* JADX WARN: Type inference failed for: r0v166, types: [pb5] */
   35: /* JADX WARN: Type inference failed for: r0v18 */
   36: /* JADX WARN: Type inference failed for: r0v182, types: [pb5] */
   37: /* JADX WARN: Type inference failed for: r0v190 */
   38: /* JADX WARN: Type inference failed for: r0v197, types: [pb5] */
   39: /* JADX WARN: Type inference failed for: r0v198 */
   40: /* JADX WARN: Type inference failed for: r0v212, types: [pb5] */
   41: /* JADX WARN: Type inference failed for: r0v215 */
   42: /* JADX WARN: Type inference failed for: r0v216 */
   43: /* JADX WARN: Type inference failed for: r0v217 */
   44: /* JADX WARN: Type inference failed for: r0v25, types: [pb5] */
   45: /* JADX WARN: Type inference failed for: r0v26, types: [java.lang.String] */
   46: /* JADX WARN: Type inference failed for: r0v66, types: [pb5] */
   47: /* JADX WARN: Type inference failed for: r0v81, types: [pb5] */
   48: /* JADX WARN: Type inference failed for: r0v88 */
   49: /* JADX WARN: Type inference failed for: r0v95, types: [pb5] */
   50: /* JADX WARN: Type inference failed for: r0v96, types: [java.lang.String] */
   51: /* JADX WARN: Type inference failed for: r15v0 */
   52: /* JADX WARN: Type inference failed for: r15v1, types: [java.lang.String] */
   53: /* JADX WARN: Type inference failed for: r15v10 */
   54: /* JADX WARN: Type inference failed for: r15v11 */
   55: /* JADX WARN: Type inference failed for: r15v12 */
   56: /* JADX WARN: Type inference failed for: r15v13 */
   57: /* JADX WARN: Type inference failed for: r15v2 */
   58: /* JADX WARN: Type inference failed for: r15v3 */
   59: /* JADX WARN: Type inference failed for: r15v4 */
   60: /* JADX WARN: Type inference failed for: r15v5 */
   61: /* JADX WARN: Type inference failed for: r15v6 */
   62: /* JADX WARN: Type inference failed for: r15v7 */
   63: /* JADX WARN: Type inference failed for: r15v8 */
   64: /* JADX WARN: Type inference failed for: r15v9 */
   65: /* JADX WARN: Type inference failed for: r24v0, types: [bj0] */
   66: /* JADX WARN: Type inference failed for: r24v1 */
   67: /* JADX WARN: Type inference failed for: r24v10 */
   68: /* JADX WARN: Type inference failed for: r24v2 */
   69: /* JADX WARN: Type inference failed for: r25v0 */
   70: /* JADX WARN: Type inference failed for: r25v1 */
   71: /* JADX WARN: Type inference failed for: r25v2 */
   72: /* JADX WARN: Type inference failed for: r25v3 */
   73: /* JADX WARN: Type inference failed for: r25v4 */
   74: /* JADX WARN: Type inference failed for: r25v5 */
   75: /* JADX WARN: Type inference failed for: r7v0 */
   76: /* JADX WARN: Type inference failed for: r7v1, types: [bj0, java.lang.String] */
   77: /* JADX WARN: Type inference failed for: r7v6 */
   78: /* JADX WARN: Type inference failed for: r8v3, types: [java.lang.String] */
   79: public static final bj0 f(beb bebVar) {
   80: int iP0;
   81: ?? R0;
   82: ?? r24;
   83: int i;
   84: long j;
   85: byte b;
   86: int iP1;
   87: int i2;
   88: ?? S0;
   89: ?? S1;
   90: ?? r15;
   91: ?? r7 = 0;
   92: if (!bebVar.m()) {
   93: return null;
   94: }
   95: int i3 = 0;
   96: byte b2 = 1;
   97: try {
   98: iP0 = e0c.p0(bebVar);
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
  109: }
  110: }
  111: int iG = s95.G(iqg.a);
  112: if (iG != 0) {
  113: if (iG == 1) {
  114: throw th;
  115: }
  116: k3g.l();
  117: return null;
  118: }
  119: iP0 = 0;
  120: }
  121: if (iP0 == 0) {
  122: return null;
  123: }
  124: long j2 = 0;
  125: ?? r16 = 0;
  126: c cVar = null;
  127: int i4 = 0;
  128: int iM0 = 0;
  129: int iM1 = 0;
  130: long jO0 = 0;
  131: long jO1 = 0;
  132: while (i4 < iP0) {
  133: try {
  134: R0 = e0c.r0(bebVar);
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
  145: }
  146: }
  147: int iG2 = s95.G(iqg.a);
  148: if (iG2 != 0) {
  149: if (iG2 == b2) {
  150: throw th3;
  151: }
  152: k3g.l();
  153: return r7;
  154: }
  155: R0 = r7;
  156: }
  157: if (R0 != 0) {
  158: switch (R0.hashCode()) {
  159: case -1135546573:
  160: j = j2;
  161: if (R0.equals("codeLength")) {
  162: i = 0;
  163: try {
  164: iM0 = e0c.m0(bebVar, 0);
  165: r16 = r16;
  166: } catch (Throwable th5) {
  167: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
  168: Iterator it3 = q1h.a.iterator();
  169: while (it3.hasNext()) {
  170: AccountInitializer accountInitializer3 = ((z6) it3.next()).a;
  171: try {
  172: f09.c0("Payload", "error while parse payload", th5);
  173: accountInitializer3.c().j().d().a(null, th5);
  174: } catch (Throwable th6) {
  175: f09.c0("Payload", "failed to collect exception", th6);
  176: }
  177: }
  178: int iG3 = s95.G(iqg.a);
  179: if (iG3 != 0) {
  180: if (iG3 == 1) {
  181: throw th5;
  182: }
  183: k3g.l();
  184: return null;
  185: }
  186: iM0 = 0;
  187: r16 = r16;
  188: }
  189: } else {
  190: bebVar.N();
  191: r15 = r16;
  192: i = 0;
  193: r16 = r15;
  194: }
  195: b = 1;
  196: r24 = 0;
  197: break;
  198: case -1007074317:
  199: if (R0.equals("altActionDuration")) {
  200: j = 0;
  201: try {
  202: jO0 = e0c.o0(bebVar, 0L);
  203: r15 = r16;
  204: } catch (Throwable th7) {
  205: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th7);
  206: Iterator it4 = q1h.a.iterator();
  207: while (it4.hasNext()) {
  208: AccountInitializer accountInitializer4 = ((z6) it4.next()).a;
  209: try {
  210: f09.c0("Payload", "error while parse payload", th7);
  211: accountInitializer4.c().j().d().a(null, th7);
  212: } catch (Throwable th8) {
  213: f09.c0("Payload", "failed to collect exception", th8);
  214: }
  215: }
  216: int iG4 = s95.G(iqg.a);
  217: if (iG4 != 0) {
  218: if (iG4 == 1) {
  219: throw th7;
  220: }
  221: k3g.l();
  222: return null;
  223: }
  224: jO0 = 0;
  225: r15 = r16;
  226: }
  227: } else {
  228: j = 0;
  229: bebVar.N();
  230: r15 = r16;
  231: }
  232: i = 0;
  233: r16 = r15;
  234: b = 1;
  235: r24 = 0;
  236: break;
  237: case -941829706:
  238: if (R0.equals("callOutParams")) {
  239: try {
  240: iP1 = e0c.p0(bebVar);
  241: } catch (Throwable th9) {
  242: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th9);
  243: Iterator it5 = q1h.a.iterator();
  244: while (it5.hasNext()) {
  245: AccountInitializer accountInitializer5 = ((z6) it5.next()).a;
  246: try {
  247: f09.c0("Payload", "error while parse payload", th9);
  248: accountInitializer5.c().j().d().a(r7, th9);
  249: } catch (Throwable th10) {
  250: f09.c0("Payload", "failed to collect exception", th10);
  251: }
  252: }
  253: int iG5 = s95.G(iqg.a);
  254: if (iG5 != 0) {
  255: if (iG5 == b2) {
  256: throw th9;
  257: }
  258: k3g.l();
  259: return r7;
  260: }
  261: iP1 = i3;
  262: }
  263: ?? S2 = r7;
  264: int i5 = 0;
  265: int iM2 = -1;
  266: int iM3 = -1;
  267: while (i5 < iP1) {
  268: try {
  269: S0 = e0c.s0(bebVar, r7);
  270: } catch (Throwable th11) {
  271: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th11);
  272: Iterator it6 = q1h.a.iterator();
  273: while (it6.hasNext()) {
  274: AccountInitializer accountInitializer6 = ((z6) it6.next()).a;
  275: try {
  276: f09.c0("Payload", "error while parse payload", th11);
  277: accountInitializer6.c().j().d().a(r7, th11);
  278: } catch (Throwable th12) {
  279: f09.c0("Payload", "failed to collect exception", th12);
  280: }
  281: }
  282: int iG6 = s95.G(iqg.a);
  283: if (iG6 != 0) {
  284: if (iG6 != b2) {
  285: throw new NoWhenBranchMatchedException();
  286: }
  287: throw th11;
  288: }
  289: S0 = r7;
  290: }
  291: if (S0 != 0) {
  292: try {
  293: int iHashCode = S0.hashCode();
  294: if (iHashCode != -1067396154) {
  295: if (iHashCode != -199210584) {
  296: if (iHashCode == 115180 && S0.equals("ttl")) {
  297: try {
  298: iM2 = e0c.m0(bebVar, -1);
  299: } catch (Throwable th13) {
  300: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th13);
  301: Iterator it7 = q1h.a.iterator();
  302: while (it7.hasNext()) {
  303: AccountInitializer accountInitializer7 = ((z6) it7.next()).a;
  304: try {
  305: f09.c0("Payload", "error while parse payload", th13);
  306: accountInitializer7.c().j().d().a(r7, th13);
  307: } catch (Throwable th14) {
  308: f09.c0("Payload", "failed to collect exception", th14);
  309: }
  310: }
  311: int iG7 = s95.G(iqg.a);
  312: if (iG7 != 0) {
  313: if (iG7 != 1) {
  314: throw new NoWhenBranchMatchedException();
  315: }
  316: throw th13;
  317: }
  318: iM2 = -1;
  319: }
  320: } else {
  321: try {
  322: bebVar.N();
  323: } catch (Throwable th15) {
  324: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th15);
  325: Iterator it8 = q1h.a.iterator();
  326: while (it8.hasNext()) {
  327: AccountInitializer accountInitializer8 = ((z6) it8.next()).a;
  328: try {
  329: f09.c0("Payload", "error while parse payload", th15);
  330: accountInitializer8.c().j().d().a(r7, th15);
  331: } catch (Throwable th16) {
  332: f09.c0("Payload", "failed to collect exception", th16);
  333: }
  334: }
  335: int iG8 = s95.G(iqg.a);
  336: if (iG8 != 0) {
  337: if (iG8 != 1) {
  338: throw new NoWhenBranchMatchedException();
  339: }
  340: throw th15;
  341: }
  342: }
  343: }
  344: } else if (S0.equals("pollingInterval")) {
  345: try {
  346: iM3 = e0c.m0(bebVar, -1);
  347: } catch (Throwable th17) {
  348: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th17);
  349: Iterator it9 = q1h.a.iterator();
  350: while (it9.hasNext()) {
  351: AccountInitializer accountInitializer9 = ((z6) it9.next()).a;
  352: try {
  353: f09.c0("Payload", "error while parse payload", th17);
  354: accountInitializer9.c().j().d().a(r7, th17);
  355: } catch (Throwable th18) {
  356: f09.c0("Payload", "failed to collect exception", th18);
  357: }
  358: }
  359: int iG9 = s95.G(iqg.a);
  360: if (iG9 != 0) {
  361: if (iG9 != 1) {
  362: throw new NoWhenBranchMatchedException();
  363: }
  364: throw th17;
  365: }
  366: iM3 = -1;
  367: }
  368: } else {
  369: bebVar.N();
  370: }
  371: } else if (S0.equals("trackId")) {
  372: try {
  373: S2 = e0c.s0(bebVar, r7);
  374: } catch (Throwable th19) {
  375: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th19);
  376: Iterator it10 = q1h.a.iterator();
  377: while (it10.hasNext()) {
  378: AccountInitializer accountInitializer10 = ((z6) it10.next()).a;
  379: try {
  380: f09.c0("Payload", "error while parse payload", th19);
  381: accountInitializer10.c().j().d().a(r7, th19);
  382: } catch (Throwable th20) {
  383: f09.c0("Payload", "failed to collect exception", th20);
  384: }
  385: }
  386: int iG10 = s95.G(iqg.a);
  387: if (iG10 != 0) {
  388: if (iG10 != 1) {
  389: throw new NoWhenBranchMatchedException();
  390: }
  391: throw th19;
  392: }
  393: S2 = r7;
  394: }
  395: } else {
  396: bebVar.N();
  397: }
  398: } catch (Throwable th21) {
  399: try {
  400: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th21);
  401: Iterator it11 = q1h.a.iterator();
  402: while (it11.hasNext()) {
  403: AccountInitializer accountInitializer11 = ((z6) it11.next()).a;
  404: try {
  405: f09.c0("Payload", "error while parse payload", th21);
  406: accountInitializer11.c().j().d().a(r7, th21);
  407: } catch (Throwable th22) {
  408: f09.c0("Payload", "failed to collect exception", th22);
  409: }
  410: }
  411: int iG11 = s95.G(iqg.a);
  412: if (iG11 != 0) {
  413: if (iG11 != 1) {
  414: throw new NoWhenBranchMatchedException();
  415: }
  416: throw th21;
  417: }
  418: } catch (Throwable th23) {
  419: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th23);
  420: Iterator it12 = q1h.a.iterator();
  421: while (it12.hasNext()) {
  422: AccountInitializer accountInitializer12 = ((z6) it12.next()).a;
  423: try {
  424: f09.c0("Payload", "error while parse payload", th23);
  425: accountInitializer12.c().j().d().a(r7, th23);
  426: } catch (Throwable th24) {
  427: f09.c0("Payload", "failed to collect exception", th24);
  428: }
  429: }
  430: int iG12 = s95.G(iqg.a);
  431: b2 = 1;
  432: if (iG12 != 0) {
  433: if (iG12 == 1) {
  434: throw th23;
  435: }
  436: k3g.l();
  437: return r7;
  438: }
  439: }
  440: }
  441: }
  442: i5++;
  443: b2 = 1;
  444: S2 = S2;
  445: break;
  446: }
  447: ?? r8 = S2;
  448: if (r8 == 0 \|\| iM2 <= 0) {
  449: i2 = iM3;
  450: } else {
  451: i2 = iM3;
  452: if (i2 > 0) {
  453: cVar = new c(r8, iM2, i2, b2);
  454: }
  455: j = 0;
  456: r15 = r16;
  457: }
  458: String name = w12.class.getName();
  459: o1d o1dVar = f09.g;
  460: if (o1dVar != null) {
  461: c6a c6aVar = c6a.f;
  462: if (o1dVar.b(c6aVar)) {
  463: o1dVar.c(c6aVar, name, s95.l(iM2, i2, "CallOutVerificationParams: invalid, ttl=", ", pollingInterval="), null);
  464: }
  465: }
  466: cVar = null;
  467: j = 0;
  468: r15 = r16;
  469: } else {
  470: j = j2;
  471: bebVar.N();
  472: r15 = r16;
  473: }
  474: i = 0;
  475: r16 = r15;
  476: b = 1;
  477: r24 = 0;
  478: break;
  479: case 6808551:
  480: if (!R0.equals("requestCountLeft")) {
  481: j = j2;
  482: bebVar.N();
  483: r15 = r16;
  484: i = 0;
  485: r16 = r15;
  486: b = 1;
  487: r24 = 0;
  488: } else {
  489: try {
  490: iM1 = e0c.m0(bebVar, i3);
  491: } catch (Throwable th25) {
  492: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th25);
  493: Iterator it13 = q1h.a.iterator();
  494: while (it13.hasNext()) {
  495: AccountInitializer accountInitializer13 = ((z6) it13.next()).a;
  496: try {
  497: f09.c0("Payload", "error while parse payload", th25);
  498: accountInitializer13.c().j().d().a(r7, th25);
  499: } catch (Throwable th26) {
  500: f09.c0("Payload", "failed to collect exception", th26);
  501: }
  502: }
  503: int iG13 = s95.G(iqg.a);
  504: if (iG13 != 0) {
  505: if (iG13 == b2) {
  506: throw th25;
  507: }
  508: k3g.l();
  509: return r7;
  510: }
  511: iM1 = i3;
  512: }
  513: r24 = r7;
  514: byte b3 = b2;
  515: i = i3;
  516: j = j2;
  517: b = b3;
  518: }
  519: break;
  520: case 110541305:
  521: if (R0.equals("token")) {
  522: try {
  523: S1 = e0c.s0(bebVar, r7);
  524: } catch (Throwable th27) {
  525: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th27);
  526: Iterator it14 = q1h.a.iterator();
  527: while (it14.hasNext()) {
  528: AccountInitializer accountInitializer14 = ((z6) it14.next()).a;
  529: try {
  530: f09.c0("Payload", "error while parse payload", th27);
  531: accountInitializer14.c().j().d().a(r7, th27);
  532: } catch (Throwable th28) {
  533: f09.c0("Payload", "failed to collect exception", th28);
  534: }
  535: }
  536: int iG14 = s95.G(iqg.a);
  537: if (iG14 != 0) {
  538: if (iG14 == b2) {
  539: throw th27;
  540: }
  541: k3g.l();
  542: return r7;
  543: }
  544: S1 = r7;
  545: }
  546: if (S1 == 0) {
  547: r24 = r7;
  548: byte b4 = b2;
  549: i = i3;
  550: j = j2;
  551: b = b4;
  552: } else {
  553: r15 = S1;
  554: j = j2;
  555: }
  556: } else {
  557: j = j2;
  558: bebVar.N();
  559: r15 = r16;
  560: }
  561: i = 0;
  562: r16 = r15;
  563: b = 1;
  564: r24 = 0;
  565: break;
  566: case 575768841:
  567: if (!R0.equals("requestMaxDuration")) {
  568: j = j2;
  569: bebVar.N();
  570: r15 = r16;
  571: i = 0;
  572: r16 = r15;
  573: b = 1;
  574: r24 = 0;
  575: } else {
  576: try {
  577: jO1 = e0c.o0(bebVar, j2);
  578: } catch (Throwable th29) {
  579: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th29);
  580: Iterator it15 = q1h.a.iterator();
  581: while (it15.hasNext()) {
  582: AccountInitializer accountInitializer15 = ((z6) it15.next()).a;
  583: try {
  584: f09.c0("Payload", "error while parse payload", th29);
  585: accountInitializer15.c().j().d().a(r7, th29);
  586: } catch (Throwable th30) {
  587: f09.c0("Payload", "failed to collect exception", th30);
  588: }
  589: }
  590: int iG15 = s95.G(iqg.a);
```

### defpackage/h79.java
Строки 1–60:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class h79 extends j {
    5: public final String b;
    6: public final String c;
    7: public final int d;
    8: public final long e;
    9: public final String f;
   10: 
   11: public h79(int i, long j, String str, String str2, String str3) {
   12: super((byte) 9);
   13: this.b = str;
   14: this.c = str2;
   15: this.d = i;
   16: this.e = j;
   17: this.f = str3;
   18: }
   19: 
   20: public final int a() {
   21: return this.d;
   22: }
   23: 
   24: public final long b() {
   25: return this.e;
   26: }
   27: 
   28: public final String c() {
   29: return this.f;
   30: }
   31: 
   32: public final String d() {
   33: return this.c;
   34: }
   35: 
   36: public final String e() {
   37: return this.b;
   38: }
   39: 
   40: public final boolean equals(Object obj) {
   41: if (this == obj) {
   42: return true;
   43: }
   44: if (!(obj instanceof h79)) {
   45: return false;
   46: }
   47: h79 h79Var = (h79) obj;
   48: return this.b.equals(h79Var.b) && g4a.c(this.c, h79Var.c) && this.d == h79Var.d && this.e == h79Var.e && g4a.c(this.f, h79Var.f);
   49: }
   50: 
   51: public final int hashCode() {
   52: return this.f.hashCode() + s95.h(a15.d(this.d, a15.e(this.b.hashCode() * 31, 31, this.c), 31), 31, this.e);
   53: }
   54: 
   55: public final String toString() {
   56: StringBuilder sbS = pq0.s("PhoneConfirmScreen(verifyToken=", this.b, ", phone=", this.c, ", codeLength=");
   57: vg9.H(sbS, this.d, ", codeResendMillis=", this.e);
   58: return pq0.m(", countryNameCode=", this.f, ")", sbS);
   59: }
   60: }
```

### defpackage/wi.java
Строки 1–340:
```java
    1: package defpackage;
    2: 
    3: import android.app.AlarmManager;
    4: import android.app.Application;
    5: import android.app.PendingIntent;
    6: import android.content.Intent;
    7: import android.graphics.Bitmap;
    8: import android.graphics.Rect;
    9: import android.graphics.RectF;
   10: import android.net.Uri;
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
   21: import java.util.Collection;
   22: import java.util.Iterator;
   23: import java.util.LinkedHashMap;
   24: import java.util.List;
   25: import java.util.Map;
   26: import java.util.Set;
   27: import java.util.concurrent.CancellationException;
   28: import java.util.concurrent.atomic.AtomicBoolean;
   29: import java.util.concurrent.atomic.AtomicReference;
   30: import me.leolin.shortcutbadger.BuildConfig;
   31: import one.me.background.wake.BackgroundCheckReceiver;
   32: import org.webrtc.PeerConnectionFactory;
   33: import ru.ok.tamtam.errors.TamErrorException;
   34: import ru.oneme.app.R;
   35: 
   36: /* JADX INFO: loaded from: classes2.dex */
   37: public final class wi extends x1j implements e18 {
   38: public final /* synthetic */ byte e;
   39: public byte f;
   40: public Object g;
   41: public Object h;
   42: public Object i;
   43: public Object j;
   44: 
   45: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   46: public wi(b55 b55Var, qw2 qw2Var, ArrayList arrayList, ArrayList arrayList2) {
   47: super(2, b55Var);
   48: this.e = (byte) 9;
   49: this.g = qw2Var;
   50: this.h = arrayList;
   51: this.i = arrayList2;
   52: }
   53: 
   54: /* JADX WARN: Code duplicated, block: B:28:0x0094 A[PHI: r0
   55: 0x0094: PHI (r0v11 java.util.Iterator) = (r0v8 java.util.Iterator), (r0v10 java.util.Iterator), (r0v23 java.util.Iterator) binds: [B:27:0x0089, B:37:0x00dc, B:7:0x001a] A[DONT_GENERATE, DONT_INLINE]] */
   56: /* JADX WARN: Code duplicated, block: B:30:0x009a  */
   57: /* JADX WARN: Code duplicated, block: B:33:0x00b9  */
   58: /* JADX WARN: Code duplicated, block: B:36:0x00be  */
   59: /* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:37:0x00dc -> B:28:0x0094). Please report as a decompilation issue!!! */
   60: /*  JADX ERROR: JadxOverflowException in pass: RegionMakerVisitor
   61: jadx.core.utils.exceptions.JadxOverflowException: Regions stack size limit reached
   62: at jadx.core.utils.ErrorsCounter.addError(ErrorsCounter.java:59)
   63: at jadx.core.utils.ErrorsCounter.error(ErrorsCounter.java:31)
   64: at jadx.core.dex.attributes.nodes.NotificationAttrNode.addError(NotificationAttrNode.java:19)
   65: */
   66: private final java.lang.Object A(java.lang.Object r17) {
   67: /*
   68: Method dump skipped, instruction units count: 227
   69: To view this dump add '--comments-level debug' option
   70: */
   71: throw new UnsupportedOperationException("Method not decompiled: defpackage.wi.A(java.lang.Object):java.lang.Object");
   72: }
   73: 
   74: /* JADX WARN: Code restructure failed: missing block: B:14:0x0064, code lost:
   75: 
   76: if (r0 == r7) goto L15;
   77: */
   78: /*
   79: Code decompiled incorrectly, please refer to instructions dump.
   80: */
   81: private final Object B(Object obj) {
   82: Object objA;
   83: p9b p9bVar;
   84: Object objR;
   85: oj3 oj3Var = (oj3) this.h;
   86: qj3 qj3Var = (qj3) oj3Var.a;
   87: byte b = this.f;
   88: ka5 ka5Var = ka5.a;
   89: if (b == 0) {
   90: xnm.y(obj);
   91: d7b d7bVar = (d7b) this.i;
   92: this.f = (byte) 1;
   93: objA = oj3Var.a(d7bVar, this);
   94: if (objA != ka5Var) {
   95: }
   96: return ka5Var;
   97: }
   98: if (b == 1) {
   99: xnm.y(obj);
  100: objA = obj;
  101: } else {
  102: if (b != 2) {
  103: k3g.o("call to 'resume' before 'invoke' with coroutine");
  104: return null;
  105: }
  106: p9b p9bVar2 = (p9b) this.g;
  107: xnm.y(obj);
  108: p9bVar = p9bVar2;
  109: objR = obj;
  110: }
  111: q53 q53Var = (q53) objR;
  112: int i = qj3Var.d;
  113: if (i > 0) {
  114: opg opgVar = (opg) ((rp9) oj3Var.g).getValue();
  115: long j = p9bVar.b;
  116: String str = qj3Var.l;
  117: int i2 = i - 1;
  118: opgVar.getClass();
  119: long jM = q53Var.m();
  120: int iN = q53Var.n();
  121: dea deaVar = new dea();
  122: if (jM > 0) {
  123: deaVar.put("conversationId", Long.valueOf(jM));
  124: }
  125: if (iN != 1) {
  126: deaVar.put("conversationType", Integer.valueOf(er2.d(iN)));
  127: }
  128: if (str != null) {
  129: deaVar.put("queryId", str);
  130: }
  131: deaVar.put("messageId", Long.valueOf(j));
  132: deaVar.put("rank", Integer.valueOf(i2));
  133: deaVar.put("section", 8);
  134: t5a.g((t5a) opgVar.a.getValue(), "search_click", deaVar.b(), null, 4);
  135: }
  136: return s1k.a;
  137: p9bVar = (p9b) objA;
  138: r4i r4iVar = (r4i) oj3Var.i;
  139: long j2 = p9bVar.b;
  140: r4iVar.j(null, new mi8(p9bVar.c, p9bVar.a, j2, ((mdb) this.j).d));
  141: this.g = p9bVar;
  142: this.f = (byte) 2;
  143: objR = hzj.R(qj3Var.a, this);
  144: }
  145: 
  146: /* JADX WARN: Code restructure failed: missing block: B:13:0x005a, code lost:
  147: 
  148: if (r9 == r3) goto L21;
  149: */
  150: /* JADX WARN: Code restructure failed: missing block: B:20:0x006e, code lost:
  151: 
  152: if (r9 == r3) goto L21;
  153: */
  154: /*
  155: Code decompiled incorrectly, please refer to instructions dump.
  156: */
  157: private final Object C(Object obj) {
  158: String absolutePath;
  159: Rect rect = (Rect) this.i;
  160: String str = (String) this.h;
  161: ss3 ss3Var = (ss3) this.g;
  162: byte b = this.f;
  163: if (b == 0) {
  164: xnm.y(obj);
  165: zm9[] zm9VarArr = ss3.A;
  166: boolean zBooleanValue = ((Boolean) ((j9e) ss3Var.o.getValue()).K6.a(j9e.w8[401]).i()).booleanValue();
  167: ka5 ka5Var = ka5.a;
  168: if (zBooleanValue) {
  169: fd5 fd5Var = (fd5) ss3Var.n.getValue();
  170: this.f = (byte) 1;
  171: obj = fd5Var.a(str, rect, this);
  172: } else {
  173: this.f = (byte) 2;
  174: obj = ss3Var.c1(str, rect, this);
  175: }
  176: return ka5Var;
  177: }
  178: if (b == 1) {
  179: xnm.y(obj);
  180: File file = (File) obj;
  181: absolutePath = file != null ? file.getAbsolutePath() : null;
  182: } else {
  183: if (b != 2) {
  184: k3g.o("call to 'resume' before 'invoke' with coroutine");
  185: return null;
  186: }
  187: xnm.y(obj);
  188: absolutePath = (String) obj;
  189: }
  190: r4i r4iVar = ss3Var.p;
  191: qs3 qs3Var = new qs3(str, absolutePath, (RectF) this.j);
  192: r4iVar.getClass();
  193: r4iVar.j(null, qs3Var);
  194: return s1k.a;
  195: }
  196: 
  197: /* JADX WARN: Code duplicated, block: B:28:0x0082  */
  198: /* JADX WARN: Code duplicated, block: B:30:0x0092  */
  199: /* JADX WARN: Multi-variable type inference failed */
  200: private final Object D(Object obj) {
  201: kv4 kv4VarV;
  202: q53 q53Var;
  203: boolean zBooleanValue;
  204: vv6 vv6Var;
  205: zw3 zw3Var = (zw3) this.i;
  206: byte b = this.f;
  207: Integer num = null;
  208: Object[] objArr = 0;
  209: s1k s1kVar = s1k.a;
  210: ka5 ka5Var = ka5.a;
  211: if (b == 0) {
  212: xnm.y(obj);
  213: zm9[] zm9VarArr = zw3.p1;
  214: dmf dmfVarJ = zw3Var.c1().j(((zq3) this.j).c);
  215: this.f = (byte) 1;
  216: obj = hzj.R(dmfVarJ, this);
  217: if (obj != ka5Var) {
  218: }
  219: return ka5Var;
  220: }
  221: if (b == 1) {
  222: xnm.y(obj);
  223: } else {
  224: if (b != 2) {
  225: k3g.o("call to 'resume' before 'invoke' with coroutine");
  226: return null;
  227: }
  228: kv4VarV = (kv4) this.h;
  229: q53Var = (q53) this.g;
  230: xnm.y(obj);
  231: }
  232: zBooleanValue = ((Boolean) obj).booleanValue();
  233: vv6Var = zw3Var.X;
  234: if (zBooleanValue) {
  235: vv6Var.e(a04.A(a04.b, kv4VarV.v(), l5l.m, null, null, 28));
  236: return s1kVar;
  237: }
  238: vv6Var.e(a04.l(a04.b, q53Var.a, null, null, 14));
  239: return s1kVar;
  240: q53 q53Var2 = (q53) obj;
  241: kv4VarV = q53Var2 != null ? q53Var2.v() : null;
  242: if (q53Var2 == null \|\| kv4VarV == null \|\| !kv4VarV.F()) {
  243: zw3Var.Y.e(new smh(new mdj(R.string.chat_list_bot_cannot_open_web_app), num, objArr == true ? 1 : 0, 6));
  244: return s1kVar;
  245: }
  246: zm9[] zm9VarArr2 = zw3.p1;
  247: z24 z24Var = (z24) zw3Var.E.getValue();
  248: long jV = kv4VarV.v();
  249: this.g = q53Var2;
  250: this.h = kv4VarV;
  251: this.f = (byte) 2;
  252: Object objA = z24Var.a(jV, this);
  253: if (objA != ka5Var) {
  254: obj = objA;
  255: q53Var = q53Var2;
  256: zBooleanValue = ((Boolean) obj).booleanValue();
  257: vv6Var = zw3Var.X;
  258: if (zBooleanValue) {
  259: vv6Var.e(a04.l(a04.b, q53Var.a, null, null, 14));
  260: return s1kVar;
  261: }
  262: vv6Var.e(a04.A(a04.b, kv4VarV.v(), l5l.m, null, null, 28));
  263: return s1kVar;
  264: }
  265: return ka5Var;
  266: }
  267: 
  268: /* JADX WARN: Code duplicated, block: B:20:0x0052  */
  269: /* JADX WARN: Code duplicated, block: B:49:0x00e7  */
  270: /* JADX WARN: Code duplicated, block: B:53:0x0117  */
  271: /* JADX WARN: Code duplicated, block: B:62:0x0146  */
  272: /* JADX WARN: Code duplicated, block: B:63:0x0147  */
  273: /* JADX WARN: Code duplicated, block: B:75:0x0186  */
  274: /* JADX WARN: Code restructure failed: missing block: B:65:0x0161, code lost:
  275: 
  276: if (r0.z(r1, r23) == r7) goto L66;
  277: */
  278: /*
  279: Code decompiled incorrectly, please refer to instructions dump.
  280: */
  281: private final Object E(Object obj) throws Exception {
  282: Object objR;
  283: d7b d7bVar;
  284: kc4 kc4Var;
  285: gt gtVar;
  286: gt gtVar2;
  287: gt gtVar3;
  288: s1k s1kVar = s1k.a;
  289: pdb pdbVar = pdb.DELETED;
  290: ka5 ka5Var = ka5.a;
  291: byte b = this.f;
  292: try {
  293: if (b == 0) {
  294: xnm.y(obj);
  295: od4 od4Var = (od4) this.i;
  296: o1d o1dVar = f09.g;
  297: if (o1dVar != null) {
  298: c6a c6aVar = c6a.d;
  299: if (o1dVar.b(c6aVar)) {
  300: o1dVar.c(c6aVar, "CommentSendApiTask", "onSuccess: commentsId=" + od4Var.f + ", messageId=" + od4Var.g, null);
  301: }
  302: }
  303: gt gtVar4 = ((od4) this.i).e;
  304: if (gtVar4 == null) {
  305: gtVar4 = null;
  306: }
  307: ph4 ph4VarG = gtVar4.g();
  308: long j = ((od4) this.i).g;
  309: this.f = (byte) 1;
  310: objR = ph4VarG.r(j, this);
  311: if (objR != ka5Var) {
  312: }
  313: return ka5Var;
  314: }
  315: if (b != 1) {
  316: if (b == 2) {
  317: d7bVar = (d7b) this.h;
  318: kc4Var = (kc4) this.g;
  319: xnm.y(obj);
  320: s1kVar = s1kVar;
  321: gtVar = ((od4) this.i).e;
  322: if (gtVar == null) {
  323: gtVar = null;
  324: }
  325: zsc zscVarA = gtVar.a();
  326: tg4 tg4Var = ((od4) this.i).f;
  327: zscVarA.k(tg4Var.a, tg4Var.b, s95.x(kc4Var.a), s95.x(d7bVar.a));
  328: f09.p("CommentSendApiTask", "onSuccess: sent api request for deletion locally deleted message");
  329: gtVar2 = ((od4) this.i).e;
  330: if (gtVar2 == null) {
  331: gtVar2 = null;
  332: }
  333: wud.k(gtVar2.j(), hzb.X, ((od4) this.i).h, null, 28);
  334: return s1kVar;
  335: }
  336: if (b == 3) {
  337: xnm.y(obj);
  338: s1kVar = s1kVar;
  339: gtVar3 = ((od4) this.i).e;
  340: if (gtVar3 != null) {
```

### defpackage/lp4.java
Строки 1–216:
```java
    1: package defpackage;
    2: 
    3: import java.util.concurrent.atomic.AtomicReference;
    4: import kotlin.collections.a;
    5: import me.leolin.shortcutbadger.BuildConfig;
    6: import ru.oneme.app.R;
    7: 
    8: /* JADX INFO: loaded from: classes2.dex */
    9: public final class lp4 extends oyk implements fs4 {
   10: public static final /* synthetic */ zm9[] x = {new c4c(lp4.class, "pollingJob", "getPollingJob()Lkotlinx/coroutines/Job;"), a15.f(luf.a, lp4.class, "refreshJob", "getRefreshJob()Lkotlinx/coroutines/Job;"), new c4c(lp4.class, "timerJob", "getTimerJob()Lkotlinx/coroutines/Job;")};
   11: public final /* synthetic */ qyk c;
   12: public final rp9 d;
   13: public final rp9 e;
   14: public final rp9 f;
   15: public final rp9 g;
   16: public final rp9 h;
   17: public final rp9 i;
   18: public final rp9 j;
   19: public final rp9 k;
   20: public final rp9 l;
   21: public final r4i m;
   22: public final dmf n;
   23: public final r4i o;
   24: public final dmf p;
   25: public final vv6 q;
   26: public final vv6 r;
   27: public final AtomicReference s;
   28: public final AtomicReference t;
   29: public final z9g u;
   30: public final z9g v;
   31: public final z9g w;
   32: 
   33: public lp4(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9, rp9 rp9Var10) {
   34: qyk qykVar = new qyk(rp9Var, new u23((byte) 26));
   35: this.c = qykVar;
   36: this.d = rp9Var2;
   37: this.e = rp9Var3;
   38: this.f = rp9Var4;
   39: this.g = rp9Var5;
   40: this.h = rp9Var6;
   41: this.i = rp9Var7;
   42: this.j = rp9Var8;
   43: this.k = rp9Var9;
   44: this.l = rp9Var10;
   45: r4i r4iVarC = az7.c(null);
   46: this.m = r4iVarC;
   47: this.n = new dmf(r4iVarC);
   48: r4i r4iVarC2 = az7.c(rdj.b);
   49: this.o = r4iVarC2;
   50: this.p = new dmf(r4iVarC2);
   51: this.q = new vv6(null);
   52: this.r = new vv6(null);
   53: this.s = new AtomicReference();
   54: this.t = new AtomicReference();
   55: this.u = c45.Q();
   56: this.v = c45.Q();
   57: this.w = c45.Q();
   58: e0c.M(h6c.p(new dk7(new c30(qykVar.d, (byte) 12), new zk3((Object) this, (b55) null, (byte) 13), (byte) 3), ((vxc) ((k6j) rp9Var2.getValue())).a()), this.b);
   59: }
   60: 
   61: @Override // defpackage.oyk
   62: public final void a1() {
   63: zm9[] zm9VarArr = x;
   64: this.w.y(this, zm9VarArr[2], null);
   65: this.u.y(this, zm9VarArr[0], null);
   66: this.v.y(this, zm9VarArr[1], null);
   67: }
   68: 
   69: public final void c1() {
   70: u12 u12Var = new u12(new mdj(R.string.oneme_login_confirm_callout_refresh_button));
   71: r4i r4iVar = this.m;
   72: r4iVar.getClass();
   73: r4iVar.j(null, u12Var);
   74: kf9 kf9Var = (kf9) this.u.s(this, x[0]);
   75: if (kf9Var != null) {
   76: kf9Var.m(null);
   77: }
   78: kf9 kf9VarF1 = f1();
   79: if (kf9VarF1 != null) {
   80: kf9VarF1.m(null);
   81: }
   82: mdj mdjVar = new mdj(R.string.oneme_login_confirm_callout_time_expired);
   83: r4i r4iVar2 = this.o;
   84: r4iVar2.getClass();
   85: r4iVar2.j(null, mdjVar);
   86: }
   87: 
   88: /* JADX WARN: Code duplicated, block: B:7:0x0019  */
   89: public final Object d1(q12 q12Var, String str, d55 d55Var) {
   90: jp4 jp4Var;
   91: String str2 = str;
   92: if (d55Var instanceof jp4) {
   93: jp4Var = (jp4) d55Var;
   94: int i = jp4Var.g;
   95: if ((i & Integer.MIN_VALUE) != 0) {
   96: jp4Var.g = i - Integer.MIN_VALUE;
   97: } else {
   98: jp4Var = new jp4(this, d55Var);
   99: }
  100: } else {
  101: jp4Var = new jp4(this, d55Var);
  102: }
  103: Object objA = jp4Var.e;
  104: ka5 ka5Var = ka5.a;
  105: int i2 = jp4Var.g;
  106: if (i2 == 0) {
  107: xnm.y(objA);
  108: fh0 fh0Var = (fh0) this.g.getValue();
  109: String str3 = q12Var.a;
  110: jp4Var.d = str2;
  111: jp4Var.g = 1;
  112: objA = fh0Var.a(str3, str2, jp4Var);
  113: if (objA == ka5Var) {
  114: return ka5Var;
  115: }
  116: } else {
  117: if (i2 != 1) {
  118: k3g.o("call to 'resume' before 'invoke' with coroutine");
  119: return null;
  120: }
  121: str2 = jp4Var.d;
  122: xnm.y(objA);
  123: }
  124: String str4 = str2;
  125: eh0 eh0Var = (eh0) objA;
  126: if (eh0Var instanceof dh0) {
  127: azc azcVar = ((dh0) eh0Var).a;
  128: ii0 ii0Var = azcVar != null ? (ii0) azcVar.e : ii0.e;
  129: m8a m8aVar = m8a.b;
  130: String str5 = azcVar != null ? (String) azcVar.b : null;
  131: String str6 = str5 == null ? BuildConfig.FLAVOR : str5;
  132: String str7 = azcVar != null ? (String) azcVar.c : null;
  133: String str8 = str7 == null ? BuildConfig.FLAVOR : str7;
  134: String str9 = azcVar != null ? (String) azcVar.d : null;
  135: this.q.e(new o12(m8aVar.m(str6, str8, str9 == null ? BuildConfig.FLAVOR : str9, str4, ii0Var.b, ii0Var.c, ii0Var.d)));
  136: } else if (g4a.c(eh0Var, ah0.a)) {
  137: this.q.e(l12.b);
  138: } else if (eh0Var instanceof ch0) {
  139: ch0 ch0Var = (ch0) eh0Var;
  140: this.q.e(new m12(ch0Var.a, ch0Var.b));
  141: } else {
  142: if (!g4a.c(eh0Var, bh0.a)) {
  143: k3g.l();
  144: return null;
  145: }
  146: String name = lp4.class.getName();
  147: o1d o1dVar = f09.g;
  148: if (o1dVar != null) {
  149: c6a c6aVar = c6a.f;
  150: if (o1dVar.b(c6aVar)) {
  151: o1dVar.c(c6aVar, name, "authByTrackUseCase execute: return None", null);
  152: }
  153: }
  154: this.q.e(k12.b);
  155: }
  156: return s1k.a;
  157: }
  158: 
  159: public final String e1(String str) {
  160: return hui.X(hui.X(fa5.s((mxd) this.j.getValue(), str, null, null), '-', (char) 160, false), ' ', (char) 160, false);
  161: }
  162: 
  163: @Override // defpackage.fs4
  164: public final cmf f0() {
  165: return this.c.d;
  166: }
  167: 
  168: public final kf9 f1() {
  169: return (kf9) this.w.s(this, x[2]);
  170: }
  171: 
  172: public final void g1(q12 q12Var, String str, String str2) {
  173: AtomicReference atomicReference = this.s;
  174: q12 q12Var2 = (q12) atomicReference.get();
  175: if (q12Var2 != null) {
  176: q12Var = q12Var2;
  177: }
  178: AtomicReference atomicReference2 = this.t;
  179: String str3 = (String) atomicReference2.get();
  180: if (str3 != null) {
  181: str2 = str3;
  182: }
  183: atomicReference.set(q12Var);
  184: atomicReference2.set(str2);
  185: r4i r4iVar = this.m;
  186: if (r4iVar.getValue() == null) {
  187: s12 s12Var = new s12(new odj(R.string.oneme_login_confirm_callout_button, a.l0(new Object[]{e1(str2)})));
  188: r4iVar.getClass();
  189: r4iVar.j(null, s12Var);
  190: }
  191: kf9 kf9Var = (kf9) this.u.s(this, x[0]);
  192: if (kf9Var == null \|\| !kf9Var.a()) {
  193: h1(q12Var, str);
  194: }
  195: if ((r4iVar.getValue() instanceof u12) \|\| (r4iVar.getValue() instanceof t12)) {
  196: return;
  197: }
  198: i1(q12Var.b);
  199: }
  200: 
  201: public final void h1(q12 q12Var, String str) {
  202: if (q12Var.b < ((hog) ((c74) this.e.getValue())).f()) {
  203: return;
  204: }
  205: g0i g0iVar = (g0i) this.c.a(this.b, ((vxc) ((k6j) this.d.getValue())).b(), 2, new cq3((Object) this, (Object) q12Var, (Object) str, (b55) null, (byte) 10));
  206: this.u.y(this, x[0], g0iVar);
  207: }
  208: 
  209: public final void i1(long j) {
  210: r4i r4iVar = this.o;
  211: r4iVar.getClass();
  212: r4iVar.j(null, rdj.b);
  213: g0i g0iVarZ0 = oyk.Z0(this, null, new gu(j, (Object) this, (b55) null, (byte) 13), 1);
  214: this.w.y(this, x[2], g0iVarZ0);
  215: }
  216: }
```

### defpackage/ph0.java
Строки 1–16:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class ph0 {
    5: public final rp9 a;
    6: public final rp9 b;
    7: 
    8: public ph0(rp9 rp9Var, rp9 rp9Var2) {
    9: this.a = rp9Var;
   10: this.b = rp9Var2;
   11: }
   12: 
   13: public final xeg a(long j, long j2, String str) {
   14: return new xeg(new oh0(this, j, str, j2, null));
   15: }
   16: }
```

### defpackage/q79.java
Строки 1–88:
```java
    1: package defpackage;
    2: 
    3: import ru.oneme.app.R;
    4: 
    5: /* JADX INFO: loaded from: classes2.dex */
    6: public final class q79 implements ri7 {
    7: public final /* synthetic */ u79 a;
    8: public final /* synthetic */ c b;
    9: public final /* synthetic */ String c;
   10: public final /* synthetic */ long d;
   11: 
   12: public q79(u79 u79Var, c cVar, String str, long j) {
   13: this.a = u79Var;
   14: this.b = cVar;
   15: this.c = str;
   16: this.d = j;
   17: }
   18: 
   19: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
   20: /* JADX WARN: Code restructure failed: missing block: B:22:0x0068, code lost:
   21: 
   22: if (r6.c1(r2, r10.c, r0) == r7) goto L29;
   23: */
   24: /* JADX WARN: Code restructure failed: missing block: B:28:0x0088, code lost:
   25: 
   26: if (r10.b(r11, r0) == r7) goto L29;
   27: */
   28: @Override // defpackage.ri7
   29: /* JADX INFO: renamed from: a, reason: merged with bridge method [inline-methods] */
   30: /*
   31: Code decompiled incorrectly, please refer to instructions dump.
   32: */
   33: public final Object b(nh0 nh0Var, b55 b55Var) {
   34: p79 p79Var;
   35: if (b55Var instanceof p79) {
   36: p79Var = (p79) b55Var;
   37: int i = p79Var.f;
   38: if ((i & Integer.MIN_VALUE) != 0) {
   39: p79Var.f = i - Integer.MIN_VALUE;
   40: } else {
   41: p79Var = new p79(this, b55Var);
   42: }
   43: } else {
   44: p79Var = new p79(this, b55Var);
   45: }
   46: x95 x95Var = p79Var.b;
   47: Object obj = p79Var.d;
   48: int i2 = p79Var.f;
   49: if (i2 == 0) {
   50: xnm.y(obj);
   51: boolean z = nh0Var instanceof kh0;
   52: c cVar = this.b;
   53: u79 u79Var = this.a;
   54: if (!z) {
   55: boolean z2 = nh0Var instanceof lh0;
   56: ka5 ka5Var = ka5.a;
   57: if (z2) {
   58: p79Var.f = 1;
   59: } else if (nh0Var instanceof mh0) {
   60: nih nihVar = u79Var.m;
   61: s7a s7aVar = new s7a(new mdj(R.string.oneme_login_call_out_common_error), null, true);
   62: p79Var.f = 2;
   63: } else if (!g4a.c(nh0Var, jh0.a)) {
   64: k3g.l();
   65: return null;
   66: }
   67: return ka5Var;
   68: }
   69: vv6 vv6Var = u79Var.l;
   70: String str = cVar.b;
   71: int i3 = cVar.d;
   72: String str2 = ((kh0) nh0Var).a;
   73: vv6Var.e(new c79(i3, this.d, this.c, str, str2));
   74: lkh.S(x95Var);
   75: } else if (i2 == 1) {
   76: xnm.y(obj);
   77: lkh.S(x95Var);
   78: } else {
   79: if (i2 != 2) {
   80: k3g.o("call to 'resume' before 'invoke' with coroutine");
   81: return null;
   82: }
   83: xnm.y(obj);
   84: lkh.S(x95Var);
   85: }
   86: return s1k.a;
   87: }
   88: }
```

### defpackage/c.java
Строки 1–55:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class c {
    5: public final /* synthetic */ byte a;
    6: public String b;
    7: public int c;
    8: public int d;
    9: 
   10: public c(int i, int i2, String str) {
   11: this.a = (byte) 0;
   12: this.c = i;
   13: this.d = i2;
   14: this.b = str;
   15: }
   16: 
   17: public int a() {
   18: return this.d;
   19: }
   20: 
   21: public String b() {
   22: return this.b;
   23: }
   24: 
   25: public String c() {
   26: return this.b;
   27: }
   28: 
   29: public int d() {
   30: return this.c;
   31: }
   32: 
   33: public String toString() {
   34: switch (this.a) {
   35: case 1:
   36: return w7g.t("CallOutVerificationParams(ttl=", this.c, ", pollingInterval=", this.d, ")");
   37: default:
   38: return super.toString();
   39: }
   40: }
   41: 
   42: public /* synthetic */ c(String str, int i, int i2, byte b) {
   43: this.a = b;
   44: this.b = str;
   45: this.c = i;
   46: this.d = i2;
   47: }
   48: 
   49: public c(String str, int i, int i2, int i3, long j) {
   50: this.a = (byte) 2;
   51: this.b = str;
   52: this.d = i;
   53: this.c = i2;
   54: }
   55: }
```

### defpackage/d2c.java
Строки 1–230:
```java
    1: package defpackage;
    2: 
    3: import java.util.ArrayList;
    4: import java.util.Collection;
    5: import java.util.Iterator;
    6: import java.util.Map;
    7: import me.leolin.shortcutbadger.BuildConfig;
    8: 
    9: /* JADX INFO: loaded from: classes.dex */
   10: public final class d2c {
   11: public final r1c a;
   12: public final s1c b;
   13: public final String c = d2c.class.getName();
   14: public final z3j d = new z3j(new wz7(17));
   15: public final dmf e;
   16: public final dmf f;
   17: public final dmf g;
   18: 
   19: public d2c(p9g p9gVar, r1c r1cVar, s1c s1cVar) {
   20: this.a = r1cVar;
   21: this.b = s1cVar;
   22: b55 b55Var = null;
   23: byte b = 0;
   24: byte b2 = 3;
   25: dk7 dk7Var = new dk7(new c30(j8.b, (byte) 17), new u1c(this, b55Var, b), b2);
   26: qzd qzdVar = hjh.a;
   27: sp6 sp6Var = sp6.a;
   28: dmf dmfVarL0 = tul.l0(dk7Var, p9gVar, qzdVar, sp6Var);
   29: this.e = dmfVarL0;
   30: byte b3 = 1;
   31: this.f = tul.l0(new dk7(new b2c(xk7.e(dmfVarL0, new qd2(b2, b55Var, (byte) 5)), b), new u1c(this, b55Var, b3), b2), p9gVar, qzdVar, sp6Var);
   32: this.g = tul.l0(new b2c(xk7.e(dmfVarL0, new qd2(b2, b55Var, (byte) 6)), b3), p9gVar, qzdVar, 0);
   33: nm9.J(p9gVar, null, 0, new y77(this, b55Var, (byte) 23), 3);
   34: }
   35: 
   36: public final q1a a(long j) {
   37: q1a q1aVar;
   38: Iterator it = ((Map) this.f.a.getValue()).entrySet().iterator();
   39: do {
   40: q1aVar = null;
   41: if (!it.hasNext()) {
   42: break;
   43: }
   44: Map.Entry entry = (Map.Entry) it.next();
   45: if (((hog) ((p1c) entry.getValue()).a()).s() == j) {
   46: q1aVar = (q1a) entry.getKey();
   47: }
   48: } while (q1aVar == null);
   49: return q1aVar;
   50: }
   51: 
   52: public final q1a b() {
   53: q1a q1aVar;
   54: q1a q1aVar2;
   55: Iterator it = ((Map) this.f.a.getValue()).entrySet().iterator();
   56: do {
   57: q1aVar = null;
   58: if (!it.hasNext()) {
   59: q1aVar2 = null;
   60: break;
   61: }
   62: q1aVar2 = (q1a) ((Map.Entry) it.next()).getKey();
   63: } while (q1aVar2 == null);
   64: if (q1aVar2 != null) {
   65: return q1aVar2;
   66: }
   67: Iterator it2 = ((Map) this.e.a.getValue()).entrySet().iterator();
   68: while (it2.hasNext()) {
   69: q1a q1aVar3 = (q1a) ((Map.Entry) it2.next()).getKey();
   70: if (q1aVar3 != null) {
   71: q1aVar = q1aVar3;
   72: break;
   73: }
   74: }
   75: return q1aVar == null ? q1a.b : q1aVar;
   76: }
   77: 
   78: /* JADX WARN: Code duplicated, block: B:27:0x0086  */
   79: /* JADX WARN: Code duplicated, block: B:29:0x009f  */
   80: /* JADX WARN: Code duplicated, block: B:30:0x00a2  */
   81: /* JADX WARN: Code duplicated, block: B:33:0x00b3 A[Catch: all -> 0x0044, CancellationException -> 0x00e5, TRY_ENTER, TRY_LEAVE, TryCatch #2 {CancellationException -> 0x00e5, all -> 0x0044, blocks: (B:13:0x003f, B:33:0x00b3), top: B:66:0x003f }] */
   82: /* JADX WARN: Code duplicated, block: B:62:0x012f  */
   83: /* JADX WARN: Code duplicated, block: B:7:0x0017  */
   84: /* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:34:0x00d8 -> B:36:0x00db). Please report as a decompilation issue!!! */
   85: /* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:39:0x00e7 -> B:36:0x00db). Please report as a decompilation issue!!! */
   86: /*  JADX ERROR: JadxOverflowException in pass: RegionMakerVisitor
   87: jadx.core.utils.exceptions.JadxOverflowException: Regions stack size limit reached
   88: at jadx.core.utils.ErrorsCounter.addError(ErrorsCounter.java:59)
   89: at jadx.core.utils.ErrorsCounter.error(ErrorsCounter.java:31)
   90: at jadx.core.dex.attributes.nodes.NotificationAttrNode.addError(NotificationAttrNode.java:19)
   91: */
   92: public final java.lang.Object c(defpackage.q1a r21, defpackage.d55 r22) {
   93: /*
   94: Method dump skipped, instruction units count: 312
   95: To view this dump add '--comments-level debug' option
   96: */
   97: throw new UnsupportedOperationException("Method not decompiled: defpackage.d2c.c(q1a, d55):java.lang.Object");
   98: }
   99: 
  100: public final ArrayList d() {
  101: Map map = (Map) this.f.a.getValue();
  102: ArrayList arrayList = new ArrayList();
  103: Iterator it = map.entrySet().iterator();
  104: while (it.hasNext()) {
  105: long jS = ((hog) ((p1c) ((Map.Entry) it.next()).getValue()).a()).s();
  106: Long lValueOf = Long.valueOf(jS);
  107: if (jS == -1) {
  108: lValueOf = null;
  109: }
  110: if (lValueOf != null) {
  111: arrayList.add(lValueOf);
  112: }
  113: }
  114: return arrayList;
  115: }
  116: 
  117: public final boolean e() {
  118: return ((Map) this.f.a.getValue()).size() < ((Number) this.g.a.getValue()).intValue();
  119: }
  120: 
  121: public final boolean f() {
  122: return ((Map) this.f.a.getValue()).size() > 1;
  123: }
  124: 
  125: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  126: public final Object g(String str, d55 d55Var) {
  127: w1c w1cVar;
  128: String str2;
  129: if (d55Var instanceof w1c) {
  130: w1cVar = (w1c) d55Var;
  131: int i = w1cVar.g;
  132: if ((i & Integer.MIN_VALUE) != 0) {
  133: w1cVar.g = i - Integer.MIN_VALUE;
  134: } else {
  135: w1cVar = new w1c(this, d55Var);
  136: }
  137: } else {
  138: w1cVar = new w1c(this, d55Var);
  139: }
  140: Object objR = w1cVar.e;
  141: int i2 = w1cVar.g;
  142: z3j z3jVar = this.d;
  143: boolean z = true;
  144: if (i2 == 0) {
  145: xnm.y(objR);
  146: String strC = ((xuf) z3jVar.getValue()).c(str, BuildConfig.FLAVOR);
  147: if (strC.length() == 0) {
  148: return Boolean.FALSE;
  149: }
  150: w1cVar.d = strC;
  151: w1cVar.g = 1;
  152: objR = hzj.R(this.f, w1cVar);
  153: ka5 ka5Var = ka5.a;
  154: if (objR == ka5Var) {
  155: return ka5Var;
  156: }
  157: str2 = strC;
  158: } else {
  159: if (i2 != 1) {
  160: k3g.o("call to 'resume' before 'invoke' with coroutine");
  161: return null;
  162: }
  163: str2 = w1cVar.d;
  164: xnm.y(objR);
  165: }
  166: Collection collectionValues = ((Map) objR).values();
  167: if ((collectionValues instanceof Collection) && collectionValues.isEmpty()) {
  168: z = false;
  169: } else {
  170: Iterator it = collectionValues.iterator();
  171: while (it.hasNext()) {
  172: String strT = ((n3a) ((p1c) it.next()).a()).T();
  173: if (g4a.c(strT != null ? ((xuf) z3jVar.getValue()).c(strT, BuildConfig.FLAVOR) : null, str2)) {
  174: }
  175: }
  176: z = false;
  177: }
  178: return Boolean.valueOf(z);
  179: }
  180: 
  181: public final q1a h() {
  182: q1a q1aVar;
  183: q1a q1aVar2;
  184: c6a c6aVar = c6a.d;
  185: f09.E(this.c, "getNotLoggedInAccountId()", null);
  186: Map map = (Map) this.e.a.getValue();
  187: Iterator it = map.entrySet().iterator();
  188: do {
  189: if (!it.hasNext()) {
  190: q1aVar = null;
  191: break;
  192: }
  193: Map.Entry entry = (Map.Entry) it.next();
  194: q1aVar = (q1a) entry.getKey();
  195: if (((hog) ((p1c) entry.getValue()).a()).s() != -1) {
  196: q1aVar = null;
  197: }
  198: } while (q1aVar == null);
  199: if (q1aVar != null) {
  200: String str = this.c;
  201: o1d o1dVar = f09.g;
  202: if (o1dVar != null && o1dVar.b(c6aVar)) {
  203: o1dVar.c(c6aVar, str, "getNotLoggedInAccountId() reuse account " + q1aVar, null);
  204: }
  205: return q1aVar;
  206: }
  207: m99 m99Var = new m99(0, Integer.MAX_VALUE, 1);
  208: qib qibVar = new qib((byte) 6);
  209: Iterator it2 = m99Var.iterator();
  210: do {
  211: l99 l99Var = (l99) it2;
  212: if (!l99Var.c) {
  213: k3g.h("Sequence contains no element matching the predicate.");
  214: return null;
  215: }
  216: q1aVar2 = (q1a) qibVar.d(l99Var.next());
  217: } while (map.get(q1aVar2) != null);
  218: String str2 = this.c;
  219: o1d o1dVar2 = f09.g;
  220: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
  221: o1dVar2.c(c6aVar, str2, "getNotLoggedInAccountId() creating new " + q1aVar2, null);
  222: }
  223: so soVar = this.b.f;
  224: btc btcVar = (btc) (soVar != null ? soVar : null).d(q1aVar2);
  225: btcVar.b();
  226: btcVar.a();
  227: btcVar.c();
  228: return q1aVar2;
  229: }
  230: }
```

### defpackage/fh0.java
Строки 1–20:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class fh0 {
    5: public final rp9 a;
    6: public final rp9 b;
    7: public final rp9 c;
    8: public final rp9 d;
    9: 
   10: public fh0(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4) {
   11: this.a = rp9Var;
   12: this.b = rp9Var2;
   13: this.c = rp9Var3;
   14: this.d = rp9Var4;
   15: }
   16: 
   17: public final Object a(String str, String str2, d55 d55Var) {
   18: return nm9.i0(((vxc) ((k6j) this.b.getValue())).b(), new wi(this, str, str2, null, (byte) 3), d55Var);
   19: }
   20: }
```

### defpackage/b79.java
Строки 1–110:
```java
    1: package defpackage;
    2: 
    3: import android.content.Context;
    4: import java.util.Iterator;
    5: import java.util.List;
    6: import me.leolin.shortcutbadger.BuildConfig;
    7: import ru.oneme.app.R;
    8: 
    9: /* JADX INFO: loaded from: classes.dex */
   10: public final class b79 {
   11: public static final /* synthetic */ zm9[] m;
   12: public final rp9 a;
   13: public final rp9 b;
   14: public final rp9 c;
   15: public final r4i e;
   16: public final nih g;
   17: public final cmf h;
   18: public final xuf i;
   19: public final r4i j;
   20: public final dmf k;
   21: public final e4c l;
   22: public final z9g d = c45.Q();
   23: public final r4i f = az7.c(BuildConfig.FLAVOR);
   24: 
   25: static {
   26: c4c c4cVar = new c4c(b79.class, "availableCountriesJob", "getAvailableCountriesJob()Lkotlinx/coroutines/Job;");
   27: luf.a.getClass();
   28: m = new zm9[]{c4cVar};
   29: }
   30: 
   31: public b79(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, Context context) {
   32: this.a = rp9Var;
   33: this.b = rp9Var2;
   34: this.c = rp9Var3;
   35: this.e = az7.c(new fyc("RU", 7, context.getString(R.string.oneme_russia_name), null));
   36: nih nihVarC = fa5.c(0, Integer.MAX_VALUE, 4);
   37: this.g = nihVarC;
   38: this.h = new cmf(nihVarC);
   39: this.i = new xuf("[^0-9+]");
   40: r4i r4iVarC = az7.c(qp6.a);
   41: this.j = r4iVarC;
   42: this.k = new dmf(r4iVarC);
   43: qdj qdjVarJ = wdc.j("123 4567 8901");
   44: qdj qdjVarJ2 = wdc.j("473 123 4567");
   45: qdj qdjVarJ3 = wdc.j("12 3456 7890");
   46: qdj qdjVarJ4 = wdc.j("9 123 456 789");
   47: qdj qdjVarJ5 = wdc.j("1 234 567");
   48: qdj qdjVarJ6 = wdc.j("869 123 4567");
   49: e4c e4cVar = new e4c(6);
   50: e4cVar.k("ID", qdjVarJ);
   51: e4cVar.k("GD", qdjVarJ2);
   52: e4cVar.k("EG", qdjVarJ3);
   53: e4cVar.k("MM", qdjVarJ4);
   54: e4cVar.k("LB", qdjVarJ5);
   55: e4cVar.k("KN", qdjVarJ6);
   56: this.l = e4cVar;
   57: }
   58: 
   59: public final qi7 a(e18 e18Var) {
   60: return h6c.p(new ol7(new u3(this.f, this, (byte) 24), new ol7(this.e, e18Var, this, (byte) 2), new x69(3, null), (byte) 0), ((vxc) ((k6j) this.c.getValue())).a());
   61: }
   62: 
   63: public final dmf b(t45 t45Var) {
   64: r4i r4iVar = this.e;
   65: return tul.l0(new ol7(r4iVar, t45Var, this, (byte) 3), t45Var, hjh.a, new ab5((fyc) r4iVar.getValue(), Integer.MAX_VALUE, new mdj(R.string.oneme_default_phone_hint)));
   66: }
   67: 
   68: public final void c(String str, String str2) {
   69: Object next;
   70: r4i r4iVar = this.f;
   71: r4iVar.getClass();
   72: r4iVar.j(null, str2);
   73: String strM = fa5.m(str.concat(str2));
   74: if (strM != null) {
   75: Iterator it = ((Iterable) this.k.a.getValue()).iterator();
   76: do {
   77: if (!it.hasNext()) {
   78: next = null;
   79: break;
   80: }
   81: next = it.next();
   82: } while (!g4a.c(((fyc) next).a, strM));
   83: fyc fycVar = (fyc) next;
   84: if (fycVar == null) {
   85: return;
   86: }
   87: r4i r4iVar2 = this.e;
   88: r4iVar2.getClass();
   89: r4iVar2.j(null, fycVar);
   90: }
   91: }
   92: 
   93: public final void d(fyc fycVar, boolean z) {
   94: int i = fycVar.b;
   95: if (z && i == 7) {
   96: String strM = fa5.m("+" + i + this.f.getValue());
   97: if (strM != null && !strM.equals(fycVar.a)) {
   98: this.g.l(u69.a);
   99: }
  100: }
  101: r4i r4iVar = this.e;
  102: r4iVar.getClass();
  103: r4iVar.j(null, fycVar);
  104: }
  105: 
  106: public final void e(ja5 ja5Var, List list) {
  107: g0i g0iVarM = e0c.M(h6c.p(new dk7(new u3(((lvf) this.a.getValue()).f, list, (byte) 25), new yj3((Object) this, (b55) null, (byte) 11), (byte) 3), ((vxc) ((k6j) this.c.getValue())).a()), ja5Var);
  108: this.d.y(this, m[0], g0iVarM);
  109: }
  110: }
```

### defpackage/s79.java
Строки 1–22:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class s79 extends d55 {
    5: public String d;
    6: public /* synthetic */ Object e;
    7: public final /* synthetic */ u79 f;
    8: public int g;
    9: 
   10: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   11: public s79(u79 u79Var, d55 d55Var) {
   12: super(d55Var);
   13: this.f = u79Var;
   14: }
   15: 
   16: @Override // defpackage.hv0
   17: public final Object w(Object obj) {
   18: this.e = obj;
   19: this.g \|= Integer.MIN_VALUE;
   20: return this.f.c1(null, null, this);
   21: }
   22: }
```

### defpackage/xfg.java
Строки 1–250:
```java
    1: package defpackage;
    2: 
    3: import android.animation.ValueAnimator;
    4: import android.content.Context;
    5: import android.content.res.ColorStateList;
    6: import android.graphics.Bitmap;
    7: import android.graphics.Rect;
    8: import android.graphics.RectF;
    9: import android.net.Uri;
   10: import android.transition.TransitionManager;
   11: import android.view.View;
   12: import android.view.ViewGroup;
   13: import android.view.ViewOutlineProvider;
   14: import android.view.ViewParent;
   15: import android.widget.ImageView;
   16: import android.widget.LinearLayout;
   17: import androidx.recyclerview.widget.RecyclerView;
   18: import com.bluelinelabs.conductor.j;
   19: import java.io.File;
   20: import java.io.FileInputStream;
   21: import java.io.FileOutputStream;
   22: import java.io.IOException;
   23: import java.io.InputStream;
   24: import java.util.ArrayList;
   25: import java.util.Collection;
   26: import java.util.Iterator;
   27: import java.util.List;
   28: import java.util.Set;
   29: import java.util.UUID;
   30: import java.util.WeakHashMap;
   31: import java.util.concurrent.atomic.AtomicLong;
   32: import java.util.zip.Inflater;
   33: import java.util.zip.InflaterInputStream;
   34: import kotlin.collections.a;
   35: import one.me.calls.ui.bottomsheet.ratecall.CallRateBottomSheet;
   36: import one.me.calls.ui.ui.call.panels.CallBottomPanelWidget;
   37: import one.me.calls.ui.ui.call.panels.CallEventsWidget;
   38: import one.me.chats.forward.ForwardPickerScreen;
   39: import one.me.chats.picker.contacts.ContactsPickerScreen;
   40: import one.me.chatscreen.ChatScreen;
   41: import one.me.chatscreen.chatpreview.ChatPreviewBottomWidget;
   42: import one.me.contactadddialog.ContactAddBottomSheet;
   43: import one.me.keyboardmedia.MediaKeyboardWidget;
   44: import one.me.mediaeditor.editandreply.EditAndReplyScreen;
   45: import one.me.profile.screens.addmembers.AddChatMembersScreen;
   46: import one.me.sdk.arch.Widget;
   47: import one.me.sdk.messagewrite.MessageWriteWidget;
   48: import org.webrtc.PeerConnection;
   49: import org.webrtc.PeerConnectionFactory;
   50: import ru.ok.tamtam.exception.IssueKeyException;
   51: import ru.oneme.app.R;
   52: 
   53: /* JADX INFO: loaded from: classes2.dex */
   54: public final class xfg extends x1j implements e18 {
   55: public final /* synthetic */ byte e;
   56: public /* synthetic */ Object f;
   57: public final /* synthetic */ Object g;
   58: public final /* synthetic */ Object h;
   59: 
   60: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   61: public /* synthetic */ xfg(Object obj, Object obj2, Object obj3, b55 b55Var, byte b) {
   62: super(2, b55Var);
   63: this.e = b;
   64: this.f = obj;
   65: this.g = obj2;
   66: this.h = obj3;
   67: }
   68: 
   69: private final Object A(Object obj) {
   70: int iIntValue;
   71: h3j h3jVar;
   72: ContactAddBottomSheet contactAddBottomSheet = (ContactAddBottomSheet) this.g;
   73: Object obj2 = this.f;
   74: xnm.y(obj);
   75: if (((y6c) obj2) instanceof q74) {
   76: zm9[] zm9VarArr = ContactAddBottomSheet.x;
   77: qv4 qv4Var = (qv4) contactAddBottomSheet.n.getValue();
   78: rz rzVar = contactAddBottomSheet.o;
   79: zm9[] zm9VarArr2 = ContactAddBottomSheet.x;
   80: zm9 zm9Var = zm9VarArr2[0];
   81: long jLongValue = ((Number) rzVar.a(contactAddBottomSheet)).longValue();
   82: t5a t5aVar = (t5a) qv4Var.a.getValue();
   83: dea deaVar = new dea();
   84: deaVar.put("user2Id", Long.valueOf(jLongValue));
   85: t5a.i(t5aVar, "CONTACT_RENAME_BANNER", "save", deaVar.b(), 8);
   86: v5d v5dVar = new v5d(contactAddBottomSheet);
   87: v5dVar.h(new l6d(R.drawable.done_fill_round_animated));
   88: v5dVar.m(new mdj(R.string.oneme_unknown_contact_snackbar_add_contact));
   89: v5dVar.l(v6d.a);
   90: rz rzVar2 = contactAddBottomSheet.p;
   91: zm9 zm9Var2 = zm9VarArr2[1];
   92: Integer num = (Integer) rzVar2.a(contactAddBottomSheet);
   93: if (num != null) {
   94: iIntValue = num.intValue();
   95: } else {
   96: Integer numH = cyk.h((View) this.h);
   97: iIntValue = numH != null ? numH.intValue() : 0;
   98: }
   99: v5dVar.c(new d6d(0, 0, iIntValue, 11));
  100: u5d u5dVarP = v5dVar.p();
  101: if (u5dVarP != null && (h3jVar = (h3j) u5dVarP.a.e) != null) {
  102: n61.e(h3jVar, zf8.e);
  103: }
  104: contactAddBottomSheet.y1(true);
  105: }
  106: return s1k.a;
  107: }
  108: 
  109: private final Object B(Object obj) {
  110: n3c n3cVar = (n3c) this.f;
  111: xnm.y(obj);
  112: int i = n3cVar.d;
  113: svc svcVar = (svc) this.g;
  114: ContactsPickerScreen contactsPickerScreen = (ContactsPickerScreen) this.h;
  115: if (i == 0) {
  116: svcVar.setVisibility(8);
  117: svcVar.j(null);
  118: } else {
  119: svcVar.setVisibility(0);
  120: svcVar.q(c45.D(R.string.contacts_picker_send_btn_title, contactsPickerScreen.getContext()));
  121: svcVar.j(new Integer(i));
  122: }
  123: return s1k.a;
  124: }
  125: 
  126: private final Object C(Object obj) {
  127: xnm.y(obj);
  128: Uri uri = (Uri) this.f;
  129: if (uri == null) {
  130: ((o08) this.g).c();
  131: } else {
  132: ((q08) this.h).d(uri);
  133: }
  134: return s1k.a;
  135: }
  136: 
  137: /* JADX WARN: Code duplicated, block: B:26:0x005f  */
  138: /* JADX WARN: Code duplicated, block: B:46:0x00c9  */
  139: /* JADX WARN: Code duplicated, block: B:48:0x0109  */
  140: /* JADX WARN: Code duplicated, block: B:49:0x010b  */
  141: /* JADX WARN: Code duplicated, block: B:51:0x010e  */
  142: /* JADX WARN: Code duplicated, block: B:58:0x011f  */
  143: /* JADX WARN: Code duplicated, block: B:60:0x012f  */
  144: /* JADX WARN: Code duplicated, block: B:62:0x0132  */
  145: /* JADX WARN: Code duplicated, block: B:65:0x0150  */
  146: private final Object D(Object obj) {
  147: Object obj2;
  148: String string;
  149: s82 s82VarO;
  150: int size;
  151: int i;
  152: yp5 yp5Var;
  153: r82 r82Var;
  154: o1d o1dVar;
  155: c6a c6aVar = c6a.d;
  156: s1k s1kVar = s1k.a;
  157: xnm.y(obj);
  158: if (((yp5) this.f).e().o()) {
  159: f09.p("CallsManager", "outgoing call skipped: waiting for SDK to finish after early decline");
  160: return s1kVar;
  161: }
  162: yp5 yp5Var2 = (yp5) this.f;
  163: y0i y0iVar = (y0i) this.g;
  164: yp5Var2.getClass();
  165: w0i w0iVar = y0iVar.a;
  166: if (w0iVar instanceof u0i) {
  167: obj2 = ((u0i) w0iVar).a;
  168: } else {
  169: obj2 = w0iVar instanceof v0i ? ((v0i) w0iVar).a : null;
  170: }
  171: sc2 sc2Var = obj2 instanceof sc2 ? (sc2) obj2 : null;
  172: if (sc2Var != null) {
  173: String str = sc2Var.b;
  174: e85 e85Var = new e85(str);
  175: if (e85.b(str)) {
  176: e85Var = null;
  177: }
  178: string = e85Var != null ? e85Var.a : null;
  179: if (string == null) {
  180: z3j z3jVar = e85.b;
  181: string = UUID.randomUUID().toString();
  182: }
  183: } else {
  184: z3j z3jVar2 = e85.b;
  185: string = UUID.randomUUID().toString();
  186: }
  187: Iterable iterable = (Iterable) ((yp5) this.f).i.getValue();
  188: if (!(iterable instanceof Collection) \|\| !((Collection) iterable).isEmpty()) {
  189: Iterator it = iterable.iterator();
  190: while (it.hasNext()) {
  191: if (g4a.c(((r82) it.next()).g(), string)) {
  192: o1d o1dVar2 = f09.g;
  193: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
  194: o1dVar2.c(c6aVar, "CallsManager", vg9.y("outgoing call skipped: session ", e85.c(string), " already exists"), null);
  195: return s1kVar;
  196: }
  197: }
  198: }
  199: if (((yp5) this.f).c(((y0i) this.g).a) == null) {
  200: f09.p("CallsManager", "outgoing call can't start because call already started.");
  201: return s1kVar;
  202: }
  203: s82VarO = ((yp5) this.f).o((q1a) this.h);
  204: size = ((List) ((yp5) this.f).i.getValue()).size();
  205: ((yp5) this.f).getClass();
  206: if (((Boolean) ((j9e) ((z3j) s82VarO.l()).getValue()).H().i()).booleanValue()) {
  207: i = 2;
  208: } else {
  209: i = 1;
  210: }
  211: if (size >= i) {
  212: r82 r82VarE = ((yp5) this.f).e();
  213: yp5Var = (yp5) this.f;
  214: r82Var = r82VarE != yp5Var.h ? r82VarE : null;
  215: if (r82Var != null) {
  216: yp5Var.k(r82Var, 2);
  217: }
  218: r82 r82VarB = ((yp5) this.f).b(s82VarO, string);
  219: s82VarO.a().b(r82VarB.c());
  220: r82VarB.d((y0i) this.g);
  221: return s1kVar;
  222: }
  223: o1dVar = f09.g;
  224: if (o1dVar != null && o1dVar.b(c6aVar)) {
  225: o1dVar.c(c6aVar, "CallsManager", "outgoing call skipped: session limit reached", null);
  226: }
  227: } else {
  228: if (((yp5) this.f).c(((y0i) this.g).a) == null) {
  229: f09.p("CallsManager", "outgoing call can't start because call already started.");
  230: return s1kVar;
  231: }
  232: s82VarO = ((yp5) this.f).o((q1a) this.h);
  233: size = ((List) ((yp5) this.f).i.getValue()).size();
  234: ((yp5) this.f).getClass();
  235: if (((Boolean) ((j9e) ((z3j) s82VarO.l()).getValue()).H().i()).booleanValue()) {
  236: i = 2;
  237: } else {
  238: i = 1;
  239: }
  240: if (size >= i) {
  241: r82 r82VarE2 = ((yp5) this.f).e();
  242: yp5Var = (yp5) this.f;
  243: if (r82VarE2 != yp5Var.h) {
  244: }
  245: if (r82Var != null) {
  246: yp5Var.k(r82Var, 2);
  247: }
  248: r82 r82VarB2 = ((yp5) this.f).b(s82VarO, string);
  249: s82VarO.a().b(r82VarB2.c());
  250: r82VarB2.d((y0i) this.g);
```

### defpackage/azc.java
Строки 1–225:
```java
    1: package defpackage;
    2: 
    3: import android.content.ContentResolver;
    4: import android.content.Context;
    5: import android.content.SharedPreferences;
    6: import android.hardware.camera2.CaptureResult;
    7: import android.net.Uri;
    8: import android.os.Build;
    9: import android.os.Environment;
   10: import android.provider.MediaStore;
   11: import android.text.TextUtils;
   12: import android.util.Base64;
   13: import android.util.Log;
   14: import android.util.LongSparseArray;
   15: import com.facebook.soloader.SoLoader;
   16: import java.io.File;
   17: import java.io.FileInputStream;
   18: import java.io.IOException;
   19: import java.io.OutputStream;
   20: import java.io.Serializable;
   21: import java.io.UnsupportedEncodingException;
   22: import java.lang.reflect.InvocationTargetException;
   23: import java.lang.reflect.Method;
   24: import java.math.BigInteger;
   25: import java.nio.ByteBuffer;
   26: import java.nio.channels.SocketChannel;
   27: import java.nio.charset.Charset;
   28: import java.security.InvalidAlgorithmParameterException;
   29: import java.security.InvalidKeyException;
   30: import java.security.MessageDigest;
   31: import java.security.NoSuchAlgorithmException;
   32: import java.util.ArrayList;
   33: import java.util.Collection;
   34: import java.util.Collections;
   35: import java.util.HashMap;
   36: import java.util.HashSet;
   37: import java.util.Iterator;
   38: import java.util.LinkedHashMap;
   39: import java.util.LinkedHashSet;
   40: import java.util.List;
   41: import java.util.Map;
   42: import java.util.Set;
   43: import java.util.concurrent.atomic.AtomicInteger;
   44: import javax.crypto.Cipher;
   45: import javax.crypto.NoSuchPaddingException;
   46: import javax.crypto.SecretKey;
   47: import javax.crypto.spec.IvParameterSpec;
   48: import javax.net.ssl.SSLEngine;
   49: import javax.net.ssl.SSLEngineResult;
   50: import me.leolin.shortcutbadger.BuildConfig;
   51: import one.video.calls.sdk.net.signaling.wt.nal.internal.WebTransportSocket;
   52: import one.video.upload.exceptions.TlsBufferOverflowException;
   53: import one.video.upload.exceptions.TlsBufferUnderflowException;
   54: import one.video.upload.exceptions.TlsConnectionClosedException;
   55: import one.video.upload.exceptions.TlsHandshakeEndOfStreamException;
   56: import org.json.JSONException;
   57: import org.json.JSONObject;
   58: import org.webrtc.SessionDescription;
   59: import ru.ok.android.externcalls.sdk.h;
   60: import ru.ok.android.externcalls.sdk.i;
   61: import ru.ok.android.externcalls.sdk.n;
   62: import ru.ok.tamtam.android.util.share.ShareData;
   63: import ru.oneme.app.R;
   64: 
   65: /* JADX INFO: loaded from: classes3.dex */
   66: public final class azc implements rt6, jh5, qkg, yr8, ltb, ct, mxi, pck {
   67: public static final Object f = new Object();
   68: public static volatile azc g;
   69: public final /* synthetic */ byte a;
   70: public Object b;
   71: public Object c;
   72: public Object d;
   73: public Object e;
   74: 
   75: public azc(byte b) {
   76: this.a = b;
   77: switch (b) {
   78: case 9:
   79: this.b = new HashMap();
   80: this.c = new HashMap();
   81: this.d = new LongSparseArray();
   82: this.e = new HashMap();
   83: break;
   84: case 11:
   85: this.b = new zxb(0);
   86: this.d = new HashSet();
   87: long jCurrentTimeMillis = (System.currentTimeMillis() / 1000) + 2082844800;
   88: this.e = new ayb(jCurrentTimeMillis, jCurrentTimeMillis);
   89: break;
   90: case 19:
   91: this.c = Runtime.getRuntime();
   92: Method nativeLoadRuntimeMethod = b4j.getNativeLoadRuntimeMethod();
   93: this.d = nativeLoadRuntimeMethod;
   94: String strJoin = null;
   95: String classLoaderLdLoadLibrary = nativeLoadRuntimeMethod != null ? b4j.getClassLoaderLdLoadLibrary() : null;
   96: this.b = classLoaderLdLoadLibrary;
   97: if (classLoaderLdLoadLibrary != null) {
   98: String[] strArrSplit = classLoaderLdLoadLibrary.split(":");
   99: ArrayList arrayList = new ArrayList(strArrSplit.length);
  100: for (String str : strArrSplit) {
  101: if (!str.contains("!")) {
  102: arrayList.add(str);
  103: }
  104: }
  105: strJoin = TextUtils.join(":", arrayList);
  106: }
  107: this.e = strJoin;
  108: break;
  109: }
  110: }
  111: 
  112: public static String A() {
  113: return new String(Base64.decode(new byte[]{98, 51, 90, 106, 99, 51, 77, 116, 77, 84, 69, 121, 78, 65, 61, 61, 10}, 0), o53.a);
  114: }
  115: 
  116: public static String H(String str) {
  117: try {
  118: File file = new File(str);
  119: MessageDigest messageDigest = MessageDigest.getInstance("MD5");
  120: FileInputStream fileInputStream = new FileInputStream(file);
  121: try {
  122: byte[] bArr = new byte[4096];
  123: while (true) {
  124: int i = fileInputStream.read(bArr);
  125: if (i <= 0) {
  126: String str2 = String.format("%32x", new BigInteger(1, messageDigest.digest()));
  127: fileInputStream.close();
  128: return str2;
  129: }
  130: messageDigest.update(bArr, 0, i);
  131: }
  132: } catch (Throwable th) {
  133: try {
  134: fileInputStream.close();
  135: } catch (Throwable th2) {
  136: th.addSuppressed(th2);
  137: }
  138: throw th;
  139: }
  140: } catch (IOException \| SecurityException \| NoSuchAlgorithmException e) {
  141: return e.toString();
  142: }
  143: }
  144: 
  145: public static String T(ShareData shareData, Uri uri, z35 z35Var) {
  146: int i;
  147: if (z35Var == null ? !((i = shareData.type) == 1 \|\| i == 2) : !(z35Var.a() \|\| z35Var.b())) {
  148: return null;
  149: }
  150: String str = z35Var != null ? z35Var.d : null;
  151: return (str == null \|\| zti.n0(str)) ? uri.toString() : str;
  152: }
  153: 
  154: public static String V() {
  155: return new String(Base64.decode(new byte[]{81, 87, 53, 107, 99, 109, 57, 112, 90, 69, 116, 108, 101, 86, 78, 48, 98, 51, 74, 108, 10}, 0), o53.a);
  156: }
  157: 
  158: public static String z() {
  159: return new String(Base64.decode(new byte[]{81, 85, 86, 84, 76, 48, 78, 67, 81, 121, 57, 81, 83, 48, 78, 84, 78, 49, 66, 104, 90, 71, 82, 112, 98, 109, 99, 61, 10}, 0), o53.a);
  160: }
  161: 
  162: public String B(String str) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException, InvalidAlgorithmParameterException {
  163: byte[] bArrDecode;
  164: String strD;
  165: SecretKey secretKey = (SecretKey) ((z3j) this.d).getValue();
  166: if (secretKey == null) {
  167: return str;
  168: }
  169: byte[] bArrDecode2 = Base64.decode(str, 0);
  170: Charset charset = o53.a;
  171: JSONObject jSONObject = new JSONObject(new String(bArrDecode2, charset));
  172: String strD2 = dom.d("r", jSONObject);
  173: if (strD2 == null \|\| (bArrDecode = Base64.decode(strD2, 0)) == null \|\| (strD = dom.d("d", jSONObject)) == null) {
  174: return null;
  175: }
  176: byte[] bArrDecode3 = Base64.decode(strD, 0);
  177: Cipher cipher = Cipher.getInstance(z());
  178: cipher.init(2, secretKey, new IvParameterSpec(bArrDecode));
  179: return new String(cipher.doFinal(bArrDecode3), charset);
  180: }
  181: 
  182: public String C(String str) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException {
  183: if (str == null) {
  184: return null;
  185: }
  186: SecretKey secretKey = (SecretKey) ((z3j) this.d).getValue();
  187: if (secretKey == null) {
  188: return str;
  189: }
  190: Cipher cipher = Cipher.getInstance(z());
  191: cipher.init(1, secretKey);
  192: Charset charset = o53.a;
  193: String strEncodeToString = Base64.encodeToString(cipher.doFinal(str.getBytes(charset)), 0);
  194: return Base64.encodeToString(new JSONObject().put("d", strEncodeToString).put("r", Base64.encodeToString(cipher.getIV(), 0)).toString().getBytes(charset), 0);
  195: }
  196: 
  197: public ii0 E() {
  198: return (ii0) this.e;
  199: }
  200: 
  201: public String F() {
  202: return (String) this.d;
  203: }
  204: 
  205: public String G() {
  206: return (String) this.c;
  207: }
  208: 
  209: public lua I() {
  210: ig1 ig1Var = (ig1) ((h) this.c).c();
  211: n5h n5hVar = ((ynd) ((ob3) this.e).b).e;
  212: if (ig1Var != null) {
  213: o3c o3cVarL = ig1Var.R1.l(n5hVar);
  214: return new lua(o3cVarL.a, o3cVarL.b, o3cVarL.c, o3cVarL.d);
  215: }
  216: kua kuaVar = kua.a;
  217: return new lua(kuaVar, kuaVar, kuaVar, kuaVar);
  218: }
  219: 
  220: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  221: public Object J(ShareData shareData, d55 d55Var) {
  222: jhh jhhVar;
  223: if (d55Var instanceof jhh) {
  224: jhhVar = (jhh) d55Var;
  225: int i = jhhVar.f;
```

### defpackage/eh0.java
Строки 1–5:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public interface eh0 {
    5: }
```

### defpackage/dh0.java
Строки 1–14:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class dh0 implements eh0 {
    5: public final azc a;
    6: 
    7: public dh0(azc azcVar) {
    8: this.a = azcVar;
    9: }
   10: 
   11: public final azc a() {
   12: return this.a;
   13: }
   14: }
```

### defpackage/ch0.java
Строки 1–20:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes2.dex */
    4: public final class ch0 implements eh0 {
    5: public final String a;
    6: public final kme b;
    7: 
    8: public ch0(String str, kme kmeVar) {
    9: this.a = str;
   10: this.b = kmeVar;
   11: }
   12: 
   13: public final kme a() {
   14: return this.b;
   15: }
   16: 
   17: public final String b() {
   18: return this.a;
   19: }
   20: }
```

### defpackage/df7.java
Строки 1–130:
```java
    1: package defpackage;
    2: 
    3: import android.os.Build;
    4: import android.os.SystemClock;
    5: import io.jsonwebtoken.JwtParser;
    6: import java.io.File;
    7: import java.util.ArrayList;
    8: import java.util.Collection;
    9: import java.util.Iterator;
   10: import java.util.LinkedHashMap;
   11: import java.util.List;
   12: import java.util.Locale;
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
   23: public static final df7 b = new df7(0);
   24: public static final df7 c = new df7(1);
   25: public static final df7 d = new df7(2);
   26: public static final df7 e = new df7(3);
   27: public static final df7 f = new df7(4);
   28: public static final df7 g = new df7(5);
   29: public static final df7 h = new df7(6);
   30: public static final df7 i = new df7(7);
   31: public static final df7 j = new df7(8);
   32: public static final df7 k = new df7(9);
   33: public static final df7 l = new df7(10);
   34: public final /* synthetic */ byte a;
   35: 
   36: public /* synthetic */ df7(byte b2) {
   37: this.a = b2;
   38: }
   39: 
   40: public static boolean b(File file) {
   41: Object n4gVar;
   42: try {
   43: n4gVar = Boolean.valueOf(file.exists() && file.canRead());
   44: } catch (Throwable th) {
   45: n4gVar = new n4g(th);
   46: }
   47: Object obj = Boolean.FALSE;
   48: if (n4gVar instanceof n4g) {
   49: n4gVar = obj;
   50: }
   51: return ((Boolean) n4gVar).booleanValue();
   52: }
   53: 
   54: public static boolean e(String str) {
   55: Object n4gVar;
   56: try {
   57: n4gVar = Boolean.valueOf(b(new File(str)));
   58: } catch (Throwable th) {
   59: n4gVar = new n4g(th);
   60: }
   61: Object obj = Boolean.FALSE;
   62: if (n4gVar instanceof n4g) {
   63: n4gVar = obj;
   64: }
   65: return ((Boolean) n4gVar).booleanValue();
   66: }
   67: 
   68: public static File f(File file, String str) {
   69: String str2;
   70: File file2 = new File(file, str);
   71: if (file2.exists()) {
   72: int iP0 = zti.p0(str, JwtParser.SEPARATOR_CHAR, 0, 6);
   73: int i2 = 0;
   74: while (i2 < 100) {
   75: if (iP0 != -1) {
   76: str2 = str.substring(0, iP0) + "(" + (i2 + 1) + ")" + str.substring(iP0);
   77: } else {
   78: str2 = str + "(" + (i2 + 1) + ")";
   79: }
   80: File file3 = new File(file, str2);
   81: if (!file3.exists()) {
   82: return file3;
   83: }
   84: i2++;
   85: file2 = file3;
   86: }
   87: }
   88: return file2;
   89: }
   90: 
   91: public static List k(List list, Collection collection) {
   92: if (list.isEmpty()) {
   93: return va4.j1(collection, md6.b);
   94: }
   95: if (collection.isEmpty()) {
   96: return list;
   97: }
   98: fy9 fy9VarG = er0.g();
   99: fy9VarG.addAll(list);
  100: Iterator it = collection.iterator();
  101: while (it.hasNext()) {
  102: l(fy9VarG, (sd6) it.next());
  103: }
  104: if (fy9VarG.a() > 15) {
  105: mhf mhfVar = nhf.a;
  106: Random randomA = gdn.a();
  107: int iB = 0;
  108: while (fy9VarG.a() > 14) {
  109: iB += ((sd6) fy9VarG.b(randomA.nextInt(fy9VarG.a()))).b();
  110: }
  111: l(fy9VarG, new sd6(iB, "unknown", "max_size_exceeded"));
  112: }
  113: return er0.d(fy9VarG);
  114: }
  115: 
  116: public static void l(fy9 fy9Var, sd6 sd6Var) {
  117: int i2;
  118: md6 md6Var = md6.b;
  119: int iA = fy9Var.a();
  120: wa4.m0(fy9Var.a(), iA);
  121: int i3 = iA - 1;
  122: int i4 = 0;
  123: while (true) {
  124: if (i4 > i3) {
  125: i2 = -(i4 + 1);
  126: break;
  127: }
  128: i2 = (i4 + i3) >>> 1;
  129: int iCompare = md6Var.compare(fy9Var.get(i2), sd6Var);
  130: if (iCompare >= 0) {
```

### defpackage/p0b.java
Строки 213–280:
```java
  213: }
  214: return av1.a(av1Var, null, o27.a, null, false, null, null, false, 16777183);
  215: }
  216: 
  217: /* JADX WARN: Multi-variable type inference failed */
  218: public void b(boolean z) {
  219: emc emcVar;
  220: int iIntValue;
  221: emc emcVar2;
  222: z3j z3jVar = (z3j) this.h;
  223: zl8 zl8Var = (zl8) this.d;
  224: u6a u6aVar = (u6a) this.e;
  225: Object[] objArr = 0;
  226: u6aVar.d("Start connect to notifier", null);
  227: ConcurrentLinkedDeque concurrentLinkedDeque = (ConcurrentLinkedDeque) this.f;
  228: if (concurrentLinkedDeque.isEmpty()) {
  229: u6aVar.e("You need to add push tokens to connect to the notifier", null);
  230: return;
  231: }
  232: List list = fmc.d;
  233: if (g5n.a(zl8Var)) {
  234: fmc fmcVar = (fmc) ((z3j) this.i).getValue();
  235: fmcVar.getClass();
  236: List list2 = fmc.d;
  237: if (g5n.a(zl8Var)) {
  238: try {
  239: mk mkVar = fmcVar.a;
  240: iu5 iu5Var = o56.a;
  241: Integer num = (Integer) fb9.w(ks5.c, new r25(mkVar, objArr == true ? 1 : 0, (byte) 11));
  242: iIntValue = (num == null \|\| num.intValue() >= list2.size() \|\| num.intValue() < 0) ? 0 : num.intValue();
  243: } catch (Exception e) {
  244: fmcVar.b.e("routeIndex=0, persistence=readFailed", e);
  245: }
  246: emcVar2 = new emc(iIntValue, (String) list2.get(iIntValue), iIntValue == 0 ? "BASE" : "FALLBACK");
  247: } else {
  248: emcVar2 = null;
  249: }
  250: emcVar = emcVar2;
  251: } else {
  252: emcVar = null;
  253: }
  254: String string = new Uri.Builder().scheme(zl8Var.w()).encodedAuthority(emcVar != null ? emcVar.b : zl8Var.x()).path("api/v3/ws").appendQueryParameter("push_tokens", va4.S0(concurrentLinkedDeque, ",", null, null, null, 62)).build().toString();
  255: spc spcVarA = ((tpc) this.c).a();
  256: spcVarA.y = rgk.b("interval", 60L, TimeUnit.SECONDS);
  257: if (z) {
  258: c47 c47Var = (c47) z3jVar.getValue();
  259: if (c47Var != spcVarA.k) {
  260: spcVarA.A = null;
  261: }
  262: spcVarA.k = c47Var;
  263: ((c47) z3jVar.getValue()).c(zl8Var.x());
  264: c47 c47Var2 = (c47) z3jVar.getValue();
  265: c47Var2.getClass();
  266: try {
  267: c47Var2.b.remove(0);
  268: } catch (IndexOutOfBoundsException unused) {
  269: }
  270: u6aVar.e("Drop unreachable notifier address", null);
  271: }
  272: spcVarA.f = false;
  273: spcVarA.c.add(new p1l());
  274: tpc tpcVar = new tpc(spcVarA);
  275: ly lyVar = new ly();
  276: lyVar.f(string);
  277: o0g o0gVarA = lyVar.a();
  278: npl[] nplVarArr = (npl[]) va4.a1((LinkedHashSet) this.a, wa4.j0(emcVar != null ? new q1l(this, emcVar) : null)).toArray(new npl[0]);
  279: znf znfVar = new znf(c9j.h, o0gVarA, new sm4((npl[]) Arrays.copyOf(nplVarArr, nplVarArr.length)), new Random(), tpcVar.y, tpcVar.z);
  280: znfVar.c(tpcVar);
```

### defpackage/p73.java
Строки 493–517:
```java
  493: this.c = (byte) 12;
  494: }
  495: 
  496: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  497: public p73(long j, long j2, int i, long j3, int i2, long j4, boolean z, dx5 dx5Var, String str, Long l) {
  498: super(tdd.p1);
  499: this.c = (byte) 4;
  500: f(j, "chatId");
  501: if (l != null) {
  502: this.a.put("postId", l);
  503: }
  504: f(j2, "from");
  505: c(i, "forward");
  506: f(j3, "forwardTime");
  507: c(i2, "backward");
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
```

### defpackage/qzb.java
Строки 1–36:
```java
    1: package defpackage;
    2: 
    3: /* JADX INFO: loaded from: classes3.dex */
    4: public final class qzb extends x6j {
    5: public d7b c;
    6: public r53 d;
    7: public String e;
    8: 
    9: public qzb(beb bebVar) {
   10: super(bebVar);
   11: }
   12: 
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
   23: case "message":
   24: this.c = e0c.O(bebVar);
   25: break;
   26: default:
   27: bebVar.N();
   28: break;
   29: }
   30: }
   31: 
   32: @Override // defpackage.mv0
   33: public final String toString() {
   34: return w7g.v("Response{, message=", String.valueOf(this.c), ", chat=", String.valueOf(this.d), "}");
   35: }
   36: }
```

### defpackage/sm0.java
Строки 65–105:
```java
   65: if (i2 == 0) {
   66: return i == 0;
   67: }
   68: return s95.e(i2, i);
   69: }
   70: 
   71: public final int hashCode() {
   72: String str = this.a;
   73: int iHashCode = ((str == null ? 0 : str.hashCode()) ^ 1000003) * 1000003;
   74: String str2 = this.b;
   75: int iHashCode2 = (iHashCode ^ (str2 == null ? 0 : str2.hashCode())) * 1000003;
   76: String str3 = this.c;
   77: int iHashCode3 = (iHashCode2 ^ (str3 == null ? 0 : str3.hashCode())) * 1000003;
   78: do0 do0Var = this.d;
   79: int iHashCode4 = (iHashCode3 ^ (do0Var == null ? 0 : do0Var.hashCode())) * 1000003;
   80: int i = this.e;
   81: return iHashCode4 ^ (i != 0 ? s95.G(i) : 0);
   82: }
   83: 
   84: public final String toString() {
   85: String str;
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
   96: if (i != 1) {
   97: str = i != 2 ? "null" : "BAD_CONFIG";
   98: } else {
   99: str = "OK";
  100: }
  101: sb.append(str);
  102: sb.append("}");
  103: return sb.toString();
  104: }
  105: }
```

### defpackage/gn0.java
Строки 80–128:
```java
   80: }
   81: return str8.equals(str7);
   82: }
   83: 
   84: public final int hashCode() {
   85: String str = this.a;
   86: int iHashCode = ((((str == null ? 0 : str.hashCode()) ^ 1000003) * 1000003) ^ s95.G(this.b)) * 1000003;
   87: String str2 = this.c;
   88: int iHashCode2 = (iHashCode ^ (str2 == null ? 0 : str2.hashCode())) * 1000003;
   89: String str3 = this.d;
   90: int iHashCode3 = (iHashCode2 ^ (str3 == null ? 0 : str3.hashCode())) * 1000003;
   91: long j = this.e;
   92: int i = (iHashCode3 ^ ((int) (j ^ (j >>> 32)))) * 1000003;
   93: long j2 = this.f;
   94: int i2 = (i ^ ((int) (j2 ^ (j2 >>> 32)))) * 1000003;
   95: String str4 = this.g;
   96: return i2 ^ (str4 != null ? str4.hashCode() : 0);
   97: }
   98: 
   99: public final String toString() {
  100: String str;
  101: StringBuilder sb = new StringBuilder("PersistedInstallationEntry{firebaseInstallationId=");
  102: sb.append(this.a);
  103: sb.append(", registrationStatus=");
  104: int i = this.b;
  105: if (i == 1) {
  106: str = "ATTEMPT_MIGRATION";
  107: } else if (i == 2) {
  108: str = "NOT_GENERATED";
  109: } else if (i == 3) {
  110: str = "UNREGISTERED";
  111: } else if (i != 4) {
  112: str = i != 5 ? "null" : "REGISTER_ERROR";
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
  123: sb.append(", tokenCreationEpochInSecs=");
  124: sb.append(this.f);
  125: sb.append(", fisError=");
  126: return w7g.w(sb, this.g, "}");
  127: }
  128: }
```

### defpackage/wpc.java
Строки 117–145:
```java
  117: if (iOException2 != null) {
  118: iOException2.initCause(iOException);
  119: }
  120: if (iOException2 != null) {
  121: iOException = iOException2;
  122: }
  123: cu2Var.g(new n4g(iOException));
  124: }
  125: 
  126: public void D(gn0 gn0Var) {
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
  137: gg7Var.a();
  138: File fileCreateTempFile = File.createTempFile("PersistedInstallation", "tmp", gg7Var.a.getFilesDir());
  139: FileOutputStream fileOutputStream = new FileOutputStream(fileCreateTempFile);
  140: fileOutputStream.write(jSONObject.toString().getBytes("UTF-8"));
  141: fileOutputStream.close();
  142: if (fileCreateTempFile.renameTo(A())) {
  143: } else {
  144: throw new IOException("unable to rename the tmpfile to PersistedInstallation");
  145: }
```
Строки 203–225:
```java
  203: throw th;
  204: } catch (Throwable th2) {
  205: th.addSuppressed(th2);
  206: throw th;
  207: }
  208: }
  209: }
  210: jSONObject = new JSONObject(byteArrayOutputStream.toString());
  211: fileInputStream.close();
  212: } catch (IOException \| JSONException unused) {
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
  223: if (i2 == 0) {
  224: k3g.q("Null registrationStatus");
  225: return null;
```

### defpackage/hg7.java
Строки 95–145:
```java
   95: }
   96: 
   97: public static long d(String str) {
   98: g4a.f("Invalid Expiration Timestamp.", d.matcher(str).matches());
   99: if (str == null \|\| str.length() == 0) {
  100: return 0L;
  101: }
  102: return Long.parseLong(str.substring(0, str.length() - 1));
  103: }
  104: 
  105: public static sm0 e(HttpURLConnection httpURLConnection) throws IOException {
  106: InputStream inputStream = httpURLConnection.getInputStream();
  107: JsonReader jsonReader = new JsonReader(new InputStreamReader(inputStream, e));
  108: jy7 jy7VarA = do0.a();
  109: jsonReader.beginObject();
  110: String strNextString = null;
  111: String strNextString2 = null;
  112: String strNextString3 = null;
  113: do0 do0Var = null;
  114: while (jsonReader.hasNext()) {
  115: String strNextName = jsonReader.nextName();
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
  126: if (strNextName2.equals("token")) {
  127: jy7VarA.c = jsonReader.nextString();
  128: } else if (strNextName2.equals("expiresIn")) {
  129: jy7VarA.d = Long.valueOf(d(jsonReader.nextString()));
  130: } else {
  131: jsonReader.skipValue();
  132: }
  133: }
  134: do0 do0VarU = jy7VarA.u();
  135: jsonReader.endObject();
  136: do0Var = do0VarU;
  137: } else {
  138: jsonReader.skipValue();
  139: }
  140: }
  141: jsonReader.endObject();
  142: jsonReader.close();
  143: inputStream.close();
  144: return new sm0(strNextString, strNextString2, strNextString3, do0Var, 1);
  145: }
```

### defpackage/ih0.java
Строки 1–130:
```java
    1: package defpackage;
    2: 
    3: import android.content.ComponentName;
    4: import android.content.Context;
    5: import android.graphics.Path;
    6: import java.lang.reflect.Constructor;
    7: import java.lang.reflect.Method;
    8: import java.net.InetAddress;
    9: import java.net.UnknownHostException;
   10: import java.util.Iterator;
   11: import java.util.List;
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
   22: /* JADX INFO: loaded from: classes.dex */
   23: public final class ih0 implements f84, g18, tl4, ek9, l66, ek0 {
   24: public static final ih0 b = new ih0((byte) 0);
   25: public static final long[] c = new long[0];
   26: public static final ih0 d = new ih0((byte) 2);
   27: public static final ih0 e = new ih0((byte) 3);
   28: public static final ih0 f = new ih0((byte) 4);
   29: public static final ih0 g = new ih0((byte) 5);
   30: public static final ih0 h = new ih0((byte) 6);
   31: public static final ih0 i = new ih0((byte) 7);
   32: public static final ih0 j = new ih0((byte) 8);
   33: public static final ih0 k = new ih0((byte) 9);
   34: public static final ih0 l = new ih0((byte) 10);
   35: public final /* synthetic */ byte a;
   36: 
   37: public ih0(wdc wdcVar) {
   38: this.a = (byte) 20;
   39: }
   40: 
   41: public static Path g(float f2, float f3, float f4, float f5) {
   42: Path path = new Path();
   43: path.moveTo(f2, f3);
   44: path.lineTo(f4, f5);
   45: return path;
   46: }
   47: 
   48: /* JADX WARN: Code duplicated, block: B:160:0x013f A[EXC_TOP_SPLITTER, SYNTHETIC] */
   49: private final x6j j(beb bebVar) {
   50: int iP0;
   51: List listA;
   52: int i2;
   53: boolean zG0;
   54: long jO0;
   55: qp6 qp6Var;
   56: String strS0;
   57: if (!bebVar.m()) {
   58: return null;
   59: }
   60: try {
   61: iP0 = e0c.p0(bebVar);
   62: while (true) {
   63: qp6Var = qp6.a;
   64: if (i2 >= iP0) {
   65: break;
   66: }
   67: try {
   68: strS0 = e0c.s0(bebVar, null);
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
   79: }
   80: }
   81: int iG = s95.G(iqg.a);
   82: if (iG != 0) {
   83: if (iG != 1) {
   84: throw new NoWhenBranchMatchedException();
   85: }
   86: throw th;
   87: }
   88: strS0 = null;
   89: }
   90: if (strS0 != null) {
   91: try {
   92: int iHashCode = strS0.hashCode();
   93: if (iHashCode != -1417629679) {
   94: if (iHashCode != -1006239478) {
   95: if (iHashCode == 108404047 && strS0.equals("reset")) {
   96: try {
   97: zG0 = e0c.g0(bebVar);
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
  108: }
  109: }
  110: int iG2 = s95.G(iqg.a);
  111: if (iG2 != 0) {
  112: if (iG2 != 1) {
  113: throw new NoWhenBranchMatchedException();
  114: }
  115: throw th3;
  116: }
  117: zG0 = false;
  118: }
  119: } else {
  120: try {
  121: bebVar.N();
  122: } catch (Throwable th5) {
  123: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
  124: Iterator it3 = q1h.a.iterator();
  125: while (it3.hasNext()) {
  126: AccountInitializer accountInitializer3 = ((z6) it3.next()).a;
  127: try {
  128: f09.c0("Payload", "error while parse payload", th5);
  129: accountInitializer3.c().j().d().a(null, th5);
  130: } catch (Throwable th6) {
```
