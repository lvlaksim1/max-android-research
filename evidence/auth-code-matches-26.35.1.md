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
- Строка 32; InputPhoneScreen: f09.f0(inputPhoneScreen.b, "open web link with terms is failed, no activity found");
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
- Строка 74; accessToken: f09.f0(ug9.class.getName(), "link or chatAccessToken must not be null");

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
Строки 1–250:
```java
    1: package defpackage;
    2: 
    3: import android.app.Activity;
    4: import android.content.Context;
    5: import android.content.Intent;
    6: import android.net.Uri;
    7: import android.os.Bundle;
    8: import android.os.DeadObjectException;
    9: import android.telephony.TelephonyManager;
   10: import com.vk.push.core.base.AidlException;
   11: import com.vk.push.core.base.AidlResult;
   12: import java.io.File;
   13: import java.io.Serializable;
   14: import java.util.ArrayList;
   15: import java.util.Collection;
   16: import java.util.Collections;
   17: import java.util.Iterator;
   18: import java.util.List;
   19: import java.util.Set;
   20: import java.util.concurrent.CancellationException;
   21: import java.util.concurrent.CopyOnWriteArraySet;
   22: import java.util.concurrent.atomic.AtomicBoolean;
   23: import me.leolin.shortcutbadger.BuildConfig;
   24: import one.me.sdk.transfer.domain.UploadException;
   25: import org.webrtc.PeerConnectionFactory;
   26: import ru.oneme.app.R;
   27: 
   28: /* JADX INFO: loaded from: classes2.dex */
   29: public final class yr0 extends x1j implements e18 {
   30: public final /* synthetic */ byte e;
   31: public byte f;
   32: public Object g;
   33: public Object h;
   34: public Object i;
   35: public Object j;
   36: public final /* synthetic */ Object k;
   37: 
   38: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
   39: public yr0(bvf bvfVar, e10 e10Var, String str, String str2, q08 q08Var, b55 b55Var) {
   40: super(2, b55Var);
   41: this.e = (byte) 15;
   42: this.g = bvfVar;
   43: this.h = e10Var;
   44: this.i = str;
   45: this.j = str2;
   46: this.k = q08Var;
   47: }
   48: 
   49: /* JADX WARN: Code duplicated, block: B:28:0x00fe A[Catch: all -> 0x011b, CancellationException -> 0x011f, TRY_LEAVE, TryCatch #2 {CancellationException -> 0x011f, all -> 0x011b, blocks: (B:26:0x00ec, B:28:0x00fe), top: B:65:0x00ec }] */
   50: /* JADX WARN: Code duplicated, block: B:32:0x011d  */
   51: /* JADX WARN: Code duplicated, block: B:38:0x012d  */
   52: /* JADX WARN: Code duplicated, block: B:41:0x0132  */
   53: /* JADX WARN: Code restructure failed: missing block: B:43:0x014d, code lost:
   54: 
   55: if (r1 == r12) goto L44;
   56: */
   57: /* JADX WARN: Instruction removed from duplicated block: B:28:0x00fe, please report this as an issue */
   58: /*
   59: Code decompiled incorrectly, please refer to instructions dump.
   60: */
   61: private final Object A(Object obj) {
   62: Object objG;
   63: ow5 ow5Var;
   64: List<vld> list;
   65: Object n4gVar;
   66: String str;
   67: Object objH0;
   68: TelephonyManager telephonyManager;
   69: Object obj2;
   70: mm8 mm8Var = (mm8) this.k;
   71: rp9 rp9Var = mm8Var.f;
   72: z3j z3jVar = mm8Var.k;
   73: ja5 ja5Var = (ja5) this.j;
   74: byte b = this.f;
   75: b55 b55Var = null;
   76: ka5 ka5Var = ka5.a;
   77: if (b == 0) {
   78: xnm.y(obj);
   79: this.j = ja5Var;
   80: this.f = (byte) 1;
   81: if (usc.n(3000L, this) != ka5Var) {
   82: }
   83: return ka5Var;
   84: }
   85: if (b == 1) {
   86: xnm.y(obj);
   87: } else if (b == 2) {
   88: ow5 ow5Var2 = (ow5) this.g;
   89: xnm.y(obj);
   90: ow5Var = ow5Var2;
   91: objG = obj;
   92: list = (List) objG;
   93: try {
   94: telephonyManager = (TelephonyManager) ((Context) mm8Var.h.getValue()).getSystemService(TelephonyManager.class);
   95: if (telephonyManager != null) {
   96: n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();
   97: } else {
   98: n4gVar = null;
   99: }
  100: } catch (CancellationException e) {
  101: throw e;
  102: } catch (Throwable th) {
  103: n4gVar = new n4g(th);
  104: }
  105: if (n4gVar instanceof n4g) {
  106: n4gVar = null;
  107: }
  108: str = (String) n4gVar;
  109: if (str == null) {
  110: str = "undefined";
  111: }
  112: u95 u95Var = new u95(ow5Var, b55Var, (byte) 1);
  113: this.j = ja5Var;
  114: this.g = ow5Var;
  115: this.h = list;
  116: this.i = str;
  117: this.f = (byte) 3;
  118: objH0 = jd0.h0(3000L, u95Var, this);
  119: obj2 = ow5Var;
  120: } else {
  121: if (b != 3) {
  122: k3g.o("call to 'resume' before 'invoke' with coroutine");
  123: return null;
  124: }
  125: str = (String) this.i;
  126: List list2 = (List) this.h;
  127: ow5 ow5Var3 = (ow5) this.g;
  128: xnm.y(obj);
  129: list = list2;
  130: obj2 = ow5Var3;
  131: objH0 = obj;
  132: }
  133: String str2 = (String) objH0;
  134: ((jg9) obj2).m(null);
  135: boolean zU0 = lkh.u0(ja5Var.d());
  136: s1k s1kVar = s1k.a;
  137: if (!zU0) {
  138: return s1kVar;
  139: }
  140: t5a t5aVar = (t5a) mm8Var.i.getValue();
  141: dea deaVar = new dea();
  142: e4c e4cVar = new e4c(list.size());
  143: for (vld vldVar : list) {
  144: e4cVar.k(vldVar.a, vldVar.b);
  145: }
  146: deaVar.put("hosts", e4cVar);
  147: deaVar.put("operator", str);
  148: ms4 ms4Var = (ms4) rp9Var.getValue();
  149: deaVar.put("connection_type", new Integer(ms4Var.g() ? ms4Var.b().a : (byte) 1));
  150: if (str2 != null) {
  151: deaVar.put("ip", str2);
  152: }
  153: if (((ms4) rp9Var.getValue()).e()) {
  154: deaVar.put("vpn", new Integer(1));
  155: }
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
  166: ArrayList arrayList = new ArrayList(xa4.p0(listI0, 10));
  167: Iterator it = listI0.iterator();
  168: while (it.hasNext()) {
  169: arrayList.add(nm9.b(t45VarA, null, 0, new rk(it.next(), (b55) null, mm8Var), 3));
  170: }
  171: this.j = ja5Var;
  172: this.g = pw5VarB;
  173: this.f = (byte) 2;
  174: objG = jd0.g(arrayList, this);
  175: ow5Var = pw5VarB;
  176: if (objG != ka5Var) {
  177: list = (List) objG;
  178: telephonyManager = (TelephonyManager) ((Context) mm8Var.h.getValue()).getSystemService(TelephonyManager.class);
  179: if (telephonyManager != null) {
  180: n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();
  181: } else {
  182: n4gVar = null;
  183: }
  184: if (n4gVar instanceof n4g) {
  185: n4gVar = null;
  186: }
  187: str = (String) n4gVar;
  188: if (str == null) {
  189: str = "undefined";
  190: }
  191: u95 u95Var2 = new u95(ow5Var, b55Var, (byte) 1);
  192: this.j = ja5Var;
  193: this.g = ow5Var;
  194: this.h = list;
  195: this.i = str;
  196: this.f = (byte) 3;
  197: objH0 = jd0.h0(3000L, u95Var2, this);
  198: obj2 = ow5Var;
  199: }
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
   71: f09.f0(ka9.class.getName(), "Early return in goBackTo cuz of newBackStack.findLast { it.tag() == tag }?.controller is null");
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
