# MAX 26.35.1 — ссылки на команды входа

Результаты поиска использований полей каталога команд.

## tdd.u
Файлов: 1
### defpackage/wh0.java
- 28: int i2 = vh0Var.g;
- 29: ka5 ka5Var = ka5.a;
- 30: if (i2 == 0) {
- 31: xnm.y(objB);
- 32: ctc ctcVar = (ctc) this.a.getValue();
- 33: String str = mvfVar.a;
- 34: String str2 = mvfVar.c;
- 35: String str3 = mvfVar.d;
- 36: Long l = mvfVar.e;
- 37: int i3 = l != null ? 1 : 0;
- 38: vh0Var.g = 1;
- 39: ctcVar.getClass();
- 40: bqc bqcVar = new bqc(tdd.u, (byte) 12);
- 41: if (str == null \|\| str.length() == 0) {
- 42: k3g.t("AuthConfirmCmd param 'token' can't be null");
- 43: return null;
- 44: }
- 45: bqcVar.h("token", str);
- 46: bqcVar.h("tokenType", "REGISTER");
- 47: if (str2 == null \|\| str2.length() == 0) {
- 48: k3g.t("AuthConfirmCmd param 'firstName' can't be null");
- 49: return null;
- 50: }
- 51: bqcVar.h("firstName", str2);
- 52: if (str3 != null && str3.length() != 0) {
- 53: bqcVar.h("lastName", str3);
- 54: }
- 55: if (l != null) {
- 56: bqcVar.f(l.longValue(), "photoId");
- 57: }
- 58: if (i3 != 0) {
- 59: bqcVar.h("avatarType", u.a(i3));


## tdd.m
Файлов: 1
### defpackage/ki0.java
- 24: }
- 25: } else {
- 26: ji0Var = new ji0(this, d55Var);
- 27: }
- 28: Object objB = ji0Var.e;
- 29: int i2 = ji0Var.g;
- 30: ka5 ka5Var = ka5.a;
- 31: if (i2 == 0) {
- 32: xnm.y(objB);
- 33: ctc ctcVar = (ctc) this.a.getValue();
- 34: ji0Var.g = 1;
- 35: f7j f7jVarA = ctcVar.a();
- 36: bqc bqcVar = new bqc(tdd.m, (byte) 11);
- 37: if (str2 == null \|\| str2.length() == 0) {
- 38: k3g.t("AuthCmd param 'token' can't be null");
- 39: return null;
- 40: }
- 41: bqcVar.h("token", str2);
- 42: if (str == null \|\| str.length() == 0) {
- 43: k3g.t("AuthCmd param 'verifyCode' can't be null when param 'authTokenType' is 'PHONE' or 'PHONE_CONFIRM'");
- 44: return null;
- 45: }
- 46: bqcVar.h("verifyCode", str);
- 47: bqcVar.h("authTokenType", "CHECK_CODE");
- 48: objB = f7jVarA.a.b(bqcVar, ji0Var);
- 49: if (objB != ka5Var) {
- 50: }
- 51: return ka5Var;
- 52: }
- 53: if (i2 != 1) {
- 54: if (i2 != 2) {
- 55: k3g.o("call to 'resume' before 'invoke' with coroutine");


## tdd.n
Файлов: 1
### defpackage/k7a.java
- 1: package defpackage;
- 2: 
- 3: import io.jsonwebtoken.Claims;
- 4: 
- 5: /* JADX INFO: loaded from: classes.dex */
- 6: public final class k7a extends u6j {
- 7: public final int c;
- 8: 
- 9: public k7a(String str, boolean z, int i, byte[] bArr, long j, long j2, String str2, long j3, long j4, long j5, u07 u07Var, String str3) {
- 10: super(tdd.n);
- 11: this.c = i;
- 12: h("token", str);
- 13: a("interactive", z);
- 14: if (j > 0) {
- 15: f(j, "chatsSync");
- 16: }
- 17: if (j2 > 0) {
- 18: f(j2, "contactsSync");
- 19: }
- 20: f(-1L, "presenceSync");
- 21: if (str2 != null && str2.length() != 0) {
- 22: h("configHash", str2);
- 23: }
- 24: if (j3 > 0) {
- 25: f(j3, "callsSync");
- 26: }
- 27: if (j4 > 0) {
- 28: f(j4, "lastLogin");
- 29: }


## tdd.l
Файлов: 1
### defpackage/aj0.java
- 1: package defpackage;
- 2: 
- 3: /* JADX INFO: loaded from: classes3.dex */
- 4: public final class aj0 extends u6j {
- 5: public final int c;
- 6: 
- 7: public aj0(int i, int i2, String str, byte[] bArr) {
- 8: String str2;
- 9: super(tdd.l);
- 10: this.c = i2;
- 11: h("phone", str);
- 12: if (i == 1) {
- 13: str2 = "START_AUTH";
- 14: } else {
- 15: if (i != 2) {
- 16: throw null;
- 17: }
- 18: str2 = "RESEND";
- 19: }
- 20: h("type", str2);
- 21: if (bArr != null) {
- 22: this.a.put("mode", bArr);
- 23: }
- 24: }
- 25: 
- 26: @Override // defpackage.u6j
- 27: public final boolean o() {
- 28: return false;

