# MAX 26.35.1 — исходные классы и модели авторизации

Точное совпадение SHA-256: e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc
Файлы Java из JADX; номер строки относится к декомпилированному представлению.
Показаны первые 450 строк файла. Для крупных классов оставлены поисковые маркеры.

## defpackage/ki0.java (75 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class ki0 {
   5: public final rp9 a;
   6: public final rp9 b;
   7: 
   8: public ki0(rp9 rp9Var, rp9 rp9Var2) {
   9: this.a = rp9Var;
  10: this.b = rp9Var2;
  11: }
  12: 
  13: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  14: public final Object a(String str, String str2, d55 d55Var) {
  15: ji0 ji0Var;
  16: cqe cqeVar;
  17: if (d55Var instanceof ji0) {
  18: ji0Var = (ji0) d55Var;
  19: int i = ji0Var.g;
  20: if ((i & Integer.MIN_VALUE) != 0) {
  21: ji0Var.g = i - Integer.MIN_VALUE;
  22: } else {
  23: ji0Var = new ji0(this, d55Var);
  24: }
  25: } else {
  26: ji0Var = new ji0(this, d55Var);
  27: }
  28: Object objB = ji0Var.e;
  29: int i2 = ji0Var.g;
  30: ka5 ka5Var = ka5.a;
  31: if (i2 == 0) {
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
  42: if (str == null \|\| str.length() == 0) {
  43: k3g.t("AuthCmd param 'verifyCode' can't be null when param 'authTokenType' is 'PHONE' or 'PHONE_CONFIRM'");
  44: return null;
  45: }
  46: bqcVar.h("verifyCode", str);
  47: bqcVar.h("authTokenType", "CHECK_CODE");
  48: objB = f7jVarA.a.b(bqcVar, ji0Var);
  49: if (objB != ka5Var) {
  50: }
  51: return ka5Var;
  52: }
  53: if (i2 != 1) {
  54: if (i2 != 2) {
  55: k3g.o("call to 'resume' before 'invoke' with coroutine");
  56: return null;
  57: }
  58: th0 th0Var = ji0Var.d;
  59: xnm.y(objB);
  60: return th0Var;
  61: }
  62: xnm.y(objB);
  63: th0 th0Var2 = (th0) objB;
  64: if (th0Var2.c.containsKey("LOGIN") && (cqeVar = th0Var2.f) != null) {
  65: f0f f0fVar = (f0f) this.b.getValue();
  66: String str3 = (String) jfa.D(th0Var2.c, "LOGIN");
  67: ji0Var.d = th0Var2;
  68: ji0Var.g = 2;
  69: if (f0fVar.d(cqeVar, str3, ji0Var) == ka5Var) {
  70: return ka5Var;
  71: }
  72: }
  73: return th0Var2;
  74: }
  75: }
~~~

## defpackage/ji0.java (22 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class ji0 extends d55 {
   5: public th0 d;
   6: public /* synthetic */ Object e;
   7: public final /* synthetic */ ki0 f;
   8: public int g;
   9: 
  10: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  11: public ji0(ki0 ki0Var, d55 d55Var) {
  12: super(d55Var);
  13: this.f = ki0Var;
  14: }
  15: 
  16: @Override // defpackage.hv0
  17: public final Object w(Object obj) {
  18: this.e = obj;
  19: this.g \|= Integer.MIN_VALUE;
  20: return this.f.a(null, null, this);
  21: }
  22: }
~~~

## defpackage/wh0.java (83 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class wh0 {
   5: public final rp9 a;
   6: public final rp9 b;
   7: 
   8: public wh0(rp9 rp9Var, rp9 rp9Var2) {
   9: this.a = rp9Var;
  10: this.b = rp9Var2;
  11: }
  12: 
  13: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  14: public final Object a(mvf mvfVar, d55 d55Var) {
  15: vh0 vh0Var;
  16: if (d55Var instanceof vh0) {
  17: vh0Var = (vh0) d55Var;
  18: int i = vh0Var.g;
  19: if ((i & Integer.MIN_VALUE) != 0) {
  20: vh0Var.g = i - Integer.MIN_VALUE;
  21: } else {
  22: vh0Var = new vh0(this, d55Var);
  23: }
  24: } else {
  25: vh0Var = new vh0(this, d55Var);
  26: }
  27: Object objB = vh0Var.e;
  28: int i2 = vh0Var.g;
  29: ka5 ka5Var = ka5.a;
  30: if (i2 == 0) {
  31: xnm.y(objB);
  32: ctc ctcVar = (ctc) this.a.getValue();
  33: String str = mvfVar.a;
  34: String str2 = mvfVar.c;
  35: String str3 = mvfVar.d;
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
  46: bqcVar.h("tokenType", "REGISTER");
  47: if (str2 == null \|\| str2.length() == 0) {
  48: k3g.t("AuthConfirmCmd param 'firstName' can't be null");
  49: return null;
  50: }
  51: bqcVar.h("firstName", str2);
  52: if (str3 != null && str3.length() != 0) {
  53: bqcVar.h("lastName", str3);
  54: }
  55: if (l != null) {
  56: bqcVar.f(l.longValue(), "photoId");
  57: }
  58: if (i3 != 0) {
  59: bqcVar.h("avatarType", u.a(i3));
  60: }
  61: objB = ctcVar.a().a.b(bqcVar, vh0Var);
  62: if (objB != ka5Var) {
  63: }
  64: }
  65: if (i2 != 1) {
  66: if (i2 != 2) {
  67: k3g.o("call to 'resume' before 'invoke' with coroutine");
  68: return null;
  69: }
  70: uh0 uh0Var = vh0Var.d;
  71: xnm.y(objB);
  72: return uh0Var;
  73: }
  74: xnm.y(objB);
  75: uh0 uh0Var2 = (uh0) objB;
  76: cqe cqeVar = uh0Var2.e;
  77: f0f f0fVar = (f0f) this.b.getValue();
  78: String str4 = uh0Var2.c;
  79: vh0Var.d = uh0Var2;
  80: vh0Var.g = 2;
  81: return f0fVar.d(cqeVar, str4, vh0Var) == ka5Var ? ka5Var : uh0Var2;
  82: }
  83: }
~~~

## defpackage/vh0.java (22 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class vh0 extends d55 {
   5: public uh0 d;
   6: public /* synthetic */ Object e;
   7: public final /* synthetic */ wh0 f;
   8: public int g;
   9: 
  10: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  11: public vh0(wh0 wh0Var, d55 d55Var) {
  12: super(d55Var);
  13: this.f = wh0Var;
  14: }
  15: 
  16: @Override // defpackage.hv0
  17: public final Object w(Object obj) {
  18: this.e = obj;
  19: this.g \|= Integer.MIN_VALUE;
  20: return this.f.a(null, this);
  21: }
  22: }
~~~

## defpackage/mvf.java (76 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.os.Parcel;
   4: import android.os.Parcelable;
   5: 
   6: /* JADX INFO: loaded from: classes2.dex */
   7: public final class mvf implements Parcelable {
   8: public static final Parcelable.Creator<mvf> CREATOR = new c3f(6);
   9: public final String a;
  10: public final String b;
  11: public final String c;
  12: public final String d;
  13: public final Long e;
  14: 
  15: public mvf(String str, String str2, String str3, String str4, Long l) {
  16: this.a = str;
  17: this.b = str2;
  18: this.c = str3;
  19: this.d = str4;
  20: this.e = l;
  21: }
  22: 
  23: public static mvf a(mvf mvfVar, Long l) {
  24: String str = mvfVar.a;
  25: String str2 = mvfVar.b;
  26: String str3 = mvfVar.c;
  27: String str4 = mvfVar.d;
  28: mvfVar.getClass();
  29: return new mvf(str, str2, str3, str4, l);
  30: }
  31: 
  32: @Override // android.os.Parcelable
  33: public final int describeContents() {
  34: return 0;
  35: }
  36: 
  37: public final boolean equals(Object obj) {
  38: if (this == obj) {
  39: return true;
  40: }
  41: if (!(obj instanceof mvf)) {
  42: return false;
  43: }
  44: mvf mvfVar = (mvf) obj;
  45: return g4a.c(this.a, mvfVar.a) && g4a.c(this.b, mvfVar.b) && g4a.c(this.c, mvfVar.c) && g4a.c(this.d, mvfVar.d) && g4a.c(this.e, mvfVar.e);
  46: }
  47: 
  48: public final int hashCode() {
  49: int iE = a15.e(a15.e(a15.e(this.a.hashCode() * 31, 31, this.b), 31, this.c), 31, this.d);
  50: Long l = this.e;
  51: return iE + (l == null ? 0 : l.hashCode());
  52: }
  53: 
  54: public final String toString() {
  55: StringBuilder sbS = pq0.s("RegistrationData(token=", this.a, ", phone=", this.b, ", name=");
  56: w7g.D(sbS, this.c, ", surname=", this.d, ", photoId=");
  57: sbS.append(this.e);
  58: sbS.append(")");
  59: return sbS.toString();
  60: }
  61: 
  62: @Override // android.os.Parcelable
  63: public final void writeToParcel(Parcel parcel, int i) {
  64: parcel.writeString(this.a);
  65: parcel.writeString(this.b);
  66: parcel.writeString(this.c);
  67: parcel.writeString(this.d);
  68: Long l = this.e;
  69: if (l == null) {
  70: parcel.writeInt(0);
  71: } else {
  72: parcel.writeInt(1);
  73: parcel.writeLong(l.longValue());
  74: }
  75: }
  76: }
~~~

## defpackage/k7a.java (62 строк)

~~~java
   1: package defpackage;
   2: 
   3: import io.jsonwebtoken.Claims;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class k7a extends u6j {
   7: public final int c;
   8: 
   9: public k7a(String str, boolean z, int i, byte[] bArr, long j, long j2, String str2, long j3, long j4, long j5, u07 u07Var, String str3) {
  10: super(tdd.n);
  11: this.c = i;
  12: h("token", str);
  13: a("interactive", z);
  14: if (j > 0) {
  15: f(j, "chatsSync");
  16: }
  17: if (j2 > 0) {
  18: f(j2, "contactsSync");
  19: }
  20: f(-1L, "presenceSync");
  21: if (str2 != null && str2.length() != 0) {
  22: h("configHash", str2);
  23: }
  24: if (j3 > 0) {
  25: f(j3, "callsSync");
  26: }
  27: if (j4 > 0) {
  28: f(j4, "lastLogin");
  29: }
  30: if (j5 > 0) {
  31: f(j5, "bannersSync");
  32: }
  33: if (bArr != null) {
  34: this.a.put("chatCacheFingerprint", bArr);
  35: }
  36: dea deaVar = new dea();
  37: byte[] bArr2 = u07Var.a;
  38: if (bArr2 != null) {
  39: deaVar.put("chatsCountGroups", bArr2);
  40: }
  41: g(Claims.EXPIRATION, deaVar.b());
  42: if (str3 == null \|\| str3.length() == 0) {
  43: return;
  44: }
  45: h("aId", str3);
  46: }
  47: 
  48: @Override // defpackage.u6j
  49: public final v6j n() {
  50: return nln.i;
  51: }
  52: 
  53: @Override // defpackage.u6j
  54: public final boolean o() {
  55: return false;
  56: }
  57: 
  58: @Override // defpackage.u6j
  59: public final int p() {
  60: return this.c;
  61: }
  62: }
~~~

## defpackage/a7a.java (16 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class a7a extends u6j {
   5: public final int c;
   6: 
   7: public a7a(int i) {
   8: super(tdd.o);
   9: this.c = i;
  10: }
  11: 
  12: @Override // defpackage.u6j
  13: public final int p() {
  14: return this.c;
  15: }
  16: }
~~~

## defpackage/aj0.java (35 строк)

~~~java
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
~~~

## defpackage/bj0.java (662 строк)

~~~java
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
~~~

Поздние сигнатуры: 634 public final boolean equals(Object obj) {; 645 public final int hashCode() {; 652 public final String toString() {

## defpackage/ej0.java (18 строк)

~~~java
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
~~~

## defpackage/cj0.java (916 строк)

~~~java
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
~~~

Поздние сигнатуры: 

## defpackage/dj0.java (26 строк)

~~~java
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
~~~

## defpackage/u6j.java (82 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.List;
   4: import java.util.Map;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public abstract class u6j {
   8: public final i00 a = new i00(0);
   9: public final tdd b;
  10: 
  11: public u6j(tdd tddVar) {
  12: this.b = tddVar;
  13: }
  14: 
  15: public final void a(String str, boolean z) {
  16: this.a.put(str, Boolean.valueOf(z));
  17: }
  18: 
  19: public final void b(byte b, String str) {
  20: this.a.put(str, Byte.valueOf(b));
  21: }
  22: 
  23: public final void c(int i, String str) {
  24: this.a.put(str, Integer.valueOf(i));
  25: }
  26: 
  27: public final void d(String str, List list) {
  28: this.a.put(str, list);
  29: }
  30: 
  31: public final void e(String str, long[] jArr) {
  32: this.a.put(str, jArr);
  33: }
  34: 
  35: public final void f(long j, String str) {
  36: this.a.put(str, Long.valueOf(j));
  37: }
  38: 
  39: public final void g(String str, Map map) {
  40: this.a.put(str, map);
  41: }
  42: 
  43: public final void h(String str, String str2) {
  44: this.a.put(str, str2);
  45: }
  46: 
  47: public boolean i() {
  48: return this instanceof yzb;
  49: }
  50: 
  51: public boolean j() {
  52: return this instanceof l63;
  53: }
  54: 
  55: public short k() {
  56: return this.b.a;
  57: }
  58: 
  59: public int l() {
  60: return this.a.hashCode();
  61: }
  62: 
  63: public o6a m() {
  64: return cp5.l;
  65: }
  66: 
  67: public v6j n() {
  68: return v6j.G0;
  69: }
  70: 
  71: public boolean o() {
  72: return !(this instanceof yg0);
  73: }
  74: 
  75: public int p() {
  76: return -1;
  77: }
  78: 
  79: public final String toString() {
  80: return az7.G(this.a, m());
  81: }
  82: }
~~~

## defpackage/bqc.java (229 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Iterator;
   5: import java.util.List;
   6: import org.webrtc.PeerConnectionFactory;
   7: 
   8: /* JADX INFO: loaded from: classes3.dex */
   9: public final class bqc extends u6j {
  10: public static final jl9 d = new jl9();
  11: public final /* synthetic */ byte c;
  12: 
  13: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  14: public bqc(int i, String str, String str2, String str3, List list) {
  15: super(tdd.E);
  16: this.c = (byte) 18;
  17: Boolean bool = Boolean.TRUE;
  18: str2 = (i & 4) != 0 ? null : str2;
  19: str3 = (i & 8) != 0 ? null : str3;
  20: bool = (i & 16) != 0 ? null : bool;
  21: h("trackId", str);
  22: if (str2 != null && str2.length() != 0) {
  23: h("password", str2);
  24: }
  25: if (str3 != null && str3.length() != 0) {
  26: h("hint", str3);
  27: }
  28: if (bool != null) {
  29: this.a.put("remove2fa", bool);
  30: }
  31: List list2 = list;
  32: ArrayList arrayList = new ArrayList(xa4.p0(list2, 10));
  33: Iterator it = list2.iterator();
  34: while (it.hasNext()) {
  35: arrayList.add(Byte.valueOf(((ovj) it.next()).a));
  36: }
  37: d("expectedCapabilities", arrayList);
  38: }
  39: 
  40: @Override // defpackage.u6j
  41: public short k() {
  42: switch (this.c) {
  43: case 1:
  44: cp5 cp5Var = tdd.c;
  45: return (short) 29;
  46: case 2:
  47: cp5 cp5Var2 = tdd.c;
  48: return (short) 26;
  49: case 3:
  50: cp5 cp5Var3 = tdd.c;
  51: return (short) 261;
  52: case 4:
  53: cp5 cp5Var4 = tdd.c;
  54: return (short) 260;
  55: case 5:
  56: cp5 cp5Var5 = tdd.c;
  57: return (short) 259;
  58: case 26:
  59: cp5 cp5Var6 = tdd.c;
  60: return (short) 76;
  61: case 29:
  62: cp5 cp5Var7 = tdd.c;
  63: return (short) 54;
  64: default:
  65: return super.k();
  66: }
  67: }
  68: 
  69: @Override // defpackage.u6j
  70: public o6a m() {
  71: switch (this.c) {
  72: case 0:
  73: return d;
  74: default:
  75: return super.m();
  76: }
  77: }
  78: 
  79: @Override // defpackage.u6j
  80: public boolean o() {
  81: switch (this.c) {
  82: case 0:
  83: return true;
  84: case 8:
  85: return false;
  86: case 9:
  87: return false;
  88: case 11:
  89: return false;
  90: case 12:
  91: return false;
  92: case 14:
  93: return false;
  94: case 15:
  95: return false;
  96: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
  97: return false;
  98: case 19:
  99: return false;
 100: case 20:
 101: return false;
 102: case 21:
 103: return false;
 104: default:
 105: return super.o();
 106: }
 107: }
 108: 
 109: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 110: public bqc() {
 111: super(tdd.v);
 112: this.c = (byte) 13;
 113: this.a.put("type", (short) 0);
 114: }
 115: 
 116: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 117: public /* synthetic */ bqc(tdd tddVar, byte b) {
 118: super(tddVar);
 119: this.c = b;
 120: }
 121: 
 122: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 123: public bqc(String str, String str2, byte b) {
 124: super(tdd.D);
 125: this.c = b;
 126: switch (b) {
 127: case 21:
 128: super(tdd.C);
 129: h("trackId", str);
 130: if (str2 != null && str2.length() != 0) {
 131: h("email", str2);
 132: break;
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
 143: public bqc(long[] jArr) {
 144: super(tdd.z3);
 145: this.c = (byte) 24;
 146: e("historyIds", jArr == null ? new long[0] : jArr);
 147: }
 148: 
 149: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 150: public bqc(String str) {
 151: super(tdd.F);
 152: this.c = (byte) 7;
 153: if (str == null \|\| str.length() == 0) {
 154: return;
 155: }
 156: h("trackId", str);
 157: }
 158: 
 159: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 160: public bqc(int i, int i2, long j, String str, String str2) {
 161: super(null);
 162: this.c = (byte) 2;
 163: if (i == 0 && f09.I(str)) {
 164: k3g.s("Asset type or sectionId should be set");
 165: throw null;
 166: }
 167: if (i != 0) {
 168: h("type", s95.g(i));
 169: }
 170: if (!f09.I(str)) {
 171: h("sectionId", str);
 172: }
 173: f(j, "from");
 174: c(i2, "count");
 175: if (str2 != null) {
 176: h("query", str2);
 177: }
 178: }
 179: 
 180: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 181: public bqc(int i, long j) {
 182: super(null);
 183: this.c = (byte) 1;
 184: if (i == 0) {
 185: k3g.t("type must not be null");
 186: throw null;
 187: }
 188: if (j != 0) {
 189: h("type", s95.g(i));
 190: f(j, "id");
 191: } else {
 192: k3g.t("id must not be null or empty");
 193: throw null;
 194: }
 195: }
 196: 
 197: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 198: public bqc(int i, long[] jArr) {
 199: super(null);
 200: this.c = (byte) 5;
 201: if (i != 0) {
 202: if (jArr != null && jArr.length != 0) {
 203: h("type", s95.g(i));
 204: e("ids", jArr);
 205: return;
 206: } else {
 207: k3g.t("ids must not be null or empty");
 208: throw null;
 209: }
 210: }
 211: k3g.t("type must not be null");
 212: throw null;
 213: }
 214: 
 215: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 216: public bqc(long j) {
 217: super(tdd.y3);
 218: this.c = (byte) 25;
 219: f(j, "callHistorySync");
 220: }
 221: 
 222: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 223: public bqc(long j, String str) {
 224: super(tdd.K2);
 225: this.c = (byte) 0;
 226: h("value", str);
 227: f(j, "userId");
 228: }
 229: }
~~~

## defpackage/f7j.java (83 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class f7j {
   5: public final r1g a;
   6: 
   7: public f7j(r1g r1gVar) {
   8: this.a = r1gVar;
   9: }
  10: 
  11: /* JADX WARN: Multi-variable type inference failed */
  12: public static long a(r1g r1gVar, e7j e7jVar) {
  13: o1d o1dVar = f09.g;
  14: if (o1dVar != null) {
  15: c6a c6aVar = c6a.d;
  16: if (o1dVar.b(c6aVar)) {
  17: o1dVar.c(c6aVar, "f7j", "execute " + e7jVar, null);
  18: }
  19: }
  20: boolean z = e7jVar.b;
  21: ft ftVar = e7jVar.a;
  22: if (!z) {
  23: return r1gVar.d(ftVar, (d7j) ftVar, e7jVar.c);
  24: }
  25: long j = e7jVar.d;
  26: int i = e7jVar.e;
  27: if (ftVar instanceof rwd) {
  28: nm9.J(r1gVar.h(), (z95) r1gVar.l.getValue(), 0, new d1g(r1gVar, ftVar, j, i, null), 2);
  29: return ftVar.a;
  30: }
  31: r1gVar.getClass();
  32: k3g.t("task must be instance of PersistableTask");
  33: return 0L;
  34: }
  35: 
  36: public static long b(f7j f7jVar, ft ftVar) {
  37: f7jVar.getClass();
  38: return a(f7jVar.a, new e7j(ftVar, false, false, 0L, 0));
  39: }
  40: 
  41: public final long c(ft ftVar, boolean z, long j, int i) {
  42: long j2;
  43: int i2;
  44: c6a c6aVar = c6a.d;
  45: o1d o1dVar = f09.g;
  46: if (o1dVar != null && o1dVar.b(c6aVar)) {
  47: StringBuilder sb = new StringBuilder("executeAndSave ");
  48: sb.append(ftVar);
  49: sb.append(", ");
  50: sb.append(z);
  51: sb.append(", ");
  52: j2 = j;
  53: sb.append(j2);
  54: sb.append(", ");
  55: i2 = i;
  56: sb.append(i2);
  57: o1dVar.c(c6aVar, "f7j", sb.toString(), null);
  58: } else {
  59: j2 = j;
  60: i2 = i;
  61: }
  62: e7j e7jVar = new e7j(ftVar, true, z, j2, i2);
  63: o1d o1dVar2 = f09.g;
  64: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
  65: o1dVar2.c(c6aVar, "f7j", "tamService != null, execute task " + e7jVar + " ", null);
  66: }
  67: return a(this.a, e7jVar);
  68: }
  69: 
  70: public final Object e(k5a k5aVar, s5a s5aVar) {
  71: return this.a.b(k5aVar, s5aVar);
  72: }
  73: 
  74: public final Object f(ft ftVar, d55 d55Var) {
  75: r1g r1gVar = this.a;
  76: r1gVar.getClass();
  77: cu2 cu2Var = new cu2(1, e0c.K(d55Var));
  78: cu2Var.w();
  79: cu2Var.y(new xf2((Object) r1gVar, (Object) ftVar, (byte) 10));
  80: r1gVar.d(ftVar, new i1g(cu2Var, ftVar), false);
  81: return cu2Var.u();
  82: }
  83: }
~~~

## defpackage/ctc.java (16 строк)

~~~java
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
~~~

## defpackage/bcc.java (689 строк)

~~~java
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
~~~

Поздние сигнатуры: 332 public final void i(int i, IOException iOException) {; 397 public final void j(int i) {; 426 public final boolean k() {; 430 public final boolean l() {; 434 public final void m(l5a l5aVar, long j, short s, short s2, boolean z, String str) {; 438 public final void n(l5a l5aVar, long j, short s, short s2, boolean z, String str, String str2, int i) {; 478 public final void o(cld cldVar, int i, dld dldVar, long j, int i2, long j2) {; 554 public final void p() {; 558 public final void q(int i) {; 577 public final void r(e46 e46Var) {; 583 public final void s(Exception exc, boolean z) {; 590 public final boolean t(final int i) {; 603 public final Object c() {; 624 public final String toString() {; 652 public final boolean u(int i) {; 672 public final void w(boolean z) {

## defpackage/ccc.java (35 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class ccc {
   5: public final o57 a;
   6: public final j6h b;
   7: public final vng c;
   8: public final st5 d;
   9: public final f6h e;
  10: public final kuc f;
  11: public final ruc g;
  12: public final q7c h;
  13: public final z3j i;
  14: public final boolean j;
  15: public final boolean k;
  16: public boolean l;
  17: public boolean m;
  18: public boolean n;
  19: public final o57 o;
  20: 
  21: public ccc(o57 o57Var, j6h j6hVar, vng vngVar, st5 st5Var, f6h f6hVar, kuc kucVar, ruc rucVar, q7c q7cVar, z3j z3jVar, boolean z, boolean z2) {
  22: this.a = o57Var;
  23: this.b = j6hVar;
  24: this.c = vngVar;
  25: this.d = st5Var;
  26: this.e = f6hVar;
  27: this.f = kucVar;
  28: this.g = rucVar;
  29: this.h = q7cVar;
  30: this.i = z3jVar;
  31: this.j = z;
  32: this.k = z2;
  33: this.o = o57Var;
  34: }
  35: }
~~~

## defpackage/z6j.java (200 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.Collections;
   4: import java.util.HashSet;
   5: import java.util.Map;
   6: import java.util.Set;
   7: import java.util.concurrent.atomic.AtomicLong;
   8: import java.util.concurrent.atomic.AtomicReference;
   9: 
  10: /* JADX INFO: loaded from: classes.dex */
  11: public final class z6j implements b6h, ls4 {
  12: public final dcc a;
  13: public final f4j b;
  14: public final boolean c;
  15: public final rp9 d;
  16: public final rp9 e;
  17: public final rp9 f;
  18: public final rp9 g;
  19: public final rp9 h;
  20: public final AtomicReference i;
  21: public final AtomicLong j;
  22: public final String k;
  23: public final Set l;
  24: 
  25: public z6j(dcc dccVar, rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, c6h c6hVar, s8a s8aVar, boolean z) {
  26: f4j f4jVar = new f4j((byte) 2);
  27: this.a = dccVar;
  28: this.b = f4jVar;
  29: this.c = z;
  30: this.d = rp9Var;
  31: this.e = rp9Var2;
  32: this.f = rp9Var3;
  33: this.g = rp9Var4;
  34: this.h = rp9Var5;
  35: this.j = new AtomicLong(0L);
  36: this.k = "SessionController";
  37: this.l = Collections.synchronizedSet(new HashSet());
  38: this.i = new AtomicReference(f());
  39: ((f6h) c6hVar).c(this);
  40: ((es4) rp9Var5.getValue()).a().d(this);
  41: s8aVar.G(!((dtc) rp9Var2.getValue()).b());
  42: }
  43: 
  44: @Override // defpackage.ls4
  45: public final void a() {
  46: e(false);
  47: }
  48: 
  49: @Override // defpackage.ls4
  50: public final void b() {
  51: f09.p(this.k, "onConnectionTypeChange");
  52: rp9 rp9Var = this.h;
  53: boolean zG = ((es4) rp9Var.getValue()).a().g();
  54: AtomicReference atomicReference = this.i;
  55: if (!zG) {
  56: ((bcc) atomicReference.get()).w(false);
  57: } else if (((es4) rp9Var.getValue()).e()) {
  58: ((bcc) atomicReference.get()).w(true);
  59: }
  60: }
  61: 
  62: @Override // defpackage.b6h
  63: public final void c(int i) {
  64: AtomicReference atomicReference = this.i;
  65: String str = this.k;
  66: if (i == 0) {
  67: f09.d0(str, "onNoNet", new Object[0]);
  68: i((bcc) atomicReference.get());
  69: return;
  70: }
  71: if (i == 1) {
  72: f09.p(str, "onDisconnected");
  73: i((bcc) atomicReference.get());
  74: } else if (i == 2) {
  75: f09.p(str, "onConnected");
  76: } else if (i == 3) {
  77: f09.p(str, "onLoggedIn");
  78: } else {
  79: k3g.o(w7g.E(i, "Unknown session state="));
  80: }
  81: }
  82: 
  83: public final void d(u6j u6jVar) {
  84: if (this.c) {
  85: bcc bccVar = (bcc) this.i.get();
  86: f09.o(bccVar.a, "cancelRequest %s", u6jVar);
  87: if (bccVar.g.get()) {
  88: f09.d0(bccVar.a, "cancelRequest ignored, session is closed!", new Object[0]);
  89: return;
  90: }
  91: synchronized (bccVar.w) {
  92: try {
  93: for (fld fldVar : bccVar.v) {
  94: eld eldVar = fldVar.b;
  95: if (eldVar != null && eldVar.a.equals(u6jVar)) {
  96: String str = bccVar.a;
  97: short sK = fldVar.b.a.k();
  98: tdd.c.getClass();
  99: f09.o(str, "cancelRequest(): remove task from mPacketSenderTasks, opcode=%s, requestId=%s", cp5.l(sK), Long.valueOf(fldVar.b.c.p()));
 100: bccVar.v.remove(fldVar);
 101: fldVar.e = true;
 102: break;
 103: }
 104: }
 105: } catch (Throwable th) {
 106: throw th;
 107: }
 108: }
 109: for (Map.Entry entry : bccVar.u.entrySet()) {
 110: eld eldVar2 = ((dld) entry.getValue()).b.b;
 111: if (eldVar2 != null && eldVar2.a.equals(u6jVar)) {
 112: f09.o(bccVar.a, "cancelRequest(): remove task from mPacketReaderTasks, seq=%s, requestId=%s", entry.getKey(), Long.valueOf(((dld) entry.getValue()).a.p()));
 113: bccVar.u.remove(entry.getKey());
 114: ((dld) entry.getValue()).e = true;
 115: return;
 116: }
 117: }
 118: }
 119: }
 120: 
 121: public final void e(boolean z) {
 122: if (!z) {
 123: rp9 rp9Var = this.h;
 124: if (!((es4) rp9Var.getValue()).a().g() \|\| !((es4) rp9Var.getValue()).e()) {
 125: return;
 126: }
 127: }
 128: ((bcc) this.i.get()).w(true);
 129: }
 130: 
 131: public final bcc f() {
 132: dcc dccVar = this.a;
 133: o57 o57Var = (o57) dccVar.d.getValue();
 134: j6h j6hVar = (j6h) dccVar.k.getValue();
 135: vng vngVar = (vng) dccVar.g.getValue();
 136: st5 st5Var = (st5) dccVar.f.getValue();
 137: f6h f6hVar = (f6h) dccVar.e.getValue();
 138: kuc kucVar = (kuc) dccVar.h.getValue();
 139: ruc rucVar = (ruc) dccVar.i.getValue();
 140: q7c q7cVar = (q7c) dccVar.j.getValue();
 141: z3j z3jVar = dccVar.a;
 142: boolean z = dccVar.b;
 143: boolean z2 = dccVar.c;
 144: rp9 rp9Var = this.d;
 145: g9e g9eVar = ((dle) rp9Var.getValue()).b.b().a.Y1;
 146: zm9[] zm9VarArr = j9e.w8;
 147: ((Number) g9eVar.a(zm9VarArr[153]).i()).intValue();
 148: boolean zBooleanValue = ((Boolean) ((dle) rp9Var.getValue()).b.a().a.j4.a(zm9VarArr[270]).i()).booleanValue();
 149: boolean zW = ((dle) rp9Var.getValue()).b.a().w();
 150: boolean zBooleanValue2 = ((Boolean) ((dle) rp9Var.getValue()).b.a().a.m4.a(zm9VarArr[273]).i()).booleanValue();
 151: ccc cccVar = new ccc(o57Var, j6hVar, vngVar, st5Var, f6hVar, kucVar, rucVar, q7cVar, z3jVar, z, z2);
 152: cccVar.l = zBooleanValue;
 153: cccVar.m = zW;
 154: cccVar.n = zBooleanValue2;
 155: return new bcc(cccVar);
 156: }
 157: 
 158: public final void g() {
 159: int iIntValue;
 160: int size;
 161: bcc bccVar = (bcc) this.i.get();
 162: if (this.l.isEmpty() && (iIntValue = ((Number) ((dle) this.d.getValue()).b.b().a.M.a(j9e.w8[31]).i()).intValue()) > 0 && ((dtc) this.e.getValue()).b() && !((wag) this.f.getValue()).g() && ((wag) ((os7) this.g.getValue())).d <= 0) {
 163: long j = this.j.get();
 164: long jK = fe6.k(this.b.V0());
 165: me6 me6Var = me6.d;
 166: boolean z = fe6.f(fe6.r(az7.V(jK, me6Var), az7.V(j, me6Var)), az7.U(iIntValue, me6Var)) > 0;
 167: if (j <= 0 \|\| !z) {
 168: return;
 169: }
 170: synchronized (bccVar.w) {
 171: size = bccVar.v.size();
 172: }
 173: if (size != 0) {
 174: return;
 175: }
 176: f09.p(this.k, "disconnectIfNeeded: timeout expired, disconnect");
 177: bccVar.w(false);
 178: }
 179: }
 180: 
 181: public final void h() {
 182: this.i.getAndUpdate(new ug1(this, (byte) 10));
 183: e(false);
 184: }
 185: 
 186: public final void i(bcc bccVar) {
 187: String str = this.k;
 188: f09.p(str, "updateSession");
 189: rp9 rp9Var = this.h;
 190: if (!((es4) rp9Var.getValue()).a().g()) {
 191: f09.d0(str, "updateSession, seems there is NO net", new Object[0]);
 192: bccVar.w(false);
 193: } else if (((es4) rp9Var.getValue()).e()) {
 194: bccVar.w(true);
 195: } else {
 196: f09.d0(str, "updateSession, connection is NOT permitted", new Object[0]);
 197: bccVar.w(false);
 198: }
 199: }
 200: }
~~~

## defpackage/v99.java (33 строк)

~~~java
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
~~~

## defpackage/wpc.java (951 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import android.content.res.Resources;
   5: import android.media.LoudnessCodecController;
   6: import android.media.MediaCodec;
   7: import android.media.MediaFormat;
   8: import android.os.Build;
   9: import android.os.Bundle;
  10: import android.os.Handler;
  11: import android.os.IBinder;
  12: import android.os.Messenger;
  13: import android.os.RemoteException;
  14: import android.os.SystemClock;
  15: import android.util.Log;
  16: import android.view.Surface;
  17: import android.view.WindowInsetsAnimation;
  18: import io.reactivex.rxjava3.exceptions.CompositeException;
  19: import java.io.ByteArrayOutputStream;
  20: import java.io.File;
  21: import java.io.FileInputStream;
  22: import java.io.FileOutputStream;
  23: import java.io.IOException;
  24: import java.nio.ByteBuffer;
  25: import java.util.ArrayList;
  26: import java.util.HashSet;
  27: import java.util.LinkedHashSet;
  28: import java.util.Objects;
  29: import java.util.concurrent.ScheduledFuture;
  30: import java.util.concurrent.locks.ReentrantLock;
  31: import me.leolin.shortcutbadger.BuildConfig;
  32: import one.me.sdk.transfer.exceptions.HttpUrlExpiredException;
  33: import one.video.calls.sdk.upload.FileUploadService;
  34: import one.video.upload.exceptions.UploadUrlExpiredException;
  35: import org.json.JSONException;
  36: import org.json.JSONObject;
  37: import ru.ok.android.externcalls.sdk.e;
  38: import ru.ok.tamtam.api.UnknownOpcodeException;
  39: import ru.ok.tamtam.errors.TamErrorException;
  40: import ru.oneme.app.R;
  41: 
  42: /* JADX INFO: loaded from: classes2.dex */
  43: public final class wpc implements ng2, w9k, y18, fv4, zif, e6j, csh, yma, u7k {
  44: public final /* synthetic */ byte a;
  45: public Object b;
  46: public Object c;
  47: 
  48: public wpc(IBinder iBinder) throws RemoteException {
  49: this.a = (byte) 26;
  50: String interfaceDescriptor = iBinder.getInterfaceDescriptor();
  51: if (Objects.equals(interfaceDescriptor, "android.os.IMessenger")) {
  52: this.b = new Messenger(iBinder);
  53: this.c = null;
  54: } else {
  55: if (!Objects.equals(interfaceDescriptor, "com.google.android.gms.iid.IMessengerCompat")) {
  56: Log.w("MessengerIpcClient", "Invalid interface descriptor: ".concat(String.valueOf(interfaceDescriptor)));
  57: throw new RemoteException();
  58: }
  59: this.c = new mrm(iBinder);
  60: this.b = null;
  61: }
  62: }
  63: 
  64: public static drh z(wpc wpcVar, Context context, int i, a9d a9dVar, int i2) {
  65: if ((i2 & 8) != 0) {
  66: a9dVar = null;
  67: }
  68: a7i a7iVar = (a7i) wpcVar.b;
  69: if (i == R.id.oneme_stickers_view_type_stickers_set_recent_add_button) {
  70: return new pp7(context, (o08) wpcVar.c, a9dVar);
  71: }
  72: if (i == R.id.oneme_stickers_view_type_sticker_webm) {
  73: return new jba(context, a7iVar, (byte) 1);
  74: }
  75: return i == R.id.oneme_stickers_view_type_sticker_lottie ? new jba(context, a7iVar, (byte) 0) : new r6i(context, a7iVar);
  76: }
  77: 
  78: public File A() {
  79: File file;
  80: File file2 = (File) this.b;
  81: if (file2 != null) {
  82: return file2;
  83: }
  84: synchronized (this) {
  85: try {
  86: file = (File) this.b;
  87: if (file == null) {
  88: gg7 gg7Var = (gg7) this.c;
  89: gg7Var.a();
  90: file = new File(gg7Var.a.getFilesDir(), "PersistedInstallation." + ((gg7) this.c).c() + ".json");
  91: this.b = file;
  92: }
  93: } catch (Throwable th) {
  94: throw th;
  95: }
  96: }
  97: return file;
  98: }
  99: 
 100: public String B(String str) {
 101: String str2 = (String) this.c;
 102: Resources resources = (Resources) this.b;
 103: int identifier = resources.getIdentifier(str, "string", str2);
 104: if (identifier == 0) {
 105: return null;
 106: }
 107: return resources.getString(identifier);
 108: }
 109: 
 110: @Override // defpackage.ng2
 111: public void C(kmf kmfVar, IOException iOException) {
 112: IOException iOException2 = (IOException) this.c;
 113: cu2 cu2Var = (cu2) this.b;
 114: if (cu2Var.v() instanceof lu2) {
 115: return;
 116: }
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
 146: } catch (IOException \| JSONException unused) {
 147: }
 148: }
 149: 
 150: public void E(ic6 ic6Var) {
 151: LinkedHashSet linkedHashSet = (LinkedHashSet) this.c;
 152: zlj zljVar = (zlj) ic6Var.a;
 153: if (zljVar != zlj.e \|\| linkedHashSet.contains(zlj.b)) {
 154: if (zljVar != zlj.d \|\| linkedHashSet.contains(zlj.c)) {
 155: ((dmj) this.b).a(ic6Var);
 156: linkedHashSet.add(zljVar);
 157: }
 158: }
 159: }
 160: 
 161: public void F() {
 162: String str = ((fdd) this.b).j;
 163: o1d o1dVar = f09.g;
 164: if (o1dVar != null) {
 165: c6a c6aVar = c6a.d;
 166: if (o1dVar.b(c6aVar)) {
 167: o1dVar.c(c6aVar, str, "finish", null);
 168: }
 169: }
 170: t7k.a((t7k) ((fdd) this.b).o.getValue(), 0L, 0.0f, null, 23);
 171: ((syg) this.c).f(new p4g(new f8k(100, ((fdd) this.b).m, null)));
 172: ((syg) this.c).c(null);
 173: }
 174: 
 175: public void G(String str) {
 176: k8k k8kVarE = ((y6k) this.b).e();
 177: String str2 = ((u5k) ((iuf) this.c).a).a.d;
 178: k8kVarE.getClass();
 179: long[] jArr = lig.a;
 180: e4c e4cVar = new e4c();
 181: if (str != null) {
 182: e4cVar.k("host_ip", str);
 183: }
 184: wud.h(k8kVarE, "url_connected", 2, str2, false, null, e4cVar, 24);
 185: }
 186: 
 187: public gn0 H() {
 188: JSONObject jSONObject;
 189: ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
 190: byte[] bArr = new byte[16384];
 191: try {
 192: FileInputStream fileInputStream = new FileInputStream(A());
 193: while (true) {
 194: try {
 195: int i = fileInputStream.read(bArr, 0, 16384);
 196: if (i < 0) {
 197: break;
 198: }
 199: byteArrayOutputStream.write(bArr, 0, i);
 200: } catch (Throwable th) {
 201: try {
 202: fileInputStream.close();
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
 226: }
 227: String str = i2 == 0 ? " registrationStatus" : BuildConfig.FLAVOR;
 228: if (str.isEmpty()) {
 229: return new gn0(i2, jOptLong2, jOptLong, strOptString, strOptString2, strOptString3, strOptString4);
 230: }
 231: k3g.o("Missing required properties:".concat(str));
 232: return null;
 233: }
 234: 
 235: @Override // defpackage.y18
 236: public void a(Object obj) {
 237: nr6 nr6Var;
 238: switch (this.a) {
 239: case 4:
 240: nr6 nr6Var2 = (nr6) obj;
 241: wsf wsfVar = (wsf) this.c;
 242: ywm.b("Recorder", "VideoEncoder can be released: " + nr6Var2);
 243: if (nr6Var2 != null) {
 244: ScheduledFuture scheduledFuture = wsfVar.b0;
 245: if (scheduledFuture != null && scheduledFuture.cancel(false) && (nr6Var = wsfVar.H) != null && nr6Var == nr6Var2) {
 246: wsf.v(nr6Var);
 247: }
 248: wsfVar.f0 = (l0c) this.b;
 249: wsfVar.G(null);
 250: wsfVar.z(wsfVar.s());
 251: break;
 252: }
 253: break;
 254: case 10:
 255: ((csh) this.b).a(obj);
 256: break;
 257: default:
 258: try {
 259: Object objMo16apply = ((g18) this.c).mo16apply(obj);
 260: Objects.requireNonNull(objMo16apply, "The mapper function returned a null value.");
~~~

Поздние сигнатуры: 272 public void accept(Object obj) {; 322 public void b(x6j x6jVar) {; 651 public void c(z56 z56Var) {; 663 public void d(long j, int i, int i2, int i3) {; 668 public void e(int i, ze5 ze5Var, long j, int i2) {; 673 public void f(l6j l6jVar) {; 681 public void flush() {; 686 public void g(long j) {; 706 public void h(int i) {; 711 public void i(long j, long j2) {; 729 public void k() {; 734 public void m(f9k f9kVar) {; 746 public void n(int i, long j) {; 751 public int o() {; 756 public void onError(Throwable th) {; 790 public void onFailure(Throwable th) {; 795 public int q(MediaCodec.BufferInfo bufferInfo) {; 804 public void r() {; 809 public void release() {; 826 public void s(Throwable th) {; 831 public void setParameters(Bundle bundle) {; 836 public void t(int i) {; 840 public String toString() {; 852 public void u(Surface surface) {

## defpackage/dq4.java (88 строк)

~~~java
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
~~~

## defpackage/yr0.java (3260 строк)

~~~java
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
~~~

Поздние сигнатуры: 1310 private final Object y(Object obj) throws Throwable {; 1451 private final Object z(Object obj) {; 1575 public final Object invoke(Object obj, Object obj2) {; 1631 public final b55 u(b55 b55Var, Object obj) {; 1840 public final Object w(Object obj) throws Throwable {

## defpackage/u79.java (156 строк)

~~~java
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
~~~

## defpackage/lp4.java (216 строк)

~~~java
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
~~~

## defpackage/s1c.java (18 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class s1c {
   7: public final r1c a;
   8: public final rp9 c;
   9: public ArrayList e;
  10: public so f;
  11: public final String b = s1c.class.getName();
  12: public final r4i d = az7.c(Boolean.FALSE);
  13: 
  14: public s1c(r1c r1cVar, rp9 rp9Var) {
  15: this.a = r1cVar;
  16: this.c = rp9Var;
  17: }
  18: }
~~~

## defpackage/r1c.java (19 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import java.io.File;
   5: import ru.ok.messages.utils.ContextDirCreationException;
   6: 
   7: /* JADX INFO: loaded from: classes.dex */
   8: public final class r1c {
   9: public final File a;
  10: 
  11: public r1c(Context context) {
  12: if (!er0.d0(false, null, new scc(context, (byte) 8))) {
  13: f09.c0("cf7", "dataDir doesn't exists.", new ContextDirCreationException("dataDir"));
  14: }
  15: File fileD0 = ef7.d0(context.getDataDir(), "accounts_db");
  16: fileD0.mkdirs();
  17: this.a = fileD0;
  18: }
  19: }
~~~

## defpackage/p1c.java (8 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class p1c extends h6 {
   5: public final c74 a() {
   6: return (c74) getAccessor().c(92);
   7: }
   8: }
~~~

## defpackage/n3a.java (296 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import android.content.SharedPreferences;
   5: import java.util.Iterator;
   6: import java.util.Map;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class n3a extends hog {
  10: public static final /* synthetic */ zm9[] g1 = {new c4c(n3a.class, "phoneCode", "getPhoneCode()Ljava/lang/String;"), a15.f(luf.a, n3a.class, "phoneNumber", "getPhoneNumber()Ljava/lang/String;"), new c4c(n3a.class, "locationCountryCode", "getLocationCountryCode()Ljava/lang/String;"), new c4c(n3a.class, "serverHost", "getServerHost()Ljava/l
  11: public final zcg A0;
  12: public final zcg B0;
  13: public final zcg C0;
  14: public final zcg D0;
  15: public final zcg E0;
  16: public final zcg F0;
  17: public final zcg G0;
  18: public final zcg H0;
  19: public final zcg I0;
  20: public final zcg J0;
  21: public final zcg K0;
  22: public final zcg L0;
  23: public final zcg M0;
  24: public final wt8 N0;
  25: public final zcg O0;
  26: public final zcg P0;
  27: public final zcg Q0;
  28: public final zcg R0;
  29: public final y3 S0;
  30: public final zcg T0;
  31: public final zcg U0;
  32: public final zcg V0;
  33: public final zcg W0;
  34: public final zcg X0;
  35: public final zcg Y0;
  36: public final y3 Z0;
  37: public final zcg a1;
  38: public final zcg b1;
  39: public final zcg c1;
  40: public final zcg d1;
  41: public final zcg e1;
  42: public final zcg f1;
  43: public final rp9 j0;
  44: public final zcg k0;
  45: public final zcg l0;
  46: public final zcg m0;
  47: public final zcg n0;
  48: public final zcg o0;
  49: public final zcg p0;
  50: public final zcg q0;
  51: public final zcg r0;
  52: public final zcg s0;
  53: public final zcg t0;
  54: public final zcg u0;
  55: public final zcg v0;
  56: public final zcg w0;
  57: public final zcg x0;
  58: public final zcg y0;
  59: public final zcg z0;
  60: 
  61: public n3a(Context context, uc7 uc7Var, q1a q1aVar, rp9 rp9Var, rp9 rp9Var2) {
  62: super(context, q1aVar.a("user", "prefs"), uc7Var, rp9Var2);
  63: this.j0 = rp9Var;
  64: this.k0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.Phone.Code");
  65: this.l0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.Phone");
  66: this.m0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "app.location.country.code");
  67: this.n0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "server.host");
  68: this.o0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "server.port");
  69: Boolean bool = Boolean.TRUE;
  70: this.p0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "server.useTls");
  71: this.q0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "server.loginError");
  72: Boolean bool2 = Boolean.FALSE;
  73: new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "user.dev.options.roaming");
  74: this.r0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.call.add.dontshowconfirmation");
  75: luf.a(Integer.class);
  76: this.s0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.last.push.alert.time");
  77: this.t0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.full.contacts.sync.completed");
  78: this.u0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "ok_push_disabled");
  79: this.v0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "web_app:ssl_check");
  80: this.w0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.disable_in_app_review_time_condition");
  81: this.x0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.enable_in_app_review_not_from_market_build");
  82: this.y0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.debug.profile.info.enabled");
  83: this.z0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.stats.session.id");
  84: this.A0 = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "version.force.update.received");
  85: this.B0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.debug.fresco");
  86: this.C0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.toggle.webapp_fullscreen");
  87: this.D0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.onboarding.author_visibility");
  88: this.E0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.audio_onboarding_ended");
  89: this.F0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.calls_sdk.debug.debug_menu");
  90: this.G0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.calls.hold_button_enabled");
  91: luf.a(Boolean.class);
  92: this.H0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "user.onboarding.scheduled_messages");
  93: this.I0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) (-1L), "app.calls.permission_request_time");
  94: qzd qzdVar = fe6.b;
  95: fe6 fe6Var = new fe6(az7.U(0, me6.b));
  96: this.J0 = new zcg(luf.a(fe6.class), (SharedPreferences) this.d, (Object) fe6Var, "app.informer_banners.show_duration");
  97: this.K0 = new zcg(luf.a(Map.class), (SharedPreferences) this.d, (Object) sp6.a, "app.calls.incoming.ringtone");
  98: this.L0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.calls.contact_ringtones_enabled");
  99: this.M0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.calls.change_mode_swipe_used");
 100: this.N0 = new wt8((Object) this, (Object) new hka(qp6.a), (byte) 22);
 101: this.O0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.informer_banners.sync");
 102: this.P0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "folders_sync");
 103: this.Q0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.complain_reasons.sync");
 104: this.R0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.video.debug.view");
 105: this.S0 = new y3("app.logging.sensitive", bool2, this.d, this.b, luf.a(Boolean.class));
 106: this.T0 = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "app.last_requested_permission");
 107: this.U0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.has_missed_calls_alert.shown_time");
 108: this.V0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.is_missed_calls_alert_read");
 109: Float fValueOf = Float.valueOf(0.0f);
 110: this.W0 = new zcg(luf.a(Float.class), (SharedPreferences) this.d, (Object) fValueOf, "app.video.player.playback_speed");
 111: this.X0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.onboarding.transcription");
 112: this.Y0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.onboarding.discussions");
 113: this.Z0 = new y3("app.player.audio_video_message_playback_speed", Float.valueOf(1.0f), this.d, this.b, luf.a(Float.class));
 114: luf.a(Boolean.class);
 115: this.a1 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) null, "app.onboarding.channels_folder_highlight_shown_first_time");
 116: this.b1 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) null, "app.onboarding.digital_id_highlight_shown_first_time");
 117: this.c1 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) null, "app.onboarding.channel_instruments_highlight_shown_first_time");
 118: new y3("app.leak.canary.enabled", bool2, this.d, this.b, luf.a(Boolean.class));
 119: this.d1 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "debug.cache.transcode_ignore");
 120: this.e1 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "debug.media.video.autoload.force");
 121: this.f1 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool2, "app.logout.started");
 122: luf.a(Long.class);
 123: }
 124: 
 125: public final x3 O() {
 126: zm9 zm9Var = g1[44];
 127: return (x3) this.Z0.g;
 128: }
 129: 
 130: public final long P() {
 131: return ((Number) this.P0.s(this, g1[34])).longValue();
 132: }
 133: 
 134: public final int Q() {
 135: return ((Number) this.T0.s(this, g1[38])).intValue();
 136: }
 137: 
 138: public final Map R() {
 139: return (Map) this.K0.s(this, g1[29]);
 140: }
 141: 
 142: public final hka S() {
 143: return (hka) this.N0.s(this, g1[32]);
 144: }
 145: 
 146: public final String T() {
 147: return (String) this.l0.s(this, g1[1]);
 148: }
 149: 
 150: public final String U() {
 151: return (String) this.n0.s(this, g1[3]);
 152: }
 153: 
 154: public final String V() {
 155: return (String) this.o0.s(this, g1[4]);
 156: }
 157: 
 158: public final long W() {
 159: return ((Number) this.z0.s(this, g1[17])).longValue();
 160: }
 161: 
 162: public final boolean X() {
 163: return ((Boolean) this.p0.s(this, g1[5])).booleanValue();
 164: }
 165: 
 166: public final float Y() {
 167: return ((Number) this.W0.s(this, g1[41])).floatValue();
 168: }
 169: 
 170: public final boolean Z() {
 171: return ((Boolean) this.F0.s(this, g1[23])).booleanValue();
 172: }
 173: 
 174: public final boolean a0() {
 175: return ((Boolean) this.L0.s(this, g1[30])).booleanValue();
 176: }
 177: 
 178: @Override // defpackage.hog, defpackage.a4
 179: public final void b() {
 180: String strU = U();
 181: String strV = V();
 182: boolean zX = X();
 183: zm9[] zm9VarArr = g1;
 184: zm9 zm9Var = zm9VarArr[6];
 185: zcg zcgVar = this.q0;
 186: String str = (String) zcgVar.s(this, zm9Var);
 187: zm9[] zm9VarArr2 = hog.i0;
 188: zm9 zm9Var2 = zm9VarArr2[5];
 189: zcg zcgVar2 = this.l;
 190: String str2 = (String) zcgVar2.s(this, zm9Var2);
 191: zm9 zm9Var3 = zm9VarArr2[2];
 192: zcg zcgVar3 = this.j;
 193: String str3 = (String) zcgVar3.s(this, zm9Var3);
 194: zm9 zm9Var4 = zm9VarArr2[3];
 195: zcg zcgVar4 = this.k;
 196: int iIntValue = ((Number) zcgVar4.s(this, zm9Var4)).intValue();
 197: zm9 zm9Var5 = zm9VarArr2[7];
 198: zcg zcgVar5 = this.m;
 199: Boolean bool = (Boolean) zcgVar5.s(this, zm9Var5);
 200: bool.getClass();
 201: zm9 zm9Var6 = zm9VarArr2[8];
 202: zcg zcgVar6 = this.n;
 203: Boolean bool2 = (Boolean) zcgVar6.s(this, zm9Var6);
 204: bool2.getClass();
 205: String strL = l();
 206: zm9 zm9Var7 = zm9VarArr2[46];
 207: zcg zcgVar7 = this.X;
 208: String str4 = (String) zcgVar7.s(this, zm9Var7);
 209: zm9 zm9Var8 = zm9VarArr2[45];
 210: zcg zcgVar8 = this.W;
 211: long jLongValue = ((Number) zcgVar8.s(this, zm9Var8)).longValue();
 212: long jW = W();
 213: Map mapR = R();
 214: boolean zBooleanValue = ((Boolean) this.f1.s(this, zm9VarArr[52])).booleanValue();
 215: int iH = h();
 216: int iIntValue2 = ((Number) this.N.s(this, zm9VarArr2[36])).intValue();
 217: i00 i00Var = new i00(0);
 218: Iterator it = ((i00) this.d.getAll()).entrySet().iterator();
 219: while (it.hasNext()) {
 220: Map.Entry entry = (Map.Entry) it.next();
 221: Iterator it2 = it;
 222: String str5 = (String) entry.getKey();
 223: Boolean bool3 = bool2;
 224: Object value = entry.getValue();
 225: zcg zcgVar9 = zcgVar6;
 226: Boolean bool4 = bool;
 227: if (hui.Z(str5, "app.pin", false) && (value instanceof String)) {
 228: i00Var.put(str5, value);
 229: }
 230: zcgVar6 = zcgVar9;
 231: bool2 = bool3;
 232: it = it2;
 233: bool = bool4;
 234: }
 235: zcg zcgVar10 = zcgVar6;
 236: super.b();
 237: this.n0.z(this, zm9VarArr[3], strU);
 238: k0(strV);
 239: this.p0.z(this, zm9VarArr[5], Boolean.valueOf(zX));
 240: zcgVar.z(this, zm9VarArr[6], str);
 241: zcgVar2.z(this, zm9VarArr2[5], str2);
 242: zcgVar3.z(this, zm9VarArr2[2], str3);
 243: zcgVar4.z(this, zm9VarArr2[3], Integer.valueOf(iIntValue));
 244: zcgVar5.z(this, zm9VarArr2[7], bool);
 245: zcgVar10.z(this, zm9VarArr2[8], bool2);
 246: D(strL);
 247: zcgVar7.z(this, zm9VarArr2[46], str4);
 248: zcgVar8.z(this, zm9VarArr2[45], Long.valueOf(jLongValue));
 249: this.z0.z(this, zm9VarArr[17], Long.valueOf(jW));
 250: h0(mapR);
 251: i0(zBooleanValue);
 252: x(iH);
 253: y(iIntValue2);
 254: i00Var.forEach(new m3a(new f60(this), (byte) 0));
 255: }
 256: 
 257: public final boolean b0() {
 258: return ((Boolean) this.w0.s(this, g1[14])).booleanValue();
 259: }
 260: 
~~~

Поздние сигнатуры: 261 public final boolean c0() {; 265 public final boolean d0() {; 269 public final boolean e0() {; 273 public final void f0(long j) {; 277 public final void g0(int i) {; 281 public final void h0(Map map) {; 285 public final void i0(boolean z) {; 289 public final void j0(String str) {; 293 public final void k0(String str) {

## defpackage/h16.java (120 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import android.provider.Settings;
   5: import java.util.UUID;
   6: import java.util.concurrent.atomic.AtomicReference;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class h16 {
  10: public final Context a;
  11: public final rp9 c;
  12: public final rp9 d;
  13: public final rp9 e;
  14: public final String b = h16.class.getName();
  15: public final AtomicReference f = new AtomicReference(null);
  16: 
  17: public h16(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, Context context) {
  18: this.a = context;
  19: this.c = rp9Var;
  20: this.d = rp9Var2;
  21: this.e = rp9Var3;
  22: }
  23: 
  24: /* JADX WARN: Code duplicated, block: B:35:0x00b6  */
  25: /* JADX WARN: Code duplicated, block: B:38:0x00bf  */
  26: /* JADX WARN: Code duplicated, block: B:45:0x00cd  */
  27: /* JADX WARN: Code duplicated, block: B:46:0x00d6  */
  28: /* JADX WARN: Code duplicated, block: B:51:0x009c A[EXC_TOP_SPLITTER, SYNTHETIC] */
  29: public final String a() {
  30: Object n4gVar;
  31: Object n4gVar2;
  32: Throwable thA;
  33: String str;
  34: n3a n3aVar = (n3a) ((c74) this.d.getValue());
  35: wp9 wp9Var = n3aVar.d;
  36: wp9 wp9Var2 = n3aVar.d;
  37: String str2 = null;
  38: if (wp9Var.contains("device.id")) {
  39: String string = wp9Var2.getString("device.id", null);
  40: y3 y3Var = ((mag) ((lag) n3aVar.j0.getValue())).g;
  41: zm9 zm9Var = mag.i[2];
  42: ((x3) y3Var.g).setValue(string);
  43: rc7 rc7Var = (rc7) wp9Var2.edit();
  44: rc7Var.remove("device.id");
  45: rc7Var.apply();
  46: }
  47: rp9 rp9Var = this.c;
  48: y3 y3Var2 = ((mag) ((lag) rp9Var.getValue())).g;
  49: zm9 zm9Var2 = mag.i[2];
  50: String str3 = (String) ((x3) y3Var2.g).g();
  51: if (str3 != null && str3.length() != 0) {
  52: return str3;
  53: }
  54: String str4 = this.b;
  55: f09.p(str4, "Generating new device id");
  56: try {
  57: n4gVar = Settings.Secure.getString(this.a.getContentResolver(), "android_id");
  58: } catch (Throwable th) {
  59: n4gVar = new n4g(th);
  60: }
  61: Throwable thA2 = p4g.a(n4gVar);
  62: if (thA2 != null) {
  63: f09.c0(str4, "Can't get hardware device id", thA2);
  64: }
  65: if (n4gVar instanceof n4g) {
  66: n4gVar = null;
  67: }
  68: String string2 = (String) n4gVar;
  69: if (string2 == null) {
  70: try {
  71: n4gVar2 = ((gci) this.e.getValue()).a();
  72: } catch (Throwable th2) {
  73: n4gVar2 = new n4g(th2);
  74: }
  75: thA = p4g.a(n4gVar2);
  76: if (thA != null) {
  77: f09.c0(str4, "Can't get service instance id", thA);
  78: }
  79: if (n4gVar2 instanceof n4g) {
  80: n4gVar2 = null;
  81: }
  82: str = (String) n4gVar2;
  83: if (str != null && str.length() > 0) {
  84: str2 = str;
  85: }
  86: if (str2 == null) {
  87: string2 = UUID.randomUUID().toString();
  88: } else {
  89: string2 = str2;
  90: }
  91: } else {
  92: if (string2.length() <= 0) {
  93: string2 = null;
  94: }
  95: if (string2 == null) {
  96: n4gVar2 = ((gci) this.e.getValue()).a();
  97: thA = p4g.a(n4gVar2);
  98: if (thA != null) {
  99: f09.c0(str4, "Can't get service instance id", thA);
 100: }
 101: if (n4gVar2 instanceof n4g) {
 102: n4gVar2 = null;
 103: }
 104: str = (String) n4gVar2;
 105: if (str != null) {
 106: str2 = str;
 107: }
 108: if (str2 == null) {
 109: string2 = UUID.randomUUID().toString();
 110: } else {
 111: string2 = str2;
 112: }
 113: }
 114: }
 115: y3 y3Var3 = ((mag) ((lag) rp9Var.getValue())).g;
 116: zm9 zm9Var3 = mag.i[2];
 117: ((x3) y3Var3.g).setValue(string2);
 118: return string2;
 119: }
 120: }
~~~

## defpackage/azc.java (1776 строк)

~~~java
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
 226: if ((i & Integer.MIN_VALUE) != 0) {
 227: jhhVar.f = i - Integer.MIN_VALUE;
 228: } else {
 229: jhhVar = new jhh(this, d55Var);
 230: }
 231: } else {
 232: jhhVar = new jhh(this, d55Var);
 233: }
 234: Object objR = jhhVar.d;
 235: int i2 = jhhVar.f;
 236: qdj qdjVar = rdj.b;
 237: if (i2 == 0) {
 238: xnm.y(objR);
 239: String str = shareData.text;
 240: if (str == null) {
 241: return new pgh(new mdj(R.string.share_sticker_set_title), qdjVar, new Integer(R.drawable.sticker_placeholder));
 242: }
 243: ((yx9) ((rp9) this.b).getValue()).getClass();
 244: long jE = yx9.e(str);
 245: if (jE == 0) {
 246: mdj mdjVar = new mdj(R.string.share_sticker_set_title);
 247: if (str.length() != 0) {
 248: qdjVar = new qdj(str);
 249: }
 250: return new pgh(mdjVar, qdjVar, new Integer(R.drawable.sticker_placeholder));
 251: }
 252: qi7 qi7VarA = ((q2j) ((rp9) this.e).getValue()).a(jE, false);
 253: jhhVar.f = 1;
 254: objR = hzj.R(qi7VarA, jhhVar);
 255: ka5 ka5Var = ka5.a;
 256: if (objR == ka5Var) {
 257: return ka5Var;
 258: }
 259: } else {
 260: if (i2 != 1) {
~~~

Поздние сигнатуры: 618 public final Object c() {; 667 public final Object c() {; 739 public Object a(d55 d55Var) {; 776 public gub c() {; 781 public void f() {; 787 public Object g(vi viVar, b55 b55Var) {; 862 public qt6 get() {; 948 public void h(ContentResolver contentResolver, Uri uri) throws IOException {; 980 public a22 i(mnd mndVar) {; 986 public mnd j(a22 a22Var) {; 997 public String l() {; 1002 public void m(bt btVar) {; 1013 public bt n() {; 1031 public Object o(Context context, vl9 vl9Var) {; 1036 public boolean p() {; 1042 public Object q(LinkedHashSet linkedHashSet, d55 d55Var) {; 1085 public void s(mnd mndVar, a22 a22Var) {; 1094 public Object t(Context context, b55 b55Var) {; 1211 public String toString() {; 1479 public Object u(final String str, d55 d55Var) {; 1522 public final Object d(Object obj) {; 1544 public final Object d(Object obj) {; 1568 public final Object d(Object obj) {; 1586 public kh5 v(h1a h1aVar, qh5 qh5Var, y1h y1hVar, int i, int[] iArr, r07 r07Var, int i2, long j, boolean z, ArrayList arrayList, a8e a8eVar, csj csjVar, d8e d8eVar) {

## defpackage/fh0.java (20 строк)

~~~java
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
~~~

## defpackage/wi.java (3176 строк)

~~~java
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
~~~

Поздние сигнатуры: 1446 private final Object y(Object obj) {; 1553 private final java.lang.Object z(java.lang.Object r14) {; 1673 public final Object invoke(Object obj, Object obj2) {; 1741 public final b55 u(b55 b55Var, Object obj) {; 1958 public final Object w(Object obj) throws Throwable {

## defpackage/tdd.java (305 строк)

~~~java
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
~~~

Поздние сигнатуры: 

## defpackage/t6a.java (77 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.util.Log;
   4: import java.util.concurrent.CancellationException;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public final class t6a extends a08 {
   8: public final byte h;
   9: 
  10: /* JADX WARN: Multi-variable type inference failed */
  11: public t6a(int i) {
  12: this.h = i;
  13: }
  14: 
  15: @Override // defpackage.a08
  16: public final void A(String str, String str2) {
  17: if (this.h <= 4) {
  18: Log.i(str, str2);
  19: }
  20: }
  21: 
  22: @Override // defpackage.a08
  23: public final void B(String str, String str2, CancellationException cancellationException) {
  24: if (this.h <= 4) {
  25: Log.i(str, str2, cancellationException);
  26: }
  27: }
  28: 
  29: @Override // defpackage.a08
  30: public final void U(String str) {
  31: if (this.h <= 2) {
  32: Log.v(str, "Rescheduling alarm that keeps track of force-stops.");
  33: }
  34: }
  35: 
  36: @Override // defpackage.a08
  37: public final void V(String str, String str2) {
  38: if (this.h <= 5) {
  39: Log.w(str, str2);
  40: }
  41: }
  42: 
  43: @Override // defpackage.a08
  44: public final void W(String str, String str2, RuntimeException runtimeException) {
  45: if (this.h <= 5) {
  46: Log.w(str, str2, runtimeException);
  47: }
  48: }
  49: 
  50: @Override // defpackage.a08
  51: public final void n(String str, String str2) {
  52: if (this.h <= 3) {
  53: Log.d(str, str2);
  54: }
  55: }
  56: 
  57: @Override // defpackage.a08
  58: public final void o(String str, String str2, Throwable th) {
  59: if (this.h <= 3) {
  60: Log.d(str, str2, th);
  61: }
  62: }
  63: 
  64: @Override // defpackage.a08
  65: public final void r(String str, String str2) {
  66: if (this.h <= 6) {
  67: Log.e(str, str2);
  68: }
  69: }
  70: 
  71: @Override // defpackage.a08
  72: public final void s(String str, String str2, Throwable th) {
  73: if (this.h <= 6) {
  74: Log.e(str, str2, th);
  75: }
  76: }
  77: }
~~~

## defpackage/ph0.java (16 строк)

~~~java
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
~~~

## defpackage/oh0.java (90 строк)

~~~java
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
~~~

## defpackage/cj3.java (161 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.Collections;
   4: import java.util.Set;
   5: import one.me.profile.screens.members.ChatMembersScreen;
   6: import ru.oneme.app.R;
   7: 
   8: /* JADX INFO: loaded from: classes2.dex */
   9: public final class cj3 extends x1j implements e18 {
  10: public final /* synthetic */ byte e;
  11: public /* synthetic */ Object f;
  12: public final /* synthetic */ ChatMembersScreen g;
  13: 
  14: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  15: public cj3(b55 b55Var, ChatMembersScreen chatMembersScreen) {
  16: super(2, b55Var);
  17: this.e = (byte) 2;
  18: this.g = chatMembersScreen;
  19: }
  20: 
  21: @Override // defpackage.e18
  22: public final Object invoke(Object obj, Object obj2) {
  23: byte b = this.e;
  24: s1k s1kVar = s1k.a;
  25: switch (b) {
  26: case 0:
  27: ((cj3) u((b55) obj2, (vi3) obj)).w(s1kVar);
  28: break;
  29: case 1:
  30: ((cj3) u((b55) obj2, (m3b) obj)).w(s1kVar);
  31: break;
  32: default:
  33: ((cj3) u((b55) obj2, obj)).w(s1kVar);
  34: break;
  35: }
  36: return s1kVar;
  37: }
  38: 
  39: @Override // defpackage.hv0
  40: public final b55 u(b55 b55Var, Object obj) {
  41: byte b = this.e;
  42: ChatMembersScreen chatMembersScreen = this.g;
  43: switch (b) {
  44: case 0:
  45: cj3 cj3Var = new cj3(chatMembersScreen, b55Var, (byte) 0);
  46: cj3Var.f = obj;
  47: return cj3Var;
  48: case 1:
  49: cj3 cj3Var2 = new cj3(chatMembersScreen, b55Var, (byte) 1);
  50: cj3Var2.f = obj;
  51: return cj3Var2;
  52: default:
  53: cj3 cj3Var3 = new cj3(b55Var, chatMembersScreen);
  54: cj3Var3.f = obj;
  55: return cj3Var3;
  56: }
  57: }
  58: 
  59: @Override // defpackage.hv0
  60: public final Object w(Object obj) {
  61: byte b = this.e;
  62: s1k s1kVar = s1k.a;
  63: ChatMembersScreen chatMembersScreen = this.g;
  64: Object obj2 = this.f;
  65: switch (b) {
  66: case 0:
  67: vi3 vi3Var = (vi3) obj2;
  68: xnm.y(obj);
  69: zm9[] zm9VarArr = ChatMembersScreen.k;
  70: chatMembersScreen.u1().E(vi3Var.a);
  71: chatMembersScreen.u1().C(vi3Var.b.b(chatMembersScreen.getContext()), false);
  72: chatMembersScreen.u1().B(vi3Var.c ? new r9d(new bad(chatMembersScreen), new y9d(R.drawable.icon_edit, null, null, new bj3(chatMembersScreen, (byte) 1), 14), null) : new r9d(null, new bad(chatMembersScreen), null));
  73: String str = (String) chatMembersScreen.t1().k.a.getValue();
  74: if (str != null) {
  75: h5d h5dVarM = chatMembersScreen.u1().m();
  76: if (h5dVarM != null) {
  77: h5dVarM.l = false;
  78: }
  79: h5d h5dVarM2 = chatMembersScreen.u1().m();
  80: if (h5dVarM2 != null && h5dVarM2.i) {
  81: h5dVarM2.c(true);
  82: rp9 rp9Var = h5dVarM2.o;
  83: if (rp9Var.d()) {
  84: ((wyc) rp9Var.getValue()).setText(str);
  85: }
  86: }
  87: h5d h5dVarM3 = chatMembersScreen.u1().m();
  88: if (h5dVarM3 != null) {
  89: h5dVarM3.l = true;
  90: }
  91: }
  92: return s1kVar;
  93: case 1:
  94: m3b m3bVar = (m3b) obj2;
  95: xnm.y(obj);
  96: if (m3bVar instanceof i3b) {
  97: eye.b.p(((i3b) m3bVar).a);
  98: } else if (m3bVar instanceof g3b) {
  99: g3b g3bVar = (g3b) m3bVar;
 100: int i = g3bVar.a;
 101: long j = g3bVar.b;
 102: zm9[] zm9VarArr2 = ChatMembersScreen.k;
 103: if (i == R.id.profile_members_list_action_select) {
 104: n3b n3bVarT1 = chatMembersScreen.t1();
 105: Set setSingleton = Collections.singleton(Long.valueOf(j));
 106: r4i r4iVar = n3bVarT1.h;
 107: r4iVar.getClass();
 108: r4iVar.j(null, setSingleton);
 109: } else if (i == R.id.profile_members_list_action_delete_from_chat \|\| i == R.id.profile_members_list_action_delete_from_channel) {
 110: lj3 lj3VarS1 = chatMembersScreen.s1();
 111: oyk.Z0(lj3VarS1, ((vxc) ((k6j) lj3VarS1.i.getValue())).b(), new os1(lj3VarS1, j, null, (byte) 3), 2);
 112: }
 113: } else if (m3bVar instanceof j3b) {
 114: int i2 = ((j3b) m3bVar).a;
 115: if (i2 == R.id.profile_members_list_add_to_chat_action) {
 116: eye eyeVar = eye.b;
 117: zm9[] zm9VarArr3 = ChatMembersScreen.k;
 118: eyeVar.k(chatMembersScreen.r1(), true);
 119: } else if (i2 == R.id.profile_members_list_add_to_channel_action) {
 120: eye eyeVar2 = eye.b;
 121: zm9[] zm9VarArr4 = ChatMembersScreen.k;
 122: eyeVar2.k(chatMembersScreen.r1(), false);
 123: } else if (i2 == R.id.profile_members_list_invite_by_link_action) {
 124: eye eyeVar3 = eye.b;
 125: zm9[] zm9VarArr5 = ChatMembersScreen.k;
 126: eyeVar3.n(chatMembersScreen.r1());
 127: }
 128: } else if (m3bVar instanceof k3b) {
 129: eye.b.p(((k3b) m3bVar).a);
 130: } else if (m3bVar instanceof l3b) {
 131: v5d v5dVar = new v5d(chatMembersScreen);
 132: v5dVar.n(c45.D(R.string.self_profile_click, chatMembersScreen.getContext()));
 133: v5dVar.p();
 134: } else if (!(m3bVar instanceof h3b)) {
 135: k3g.l();
 136: return null;
 137: }
 138: return s1kVar;
 139: default:
 140: xnm.y(obj);
 141: Set set = (Set) obj2;
 142: if (set != null) {
 143: zm9[] zm9VarArr6 = ChatMembersScreen.k;
 144: chatMembersScreen.u1().d(String.valueOf(set.size()), Collections.singletonList(new dad(10101, R.string.menu_delete, R.drawable.icon_delete, false, null, 56)), new md2(chatMembersScreen, (byte) 13), new xf2(set, chatMembersScreen, (byte) 1), new h1f((byte) 24));
 145: } else {
 146: zm9[] zm9VarArr7 = ChatMembersScreen.k;
 147: if (chatMembersScreen.u1().c()) {
 148: chatMembersScreen.u1().b();
 149: }
 150: }
 151: return s1kVar;
 152: }
 153: }
 154: 
 155: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 156: public /* synthetic */ cj3(ChatMembersScreen chatMembersScreen, b55 b55Var, byte b) {
 157: super(2, b55Var);
 158: this.e = b;
 159: this.g = chatMembersScreen;
 160: }
 161: }
~~~

