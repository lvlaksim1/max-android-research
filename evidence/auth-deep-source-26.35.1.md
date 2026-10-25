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

## defpackage/f0f.java (337 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Collections;
   5: import java.util.EnumMap;
   6: import java.util.HashMap;
   7: import java.util.Iterator;
   8: import java.util.LinkedHashMap;
   9: import java.util.List;
  10: import java.util.Map;
  11: import java.util.concurrent.ConcurrentHashMap;
  12: import java.util.concurrent.atomic.AtomicReference;
  13: 
  14: /* JADX INFO: loaded from: classes.dex */
  15: public final class f0f {
  16: public final k6j a;
  17: public final p9g b;
  18: public final rp9 c;
  19: public final rp9 d;
  20: public final rp9 e;
  21: public final rp9 f;
  22: public final ConcurrentHashMap g = new ConcurrentHashMap(1);
  23: public final AtomicReference h;
  24: 
  25: public f0f(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, p9g p9gVar, k6j k6jVar) {
  26: this.a = k6jVar;
  27: this.b = p9gVar;
  28: this.c = rp9Var2;
  29: this.d = rp9Var;
  30: this.e = rp9Var3;
  31: this.f = rp9Var4;
  32: AtomicReference atomicReference = new AtomicReference(null);
  33: this.h = atomicReference;
  34: atomicReference.set(nm9.J(p9gVar, ((vxc) k6jVar).b(), 0, new er(this, null, (byte) 11), 2));
  35: }
  36: 
  37: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  38: public final Object a(d55 d55Var) {
  39: b0f b0fVar;
  40: if (d55Var instanceof b0f) {
  41: b0fVar = (b0f) d55Var;
  42: int i = b0fVar.f;
  43: if ((i & Integer.MIN_VALUE) != 0) {
  44: b0fVar.f = i - Integer.MIN_VALUE;
  45: } else {
  46: b0fVar = new b0f(this, d55Var);
  47: }
  48: } else {
  49: b0fVar = new b0f(this, d55Var);
  50: }
  51: Object obj = b0fVar.d;
  52: int i2 = b0fVar.f;
  53: s1k s1kVar = s1k.a;
  54: if (i2 == 0) {
  55: xnm.y(obj);
  56: mse mseVar = (mse) this.d.getValue();
  57: b0fVar.f = 1;
  58: Object objK = az7.K(b0fVar, mseVar.a, false, true, new noe((byte) 2));
  59: ka5 ka5Var = ka5.a;
  60: if (objK != ka5Var) {
  61: objK = s1kVar;
  62: }
  63: if (objK == ka5Var) {
  64: return ka5Var;
  65: }
  66: } else {
  67: if (i2 != 1) {
  68: k3g.o("call to 'resume' before 'invoke' with coroutine");
  69: return null;
  70: }
  71: xnm.y(obj);
  72: }
  73: udn.b(this.g, new noe((byte) 6));
  74: this.h.set(null);
  75: return s1kVar;
  76: }
  77: 
  78: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  79: public final Object b(long j, d55 d55Var) {
  80: c0f c0fVar;
  81: if (d55Var instanceof c0f) {
  82: c0fVar = (c0f) d55Var;
  83: int i = c0fVar.g;
  84: if ((i & Integer.MIN_VALUE) != 0) {
  85: c0fVar.g = i - Integer.MIN_VALUE;
  86: } else {
  87: c0fVar = new c0f(this, d55Var);
  88: }
  89: } else {
  90: c0fVar = new c0f(this, d55Var);
  91: }
  92: Object obj = c0fVar.e;
  93: ka5 ka5Var = ka5.a;
  94: int i2 = c0fVar.g;
  95: if (i2 == 0) {
  96: xnm.y(obj);
  97: kf9 kf9Var = (kf9) this.h.updateAndGet(new w20(this, (byte) 5));
  98: if (kf9Var != null) {
  99: c0fVar.d = j;
 100: c0fVar.g = 1;
 101: if (kf9Var.q(c0fVar) == ka5Var) {
 102: return ka5Var;
 103: }
 104: }
 105: } else {
 106: if (i2 != 1) {
 107: k3g.o("call to 'resume' before 'invoke' with coroutine");
 108: return null;
 109: }
 110: j = c0fVar.d;
 111: xnm.y(obj);
 112: }
 113: long j2 = j;
 114: i4c i4cVar = (i4c) this.g.get(new Long(j2));
 115: dqe dqeVar = i4cVar != null ? (dqe) i4cVar.getValue() : null;
 116: if (dqeVar != null) {
 117: return dqeVar;
 118: }
 119: String name = f0f.class.getName();
 120: o1d o1dVar = f09.g;
 121: if (o1dVar != null) {
 122: c6a c6aVar = c6a.d;
 123: if (o1dVar.b(c6aVar)) {
 124: o1dVar.c(c6aVar, name, "getProfile: return stubProfile", null);
 125: }
 126: }
 127: return new dqe(j2, sp6.a, qp6.a, ((c35) this.c.getValue()).g(j2));
 128: }
 129: 
 130: public final l4i c(long j) {
 131: return (l4i) this.g.computeIfAbsent(Long.valueOf(j), new ep(new noe((byte) 5), (byte) 20));
 132: }
 133: 
 134: /* JADX WARN: Code duplicated, block: B:46:0x00fe A[LOOP:0: B:44:0x00f8->B:46:0x00fe, LOOP_END] */
 135: /* JADX WARN: Code duplicated, block: B:50:0x014e  */
 136: /* JADX WARN: Code duplicated, block: B:53:0x0152  */
 137: /* JADX WARN: Code duplicated, block: B:57:0x0161 A[RETURN] */
 138: /* JADX WARN: Code duplicated, block: B:7:0x001f  */
 139: public final Object d(cqe cqeVar, String str, d55 d55Var) {
 140: d0f d0fVar;
 141: LinkedHashMap linkedHashMap;
 142: kve kveVar;
 143: Object objK;
 144: kve kveVar2;
 145: cqe cqeVar2 = cqeVar;
 146: Object obj = s1k.a;
 147: Object obj2 = ka5.a;
 148: if (d55Var instanceof d0f) {
 149: d0fVar = (d0f) d55Var;
 150: int i = d0fVar.h;
 151: if ((i & Integer.MIN_VALUE) != 0) {
 152: d0fVar.h = i - Integer.MIN_VALUE;
 153: } else {
 154: d0fVar = new d0f(this, d55Var);
 155: }
 156: } else {
 157: d0fVar = new d0f(this, d55Var);
 158: }
 159: Object obj3 = d0fVar.f;
 160: int i2 = d0fVar.h;
 161: if (i2 == 0) {
 162: xnm.y(obj3);
 163: String name = f0f.class.getName();
 164: o1d o1dVar = f09.g;
 165: if (o1dVar != null) {
 166: c6a c6aVar = c6a.d;
 167: if (o1dVar.b(c6aVar)) {
 168: o1dVar.c(c6aVar, name, "putProfile: " + cqeVar2 + "; token=" + ((str == null \|\| zti.n0(str)) ? "null" : "***"), null);
 169: }
 170: }
 171: if (str != null && str.length() != 0) {
 172: u6 u6Var = new u6(this, cqeVar2, str, (byte) 11);
 173: d0fVar.d = cqeVar2;
 174: d0fVar.h = 1;
 175: if (qo9.E(jp6.a, u6Var, d0fVar) != obj2) {
 176: }
 177: }
 178: return obj2;
 179: }
 180: if (i2 == 1) {
 181: cqeVar2 = d0fVar.d;
 182: xnm.y(obj3);
 183: } else {
 184: if (i2 == 2) {
 185: cqeVar2 = d0fVar.d;
 186: xnm.y(obj3);
 187: long j = cqeVar2.a.a;
 188: LinkedHashMap linkedHashMap2 = cqeVar2.b;
 189: linkedHashMap = new LinkedHashMap(jfa.F(linkedHashMap2.size()));
 190: for (Map.Entry entry : linkedHashMap2.entrySet()) {
 191: linkedHashMap.put(entry.getKey(), new j4g(((k4g) entry.getValue()).a()));
 192: }
 193: kveVar = new kve(0L, j, new eu8(linkedHashMap, cqeVar2.c));
 194: mse mseVar = (mse) this.d.getValue();
 195: d0fVar.d = null;
 196: d0fVar.e = kveVar;
 197: d0fVar.h = 3;
 198: objK = az7.K(d0fVar, mseVar.a, false, true, new so((Object) mseVar, (Object) kveVar, (byte) 15));
 199: if (objK != obj2) {
 200: objK = obj;
 201: }
 202: if (objK != obj2) {
 203: kveVar2 = kveVar;
 204: }
 205: return obj2;
 206: }
 207: if (i2 != 3) {
 208: if (i2 == 4) {
 209: xnm.y(obj3);
 210: return obj;
 211: }
 212: k3g.o("call to 'resume' before 'invoke' with coroutine");
 213: return null;
 214: }
 215: kveVar2 = d0fVar.e;
 216: xnm.y(obj3);
 217: }
 218: d0fVar.d = null;
 219: d0fVar.e = null;
 220: d0fVar.h = 4;
 221: if (e(kveVar2, d0fVar) != obj2) {
 222: return obj2;
 223: }
 224: return obj;
 225: ((hog) ((c74) this.e.getValue())).L(cqeVar2.a.a);
 226: ey4 ey4Var = cqeVar2.a;
 227: c35 c35Var = (c35) this.c.getValue();
 228: List listSingletonList = Collections.singletonList(ey4Var);
 229: zw4 zw4Var = zw4.a;
 230: d0fVar.d = cqeVar2;
 231: d0fVar.h = 2;
 232: if (c35Var.m(listSingletonList, zw4Var, d0fVar) != obj2) {
 233: long j2 = cqeVar2.a.a;
 234: LinkedHashMap linkedHashMap3 = cqeVar2.b;
 235: linkedHashMap = new LinkedHashMap(jfa.F(linkedHashMap3.size()));
 236: while (r7.hasNext()) {
 237: linkedHashMap.put(entry.getKey(), new j4g(((k4g) entry.getValue()).a()));
 238: }
 239: kveVar = new kve(0L, j2, new eu8(linkedHashMap, cqeVar2.c));
 240: mse mseVar2 = (mse) this.d.getValue();
 241: d0fVar.d = null;
 242: d0fVar.e = kveVar;
 243: d0fVar.h = 3;
 244: objK = az7.K(d0fVar, mseVar2.a, false, true, new so((Object) mseVar2, (Object) kveVar, (byte) 15));
 245: if (objK != obj2) {
 246: objK = obj;
 247: }
 248: if (objK != obj2) {
 249: kveVar2 = kveVar;
 250: d0fVar.d = null;
 251: d0fVar.e = null;
 252: d0fVar.h = 4;
 253: if (e(kveVar2, d0fVar) != obj2) {
 254: return obj;
 255: }
 256: }
 257: }
 258: return obj2;
 259: }
 260: 
 261: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
 262: public final Object e(kve kveVar, d55 d55Var) {
 263: e0f e0fVar;
 264: Object next;
 265: if (d55Var instanceof e0f) {
 266: e0fVar = (e0f) d55Var;
 267: int i = e0fVar.g;
 268: if ((i & Integer.MIN_VALUE) != 0) {
 269: e0fVar.g = i - Integer.MIN_VALUE;
 270: } else {
 271: e0fVar = new e0f(this, d55Var);
 272: }
 273: } else {
 274: e0fVar = new e0f(this, d55Var);
 275: }
 276: Object objI = e0fVar.e;
 277: int i2 = e0fVar.g;
 278: if (i2 == 0) {
 279: xnm.y(objI);
 280: c35 c35Var = (c35) this.c.getValue();
 281: long j = kveVar.b;
 282: e0fVar.d = kveVar;
 283: e0fVar.g = 1;
 284: objI = c35Var.i(j);
 285: ka5 ka5Var = ka5.a;
 286: if (objI == ka5Var) {
 287: return ka5Var;
 288: }
 289: } else {
 290: if (i2 != 1) {
 291: k3g.o("call to 'resume' before 'invoke' with coroutine");
 292: return null;
 293: }
 294: kveVar = e0fVar.d;
 295: xnm.y(objI);
 296: }
 297: kv4 kv4Var = (kv4) objI;
 298: s1k s1kVar = s1k.a;
 299: if (kv4Var == null) {
 300: return s1kVar;
 301: }
 302: HashMap map = kveVar.c.a;
 303: ArrayList arrayList = new ArrayList();
 304: for (Map.Entry entry : map.entrySet()) {
 305: int iIntValue = ((Number) entry.getKey()).intValue();
 306: j4g j4gVar = (j4g) entry.getValue();
 307: Iterator it = l4g.b.iterator();
 308: do {
 309: if (!it.hasNext()) {
 310: next = null;
 311: break;
 312: }
 313: next = it.next();
 314: ((l4g) next).getClass();
 315: } while (1 != iIntValue);
 316: l4g l4gVar = (l4g) next;
 317: vld vldVar = l4gVar == null ? null : new vld(l4gVar, new j4g(j4gVar.a()));
 318: if (vldVar != null) {
 319: arrayList.add(vldVar);
 320: }
 321: }
 322: EnumMap enumMap = new EnumMap(l4g.class);
 323: jfa.K(enumMap, arrayList);
 324: ArrayList arrayList2 = kveVar.c.b;
 325: ArrayList arrayList3 = new ArrayList();
 326: Iterator it2 = arrayList2.iterator();
 327: while (it2.hasNext()) {
 328: eze ezeVarB = cfn.b(((Number) it2.next()).intValue());
 329: if (ezeVarB != null) {
 330: arrayList3.add(ezeVarB);
 331: }
 332: }
 333: long j2 = kveVar.b;
 334: this.g.compute(new Long(j2), new pz7(new s40(new dqe(j2, enumMap, arrayList3, kv4Var), (byte) 5), (byte) 4));
 335: return s1kVar;
 336: }
 337: }
~~~

## defpackage/cqe.java (36 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.LinkedHashMap;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public final class cqe {
   8: public final ey4 a;
   9: public final LinkedHashMap b;
  10: public final ArrayList c;
  11: 
  12: public cqe(ey4 ey4Var, LinkedHashMap linkedHashMap, ArrayList arrayList) {
  13: this.a = ey4Var;
  14: this.b = linkedHashMap;
  15: this.c = arrayList;
  16: }
  17: 
  18: public final boolean equals(Object obj) {
  19: if (this == obj) {
  20: return true;
  21: }
  22: if (!(obj instanceof cqe)) {
  23: return false;
  24: }
  25: cqe cqeVar = (cqe) obj;
  26: return this.a.equals(cqeVar.a) && this.b.equals(cqeVar.b) && this.c.equals(cqeVar.c);
  27: }
  28: 
  29: public final int hashCode() {
  30: return this.c.hashCode() + ((this.b.hashCode() + (this.a.hashCode() * 31)) * 31);
  31: }
  32: 
  33: public final String toString() {
  34: return "Profile(contactInfo=" + this.a + ", restrictions=" + this.b + ", profileOptions=" + this.c + ")";
  35: }
  36: }
~~~

## defpackage/th0.java (339 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Collection;
   5: import java.util.Iterator;
   6: import java.util.LinkedHashMap;
   7: import java.util.List;
   8: import one.me.android.initialization.AccountInitializer;
   9: 
  10: /* JADX INFO: loaded from: classes2.dex */
  11: public final class th0 extends x6j {
  12: public static final /* synthetic */ int g = 0;
  13: public final LinkedHashMap c;
  14: public final ArrayList d;
  15: public final azc e;
  16: public final cqe f;
  17: 
  18: public th0(LinkedHashMap linkedHashMap, ArrayList arrayList, azc azcVar, cqe cqeVar) {
  19: this.c = linkedHashMap;
  20: this.d = arrayList;
  21: this.e = azcVar;
  22: this.f = cqeVar;
  23: }
  24: 
  25: /* JADX WARN: Code duplicated, block: B:47:0x00b5  */
  26: /* JADX WARN: Multi-variable type inference failed */
  27: /* JADX WARN: Type inference failed for: r0v18 */
  28: /* JADX WARN: Type inference failed for: r0v25, types: [pb5] */
  29: /* JADX WARN: Type inference failed for: r0v26, types: [java.lang.String] */
  30: /* JADX WARN: Type inference failed for: r0v34 */
  31: /* JADX WARN: Type inference failed for: r0v41, types: [pb5] */
  32: /* JADX WARN: Type inference failed for: r0v42, types: [java.lang.Integer] */
  33: /* JADX WARN: Type inference failed for: r0v65 */
  34: /* JADX WARN: Type inference failed for: r0v66, types: [java.lang.Iterable] */
  35: /* JADX WARN: Type inference failed for: r0v67 */
  36: /* JADX WARN: Type inference failed for: r0v68 */
  37: /* JADX WARN: Type inference failed for: r0v69 */
  38: /* JADX WARN: Type inference failed for: r0v71, types: [qp6] */
  39: /* JADX WARN: Type inference failed for: r0v73, types: [java.util.ArrayList] */
  40: /* JADX WARN: Type inference failed for: r0v89 */
  41: /* JADX WARN: Type inference failed for: r0v90 */
  42: /* JADX WARN: Type inference failed for: r0v91 */
  43: /* JADX WARN: Type inference failed for: r17v0 */
  44: /* JADX WARN: Type inference failed for: r17v1 */
  45: /* JADX WARN: Type inference failed for: r17v3 */
  46: /* JADX WARN: Type inference failed for: r17v4 */
  47: /* JADX WARN: Type inference failed for: r17v6 */
  48: /* JADX WARN: Type inference failed for: r17v7 */
  49: /* JADX WARN: Type inference failed for: r6v0 */
  50: /* JADX WARN: Type inference failed for: r6v1, types: [java.lang.String, th0] */
  51: /* JADX WARN: Type inference failed for: r6v10 */
  52: /* JADX WARN: Type inference failed for: r6v11 */
  53: /* JADX WARN: Type inference failed for: r6v4, types: [java.lang.String] */
  54: /* JADX WARN: Type inference failed for: r6v6 */
  55: public static final th0 f(beb bebVar) {
  56: int iP0;
  57: ?? R0;
  58: beb bebVar2;
  59: int i;
  60: ?? r17;
  61: ?? ValueOf;
  62: ?? r6;
  63: int i2;
  64: String strS0;
  65: int i3;
  66: ?? arrayList;
  67: ?? r0;
  68: List listH0;
  69: ?? r7 = 0;
  70: if (!bebVar.m()) {
  71: return null;
  72: }
  73: int i4 = 1;
  74: try {
  75: iP0 = e0c.p0(bebVar);
  76: } catch (Throwable th) {
  77: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th);
  78: Iterator it = q1h.a.iterator();
  79: while (it.hasNext()) {
  80: AccountInitializer accountInitializer = ((z6) it.next()).a;
  81: try {
  82: f09.c0("Payload", "error while parse payload", th);
  83: accountInitializer.c().j().d().a(null, th);
  84: } catch (Throwable th2) {
  85: f09.c0("Payload", "failed to collect exception", th2);
  86: }
  87: }
  88: int iG = s95.G(iqg.a);
  89: if (iG != 0) {
  90: if (iG == 1) {
  91: throw th;
  92: }
  93: k3g.l();
  94: return null;
  95: }
  96: iP0 = 0;
  97: }
  98: if (iP0 == 0) {
  99: return null;
 100: }
 101: LinkedHashMap linkedHashMap = new LinkedHashMap();
 102: ArrayList arrayList2 = new ArrayList();
 103: azc azcVarB = null;
 104: cqe cqeVarS = null;
 105: int i5 = 0;
 106: while (i5 < iP0) {
 107: try {
 108: R0 = e0c.r0(bebVar);
 109: } catch (Throwable th3) {
 110: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th3);
 111: Iterator it2 = q1h.a.iterator();
 112: while (it2.hasNext()) {
 113: AccountInitializer accountInitializer2 = ((z6) it2.next()).a;
 114: try {
 115: f09.c0("Payload", "error while parse payload", th3);
 116: accountInitializer2.c().j().d().a(r7, th3);
 117: } catch (Throwable th4) {
 118: f09.c0("Payload", "failed to collect exception", th4);
 119: }
 120: }
 121: int iG2 = s95.G(iqg.a);
 122: if (iG2 != 0) {
 123: if (iG2 == i4) {
 124: throw th3;
 125: }
 126: k3g.l();
 127: return r7;
 128: }
 129: R0 = r7;
 130: }
 131: if (R0 != 0) {
 132: switch (R0.hashCode()) {
 133: case -309425751:
 134: bebVar2 = bebVar;
 135: if (R0.equals("profile")) {
 136: i = 1;
 137: r17 = 0;
 138: cqeVarS = wt3.s(bebVar2);
 139: } else {
 140: try {
 141: bebVar2.N();
 142: } catch (Throwable th5) {
 143: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th5);
 144: Iterator it3 = q1h.a.iterator();
 145: while (it3.hasNext()) {
 146: AccountInitializer accountInitializer3 = ((z6) it3.next()).a;
 147: try {
 148: f09.c0("Payload", "error while parse payload", th5);
 149: accountInitializer3.c().j().d().a(null, th5);
 150: } catch (Throwable th6) {
 151: f09.c0("Payload", "failed to collect exception", th6);
 152: }
 153: }
 154: int iG3 = s95.G(iqg.a);
 155: if (iG3 != 0) {
 156: if (iG3 == 1) {
 157: throw th5;
 158: }
 159: k3g.l();
 160: return null;
 161: }
 162: }
 163: i = 1;
 164: r17 = 0;
 165: }
 166: break;
 167: case 73797161:
 168: if (R0.equals("tokenAttrs")) {
 169: try {
 170: ValueOf = Integer.valueOf(e0c.p0(bebVar));
 171: } catch (Throwable th7) {
 172: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th7);
 173: Iterator it4 = q1h.a.iterator();
 174: while (it4.hasNext()) {
 175: AccountInitializer accountInitializer4 = ((z6) it4.next()).a;
 176: try {
 177: f09.c0("Payload", "error while parse payload", th7);
 178: accountInitializer4.c().j().d().a(r7, th7);
 179: } catch (Throwable th8) {
 180: f09.c0("Payload", "failed to collect exception", th8);
 181: }
 182: }
 183: int iG4 = s95.G(iqg.a);
 184: if (iG4 != 0) {
 185: if (iG4 == 1) {
 186: throw th7;
 187: }
 188: k3g.l();
 189: return r7;
 190: }
 191: ValueOf = r7;
 192: }
 193: if (ValueOf != 0) {
 194: int iIntValue = ValueOf.intValue();
 195: int i6 = 0;
 196: while (i6 < iIntValue) {
 197: r6 = r7;
 198: try {
 199: strS0 = e0c.s0(bebVar, r6);
 200: i2 = iIntValue;
 201: } catch (Throwable th9) {
 202: f09.c0("ServerPayload/PayloadCatching", "payloadCatching catch error", th9);
 203: Iterator it5 = q1h.a.iterator();
 204: while (it5.hasNext()) {
 205: AccountInitializer accountInitializer5 = ((z6) it5.next()).a;
 206: try {
 207: f09.c0("Payload", "error while parse payload", th9);
 208: i3 = iIntValue;
 209: try {
 210: accountInitializer5.c().j().d().a(null, th9);
 211: } catch (Throwable th10) {
 212: th = th10;
 213: f09.c0("Payload", "failed to collect exception", th);
 214: iIntValue = i3;
 215: }
 216: } catch (Throwable th11) {
 217: th = th11;
 218: i3 = iIntValue;
 219: }
 220: iIntValue = i3;
 221: }
 222: i2 = iIntValue;
 223: int iG5 = s95.G(iqg.a);
 224: if (iG5 != 0) {
 225: if (iG5 == 1) {
 226: throw th9;
 227: }
 228: k3g.l();
 229: return null;
 230: }
 231: strS0 = null;
 232: }
 233: if (strS0 != null) {
 234: linkedHashMap.put(strS0, zzm.c(bebVar).a);
 235: }
 236: i6++;
 237: iIntValue = i2;
 238: r6 = 0;
 239: }
 240: r6 = r7;
 241: r17 = r6;
 242: i = 1;
 243: } else {
 244: i = 1;
 245: r17 = 0;
 246: }
 247: } else {
 248: bebVar2 = bebVar;
 249: bebVar2.N();
 250: i = 1;
 251: r17 = 0;
 252: }
 253: break;
 254: case 269284955:
 255: if (R0.equals("presetAvatars")) {
 256: if (bebVar.p().a() == 7) {
 257: arrayList = new ArrayList();
 258: int iS = bebVar.S();
 259: for (int i7 = 0; i7 < iS; i7++) {
 260: arrayList.add(gd9.g(bebVar));
 261: }
 262: } else {
 263: bebVar.N();
 264: arrayList = r7;
 265: }
 266: if (arrayList != 0) {
 267: listH0 = va4.H0(arrayList);
 268: } else {
 269: r0 = r7;
 270: }
 271: if (r0 == 0) {
 272: r0 = listH0;
 273: r0 = qp6.a;
 274: }
 275: r0 = listH0;
 276: arrayList2.addAll((Collection) r0);
 277: i = 1;
 278: r17 = r7;
 279: } else {
 280: bebVar2 = bebVar;
 281: bebVar2.N();
 282: i = 1;
 283: r17 = 0;
 284: }
 285: break;
 286: case 1363910664:
 287: if (R0.equals("passwordChallenge")) {
 288: azcVarB = b0n.b(bebVar);
 289: r17 = r7;
 290: i = i4;
 291: } else {
 292: bebVar2 = bebVar;
 293: bebVar2.N();
 294: i = 1;
 295: r17 = 0;
 296: }
 297: break;
 298: default:
 299: bebVar2 = bebVar;
 300: bebVar2.N();
 301: i = 1;
 302: r17 = 0;
 303: break;
 304: }
 305: } else {
 306: i = 1;
 307: r17 = 0;
 308: }
 309: i5++;
 310: i4 = i;
 311: r7 = r17;
 312: }
 313: return new th0(linkedHashMap, arrayList2, azcVarB, cqeVarS);
 314: }
 315: 
 316: public final boolean equals(Object obj) {
 317: if (this == obj) {
 318: return true;
 319: }
 320: if (!(obj instanceof th0)) {
 321: return false;
 322: }
 323: th0 th0Var = (th0) obj;
 324: return this.c.equals(th0Var.c) && this.d.equals(th0Var.d) && g4a.c(this.e, th0Var.e) && g4a.c(this.f, th0Var.f);
 325: }
 326: 
 327: public final int hashCode() {
 328: int iD = vw4.d(this.d, this.c.hashCode() * 31, 31);
 329: azc azcVar = this.e;
 330: int iHashCode = (iD + (azcVar == null ? 0 : azcVar.hashCode())) * 31;
 331: cqe cqeVar = this.f;
 332: return iHashCode + (cqeVar != null ? cqeVar.hashCode() : 0);
 333: }
 334: 
 335: @Override // defpackage.mv0
 336: public final String toString() {
 337: return "{profile=" + this.f + ",tokenTypes=" + f09.O(this.c) + ",passwordChallenge=" + this.e + ",}";
 338: }
 339: }
~~~

## defpackage/i7a.java (277 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.concurrent.CancellationException;
   4: import kotlin.NoWhenBranchMatchedException;
   5: import one.me.sdk.tasks.login.LoginException;
   6: import ru.ok.tamtam.errors.TamErrorException;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class i7a extends ft implements d7j {
  10: public final int f;
  11: public final byte[] g;
  12: public final String h;
  13: public final String i;
  14: public final c7j j;
  15: public long k;
  16: 
  17: public i7a(long j, int i, Long l, byte[] bArr, String str) {
  18: super(j);
  19: this.f = i;
  20: this.g = bArr;
  21: this.h = str;
  22: String name = i7a.class.getName();
  23: this.i = name;
  24: f09.p(name, "Creating Login task");
  25: this.j = new c7j();
  26: }
  27: 
  28: @Override // defpackage.d7j, defpackage.rwd
  29: public final boolean a() {
  30: return true;
  31: }
  32: 
  33: @Override // defpackage.d7j
  34: public final void b(x6j x6jVar) {
  35: l7a l7aVar = (l7a) x6jVar;
  36: gt gtVar = this.e;
  37: b55 b55Var = null;
  38: if (gtVar == null) {
  39: gtVar = null;
  40: }
  41: vck vckVarL = gtVar.l();
  42: gt gtVar2 = this.e;
  43: if (gtVar2 == null) {
  44: gtVar2 = null;
  45: }
  46: nm9.J(vckVarL, ((vxc) gtVar2.h()).a(), 0, new gh6((byte) 28, b55Var, this, l7aVar, false), 2);
  47: }
  48: 
  49: @Override // defpackage.d7j
  50: public final c7j d() {
  51: return this.j;
  52: }
  53: 
  54: @Override // defpackage.d7j
  55: public final Object e(l6j l6jVar, d55 d55Var) {
  56: gt gtVar = this.e;
  57: if (gtVar == null) {
  58: gtVar = null;
  59: }
  60: Object objE = qo9.E(((vxc) gtVar.h()).a(), new dv8(this, l6jVar, (byte) 7), d55Var);
  61: return objE == ka5.a ? objE : s1k.a;
  62: }
  63: 
  64: @Override // defpackage.d7j
  65: public final void f(l6j l6jVar) {
  66: gt gtVar = this.e;
  67: if (gtVar == null) {
  68: gtVar = null;
  69: }
  70: ((d8a) gtVar.m.getValue()).a(l6jVar, 0);
  71: }
  72: 
  73: /* JADX WARN: Code duplicated, block: B:25:0x006b  */
  74: /* JADX WARN: Code duplicated, block: B:26:0x006e  */
  75: /* JADX WARN: Multi-variable type inference failed */
  76: @Override // defpackage.ft
  77: public final Object n() {
  78: byte[] bArr;
  79: char c;
  80: gt gtVar;
  81: String str;
  82: c6a c6aVar = c6a.d;
  83: gt gtVar2 = this.e;
  84: if (gtVar2 == null) {
  85: gtVar2 = null;
  86: }
  87: xt3 xt3Var = (xt3) gtVar2.p0.getValue();
  88: xt3Var.getClass();
  89: try {
  90: int iT = xt3Var.b.heightPixels / nb6.t(80.0f * Math.max(xt3Var.b.density, 1.0f));
  91: int i = 50;
  92: if (iT > 50) {
  93: iT = 50;
  94: }
  95: if (((ms4) xt3Var.a.getValue()).g()) {
  96: int iOrdinal = ((ms4) xt3Var.a.getValue()).b().ordinal();
  97: if (iOrdinal == 0) {
  98: i = 20;
  99: } else if (iOrdinal != 1) {
 100: if (iOrdinal == 2) {
 101: i = 12;
 102: } else if (iOrdinal == 3) {
 103: i = 20;
 104: } else if (iOrdinal != 4) {
 105: throw new NoWhenBranchMatchedException();
 106: }
 107: }
 108: } else {
 109: i = 12;
 110: }
 111: bArr = new byte[]{(byte) iT, (byte) i};
 112: } catch (Throwable th) {
 113: String str2 = xt3.c;
 114: vt3 vt3Var = new vt3(th);
 115: o1d o1dVar = f09.g;
 116: if (o1dVar != null) {
 117: c6a c6aVar2 = c6a.f;
 118: if (o1dVar.b(c6aVar2)) {
 119: o1dVar.c(c6aVar2, str2, "failed to count chats for login", vt3Var);
 120: }
 121: }
 122: bArr = null;
 123: }
 124: u07 u07Var = new u07(bArr);
 125: dle dleVarU = u();
 126: n3a n3aVar = dleVarU.a;
 127: this.k = n3aVar.w();
 128: long jI = n3aVar.i();
 129: String name = i7a.class.getName();
 130: o1d o1dVar2 = f09.g;
 131: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
 132: c = '\f';
 133: vg9.J(pq0.s("LoginApiTask: chatsLastSync = ", qo9.C(new Long(this.k)), ", lastChatMarker = ", qo9.C(new Long(((Number) n3aVar.L.s(n3aVar, hog.i0[34])).longValue())), ", contactLastSync = "), qo9.C(new Long(jI)), o1dVar2, c6aVar, name);
 134: } else {
 135: c = '\f';
 136: }
 137: String str3 = (String) dleVarU.b.D().i();
 138: int i2 = dleVarU.b.b().a.y().getInt("version", 1);
 139: String str4 = this.i;
 140: o1d o1dVar3 = f09.g;
 141: if (o1dVar3 != null) {
 142: c6a c6aVar3 = c6a.e;
 143: if (o1dVar3.b(c6aVar3)) {
 144: ihk.k("version=", i2, o1dVar3, c6aVar3, str4);
 145: }
 146: }
 147: if (i2 < 7) {
 148: dleVarU.b.b().a.D().a(null);
 149: if (i2 != 6) {
 150: String name2 = i7a.class.getName();
 151: o1d o1dVar4 = f09.g;
 152: if (o1dVar4 != null && o1dVar4.b(c6aVar)) {
 153: o1dVar4.c(c6aVar, name2, "LoginApiTask: clear chatsLastSync and lastChatMarker", null);
 154: }
 155: this.k = 0L;
 156: f09.p(n3aVar.c, "clear chatsLastSync");
 157: zcg zcgVar = n3aVar.a0;
 158: zm9[] zm9VarArr = hog.i0;
 159: zcgVar.z(n3aVar, zm9VarArr[49], 0L);
 160: n3aVar.L.z(n3aVar, zm9VarArr[34], 0L);
 161: }
 162: dleVarU.b.b().a.y().edit().putInt("version", 7).commit();
 163: str3 = null;
 164: }
 165: char c2 = c;
 166: String str5 = this.h;
 167: if (str5 == null) {
 168: gt gtVar3 = this.e;
 169: if (gtVar3 == null) {
 170: gtVar3 = null;
 171: }
 172: String strC = ((dtc) gtVar3.f.getValue()).c();
 173: if (strC == null) {
 174: k3g.t("Required value was null.");
 175: return null;
 176: }
 177: str = strC;
 178: gtVar = null;
 179: } else {
 180: gtVar = null;
 181: str = str5;
 182: }
 183: gt gtVar4 = this.e;
 184: if (gtVar4 == null) {
 185: gtVar4 = gtVar;
 186: }
 187: boolean zA = ((rd9) gtVar4.k0.getValue()).a();
 188: int i3 = this.f;
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
 199: if (r14 == r13) goto L33;
 200: */
 201: /* JADX WARN: Code restructure failed: missing block: B:32:0x0075, code lost:
 202: 
 203: if (r14.e(r0.a, r10) == r13) goto L33;
 204: */
 205: /* JADX WARN: Code restructure failed: missing block: B:33:0x0077, code lost:
 206: 
 207: return r13;
 208: */
 209: /* JADX WARN: Multi-variable type inference failed */
 210: /* JADX WARN: Type inference failed for: r14v10 */
 211: @Override // defpackage.d7j
 212: /* JADX INFO: renamed from: x, reason: merged with bridge method [inline-methods] */
 213: /*
 214: Code decompiled incorrectly, please refer to instructions dump.
 215: */
 216: public final Object k(l7a l7aVar, d55 d55Var) {
 217: h7a h7aVar;
 218: if (d55Var instanceof h7a) {
 219: h7aVar = (h7a) d55Var;
 220: int i = h7aVar.g;
 221: if ((i & Integer.MIN_VALUE) != 0) {
 222: h7aVar.g = i - Integer.MIN_VALUE;
 223: } else {
 224: h7aVar = new h7a(this, d55Var);
 225: }
 226: } else {
 227: h7aVar = new h7a(this, d55Var);
 228: }
 229: h7a h7aVar2 = h7aVar;
 230: Object obj = h7aVar2.e;
 231: int i2 = h7aVar2.g;
 232: ka5 ka5Var = ka5.a;
 233: try {
 234: if (i2 != 0) {
 235: if (i2 == 1) {
 236: i2 = h7aVar2.d;
 237: xnm.y(obj);
 238: this = this;
 239: } else {
 240: if (i2 != 2) {
 241: k3g.o("call to 'resume' before 'invoke' with coroutine");
 242: return null;
 243: }
 244: xnm.y(obj);
 245: }
 246: return s1k.a;
 247: }
 248: xnm.y(obj);
 249: i2 = 0;
 250: gt gtVar = this.e;
 251: if (gtVar == null) {
 252: gtVar = null;
 253: }
 254: k8a k8aVar = (k8a) gtVar.j.getValue();
 255: long j = this.a;
 256: long j2 = this.k;
 257: int i3 = this.f;
 258: String str = this.h;
 259: h7aVar2.d = 0;
 260: h7aVar2.g = 1;
 261: Object objF = k8aVar.f(j, l7aVar, j2, i3, str, h7aVar2);
 262: this = objF;
 263: } catch (CancellationException e) {
 264: throw e;
 265: } catch (Throwable th) {
 266: if (th instanceof TamErrorException) {
 267: h7aVar2.d = i2;
 268: h7aVar2.g = 2;
 269: } else {
 270: f09.c0(this.i, "login failed", new LoginException(th));
 271: gt gtVar2 = this.e;
 272: (gtVar2 != null ? gtVar2 : null).a.E(th.getClass().getName(), n8a.n);
 273: }
 274: }
 275: return s1k.a;
 276: }
 277: }
~~~

## defpackage/f6f.java (96 строк)

~~~java
   1: package defpackage;
   2: 
   3: import com.google.protobuf.nano.CodedOutputByteBufferNano$OutOfSpaceException;
   4: import com.google.protobuf.nano.InvalidProtocolBufferNanoException;
   5: import me.leolin.shortcutbadger.BuildConfig;
   6: 
   7: /* JADX INFO: loaded from: classes3.dex */
   8: public final class f6f extends mcb {
   9: public static volatile f6f[] g;
  10: public String b = BuildConfig.FLAVOR;
  11: public int c = 0;
  12: public int d = 0;
  13: public y5f e = null;
  14: public long f = 0;
  15: 
  16: public f6f() {
  17: this.a = -1;
  18: }
  19: 
  20: @Override // defpackage.mcb
  21: public final int a() {
  22: int iU = !this.b.equals(BuildConfig.FLAVOR) ? d0i.u(1, this.b) : 0;
  23: int i = this.c;
  24: if (i != 0) {
  25: iU += d0i.o(2, i);
  26: }
  27: int i2 = this.d;
  28: if (i2 != 0) {
  29: iU += d0i.o(3, i2);
  30: }
  31: y5f y5fVar = this.e;
  32: if (y5fVar != null) {
  33: iU += d0i.r(4, y5fVar);
  34: }
  35: long j = this.f;
  36: return j != 0 ? d0i.q(5, j) + iU : iU;
  37: }
  38: 
  39: @Override // defpackage.mcb
  40: public final mcb b(s84 s84Var) throws InvalidProtocolBufferNanoException {
  41: while (true) {
  42: int iR = s84Var.r();
  43: if (iR == 0) {
  44: break;
  45: }
  46: if (iR == 10) {
  47: this.b = s84Var.q();
  48: } else if (iR == 16) {
  49: int iO = s84Var.o();
  50: if (iO == 0 \|\| iO == 1 \|\| iO == 2 \|\| iO == 3 \|\| iO == 4) {
  51: this.c = iO;
  52: }
  53: } else if (iR == 24) {
  54: int iO2 = s84Var.o();
  55: if (iO2 == 0 \|\| iO2 == 1 \|\| iO2 == 2 \|\| iO2 == 3) {
  56: this.d = iO2;
  57: }
  58: } else if (iR == 34) {
  59: y5f y5fVar = this.e;
  60: if (y5fVar == null) {
  61: y5fVar = new y5f();
  62: this.e = y5fVar;
  63: }
  64: s84Var.i(y5fVar);
  65: } else if (iR == 40) {
  66: this.f = s84Var.p();
  67: } else if (!s84Var.t(iR)) {
  68: break;
  69: }
  70: }
  71: return this;
  72: }
  73: 
  74: @Override // defpackage.mcb
  75: public final void f(d0i d0iVar) throws CodedOutputByteBufferNano$OutOfSpaceException {
  76: if (!this.b.equals(BuildConfig.FLAVOR)) {
  77: d0iVar.X(1, this.b);
  78: }
  79: int i = this.c;
  80: if (i != 0) {
  81: d0iVar.P(2, i);
  82: }
  83: int i2 = this.d;
  84: if (i2 != 0) {
  85: d0iVar.P(3, i2);
  86: }
  87: y5f y5fVar = this.e;
  88: if (y5fVar != null) {
  89: d0iVar.R(4, y5fVar);
  90: }
  91: long j = this.f;
  92: if (j != 0) {
  93: d0iVar.Q(5, j);
  94: }
  95: }
  96: }
~~~

## defpackage/g0f.java (227 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.view.View;
   4: import android.view.ViewGroup;
   5: import android.widget.FrameLayout;
   6: import android.widget.LinearLayout;
   7: import android.widget.TextView;
   8: import androidx.appcompat.widget.AppCompatTextView;
   9: import androidx.appcompat.widget.Toolbar;
  10: import androidx.core.widget.NestedScrollView;
  11: import one.me.profile.ProfileScreen;
  12: import one.video.calls.sdk.net.signaling.wt.nal.internal.WebTransportSocket;
  13: import org.webrtc.PeerConnection;
  14: import ru.oneme.app.R;
  15: 
  16: /* JADX INFO: loaded from: classes2.dex */
  17: public final /* synthetic */ class g0f implements q08 {
  18: public final /* synthetic */ byte a;
  19: public final /* synthetic */ ProfileScreen b;
  20: 
  21: public /* synthetic */ g0f(ProfileScreen profileScreen, byte b) {
  22: this.a = b;
  23: this.b = profileScreen;
  24: }
  25: 
  26: /* JADX WARN: Type inference fix 'apply assigned field type' failed
  27: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
  28: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
  29: at jadx.core.dex.attributes.nodes.ClassTypeVarsAttr.getTypeVarsMapFor(ClassTypeVarsAttr.java:35)
  30: at jadx.core.dex.nodes.utils.TypeUtils.replaceClassGenerics(TypeUtils.java:177)
  31: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.insertExplicitUseCast(FixTypesVisitor.java:397)
  32: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryFieldTypeWithNewCasts(FixTypesVisitor.java:359)
  33: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.applyFieldType(FixTypesVisitor.java:309)
  34: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
  35: */
  36: @Override // defpackage.q08
  37: public final Object d(Object obj) {
  38: byte b = this.a;
  39: byte b2 = 4;
  40: lrh lrhVar = u34.j;
  41: byte b3 = 3;
  42: ProfileScreen profileScreen = this.b;
  43: s1k s1kVar = s1k.a;
  44: byte b4 = 0;
  45: byte b5 = 1;
  46: switch (b) {
  47: case 0:
  48: LinearLayout linearLayout = (LinearLayout) obj;
  49: fd9 fd9Var = ProfileScreen.D;
  50: vtc vtcVar = new vtc(linearLayout.getContext());
  51: vtcVar.setId(R.id.profile_screen_avatar_view);
  52: int iT = nb6.t(ProfileScreen.F * i36.d().getDisplayMetrics().density);
  53: vtc.F(vtcVar, iT);
  54: LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(iT, iT);
  55: layoutParams.gravity = 1;
  56: layoutParams.topMargin = nb6.t(i36.d().getDisplayMetrics().density * 8.0f);
  57: vtcVar.setLayoutParams(layoutParams);
  58: linearLayout.addView(vtcVar);
  59: TextView textView = new TextView(linearLayout.getContext());
  60: textView.setId(R.id.profile_screen_expandedtitle_view);
  61: textView.setSaveEnabled(false);
  62: LinearLayout.LayoutParams layoutParams2 = new LinearLayout.LayoutParams(-2, -2);
  63: layoutParams2.leftMargin = nb6.t(i36.d().getDisplayMetrics().density * 20.0f);
  64: layoutParams2.rightMargin = nb6.t(i36.d().getDisplayMetrics().density * 20.0f);
  65: layoutParams2.topMargin = nb6.t(16.0f * i36.d().getDisplayMetrics().density);
  66: layoutParams2.gravity = 1;
  67: textView.setLayoutParams(layoutParams2);
  68: qo9.H(textView);
  69: textView.setMaxLines(3);
  70: textView.setGravity(1);
  71: fej fejVar = tzj.a;
  72: tzj.a(tzj.b, textView);
  73: textView.setTextColor(lrhVar.f(textView).getText().a);
  74: linearLayout.addView(textView);
  75: g0f g0fVar = new g0f(profileScreen, b5);
  76: LinearLayout linearLayout2 = new LinearLayout(linearLayout.getContext());
  77: linearLayout2.setLayoutParams(new ViewGroup.LayoutParams(-1, -2));
  78: linearLayout2.setPaddingRelative(nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(4.0f * i36.d().getDisplayMetrics().density), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), linearLayout2.getPaddingBottom());
  79: linearLayout2.setOrientation(0);
  80: linearLayout2.setBackground(null);
  81: linearLayout2.setGravity(1);
  82: g0fVar.d(linearLayout2);
  83: linearLayout.addView(linearLayout2);
  84: break;
  85: case 1:
  86: LinearLayout linearLayout3 = (LinearLayout) obj;
  87: fd9 fd9Var2 = ProfileScreen.D;
  88: linearLayout3.addView(new cx9(linearLayout3.getContext(), new b3b(2, this.b, ProfileScreen.class, "copyLinkToClipboardWithNotif", "copyLinkToClipboardWithNotif(Ljava/lang/String;Lru/ok/tamtam/android/link/LinkType;)V", 0, (byte) 16)));
  89: AppCompatTextView appCompatTextView = new AppCompatTextView(linearLayout3.getContext());
  90: appCompatTextView.setId(R.id.profile_dot_divider_view);
  91: appCompatTextView.setSaveEnabled(false);
  92: LinearLayout.LayoutParams layoutParams3 = new LinearLayout.LayoutParams(-2, -2);
  93: layoutParams3.setMarginEnd(nb6.t(4.0f * er2.e(4.0f, i36.d().getDisplayMetrics().density, layoutParams3).density));
  94: appCompatTextView.setLayoutParams(layoutParams3);
  95: appCompatTextView.setText("·");
  96: appCompatTextView.setGravity(1);
  97: fej fejVar2 = tzj.a;
  98: fej fejVar3 = tzj.i;
  99: tzj.a(fejVar3, appCompatTextView);
 100: c45.J(new b57(3, (b55) null), appCompatTextView);
 101: linearLayout3.addView(appCompatTextView);
 102: TextView textView2 = new TextView(linearLayout3.getContext());
 103: textView2.setId(R.id.profile_screen_expandedsubtitle_view);
 104: textView2.setSaveEnabled(false);
 105: LinearLayout.LayoutParams layoutParams4 = new LinearLayout.LayoutParams(-2, -2);
 106: layoutParams4.rightMargin = nb6.t(i36.d().getDisplayMetrics().density * 20.0f);
 107: textView2.setLayoutParams(layoutParams4);
 108: textView2.setGravity(1);
 109: tzj.a(fejVar3, textView2);
 110: textView2.setTextColor(lrhVar.f(textView2).getText().c);
 111: linearLayout3.addView(textView2);
 112: break;
 113: case 2:
 114: g95 g95Var = (g95) obj;
 115: fd9 fd9Var3 = ProfileScreen.D;
 116: cu cuVar = new cu(g95Var.getContext());
 117: cuVar.setId(R.id.profile_screen_appbarlayout);
 118: cuVar.setSaveEnabled(false);
 119: cuVar.setLayoutParams(new ViewGroup.LayoutParams(-1, -2));
 120: cuVar.setBackground(null);
 121: fd9 fd9Var4 = ProfileScreen.D;
 122: g0f g0fVar2 = new g0f(profileScreen, b2);
 123: oa4 oa4Var = new oa4(cuVar.getContext());
 124: zt ztVar = new zt();
 125: ztVar.a = 19;
 126: oa4Var.setLayoutParams(ztVar);
 127: oa4Var.e();
 128: g0fVar2.d(oa4Var);
 129: cuVar.addView(oa4Var);
 130: g95Var.addView(cuVar);
 131: NestedScrollView nestedScrollView = new NestedScrollView(g95Var.getContext());
 132: nestedScrollView.setId(R.id.profile_screen_nestedscrollview);
 133: d95 d95Var = new d95(-1, -1);
 134: d95Var.b(new bu());
 135: nestedScrollView.setLayoutParams(d95Var);
 136: g0f g0fVar3 = new g0f(profileScreen, b3);
 137: LinearLayout linearLayout4 = new LinearLayout(nestedScrollView.getContext());
 138: linearLayout4.setLayoutParams(new LinearLayout.LayoutParams(-1, -2));
 139: linearLayout4.setOrientation(1);
 140: g0fVar3.d(linearLayout4);
 141: nestedScrollView.addView(linearLayout4);
 142: g95Var.addView(nestedScrollView);
 143: break;
 144: case 3:
 145: LinearLayout linearLayout5 = (LinearLayout) obj;
 146: fd9 fd9Var5 = ProfileScreen.D;
 147: ks6 ks6Var = new ks6(linearLayout5.getContext());
 148: ks6Var.setId(R.id.profile_screen_recyclerview);
 149: ks6Var.setLayoutParams(new ViewGroup.LayoutParams(-1, -2));
 150: ks6Var.A0(null);
 151: ks6Var.getContext();
 152: ks6Var.B0(new zs9());
 153: ks6Var.setOverScrollMode(2);
 154: qtf qtfVar = new qtf();
 155: qtfVar.e(1, 1);
 156: qtfVar.e(2, 1);
 157: qtfVar.e(128, 1);
 158: qtfVar.e(2097152, 1);
 159: qtfVar.e(16777216, 1);
 160: qtfVar.e(64, 1);
 161: qtfVar.e(PeerConnection.PORTALLOCATOR_ENABLE_ANY_ADDRESS_PORTS, 1);
 162: qtfVar.e(32, 1);
 163: qtfVar.e(16, 1);
 164: qtfVar.e(8, 1);
 165: qtfVar.e(65536, 1);
 166: qtfVar.e(4096, 1);
 167: ks6Var.C0(qtfVar);
 168: uua uuaVar = profileScreen.c;
 169: ks6Var.y0(new o0f(uuaVar.getExecutors().a(), uuaVar.getAccessor().d(31), profileScreen));
 170: ugd ugdVar = new ugd((ihd) uuaVar.getAccessor().d(1143).getValue(), (o0f) ks6Var.m, ((j9e) uuaVar.getAccessor().d(31).getValue()).p());
 171: profileScreen.C = ugdVar;
 172: ks6Var.k(ugdVar);
 173: ks6Var.setClipToPadding(false);
 174: ks6Var.setClipChildren(false);
 175: ks6Var.V0(new uv3(profileScreen, (byte) 8));
 176: g3c g3cVar = o99.a;
 177: g3c g3cVar2 = new g3c(3);
 178: g3cVar2.h(1);
 179: g3cVar2.h(4);
 180: g3cVar2.h(2);
 181: yrd yrdVar = new yrd(ks6Var, g3cVar2, (byte) 8);
 182: ckd ckdVar = new ckd(ks6Var, (byte) 10);
 183: ks6Var.h(new wsg(lrhVar.f(ks6Var), yrdVar, null, null, null, 60), -1);
 184: ks6Var.h(new ll8(lrhVar.f(ks6Var), ckdVar), -1);
 185: ks6Var.h(new lfa(z9m.a(nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 24.0f), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t(i36.d().getDisplayMetrics().density * 12.0f), nb6.t
 186: linearLayout5.addView(ks6Var);
 187: View pz2Var = new pz2(linearLayout5.getContext());
 188: pz2Var.setId(R.id.profile_screen_memberlist_container);
 189: pz2Var.setSaveEnabled(false);
 190: LinearLayout.LayoutParams layoutParams5 = new LinearLayout.LayoutParams(-1, -2);
 191: layoutParams5.rightMargin = nb6.t(12.0f * i36.d().getDisplayMetrics().density);
 192: layoutParams5.leftMargin = nb6.t(12.0f * i36.d().getDisplayMetrics().density);
 193: layoutParams5.bottomMargin = nb6.t(24.0f * i36.d().getDisplayMetrics().density);
 194: layoutParams5.topMargin = nb6.t(3.0f * i36.d().getDisplayMetrics().density);
 195: pz2Var.setLayoutParams(layoutParams5);
 196: pz2Var.setOutlineProvider(new p95(i36.d().getDisplayMetrics().density * 16.0f));
 197: c45.J(new p4a(3, (b55) null, (byte) 20), pz2Var);
 198: linearLayout5.addView(pz2Var);
 199: break;
 200: default:
 201: oa4 oa4Var2 = (oa4) obj;
 202: fd9 fd9Var6 = ProfileScreen.D;
 203: noe noeVar = new noe(profileScreen);
 204: Toolbar toolbar = new Toolbar(oa4Var2.getContext());
 205: ma4 ma4Var = new ma4(-1, -2);
 206: ma4Var.a = 1;
 207: toolbar.setLayoutParams(ma4Var);
 208: toolbar.x(null);
 209: toolbar.u(0, 0);
 210: noeVar.d(toolbar);
 211: oa4Var2.addView(toolbar);
 212: g0f g0fVar4 = new g0f(profileScreen, b4);
 213: LinearLayout linearLayout6 = new LinearLayout(oa4Var2.getContext());
 214: linearLayout6.setId(R.id.profile_screen_collapsiblecontainerlinearlayout);
 215: linearLayout6.setSaveEnabled(false);
 216: ma4 ma4Var2 = new ma4(-1, -2);
 217: ma4Var2.a = 2;
 218: ((FrameLayout.LayoutParams) ma4Var2).bottomMargin = nb6.t(16.0f * i36.d().getDisplayMetrics().density);
 219: linearLayout6.setLayoutParams(ma4Var2);
 220: linearLayout6.setOrientation(1);
 221: g0fVar4.d(linearLayout6);
 222: oa4Var2.addView(linearLayout6);
 223: break;
 224: }
 225: return s1kVar;
 226: }
 227: }
~~~

## defpackage/d0f.java (23 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class d0f extends d55 {
   5: public cqe d;
   6: public kve e;
   7: public /* synthetic */ Object f;
   8: public final /* synthetic */ f0f g;
   9: public int h;
  10: 
  11: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  12: public d0f(f0f f0fVar, d55 d55Var) {
  13: super(d55Var);
  14: this.g = f0fVar;
  15: }
  16: 
  17: @Override // defpackage.hv0
  18: public final Object w(Object obj) {
  19: this.f = obj;
  20: this.h \|= Integer.MIN_VALUE;
  21: return this.g.d(null, null, this);
  22: }
  23: }
~~~

## defpackage/q1a.java (34 строк)

~~~java
   1: package defpackage;
   2: 
   3: import me.leolin.shortcutbadger.BuildConfig;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class q1a {
   7: public static final q1a b = new q1a(0);
   8: public static final q1a c = new q1a(-1);
   9: public final int a;
  10: 
  11: public q1a(int i) {
  12: this.a = i;
  13: }
  14: 
  15: public final String a(String str, String str2) {
  16: String strR = equals(b) ? BuildConfig.FLAVOR : w7g.r(this.a, "_");
  17: return str2 == null ? str.concat(strR) : pq0.k(str, strR, ".", str2);
  18: }
  19: 
  20: public final boolean equals(Object obj) {
  21: if (this == obj) {
  22: return true;
  23: }
  24: return (obj instanceof q1a) && this.a == ((q1a) obj).a;
  25: }
  26: 
  27: public final int hashCode() {
  28: return Integer.hashCode(this.a);
  29: }
  30: 
  31: public final String toString() {
  32: return vg9.v(this.a, "LocalAccountId(raw=", ")");
  33: }
  34: }
~~~

## defpackage/hog.java (335 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import android.content.SharedPreferences;
   5: import java.util.Locale;
   6: import java.util.concurrent.atomic.AtomicInteger;
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
  17: public final zcg F;
  18: public final zcg G;
  19: public final zcg H;
  20: public final zcg I;
  21: public final zcg J;
  22: public final zcg K;
  23: public final zcg L;
  24: public final zcg M;
  25: public final zcg N;
  26: public final zcg O;
  27: public final zcg P;
  28: public final zcg Q;
  29: public final zcg R;
  30: public final zcg S;
  31: public final zcg T;
  32: public final zcg U;
  33: public final zcg V;
  34: public final zcg W;
  35: public final zcg X;
  36: public final zcg Y;
  37: public final zcg Z;
  38: public final zcg a0;
  39: public final zcg b0;
  40: public final zcg c0;
  41: public final zcg d0;
  42: public final rp9 e;
  43: public final zcg e0;
  44: public volatile f34 f;
  45: public final zcg f0;
  46: public final nih g;
  47: public final zcg g0;
  48: public final zcg h;
  49: public final zcg h0;
  50: public final zcg i;
  51: public final zcg j;
  52: public final zcg k;
  53: public final zcg l;
  54: public final zcg m;
  55: public final zcg n;
  56: public final zcg o;
  57: public final zcg p;
  58: public final zcg q;
  59: public final zcg r;
  60: public final zcg s;
  61: public final zcg t;
  62: public final zcg u;
  63: public final zcg v;
  64: public final zcg w;
  65: public final zcg x;
  66: public final zcg y;
  67: public final zcg z;
  68: 
  69: public hog(Context context, String str, uc7 uc7Var, rp9 rp9Var) {
  70: super(context, str, uc7Var);
  71: this.e = rp9Var;
  72: this.g = fa5.c(1, 0, 2);
  73: this.h = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) (-1L), "user.Id");
  74: this.i = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.contactsLastSync");
  75: this.j = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "app.currentProxyList");
  76: this.k = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 299, "app.currentProxyListTtl");
  77: luf.a(String.class);
  78: this.l = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "app.lastSuccessProxy");
  79: luf.a(Long.class);
  80: Boolean bool = Boolean.FALSE;
  81: this.m = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.debugHostRotation");
  82: this.n = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.debugUaDnsEmulation");
  83: this.o = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.callsLastSync");
  84: this.p = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.newCallHistorySync");
  85: this.q = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.deviceAvatarPath");
  86: this.r = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.aId");
  87: this.s = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "server.timeDelta");
  88: luf.a(Boolean.class);
  89: this.t = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "user.unexpectedLogErrorCount");
  90: this.u = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.lastLogSendTime");
  91: luf.a(String.class);
  92: this.v = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.stickersLastSync");
  93: this.w = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.favoritesLastSync");
  94: this.x = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "notif.isVisible");
  95: this.y = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.forceConnection");
  96: this.z = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.lastSuccessfulRequestTime");
  97: this.A = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.contactSortLastSync");
  98: this.B = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.phonesSortLastSync");
  99: this.C = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.reservedPushToken");
 100: this.D = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) (-1L), "user.pushOptions");
 101: this.E = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.okToken");
 102: this.F = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.last.firebase_push_time");
 103: this.G = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.ok.update_time");
 104: this.H = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.writeConctatsRequested");
 105: this.I = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.pushNotificationsRequested");
 106: this.J = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.first.login.time");
 107: this.K = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.last.login.time");
 108: this.L = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.last.chat.marker");
 109: this.M = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) (-1), "app.cache.clear.ver");
 110: this.N = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "app.cache.clear.mask");
 111: this.O = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.invalidate.exception.flag");
 112: this.P = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) BuildConfig.FLAVOR, "install-market");
 113: this.Q = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) BuildConfig.FLAVOR, "install-version");
 114: this.R = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.favorites.stickers.updateTime");
 115: this.S = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.favorites.stickerSets.updateTime");
 116: this.T = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.animojiSetsLastSync");
 117: this.U = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.reactionsLastSync");
 118: this.V = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "user.inviteLinkClicked");
 119: this.W = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "app.last.push.state.time");
 120: this.X = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) null, "user.systemLang");
 121: this.Y = new zcg(luf.a(String.class), (SharedPreferences) this.d, (Object) "ru", "user.lang");
 122: this.Z = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "app.lang.customLang");
 123: this.a0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "user.chatsLastSync");
 124: this.b0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "user.shownDigitalIdTooltip");
 125: this.c0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "background.wake.enabled");
 126: this.d0 = new zcg(luf.a(Long.class), (SharedPreferences) this.d, (Object) 0L, "background.wake.suggestion.shown.time");
 127: this.e0 = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "transmit.version");
 128: luf.a(Integer.class);
 129: this.f0 = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "user.channelHubLastSeenBadge");
 130: this.g0 = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "app.calls_sdk.ice_candidate_emulation");
 131: this.h0 = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "debug.stories.layers.highlight");
 132: }
 133: 
 134: public final void A(long j) {
 135: this.w.z(this, i0[19], Long.valueOf(j));
 136: }
 137: 
 138: public final void B(boolean z) {
 139: this.y.z(this, i0[21], Boolean.valueOf(z));
 140: }
 141: 
 142: public final void C(boolean z) {
 143: this.O.z(this, i0[37], Boolean.valueOf(z));
 144: }
 145: 
 146: public final void D(String str) {
 147: this.Y.z(this, i0[47], str);
 148: }
 149: 
 150: public final void E(long j) {
 151: this.K.z(this, i0[33], Long.valueOf(j));
 152: }
 153: 
 154: public final void F(long j) {
 155: this.p.z(this, i0[10], Long.valueOf(j));
 156: }
 157: 
 158: public final void G(long j) {
 159: this.U.z(this, i0[43], Long.valueOf(j));
 160: }
 161: 
 162: public final void H(String str) {
 163: this.C.z(this, i0[25], str);
 164: }
 165: 
 166: public final void I(long j) {
 167: this.v.z(this, i0[18], Long.valueOf(j));
 168: }
 169: 
 170: public final void J(int i) {
 171: this.e0.z(this, i0[53], Integer.valueOf(i));
 172: }
 173: 
 174: public final void K(int i) {
 175: this.t.z(this, i0[15], Integer.valueOf(i));
 176: }
 177: 
 178: public final void L(long j) {
 179: this.h.z(this, i0[0], Long.valueOf(j));
 180: this.g.l(Long.valueOf(j));
 181: }
 182: 
 183: public final void M(lcf lcfVar) {
 184: rc7 rc7Var = (rc7) this.d.edit();
 185: rc7Var.remove("user.fcmToken");
 186: rc7Var.remove("user.pushDeviceType");
 187: String str = this.c;
 188: if (lcfVar == null) {
 189: rc7Var.remove("user.vendor.pushtoken");
 190: try {
 191: rc7Var.commit();
 192: return;
 193: } catch (Exception e) {
 194: f09.c0(str, "fail to remove vendor push token", e);
 195: return;
 196: }
 197: }
 198: try {
 199: mj9 mj9Var = (mj9) this.e.getValue();
 200: mj9Var.getClass();
 201: rc7Var.putString("user.vendor.pushtoken", mj9Var.b(lcf.Companion.serializer(), lcfVar));
 202: rc7Var.commit();
 203: } catch (Exception e2) {
 204: f09.c0(str, "fail to save vendorPushToken", e2);
 205: }
 206: }
 207: 
 208: public final void N() {
 209: this.H.z(this, i0[30], Boolean.TRUE);
 210: }
 211: 
 212: @Override // defpackage.a4
 213: public void b() {
 214: super.b();
 215: this.f = null;
 216: this.g.l(Long.valueOf(s()));
 217: }
 218: 
 219: public final long f() {
 220: return q() + System.currentTimeMillis();
 221: }
 222: 
 223: public final synchronized long g() {
 224: f34 f34Var;
 225: try {
 226: if (this.f == null) {
 227: this.f = new f34(new gog(this, (byte) 0), new f83(this));
 228: }
 229: f34Var = this.f;
 230: if (f34Var == null) {
 231: throw new IllegalArgumentException("Required value was null.");
 232: }
 233: } catch (Throwable th) {
 234: throw th;
 235: }
 236: return f34Var.b + ((long) ((AtomicInteger) f34Var.c).getAndIncrement());
 237: }
 238: 
 239: public final int h() {
 240: return ((Number) this.M.s(this, i0[35])).intValue();
 241: }
 242: 
 243: public final long i() {
 244: return ((Number) this.i.s(this, i0[1])).longValue();
 245: }
 246: 
 247: public final String j() {
 248: return (String) this.q.s(this, i0[11]);
 249: }
 250: 
 251: public final long k() {
 252: return ((Number) this.J.s(this, i0[32])).longValue();
 253: }
 254: 
 255: public final String l() {
 256: return (String) this.Y.s(this, i0[47]);
 257: }
 258: 
 259: public final long m() {
 260: return ((Number) this.p.s(this, i0[10])).longValue();
 261: }
 262: 
 263: public final String n() {
 264: return (String) this.E.s(this, i0[27]);
 265: }
 266: 
 267: public final long o() {
 268: return ((Number) this.G.s(this, i0[29])).longValue();
 269: }
 270: 
 271: public final long p() {
 272: return ((Number) this.D.s(this, i0[26])).longValue();
 273: }
 274: 
 275: public final long q() {
 276: return ((Number) this.s.s(this, i0[13])).longValue();
 277: }
 278: 
 279: public final int r() {
 280: return ((Number) this.e0.s(this, i0[53])).intValue();
 281: }
 282: 
 283: public final long s() {
 284: return ((Number) this.h.s(this, i0[0])).longValue();
 285: }
 286: 
 287: public final dk7 t() {
 288: return new dk7(this.g, new fw8(this, null, (byte) 20));
 289: }
 290: 
 291: public final Locale u() {
 292: return Locale.forLanguageTag(l());
 293: }
 294: 
 295: public final lcf v() {
 296: wp9 wp9Var = this.d;
 297: String string = wp9Var.getString("user.vendor.pushtoken", null);
 298: if (string != null && string.length() != 0) {
 299: try {
 300: mj9 mj9Var = (mj9) this.e.getValue();
 301: mj9Var.getClass();
 302: return (lcf) mj9Var.a(qo9.u(lcf.Companion.serializer()), string);
 303: } catch (Exception e) {
 304: f09.c0(this.c, "fail to get vendorPushToken", e);
 305: return null;
 306: }
 307: }
 308: String string2 = wp9Var.getString("user.fcmToken", null);
 309: String string3 = wp9Var.getString("user.pushDeviceType", null);
 310: baf bafVar = string3 != null ? (baf) Enum.valueOf(baf.class, string3) : null;
 311: if (bafVar == null \|\| string2 == null) {
 312: return null;
 313: }
 314: return new lcf(bafVar, string2, new tbf(p()));
 315: }
 316: 
 317: public final long w() {
 318: return ((Number) this.a0.s(this, i0[49])).longValue();
 319: }
 320: 
 321: public final void x(int i) {
 322: this.M.z(this, i0[35], Integer.valueOf(i));
 323: }
 324: 
 325: public final void y(int i) {
 326: this.N.z(this, i0[36], Integer.valueOf(i));
 327: }
 328: 
 329: public final void z(long j) {
 330: if (j > w()) {
 331: f09.o(this.c, "setChatsLastSync %d", Long.valueOf(j));
 332: this.a0.z(this, i0[49], Long.valueOf(j));
 333: }
 334: }
 335: }
~~~

## defpackage/mag.java (27 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.Context;
   4: import android.content.SharedPreferences;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public final class mag extends a4 implements lag {
   8: public static final /* synthetic */ zm9[] i = {new v4f(mag.class, "fontSizeModeFlow", "getFontSizeModeFlow()Lkotlinx/coroutines/flow/MutableStateFlow;", 0), a15.f(luf.a, mag.class, "isDisableIncomingCalls", "isDisableIncomingCalls()Z"), new v4f(mag.class, "deviceIdFlow", "getDeviceIdFlow()Lkotlinx/coroutines/flow/MutableStateFlow;", 0), n
   9: public final y3 e;
  10: public final zcg f;
  11: public final y3 g;
  12: public final zcg h;
  13: 
  14: public mag(Context context, uc7 uc7Var) {
  15: super(context, "root", uc7Var);
  16: this.e = new y3("font.size", 1, this.d, this.b, luf.a(Integer.class));
  17: Boolean bool = Boolean.FALSE;
  18: this.f = new zcg(luf.a(Boolean.class), (SharedPreferences) this.d, (Object) bool, "dev.calls.disable_incoming");
  19: this.g = new y3("device.id", null, this.d, this.b, luf.a(String.class));
  20: this.h = new zcg(luf.a(Integer.class), (SharedPreferences) this.d, (Object) 0, "emoji.remote_sprites.version");
  21: }
  22: 
  23: public final x3 f() {
  24: zm9 zm9Var = i[0];
  25: return (x3) this.e.g;
  26: }
  27: }
~~~

## defpackage/lag.java (5 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public interface lag {
   5: }
~~~

## defpackage/r1g.java (504 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.List;
   5: import java.util.concurrent.CancellationException;
   6: import java.util.concurrent.ConcurrentHashMap;
   7: import java.util.concurrent.atomic.AtomicBoolean;
   8: 
   9: /* JADX INFO: loaded from: classes.dex */
  10: public final class r1g implements b6h {
  11: public final f4j a;
  12: public final f4j b;
  13: public final xu3 c;
  14: public final rp9 d;
  15: public final rp9 e;
  16: public final rp9 f;
  17: public final rp9 g;
  18: public final rp9 h;
  19: public final rp9 i;
  20: public final z3j j;
  21: public final z3j k;
  22: public final z3j l;
  23: public final rp9 m;
  24: public final wyi n;
  25: public volatile boolean o;
  26: public final z3j p;
  27: public final ConcurrentHashMap q;
  28: public final ConcurrentHashMap.KeySetView r;
  29: public final String s;
  30: 
  31: public r1g(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, z3j z3jVar, z3j z3jVar2, z3j z3jVar3, rp9 rp9Var4, rp9 rp9Var5, st5 st5Var, rp9 rp9Var6, c6h c6hVar, rp9 rp9Var7, p9g p9gVar, xu3 xu3Var) {
  32: f4j f4jVar = new f4j((byte) 0);
  33: f4j f4jVar2 = new f4j((byte) 2);
  34: this.a = f4jVar;
  35: this.b = f4jVar2;
  36: this.c = xu3Var;
  37: this.d = rp9Var;
  38: this.e = rp9Var2;
  39: this.f = rp9Var3;
  40: this.g = rp9Var4;
  41: this.h = rp9Var5;
  42: this.i = rp9Var7;
  43: this.j = z3jVar;
  44: this.k = z3jVar2;
  45: this.l = z3jVar3;
  46: this.m = rp9Var6;
  47: this.n = a8g.a();
  48: this.p = new z3j(new u6(p9gVar, this, z3jVar2, (byte) 12));
  49: this.q = new ConcurrentHashMap();
  50: this.r = ConcurrentHashMap.newKeySet();
  51: this.s = r1g.class.getName();
  52: ((f6h) c6hVar).c(this);
  53: st5Var.n = this;
  54: }
  55: 
  56: /* JADX WARN: Code duplicated, block: B:7:0x0019  */
  57: /* JADX WARN: Code restructure failed: missing block: B:32:0x00e9, code lost:
  58: 
  59: if (r0.e(r7, r3) == r4) goto L33;
  60: */
  61: /*
  62: Code decompiled incorrectly, please refer to instructions dump.
  63: */
  64: public final Object a(swd swdVar, q08 q08Var, d55 d55Var) {
  65: c1g c1gVar;
  66: q08 q08Var2;
  67: swd swdVar2 = swdVar;
  68: if (d55Var instanceof c1g) {
  69: c1gVar = (c1g) d55Var;
  70: int i = c1gVar.h;
  71: if ((i & Integer.MIN_VALUE) != 0) {
  72: c1gVar.h = i - Integer.MIN_VALUE;
  73: } else {
  74: c1gVar = new c1g(this, d55Var);
  75: }
  76: } else {
  77: c1gVar = new c1g(this, d55Var);
  78: }
  79: Object objF = c1gVar.f;
  80: ka5 ka5Var = ka5.a;
  81: int i2 = c1gVar.h;
  82: if (i2 == 0) {
  83: xnm.y(objF);
  84: i9g i9gVar = (i9g) this.e.getValue();
  85: c1gVar.d = swdVar2;
  86: q08Var2 = q08Var;
  87: c1gVar.e = q08Var2;
  88: c1gVar.h = 1;
  89: objF = i9gVar.f(swdVar2, c1gVar);
  90: if (objF != ka5Var) {
  91: }
  92: return ka5Var;
  93: }
  94: if (i2 == 1) {
  95: q08 q08Var3 = c1gVar.e;
  96: swd swdVar3 = c1gVar.d;
  97: xnm.y(objF);
  98: q08Var2 = q08Var3;
  99: swdVar2 = swdVar3;
 100: } else {
 101: if (i2 != 2) {
 102: k3g.o("call to 'resume' before 'invoke' with coroutine");
 103: return null;
 104: }
 105: xnm.y(objF);
 106: }
 107: return s1k.a;
 108: ArrayList arrayList = new ArrayList();
 109: for (g8j g8jVar : (List) objF) {
 110: if (((Boolean) q08Var2.d(g8jVar.f)).booleanValue()) {
 111: String str = this.s;
 112: o1d o1dVar = f09.g;
 113: if (o1dVar != null) {
 114: c6a c6aVar = c6a.e;
 115: if (o1dVar.b(c6aVar)) {
 116: o1dVar.c(c6aVar, str, "Cancelling task of type=" + swdVar2 + ",task=" + g8jVar + ",id=" + g8jVar.a + ",status=" + g8jVar.b, null);
 117: }
 118: }
 119: this.r.add(new Long(g8jVar.a));
 120: s95.C(g8jVar.a, arrayList);
 121: }
 122: }
 123: b9j b9jVar = (b9j) this.d.getValue();
 124: c1gVar.d = null;
 125: c1gVar.e = null;
 126: c1gVar.h = 2;
 127: }
 128: 
 129: public final Object b(u6j u6jVar, b55 b55Var) {
 130: cu2 cu2Var = new cu2(1, e0c.K(b55Var));
 131: cu2Var.w();
 132: cu2Var.y(new hy3(this, u6jVar, (byte) 2));
 133: g().e(false);
 134: cv3 cv3Var = new cv3();
 135: cv3Var.b = cu2Var;
 136: cv3Var.c = u6jVar;
 137: cv3Var.a = new AtomicBoolean(false);
 138: z6j z6jVarG = g();
 139: long jF = f(u6jVar);
 140: bcc bccVar = (bcc) z6jVarG.i.get();
 141: if (bccVar != null) {
 142: bccVar.g(u6jVar, false, jF, cv3Var);
 143: }
 144: return cu2Var.u();
 145: }
 146: 
 147: @Override // defpackage.b6h
 148: public final void c(int i) {
 149: if (i == 2) {
 150: c5h c5hVar = new c5h(((hog) e()).g());
 151: d(c5hVar, c5hVar, false);
 152: }
 153: }
 154: 
 155: public final long d(ft ftVar, d7j d7jVar, boolean z) {
 156: String str = this.s;
 157: o1d o1dVar = f09.g;
 158: if (o1dVar != null) {
 159: c6a c6aVar = c6a.e;
 160: if (o1dVar.b(c6aVar)) {
 161: o1dVar.c(c6aVar, str, "executeTask " + ftVar + ", isRetry=" + z, null);
 162: }
 163: }
 164: g().e(false);
 165: nm9.J(h(), (z95) this.j.getValue(), 0, new f1g(ftVar, this, z, new m1g(this, ftVar, d7jVar), d7jVar, null), 2);
 166: return ftVar.a;
 167: }
 168: 
 169: public final c74 e() {
 170: return (c74) this.f.getValue();
 171: }
 172: 
 173: public final long f(u6j u6jVar) {
 174: long jK = fe6.k(this.a.V0());
 175: b1g b1gVar = (b1g) this.q.get(Short.valueOf(u6jVar.k()));
 176: if (b1gVar == null) {
 177: return jK;
 178: }
 179: float fB = nhf.b.b() * 0.2f;
 180: return u6jVar.n().a(fB, b1gVar.a, b1gVar.b);
 181: }
 182: 
 183: public final z6j g() {
 184: return (z6j) this.m.getValue();
 185: }
 186: 
 187: public final ja5 h() {
 188: return (ja5) this.p.getValue();
 189: }
 190: 
 191: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
 192: public final Object i(long j, d55 d55Var) {
 193: n1g n1gVar;
 194: boolean zRemove;
 195: boolean z;
 196: if (d55Var instanceof n1g) {
 197: n1gVar = (n1g) d55Var;
 198: int i = n1gVar.g;
 199: if ((i & Integer.MIN_VALUE) != 0) {
 200: n1gVar.g = i - Integer.MIN_VALUE;
 201: } else {
 202: n1gVar = new n1g(this, d55Var);
 203: }
 204: } else {
 205: n1gVar = new n1g(this, d55Var);
 206: }
 207: Object obj = n1gVar.e;
 208: int i2 = n1gVar.g;
 209: if (i2 == 0) {
 210: xnm.y(obj);
 211: zRemove = this.r.remove(new Long(j));
 212: if (zRemove) {
 213: b9j b9jVar = (b9j) this.d.getValue();
 214: n1gVar.d = zRemove;
 215: n1gVar.g = 1;
 216: Object objM = b9jVar.m(j, n1gVar);
 217: ka5 ka5Var = ka5.a;
 218: if (objM == ka5Var) {
 219: return ka5Var;
 220: }
 221: z = zRemove;
 222: }
 223: return Boolean.valueOf(zRemove);
 224: }
 225: if (i2 != 1) {
 226: k3g.o("call to 'resume' before 'invoke' with coroutine");
 227: return null;
 228: }
 229: z = n1gVar.d;
 230: xnm.y(obj);
 231: zRemove = z;
 232: return Boolean.valueOf(zRemove);
 233: }
 234: 
 235: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
 236: public final Object j(d55 d55Var) {
 237: o1g o1gVar;
 238: if (d55Var instanceof o1g) {
 239: o1gVar = (o1g) d55Var;
 240: int i = o1gVar.f;
 241: if ((i & Integer.MIN_VALUE) != 0) {
 242: o1gVar.f = i - Integer.MIN_VALUE;
 243: } else {
 244: o1gVar = new o1g(this, d55Var);
 245: }
 246: } else {
 247: o1gVar = new o1g(this, d55Var);
 248: }
 249: Object objI0 = o1gVar.d;
 250: ka5 ka5Var = ka5.a;
 251: int i2 = o1gVar.f;
 252: b55 b55Var = null;
 253: try {
 254: if (i2 == 0) {
 255: xnm.y(objI0);
 256: f09.E(this.s, "logoutAndSessionClose started", null);
 257: this.o = true;
 258: lkh.V(this.n);
 259: d9a d9aVar = (d9a) this.c.c();
 260: qzd qzdVar = fe6.b;
 261: long jU = az7.U(5, me6.e);
 262: rve rveVar = new rve(this, d9aVar, b55Var, (byte) 21);
 263: o1gVar.f = 1;
 264: objI0 = jd0.i0(jU, rveVar, o1gVar);
 265: if (objI0 == ka5Var) {
 266: return ka5Var;
 267: }
 268: } else {
 269: if (i2 != 1) {
 270: k3g.o("call to 'resume' before 'invoke' with coroutine");
 271: return null;
 272: }
 273: xnm.y(objI0);
 274: }
 275: if (((x6j) objI0) == null) {
 276: f09.d0(this.s, "logoutAndSessionClose: timeout!", new Object[0]);
 277: }
 278: ((bcc) g().i.get()).b(true);
 279: f09.E(this.s, "logoutAndSessionClose finished", null);
 280: this.o = false;
 281: return s1k.a;
 282: } catch (Throwable th) {
 283: this.o = false;
 284: throw th;
 285: }
 286: }
 287: 
 288: public final void k(boolean z) {
 289: z6j z6jVarG = g();
 290: z6jVarG.j.set(fe6.k(z6jVarG.b.V0()));
 291: if (z) {
 292: this.q.clear();
 293: if (this.m.d()) {
 294: bcc bccVar = (bcc) g().i.get();
 295: bccVar.j.set(0L);
 296: bccVar.i.set(0);
 297: f09.p(bccVar.a, "resetConnectionTimeout");
 298: }
 299: }
 300: }
 301: 
 302: /* JADX WARN: Code duplicated, block: B:7:0x0015  */
 303: /* JADX WARN: Code restructure failed: missing block: B:37:0x00bd, code lost:
 304: 
 305: if (r10 == r2) goto L38;
 306: */
 307: /* JADX WARN: Multi-variable type inference failed */
 308: /* JADX WARN: Type inference failed for: r10v0, types: [ft, java.lang.Object] */
 309: /* JADX WARN: Type inference failed for: r10v1, types: [java.lang.Object] */
 310: /* JADX WARN: Type inference failed for: r10v12 */
 311: /* JADX WARN: Type inference failed for: r10v13 */
 312: /* JADX WARN: Type inference failed for: r10v14 */
 313: /* JADX WARN: Type inference failed for: r10v15 */
 314: /* JADX WARN: Type inference failed for: r10v7, types: [ft] */
 315: /* JADX WARN: Type inference failed for: r10v9 */
 316: /* JADX WARN: Type inference failed for: r11v5 */
 317: /* JADX WARN: Type inference failed for: r2v2 */
 318: /* JADX WARN: Type inference failed for: r3v1, types: [java.lang.StringBuilder] */
 319: /*
 320: Code decompiled incorrectly, please refer to instructions dump.
 321: */
 322: public final Object l(ft ftVar, l6j l6jVar, d55 d55Var) {
 323: p1g p1gVar;
 324: ?? r10;
 325: Object objC;
 326: c6a c6aVar = c6a.f;
 327: if (d55Var instanceof p1g) {
 328: p1gVar = (p1g) d55Var;
 329: int i = p1gVar.h;
 330: if ((i & Integer.MIN_VALUE) != 0) {
 331: p1gVar.h = i - Integer.MIN_VALUE;
 332: } else {
 333: p1gVar = new p1g(this, d55Var);
 334: }
 335: } else {
 336: p1gVar = new p1g(this, d55Var);
 337: }
 338: Object obj = p1gVar.f;
 339: ka5 ka5Var = ka5.a;
 340: int i2 = p1gVar.h;
 341: try {
 342: if (i2 != 0) {
 343: if (i2 == 1) {
 344: l6jVar = p1gVar.e;
 345: ft ftVar2 = p1gVar.d;
 346: xnm.y(obj);
 347: r10 = ftVar2;
 348: } else {
 349: if (i2 != 2) {
 350: k3g.o("call to 'resume' before 'invoke' with coroutine");
 351: return null;
 352: }
 353: ft ftVar3 = p1gVar.d;
 354: xnm.y(obj);
 355: ftVar = ftVar3;
 356: }
 357: ftVar = objC;
 358: ((q8j) this.h.getValue()).a();
 359: ((dwl) this.g.getValue()).d();
 360: return s1k.a;
 361: }
 362: xnm.y(obj);
 363: String str = this.s;
 364: o1d o1dVar = f09.g;
 365: if (o1dVar != null && o1dVar.b(c6aVar)) {
 366: o1dVar.c(c6aVar, str, "onTaskFailed " + ((Object) ftVar) + "\|" + l6jVar, null);
 367: }
 368: if ("proto.ver".equals(l6jVar.b)) {
 369: f09.E(this.s, "got version error: mark current version as deprecated, close connection", null);
 370: ((bcc) g().i.get()).w(false);
 371: }
 372: if (ftVar instanceof rwd) {
 373: i9g i9gVar = (i9g) this.e.getValue();
 374: long j = ftVar.a;
 375: p1gVar.d = ftVar;
 376: p1gVar.e = l6jVar;
 377: p1gVar.h = 1;
 378: if (i9gVar.a(j, p1gVar) != ka5Var) {
 379: }
 380: r10 = ftVar;
 381: ftVar = objC;
 382: return ka5Var;
 383: }
 384: return s1k.a;
 385: r10 = ftVar;
 386: if ("proto.payload".equals(l6jVar.b)) {
 387: p1gVar.d = r10;
 388: p1gVar.e = null;
 389: p1gVar.h = 2;
 390: objC = ((rwd) r10).c(p1gVar);
 391: }
 392: } catch (CancellationException e) {
 393: throw e;
 394: } catch (Throwable th) {
 395: String str2 = this.s;
 396: o1d o1dVar2 = f09.g;
 397: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
 398: o1dVar2.c(c6aVar, str2, "fail to onMaxFailCount for " + ftVar + " type=" + ((rwd) ftVar).getType(), th);
 399: }
 400: }
 401: ((q8j) this.h.getValue()).a();
 402: ((dwl) this.g.getValue()).d();
 403: return s1k.a;
 404: }
 405: 
 406: /* JADX WARN: Code duplicated, block: B:7:0x0015  */
 407: /* JADX WARN: Code restructure failed: missing block: B:40:0x00e7, code lost:
 408: 
 409: if (r15 == r2) goto L55;
 410: */
 411: /* JADX WARN: Code restructure failed: missing block: B:54:0x0118, code lost:
 412: 
 413: if (r15 == r2) goto L55;
 414: */
 415: /*
 416: Code decompiled incorrectly, please refer to instructions dump.
 417: */
 418: public final Object m(ft ftVar, d55 d55Var) {
 419: q1g q1gVar;
 420: c6a c6aVar = c6a.e;
 421: if (d55Var instanceof q1g) {
 422: q1gVar = (q1g) d55Var;
 423: int i = q1gVar.g;
 424: if ((i & Integer.MIN_VALUE) != 0) {
 425: q1gVar.g = i - Integer.MIN_VALUE;
 426: } else {
 427: q1gVar = new q1g(this, d55Var);
 428: }
 429: } else {
 430: q1gVar = new q1g(this, d55Var);
 431: }
 432: Object objV = q1gVar.e;
 433: ka5 ka5Var = ka5.a;
 434: int i2 = q1gVar.g;
 435: if (i2 == 0) {
 436: xnm.y(objV);
 437: String str = this.s;
 438: o1d o1dVar = f09.g;
 439: if (o1dVar != null && o1dVar.b(c6aVar)) {
 440: o1dVar.c(c6aVar, str, "onTaskSuccess " + ftVar.getClass().getName() + " requestId=" + ftVar.a, null);
 441: }
 442: if (ftVar instanceof i7a) {
 443: z6j z6jVarG = g();
 444: z6jVarG.j.set(fe6.k(z6jVarG.b.V0()));
 445: ((dwl) this.g.getValue()).d();
 446: }
 447: if (ftVar instanceof rwd) {
 448: b9j b9jVar = (b9j) this.d.getValue();
 449: long j = ftVar.a;
 450: q1gVar.d = ftVar;
 451: q1gVar.g = 1;
 452: if (b9jVar.m(j, q1gVar) != ka5Var) {
 453: }
 454: }
 455: return ka5Var;
 456: }
 457: if (i2 == 1) {
 458: ftVar = q1gVar.d;
 459: xnm.y(objV);
 460: } else if (i2 == 2) {
 461: ftVar = q1gVar.d;
 462: xnm.y(objV);
 463: u6j u6jVar = (u6j) objV;
 464: if (u6jVar != null && u6jVar.o()) {
 465: String str2 = this.s;
 466: o1d o1dVar2 = f09.g;
 467: if (o1dVar2 != null && o1dVar2.b(c6aVar)) {
 468: o1dVar2.c(c6aVar, str2, "onTaskSuccess: set force connection to false after success tam task", null);
 469: }
 470: ((hog) e()).B(false);
 471: }
 472: q1gVar.d = null;
 473: q1gVar.g = 3;
 474: objV = ftVar.v(q1gVar);
 475: } else {
 476: if (i2 != 3) {
 477: k3g.o("call to 'resume' before 'invoke' with coroutine");
 478: return null;
 479: }
 480: xnm.y(objV);
 481: }
 482: u6j u6jVar2 = (u6j) objV;
 483: if (u6jVar2 != null && u6jVar2.o()) {
 484: hog hogVar = (hog) e();
 485: hogVar.z.z(hogVar, hog.i0[22], Long.valueOf(fe6.k(this.b.V0())));
 486: }
 487: g().g();
 488: return s1k.a;
 489: if ((ftVar instanceof ozb) \|\| (ftVar instanceof od4)) {
 490: ((dwl) this.g.getValue()).d();
 491: }
 492: hog hogVar2 = (hog) e();
 493: if (((Boolean) hogVar2.y.s(hogVar2, hog.i0[21])).booleanValue()) {
 494: q1gVar.d = ftVar;
 495: q1gVar.g = 2;
 496: objV = ftVar.v(q1gVar);
 497: } else {
 498: q1gVar.d = null;
 499: q1gVar.g = 3;
 500: objV = ftVar.v(q1gVar);
 501: }
 502: return ka5Var;
 503: }
 504: }
~~~

## defpackage/k5a.java (50 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Iterator;
   5: import java.util.List;
   6: import java.util.Map;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class k5a extends u6j {
  10: public k5a(List list) {
  11: super(null);
  12: if (list == null \|\| list.isEmpty()) {
  13: k3g.t("status can't be null or empty");
  14: throw null;
  15: }
  16: ArrayList arrayList = new ArrayList();
  17: Iterator it = list.iterator();
  18: while (it.hasNext()) {
  19: os osVar = (os) it.next();
  20: osVar.getClass();
  21: dea deaVar = new dea();
  22: deaVar.put("time", Long.valueOf(osVar.a));
  23: deaVar.put("userId", Long.valueOf(osVar.b));
  24: deaVar.put("type", osVar.d);
  25: deaVar.put("event", osVar.e);
  26: Map map = osVar.f;
  27: if (map != null) {
  28: deaVar.put("params", map);
  29: }
  30: long j = osVar.c;
  31: Long lValueOf = j <= 0 ? null : Long.valueOf(j);
  32: if (lValueOf != null) {
  33: deaVar.put("sessionId", Long.valueOf(lValueOf.longValue()));
  34: }
  35: arrayList.add(deaVar.b());
  36: }
  37: d("events", arrayList);
  38: }
  39: 
  40: @Override // defpackage.u6j
  41: public final short k() {
  42: cp5 cp5Var = tdd.c;
  43: return (short) 5;
  44: }
  45: 
  46: @Override // defpackage.u6j
  47: public final boolean o() {
  48: return true;
  49: }
  50: }
~~~

## defpackage/s5a.java (1145 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Iterator;
   5: import java.util.List;
   6: import java.util.Set;
   7: import java.util.concurrent.CancellationException;
   8: import ru.ok.tamtam.errors.TamErrorException;
   9: 
  10: /* JADX INFO: loaded from: classes.dex */
  11: public final class s5a extends x1j implements e18 {
  12: public List e;
  13: public iuf f;
  14: public int g;
  15: public int h;
  16: public byte i;
  17: public /* synthetic */ Object j;
  18: public final /* synthetic */ t5a k;
  19: public final /* synthetic */ boolean l;
  20: public final /* synthetic */ String m;
  21: 
  22: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  23: public s5a(t5a t5aVar, boolean z, String str, b55 b55Var) {
  24: super(2, b55Var);
  25: this.k = t5aVar;
  26: this.l = z;
  27: this.m = str;
  28: }
  29: 
  30: @Override // defpackage.e18
  31: public final Object invoke(Object obj, Object obj2) {
  32: return ((s5a) u((b55) obj2, (ja5) obj)).w(s1k.a);
  33: }
  34: 
  35: @Override // defpackage.hv0
  36: public final b55 u(b55 b55Var, Object obj) {
  37: s5a s5aVar = new s5a(this.k, this.l, this.m, b55Var);
  38: s5aVar.j = obj;
  39: return s5aVar;
  40: }
  41: 
  42: /* JADX WARN: Code duplicated, block: B:101:0x01f4 A[Catch: all -> 0x0157, CancellationException -> 0x0164, Exception -> 0x0205, TamErrorException -> 0x020a, LOOP:0: B:99:0x01ee->B:101:0x01f4, LOOP_END, TryCatch #23 {CancellationException -> 0x0164, all -> 0x0157, blocks: (B:121:0x0293, B:122:0x029f, B:84:0x0193, B:86:0x0197, B:88:0x019f,
  43: /* JADX WARN: Code duplicated, block: B:109:0x0238  */
  44: /* JADX WARN: Code duplicated, block: B:113:0x025c A[Catch: all -> 0x0157, CancellationException -> 0x0164, Exception -> 0x0271, TamErrorException -> 0x0275, LOOP:1: B:111:0x0256->B:113:0x025c, LOOP_END, TryCatch #30 {TamErrorException -> 0x0275, Exception -> 0x0271, blocks: (B:110:0x023a, B:111:0x0256, B:113:0x025c, B:118:0x0279), top: B
  45: /* JADX WARN: Code duplicated, block: B:140:0x02f0  */
  46: /* JADX WARN: Code duplicated, block: B:141:0x02f3  */
  47: /* JADX WARN: Code duplicated, block: B:173:0x03c7 A[Catch: all -> 0x03b8, TryCatch #13 {all -> 0x03b8, blocks: (B:179:0x03ee, B:181:0x0415, B:165:0x0372, B:171:0x03bb, B:173:0x03c7, B:175:0x03cf, B:176:0x03e9), top: B:188:0x001a }] */
  48: /* JADX WARN: Code duplicated, block: B:175:0x03cf A[Catch: all -> 0x03b8, TryCatch #13 {all -> 0x03b8, blocks: (B:179:0x03ee, B:181:0x0415, B:165:0x0372, B:171:0x03bb, B:173:0x03c7, B:175:0x03cf, B:176:0x03e9), top: B:188:0x001a }] */
  49: /* JADX WARN: Code duplicated, block: B:181:0x0415 A[Catch: all -> 0x03b8, TRY_LEAVE, TryCatch #13 {all -> 0x03b8, blocks: (B:179:0x03ee, B:181:0x0415, B:165:0x0372, B:171:0x03bb, B:173:0x03c7, B:175:0x03cf, B:176:0x03e9), top: B:188:0x001a }] */
  50: /* JADX WARN: Code duplicated, block: B:190:0x02fe A[EXC_TOP_SPLITTER, SYNTHETIC] */
  51: /* JADX WARN: Code duplicated, block: B:209:0x00fe A[EXC_TOP_SPLITTER, SYNTHETIC] */
  52: /* JADX WARN: Code duplicated, block: B:56:0x0124  */
  53: /* JADX WARN: Code duplicated, block: B:58:0x0128  */
  54: /* JADX WARN: Code duplicated, block: B:86:0x0197 A[Catch: all -> 0x0157, Exception -> 0x015c, CancellationException -> 0x0164, TamErrorException -> 0x0169, TryCatch #26 {TamErrorException -> 0x0169, Exception -> 0x015c, blocks: (B:84:0x0193, B:86:0x0197, B:88:0x019f, B:92:0x01ad, B:95:0x01d2, B:61:0x0131), top: B:210:0x0193 }] */
  55: /* JADX WARN: Code duplicated, block: B:88:0x019f A[Catch: all -> 0x0157, Exception -> 0x015c, CancellationException -> 0x0164, TamErrorException -> 0x0169, TryCatch #26 {TamErrorException -> 0x0169, Exception -> 0x015c, blocks: (B:84:0x0193, B:86:0x0197, B:88:0x019f, B:92:0x01ad, B:95:0x01d2, B:61:0x0131), top: B:210:0x0193 }] */
  56: /* JADX WARN: Code duplicated, block: B:90:0x01a9 A[ADDED_TO_REGION] */
  57: /* JADX WARN: Code duplicated, block: B:94:0x01d0  */
  58: /* JADX WARN: Code duplicated, block: B:95:0x01d2 A[Catch: all -> 0x0157, Exception -> 0x015c, CancellationException -> 0x0164, TamErrorException -> 0x0169, PHI: r4 r5 r6 r10 r20 r21
  59: 0x01d2: PHI (r4v16 int) = (r4v6 int), (r4v30 int) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE]
  60: 0x01d2: PHI (r5v23 int) = (r5v4 int), (r5v34 int) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE]
  61: 0x01d2: PHI (r6v15 java.lang.Object) = (r6v3 java.lang.Object), (r6v40 java.lang.Object) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE]
  62: 0x01d2: PHI (r10v9 iuf) = (r10v35 iuf), (r10v36 iuf) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE]
  63: 0x01d2: PHI (r20v10 java.lang.String) = (r20v1 java.lang.String), (r20v23 java.lang.String) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE]
  64: 0x01d2: PHI (r21v7 java.lang.String) = (r21v0 java.lang.String), (r6v29 java.lang.String) binds: [B:38:0x009f, B:93:0x01ce] A[DONT_GENERATE, DONT_INLINE], TRY_LEAVE, TryCatch #26 {TamErrorException -> 0x0169, Exception -> 0x015c, blocks: (B:84:0x0193, B:86:0x0197, B:88:0x019f, B:92:0x01ad, B:95:0x01d2, B:61:0x0131), top: B:210:0x0193 }] *
  65: /* JADX WARN: Code duplicated, block: B:98:0x01da A[Catch: all -> 0x0157, CancellationException -> 0x0164, Exception -> 0x0205, TamErrorException -> 0x020a, TryCatch #23 {CancellationException -> 0x0164, all -> 0x0157, blocks: (B:121:0x0293, B:122:0x029f, B:84:0x0193, B:86:0x0197, B:88:0x019f, B:144:0x02fe, B:150:0x0322, B:92:0x01ad, B:95
  66: /* JADX WARN: Code restructure failed: missing block: B:119:0x028f, code lost:
  67: 
  68: if (((defpackage.c9g) r6).a(r11, r22) == r3) goto L183;
  69: */
  70: /* JADX WARN: Code restructure failed: missing block: B:166:0x03a7, code lost:
  71: 
  72: if (r2.c(r6, r5, r0, r22) == r3) goto L183;
  73: */
  74: /* JADX WARN: Code restructure failed: missing block: B:182:0x042b, code lost:
  75: 
  76: if (r2.c(r6, r5, r0, r22) == r3) goto L183;
  77: */
  78: /* JADX WARN: Instruction removed from duplicated block: B:175:0x03cf, please report this as an issue */
  79: /* JADX WARN: Multi-variable type inference failed */
  80: /* JADX WARN: Path cross not found for [B:50:0x0108, B:51:0x0110], limit reached: 207 */
  81: /* JADX WARN: Type inference failed for: r10v0 */
  82: /* JADX WARN: Type inference failed for: r10v11, types: [iuf] */
  83: /* JADX WARN: Type inference failed for: r10v13, types: [iuf] */
  84: /* JADX WARN: Type inference failed for: r10v18 */
  85: /* JADX WARN: Type inference failed for: r10v23 */
  86: /* JADX WARN: Type inference failed for: r10v24 */
  87: /* JADX WARN: Type inference failed for: r10v25 */
  88: /* JADX WARN: Type inference failed for: r10v26 */
  89: /* JADX WARN: Type inference failed for: r10v27 */
  90: /* JADX WARN: Type inference failed for: r10v28 */
  91: /* JADX WARN: Type inference failed for: r10v29 */
  92: /* JADX WARN: Type inference failed for: r10v30 */
  93: /* JADX WARN: Type inference failed for: r10v31 */
  94: /* JADX WARN: Type inference failed for: r10v32 */
  95: /* JADX WARN: Type inference failed for: r2v10, types: [t5a] */
  96: /* JADX WARN: Type inference failed for: r2v18, types: [t5a] */
  97: /* JADX WARN: Type inference failed for: r3v1, types: [java.util.Set] */
  98: /* JADX WARN: Type inference failed for: r4v0, types: [byte] */
  99: /* JADX WARN: Type inference failed for: r4v1 */
 100: /* JADX WARN: Type inference failed for: r4v18 */
 101: /* JADX WARN: Type inference failed for: r4v3, types: [java.lang.Object] */
 102: /* JADX WARN: Type inference failed for: r5v17 */
 103: /* JADX WARN: Type inference failed for: r5v18 */
 104: /* JADX WARN: Type inference failed for: r5v2 */
 105: /* JADX WARN: Type inference failed for: r5v29, types: [java.util.List] */
 106: /* JADX WARN: Type inference failed for: r5v3 */
 107: /* JADX WARN: Type inference failed for: r5v31, types: [java.util.List] */
 108: /* JADX WARN: Type inference failed for: r5v35 */
 109: /* JADX WARN: Type inference failed for: r5v42 */
 110: /* JADX WARN: Type inference failed for: r5v43 */
 111: /* JADX WARN: Type inference failed for: r5v44 */
 112: /* JADX WARN: Type inference failed for: r5v45 */
 113: /* JADX WARN: Type inference failed for: r5v46 */
 114: /* JADX WARN: Type inference failed for: r5v47 */
 115: /* JADX WARN: Type inference failed for: r5v48 */
 116: /* JADX WARN: Type inference fix 'apply assigned field type' failed
 117: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
 118: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
 119: at jadx.core.dex.attributes.nodes.ClassTypeVarsAttr.getTypeVarsMapFor(ClassTypeVarsAttr.java:35)
 120: at jadx.core.dex.nodes.utils.TypeUtils.replaceClassGenerics(TypeUtils.java:177)
 121: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.insertExplicitUseCast(FixTypesVisitor.java:397)
 122: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryFieldTypeWithNewCasts(FixTypesVisitor.java:359)
 123: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.applyFieldType(FixTypesVisitor.java:309)
 124: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 125: */
 126: /* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:133:0x02e0 -> B:206:0x00f8). Please report as a decompilation issue!!! */
 127: @Override // defpackage.hv0
 128: /*
 129: Code decompiled incorrectly, please refer to instructions dump.
 130: */
 131: public final Object w(Object obj) throws Throwable {
 132: String str;
 133: String str2;
 134: boolean z;
 135: o1d o1dVar;
 136: c6a c6aVar;
 137: int i;
 138: String str3;
 139: ?? r5;
 140: String str4;
 141: ?? r6;
 142: int i2;
 143: int i3;
 144: Object objB;
 145: int i4;
 146: List list;
 147: iuf iufVar;
 148: List list2;
 149: List list3;
 150: ArrayList arrayList;
 151: Iterator it;
 152: List list4;
 153: t5a t5aVar;
 154: ArrayList arrayList2;
 155: f7j f7jVarB;
 156: k5a k5aVar;
 157: iuf iufVar2;
 158: List list5;
 159: Set set;
 160: z6j z6jVar;
 161: List list6;
 162: List list7;
 163: t5a t5aVar2;
 164: String str5;
 165: boolean z2;
 166: o1d o1dVar2;
 167: boolean z3;
 168: List list8;
 169: c6a c6aVar2 = c6a.d;
 170: ja5 ja5Var = (ja5) this.j;
 171: ka5 ka5Var = ka5.a;
 172: ?? r4 = this.i;
 173: String str6 = "LOG_DISCONNECTION_BLOCKER";
 174: String str7 = "Failed to send logs ";
 175: ?? r10 = 5;
 176: ?? r11 = 5;
 177: try {
 178: try {
 179: try {
 180: if (r4 != 0) {
 181: try {
 182: if (r4 == 1) {
 183: i2 = this.h;
 184: i3 = this.g;
 185: iuf iufVar3 = this.f;
 186: List list9 = this.e;
 187: xnm.y(obj);
 188: str6 = "LOG_DISCONNECTION_BLOCKER";
 189: str3 = "Failed to send logs ";
 190: objB = obj;
 191: iufVar = iufVar3;
 192: list4 = (List) objB;
 193: if (!list4.isEmpty()) {
 194: List<w3i> list10 = list4;
 195: t5aVar = this.k;
 196: arrayList2 = new ArrayList(xa4.p0(list10, 10));
 197: for (w3i w3iVar : list10) {
 198: t5aVar.getClass();
 199: arrayList2.add(t5a.j(w3iVar));
 200: }
 201: iufVar.a = arrayList2;
 202: f7jVarB = this.k.b();
 203: k5aVar = new k5a((List) iufVar.a);
 204: this.j = ja5Var;
 205: this.e = list4;
 206: this.f = iufVar;
 207: this.g = i3;
 208: this.h = i2;
 209: this.i = (byte) 2;
 210: if (f7jVarB.e(k5aVar, this) != ka5Var) {
 211: i4 = i3;
 212: list = list4;
 213: iufVar = iufVar;
 214: u5i u5iVar = (u5i) this.k.f.getValue();
 215: List list11 = list;
 216: arrayList = new ArrayList(xa4.p0(list11, 10));
 217: for (it = list11.iterator(); it.hasNext(); it = it) {
 218: arrayList.add(f09.e(((w3i) it.next()).a));
 219: }
 220: this.j = ja5Var;
 221: this.e = list;
 222: this.f = iufVar;
 223: this.g = i4;
 224: this.h = i2;
 225: this.i = (byte) 3;
 226: list2 = list;
 227: iufVar = iufVar;
 228: }
 229: return ka5Var;
 230: }
 231: i = i3;
 232: list = list4;
 233: if (i != 0) {
 234: iufVar = iufVar;
 235: hog hogVar = (hog) this.k.a();
 236: hogVar.u.z(hogVar, hog.i0[16], Long.valueOf(this.k.c.getAsLong()));
 237: }
 238: iufVar = iufVar;
 239: f09.p(this.k.m, "Finished sending logs");
 240: z6jVar = (z6j) this.k.j.getValue();
 241: set = z6jVar.l;
 242: str6 = str6;
 243: } else if (r4 == 2) {
 244: i2 = this.h;
 245: int i5 = this.g;
 246: iuf iufVar4 = this.f;
 247: List list12 = this.e;
 248: xnm.y(obj);
 249: i4 = i5;
 250: list = list12;
 251: str6 = "LOG_DISCONNECTION_BLOCKER";
 252: str3 = "Failed to send logs ";
 253: iufVar = iufVar4;
 254: u5i u5iVar2 = (u5i) this.k.f.getValue();
 255: List list13 = list;
 256: arrayList = new ArrayList(xa4.p0(list13, 10));
 257: while (it.hasNext()) {
 258: arrayList.add(f09.e(((w3i) it.next()).a));
 259: }
 260: this.j = ja5Var;
~~~

Поздние сигнатуры: 

## defpackage/dcc.java (30 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class dcc {
   5: public final z3j a;
   6: public final boolean b;
   7: public final boolean c;
   8: public final rp9 d;
   9: public final rp9 e;
  10: public final rp9 f;
  11: public final z3j g;
  12: public final rp9 h;
  13: public final rp9 i;
  14: public final rp9 j;
  15: public final z3j k;
  16: 
  17: public dcc(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, z3j z3jVar, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, z3j z3jVar2, boolean z, boolean z2) {
  18: this.a = z3jVar2;
  19: this.b = z;
  20: this.c = z2;
  21: this.d = rp9Var;
  22: this.e = rp9Var2;
  23: this.f = rp9Var3;
  24: this.g = z3jVar;
  25: this.h = rp9Var5;
  26: this.i = rp9Var6;
  27: this.j = rp9Var7;
  28: this.k = new z3j(new zx(rp9Var4, (byte) 9));
  29: }
  30: }
~~~

## defpackage/gci.java (22 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public interface gci {
   5: String a();
   6: 
   7: int b();
   8: 
   9: String c();
  10: 
  11: Object d(b55 b55Var);
  12: 
  13: boolean e();
  14: 
  15: Object f(b55 b55Var);
  16: 
  17: baf g();
  18: 
  19: int h();
  20: 
  21: Object i(b55 b55Var);
  22: }
~~~

## defpackage/i00.java (83 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.Collection;
   4: import java.util.Iterator;
   5: import java.util.Map;
   6: import java.util.Set;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class i00 extends uph implements Map {
  10: public c00 d;
  11: public e00 e;
  12: public g00 f;
  13: 
  14: @Override // java.util.Map
  15: public final Set entrySet() {
  16: c00 c00Var = this.d;
  17: if (c00Var != null) {
  18: return c00Var;
  19: }
  20: c00 c00Var2 = new c00(this);
  21: this.d = c00Var2;
  22: return c00Var2;
  23: }
  24: 
  25: public final boolean j(Collection collection) {
  26: Iterator it = collection.iterator();
  27: while (it.hasNext()) {
  28: if (!super.containsKey(it.next())) {
  29: return false;
  30: }
  31: }
  32: return true;
  33: }
  34: 
  35: public final boolean k(Collection collection) {
  36: int i = this.c;
  37: Iterator it = collection.iterator();
  38: while (it.hasNext()) {
  39: super.remove(it.next());
  40: }
  41: return i != this.c;
  42: }
  43: 
  44: @Override // java.util.Map
  45: public final Set keySet() {
  46: e00 e00Var = this.e;
  47: if (e00Var != null) {
  48: return e00Var;
  49: }
  50: e00 e00Var2 = new e00(this);
  51: this.e = e00Var2;
  52: return e00Var2;
  53: }
  54: 
  55: public final boolean l(Collection collection) {
  56: int i = this.c;
  57: for (int i2 = i - 1; i2 >= 0; i2--) {
  58: if (!collection.contains(f(i2))) {
  59: g(i2);
  60: }
  61: }
  62: return i != this.c;
  63: }
  64: 
  65: @Override // java.util.Map
  66: public final void putAll(Map map) {
  67: b(map.size() + this.c);
  68: for (Map.Entry entry : map.entrySet()) {
  69: put(entry.getKey(), entry.getValue());
  70: }
  71: }
  72: 
  73: @Override // java.util.Map
  74: public final Collection values() {
  75: g00 g00Var = this.f;
  76: if (g00Var != null) {
  77: return g00Var;
  78: }
  79: g00 g00Var2 = new g00(this);
  80: this.f = g00Var2;
  81: return g00Var2;
  82: }
  83: }
~~~

## defpackage/dle.java (37 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.SharedPreferences;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class dle {
   7: public final n3a a;
   8: public final j9e b;
   9: public final mdk c;
  10: public final qi0 d;
  11: public final h7d e;
  12: 
  13: public dle(n3a n3aVar, j9e j9eVar, mdk mdkVar, qi0 qi0Var, h7d h7dVar) {
  14: this.a = n3aVar;
  15: this.b = j9eVar;
  16: this.c = mdkVar;
  17: this.d = qi0Var;
  18: this.e = h7dVar;
  19: }
  20: 
  21: public final void a() {
  22: this.a.b();
  23: j9e j9eVar = this.b;
  24: j9eVar.y().edit().clear().commit();
  25: ((SharedPreferences) j9eVar.g.getValue()).edit().clear().commit();
  26: ((SharedPreferences) j9eVar.f.getValue()).edit().clear().commit();
  27: for (o9e o9eVar : j9eVar.v().values()) {
  28: o9eVar.g().edit().remove(o9eVar.a).commit();
  29: o9eVar.o = 5;
  30: o9eVar.p.a();
  31: ((i4c) o9eVar.q.getValue()).setValue(o9eVar.b);
  32: }
  33: this.c.b();
  34: this.d.b();
  35: this.e.b();
  36: }
  37: }
~~~

## defpackage/m8a.java (32 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class m8a extends x6c {
   5: public static final m8a b = new m8a();
   6: 
   7: public final an5 k() {
   8: return new an5(":chat-list", null);
   9: }
  10: 
  11: public final an5 l() {
  12: return new an5(":webview/faq", null);
  13: }
  14: 
  15: public final an5 m(final String str, final String str2, final String str3, final String str4, final int i, final int i2, final int i3) {
  16: return g(new q08() { // from class: l8a
  17: @Override // defpackage.q08
  18: public final Object d(Object obj) {
  19: en5 en5Var = (en5) obj;
  20: en5Var.a = ":twofa/auth/password/check";
  21: en5Var.d(str, "track_id");
  22: en5Var.c("hint", str2);
  23: en5Var.d(str3, "email");
  24: en5Var.d(str4, "phone");
  25: en5Var.d(Integer.valueOf(i), "p_mn_l");
  26: en5Var.d(Integer.valueOf(i2), "p_mx_l");
  27: en5Var.d(Integer.valueOf(i3), "h_mx_l");
  28: return s1k.a;
  29: }
  30: });
  31: }
  32: }
~~~

## defpackage/rh0.java (26 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes3.dex */
   4: public final class rh0 extends x6j {
   5: public final String c;
   6: 
   7: public rh0(String str) {
   8: this.c = str;
   9: }
  10: 
  11: public final boolean equals(Object obj) {
  12: if (this == obj) {
  13: return true;
  14: }
  15: return (obj instanceof rh0) && this.c.equals(((rh0) obj).c);
  16: }
  17: 
  18: public final int hashCode() {
  19: return this.c.hashCode();
  20: }
  21: 
  22: @Override // defpackage.mv0
  23: public final String toString() {
  24: return vg9.y("Response(trackId='", this.c, "')");
  25: }
  26: }
~~~

## defpackage/gh0.java (15 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX WARN: $VALUES field not found */
   4: /* JADX WARN: Failed to restore enum class, 'enum' modifier and super class removed */
   5: /* JADX INFO: loaded from: classes2.dex */
   6: public final class gh0 {
   7: public static final /* synthetic */ ut6 b = new ut6(new gh0[]{new gh0("NUMBER_NOT_ASSIGNED", 0, 0), new gh0("NUMBER_ASSIGNED", 1, 1), new gh0("VERIFICATION_PASSED", 2, 2), new gh0("VERIFICATION_TIMEOUT", 3, 3)});
   8: public final byte a;
   9: 
  10: /* JADX WARN: Multi-variable type inference failed */
  11: public gh0(String str, int i, short s) {
  12: super(str, i);
  13: this.a = s;
  14: }
  15: }
~~~

## defpackage/u6.java (271 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.os.Build;
   4: import androidx.work.impl.WorkDatabase;
   5: import java.util.ArrayList;
   6: import java.util.Collections;
   7: import java.util.Iterator;
   8: import java.util.List;
   9: import java.util.Set;
  10: import java.util.concurrent.atomic.AtomicBoolean;
  11: import java.util.concurrent.atomic.AtomicReference;
  12: import one.me.android.initialization.AccountInitializer;
  13: 
  14: /* JADX INFO: loaded from: classes.dex */
  15: public final /* synthetic */ class u6 implements o08 {
  16: public final /* synthetic */ byte a;
  17: public final /* synthetic */ Object b;
  18: public final /* synthetic */ Object c;
  19: public final /* synthetic */ Object d;
  20: 
  21: public /* synthetic */ u6(Object obj, Object obj2, Object obj3, byte b) {
  22: this.a = b;
  23: this.b = obj;
  24: this.c = obj2;
  25: this.d = obj3;
  26: }
  27: 
  28: /* JADX WARN: Multi-variable type inference failed */
  29: @Override // defpackage.o08
  30: public final Object c() throws IllegalAccessException {
  31: String[] strArr;
  32: q53 q53Var;
  33: final boolean z;
  34: int i = 0;
  35: Object[] objArr = 0;
  36: Object[] objArr2 = 0;
  37: b55 b55Var = null;
  38: switch (this.a) {
  39: case 0:
  40: AccountInitializer accountInitializer = (AccountInitializer) this.b;
  41: AtomicBoolean atomicBoolean = (AtomicBoolean) this.c;
  42: AtomicReference atomicReference = (AtomicReference) this.d;
  43: s1k s1kVar = s1k.a;
  44: l6 l6Var = new l6(accountInitializer, objArr2 == true ? 1 : 0);
  45: boolean zB = accountInitializer.c().a().b();
  46: if (zB && !atomicBoolean.get()) {
  47: long jNanoTime = System.nanoTime();
  48: ((qw4) vg9.u(accountInitializer, 241)).a();
  49: o1d o1dVar = f09.g;
  50: if (o1dVar != null) {
  51: c6a c6aVar = c6a.d;
  52: if (o1dVar.b(c6aVar)) {
  53: qzd qzdVar = fe6.b;
  54: o1dVar.c(c6aVar, "InitialDataStorage", "bannersInitialDataStorage.load by ".concat(fe6.x(az7.V(System.nanoTime() - jNanoTime, me6.b))), null);
  55: }
  56: }
  57: }
  58: if (((Boolean) atomicReference.get()).booleanValue() \|\| !zB) {
  59: f09.p(accountInitializer.d, "LegacyChats: async load");
  60: ((vxc) ((k6j) accountInitializer.c().getAccessor().d(7).getValue())).b().A0(jec.b, new n6((Object) l6Var, (byte) (objArr == true ? 1 : 0)));
  61: } else {
  62: f09.p(accountInitializer.d, "LegacyChats: sync load");
  63: l6Var.c();
  64: }
  65: return s1kVar;
  66: case 1:
  67: mz4 mz4Var = (mz4) this.b;
  68: return new ble("contactlist-presence", mz4Var.b, ((vxc) ((k6j) ((rp9) this.c).getValue())).a().K0(1, "presences"), new y30((rp9) this.d, mz4Var, b55Var, (byte) 17));
  69: case 2:
  70: return Integer.valueOf(((c35) this.b).a.n((List) this.c, (zw4) this.d));
  71: case 3:
  72: vck vckVar = (vck) this.b;
  73: st5 st5Var = (st5) this.c;
  74: return new d23(vckVar, new ov4((byte) 16), new dp5(st5Var, (byte) 3), new rt5(st5Var, (rp9) this.d, null));
  75: case 4:
  76: ep6 ep6Var = (ep6) this.b;
  77: return new jo6(ep6Var.b, ep6Var.f, ep6Var.a, ep6Var.c, (rp9) this.c, (rp9) this.d);
  78: case 5:
  79: f87 f87Var = (f87) this.b;
  80: thc thcVar = (thc) this.c;
  81: iuf iufVar = (iuf) this.d;
  82: ((n83) f87Var.i.getValue()).i0(thcVar.a, ((i87) iufVar.a).g(), ((i87) iufVar.a).m(), ((i87) iufVar.a).l());
  83: return s1k.a;
  84: case 6:
  85: vb8 vb8Var = (vb8) this.b;
  86: rp9 rp9Var = (rp9) this.c;
  87: rp9 rp9Var2 = (rp9) this.d;
  88: boolean zE = vb8Var.e();
  89: String str = vb8Var.b;
  90: if (!zE) {
  91: f09.p(str, "Can't init firebaseApp because !areServicesAvailable()");
  92: return null;
  93: }
  94: f09.p(str, "Start creating FirebaseApp");
  95: long jNanoTime2 = System.nanoTime();
  96: if (Build.VERSION.SDK_INT <= 36 && ((Boolean) ((l4i) ((kag) rp9Var.getValue()).c.getValue()).getValue()).booleanValue()) {
  97: Set set = (Set) ((l4i) ((kag) rp9Var.getValue()).d.getValue()).getValue();
  98: if (set == null \|\| (strArr = (String[]) set.toArray(new String[0])) == null) {
  99: strArr = new String[0];
 100: }
 101: ngm.b(rp9Var2, strArr);
 102: }
 103: gg7 gg7VarE = gg7.e(vb8Var.a);
 104: qzd qzdVar2 = fe6.b;
 105: f09.p(str, "End creating FirebaseApp. Takes ".concat(fe6.x(az7.V(System.nanoTime() - jNanoTime2, me6.b))));
 106: return gg7VarE;
 107: case 7:
 108: k6j k6jVar = (k6j) this.b;
 109: ja5 ja5Var = (ja5) this.c;
 110: pu8 pu8Var = (pu8) this.d;
 111: vxc vxcVar = (vxc) k6jVar;
 112: z95 z95VarA = vxcVar.a();
 113: z95 z95VarA2 = vxcVar.a();
 114: qzd qzdVar3 = fe6.b;
 115: return new y91("image-stat-measurement", z95VarA, z95VarA2, ja5Var, az7.U(2, me6.e), new klc((Object) pu8Var, b55Var, (byte) 29), new r3((Object) pu8Var, (byte) 12), null, 128);
 116: case 8:
 117: return Integer.valueOf(((u8g) ((k8a) this.b).c().c()).D((d7b) this.c, ((q53) this.d).a, 0L, false, null, false));
 118: case 9:
 119: return new xub((rp9) this.b, (rp9) this.c, (q1a) this.d);
 120: case 10:
 121: j3e j3eVar = (j3e) this.b;
 122: gc1 gc1Var = (gc1) this.c;
 123: k6j k6jVar2 = (k6j) this.d;
 124: l4i l4iVar = j3eVar.d.c;
 125: return new o4e((l4iVar == null \|\| (q53Var = (q53) l4iVar.getValue()) == null) ? 0L : q53Var.a, gc1Var, k6jVar2, j3eVar.b);
 126: case 11:
 127: f0f f0fVar = (f0f) this.b;
 128: cqe cqeVar = (cqe) this.c;
 129: String str2 = (String) this.d;
 130: dtc dtcVar = (dtc) f0fVar.f.getValue();
 131: String strA = cqeVar.a.a();
 132: qi0 qi0Var = dtcVar.a().d;
 133: if (strA != null) {
 134: qi0Var.e("auth.account.name", strA);
 135: }
 136: qi0Var.e("auth.token", str2);
 137: return s1k.a;
 138: case 12:
 139: return fa5.F(fa5.F((p9g) this.b, ((r1g) this.c).n), (x95) ((z3j) this.d).getValue());
 140: case 13:
 141: f6h f6hVar = (f6h) this.b;
 142: b6h b6hVar = (b6h) this.c;
 143: euf eufVar = (euf) this.d;
 144: ArrayList arrayList = f6hVar.l;
 145: while (true) {
 146: if (i < arrayList.size()) {
 147: int i2 = i + 1;
 148: if (!g4a.c(((vld) arrayList.get(i)).a, b6hVar)) {
 149: i = i2;
 150: }
 151: } else {
 152: i = -1;
 153: }
 154: }
 155: if (i != -1 && !((Boolean) ((vld) arrayList.get(i)).b).booleanValue()) {
 156: eufVar.a = true;
 157: }
 158: return s1k.a;
 159: default:
 160: rul rulVar = (rul) this.b;
 161: String str3 = (String) this.c;
 162: lvl lvlVar = (lvl) this.d;
 163: s1k s1kVar2 = s1k.a;
 164: vvl vvlVarC = rulVar.c.C();
 165: List listE = vvlVarC.e(str3);
 166: if (listE.size() > 1) {
 167: m00.i("Can't apply UPDATE policy to the chains of work.");
 168: return null;
 169: }
 170: ovl ovlVar = (ovl) va4.M0(listE);
 171: if (ovlVar == null) {
 172: ct6.a(new gul(rulVar, str3, 2, Collections.singletonList(lvlVar), null));
 173: } else {
 174: String str4 = ovlVar.a;
 175: qvl qvlVarD = vvlVarC.d(str4);
 176: if (qvlVarD == null) {
 177: k3g.o(w7g.v("WorkSpec with ", str4, ", that matches a name \"", str3, "\", wasn't found"));
 178: return null;
 179: }
 180: if (!qvlVarD.c()) {
 181: m00.i("Can't update OneTimeWorker to Periodic Worker. Update operation must preserve worker's type.");
 182: return null;
 183: }
 184: if (ovlVar.b == nul.f) {
 185: az7.I(vvlVarC.a, false, true, new py5((byte) 13, str4));
 186: ct6.a(new gul(rulVar, str3, 2, Collections.singletonList(lvlVar), null));
 187: } else {
 188: final qvl qvlVarB = qvl.b(lvlVar.b, ovlVar.a, null, null, 0, 0L, 0, 0, 0L, 0, 33554430);
 189: rpe rpeVar = rulVar.f;
 190: final WorkDatabase workDatabase = rulVar.c;
 191: to4 to4Var = rulVar.b;
 192: final List list = rulVar.e;
 193: final Set set2 = lvlVar.c;
 194: final String str5 = qvlVarB.a;
 195: final qvl qvlVarD2 = workDatabase.C().d(str5);
 196: if (qvlVarD2 == null) {
 197: k3g.t(vg9.y("Worker with ", str5, " doesn't exist"));
 198: return null;
 199: }
 200: if (!qvlVarD2.b.a()) {
 201: if (qvlVarD2.c() ^ qvlVarB.c()) {
 202: StringBuilder sb = new StringBuilder("Can't update ");
 203: sb.append(qvlVarD2.c() ? "Periodic" : "OneTime");
 204: sb.append(" Worker to ");
 205: throw new UnsupportedOperationException(w7g.w(sb, qvlVarB.c() ? "Periodic" : "OneTime", " Worker. Update operation must preserve worker's type."));
 206: }
 207: synchronized (rpeVar.k) {
 208: z = rpeVar.c(str5) != null;
 209: break;
 210: }
 211: if (!z) {
 212: Iterator it = list.iterator();
 213: while (it.hasNext()) {
 214: ((ujg) it.next()).d(str5);
 215: }
 216: }
 217: workDatabase.s(new gzc(new Runnable(qvlVarD2, qvlVarB, list, str5, set2, z) { // from class: ewl
 218: public final /* synthetic */ qvl b;
 219: public final /* synthetic */ qvl c;
 220: public final /* synthetic */ String d;
 221: public final /* synthetic */ Set e;
 222: public final /* synthetic */ boolean f;
 223: 
 224: {
 225: this.d = str5;
 226: this.e = set2;
 227: this.f = z;
 228: }
 229: 
 230: @Override // java.lang.Runnable
 231: public final void run() {
 232: WorkDatabase workDatabase2 = this.a;
 233: vvl vvlVarC2 = workDatabase2.C();
 234: yvl yvlVarD = workDatabase2.D();
 235: qvl qvlVar = this.b;
 236: nul nulVar = qvlVar.b;
 237: int i3 = qvlVar.k;
 238: long j = qvlVar.n;
 239: byte b = 1;
 240: int i4 = qvlVar.t + 1;
 241: int i5 = qvlVar.s;
 242: long j2 = qvlVar.u;
 243: int i6 = qvlVar.v;
 244: qvl qvlVar2 = this.c;
 245: qvl qvlVarB2 = qvl.b(qvlVar2, null, nulVar, null, i3, j, i5, i4, j2, i6, 29613053);
 246: if (qvlVar2.v == 1) {
 247: qvlVarB2.u = qvlVar2.u;
 248: qvlVarB2.v++;
 249: }
 250: az7.I(vvlVarC2.a, false, true, new svl(vvlVarC2, usc.K(qvlVarB2), b));
 251: x7g x7gVar = yvlVarD.a;
 252: String str6 = this.d;
 253: az7.I(x7gVar, false, true, new py5((byte) 16, str6));
 254: yvlVarD.a(str6, this.e);
 255: if (this.f) {
 256: return;
 257: }
 258: vvlVarC2.f(-1L, str6);
 259: az7.I(workDatabase2.B().a, false, true, new py5((byte) 4, str6));
 260: }
 261: }, (byte) 1));
 262: if (!z) {
 263: dkg.b(to4Var, workDatabase, list);
 264: }
 265: }
 266: }
 267: }
 268: return s1kVar2;
 269: }
 270: }
 271: }
~~~

## defpackage/c5h.java (162 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.Collections;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public final class c5h extends ft implements d7j {
   8: public final String f;
   9: 
  10: public c5h(long j) {
  11: super(j);
  12: this.f = c5h.class.getName();
  13: }
  14: 
  15: @Override // defpackage.d7j
  16: public final void b(x6j x6jVar) {
  17: Object value;
  18: e5h e5hVar = (e5h) x6jVar;
  19: u().b.b().a.w.a(j9e.w8[14]).a(Integer.valueOf(e5hVar.d));
  20: u().b.L().k(e5hVar.f);
  21: if (e5hVar.d == 1) {
  22: gt gtVar = this.e;
  23: if (gtVar == null) {
  24: gtVar = null;
  25: }
  26: quc qucVar = (quc) gtVar.i.getValue();
  27: c74 c74Var = qucVar.b;
  28: qucVar.d.getClass();
  29: n3a n3aVar = (n3a) c74Var;
  30: n3aVar.A0.z(n3aVar, n3a.g1[18], "26.35.1");
  31: gt gtVar2 = this.e;
  32: if (gtVar2 == null) {
  33: gtVar2 = null;
  34: }
  35: ((quc) gtVar2.i.getValue()).b();
  36: gt gtVar3 = this.e;
  37: if (gtVar3 == null) {
  38: gtVar3 = null;
  39: }
  40: s8a s8aVar = gtVar3.a;
  41: n8a n8aVar = n8a.i;
  42: s8a s8aVar2 = s8a.i;
  43: s8aVar.E(null, n8aVar);
  44: return;
  45: }
  46: if (e5hVar.c != null) {
  47: n3a n3aVar2 = u().a;
  48: n3aVar2.m0.z(n3aVar2, n3a.g1[2], e5hVar.c);
  49: }
  50: if (!(e5hVar.e == null ? Collections.EMPTY_LIST : new ArrayList(e5hVar.e)).isEmpty()) {
  51: gt gtVar4 = this.e;
  52: if (gtVar4 == null) {
  53: gtVar4 = null;
  54: }
  55: za5 za5Var = (za5) gtVar4.o0.getValue();
  56: Object arrayList = e5hVar.e == null ? Collections.EMPTY_LIST : new ArrayList(e5hVar.e);
  57: r4i r4iVar = za5Var.a;
  58: do {
  59: value = r4iVar.getValue();
  60: } while (!r4iVar.f(value, arrayList));
  61: }
  62: if (e5hVar.i) {
  63: gt gtVar5 = this.e;
  64: if (gtVar5 == null) {
  65: gtVar5 = null;
  66: }
  67: ((i3l) gtVar5.q0.getValue()).c(e5hVar.i);
  68: }
  69: gt gtVar6 = this.e;
  70: if (gtVar6 == null) {
  71: gtVar6 = null;
  72: }
  73: String strC = ((dtc) gtVar6.f.getValue()).c();
  74: gt gtVar7 = this.e;
  75: if (gtVar7 == null) {
  76: gtVar7 = null;
  77: }
  78: s8a s8aVar3 = gtVar7.a;
  79: String str = s8aVar3.g;
  80: lmj lmjVar = str != null ? new lmj(str) : null;
  81: String str2 = lmjVar != null ? lmjVar.a : null;
  82: if (str2 == null) {
  83: String str3 = s8aVar3.b;
  84: o1d o1dVar = f09.g;
  85: if (o1dVar != null) {
  86: c6a c6aVar = c6a.f;
  87: if (o1dVar.b(c6aVar)) {
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
  98: gt gtVar8 = this.e;
  99: if (gtVar8 == null) {
 100: gtVar8 = null;
 101: }
 102: byte[] bArrA = ((v99) gtVar8.k.getValue()).a(e5hVar.g);
 103: gt gtVar9 = this.e;
 104: k8a k8aVar = (k8a) (gtVar9 != null ? gtVar9 : null).j.getValue();
 105: int i = e5hVar.h;
 106: Long l = e5hVar.g;
 107: ctc ctcVar = (ctc) k8aVar.D.getValue();
 108: f7j.b(ctcVar.a(), new i7a(((hog) ((c74) ctcVar.b.getValue())).g(), i, l, bArrA, null));
 109: }
 110: 
 111: @Override // defpackage.d7j
 112: public final void f(l6j l6jVar) {
 113: gt gtVar = this.e;
 114: if (gtVar == null) {
 115: gtVar = null;
 116: }
 117: ((f5h) gtVar.h.getValue()).a(this.a, l6jVar);
 118: }
 119: 
 120: @Override // defpackage.ft
 121: public final Object n() {
 122: gt gtVar = this.e;
 123: if (gtVar == null) {
 124: gtVar = null;
 125: }
 126: rck rckVarA = ((tck) gtVar.s0.getValue()).a();
 127: gt gtVar2 = this.e;
 128: if (gtVar2 == null) {
 129: gtVar2 = null;
 130: }
 131: String strA = ((h16) gtVar2.r0.getValue()).a();
 132: long jW = u().a.W();
 133: gt gtVar3 = this.e;
 134: if (gtVar3 == null) {
 135: gtVar3 = null;
 136: }
 137: String str = (String) ((h16) gtVar3.r0.getValue()).f.get();
 138: d5h d5hVar = new d5h(null);
 139: i00 i00Var = new i00(0);
 140: i00Var.put("deviceType", "ANDROID");
 141: baf bafVar = rckVarA.g;
 142: if (bafVar != null) {
 143: i00Var.put("pushDeviceType", bafVar.a);
 144: }
 145: i00Var.put("appVersion", "26.35.1");
 146: i00Var.put("arch", rckVarA.b);
 147: i00Var.put("buildNumber", 6867);
 148: i00Var.put("osVersion", rckVarA.a);
 149: i00Var.put("locale", rckVarA.c);
 150: i00Var.put("deviceLocale", rckVarA.d);
 151: i00Var.put("deviceName", rckVarA.e);
 152: i00Var.put("screen", rckVarA.f);
 153: i00Var.put("timezone", rckVarA.h.getID());
 154: d5hVar.g("userAgent", i00Var);
 155: d5hVar.h("deviceId", strA);
 156: d5hVar.f(jW, "clientSessionId");
 157: if (f09.J(str)) {
 158: d5hVar.h("mt_instanceid", str);
 159: }
 160: return d5hVar;
 161: }
 162: }
~~~

## defpackage/gn0.java (128 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class gn0 {
   5: public final String a;
   6: public final int b;
   7: public final String c;
   8: public final String d;
   9: public final long e;
  10: public final long f;
  11: public final String g;
  12: 
  13: public gn0(int i, long j, long j2, String str, String str2, String str3, String str4) {
  14: this.a = str;
  15: this.b = i;
  16: this.c = str2;
  17: this.d = str3;
  18: this.e = j;
  19: this.f = j2;
  20: this.g = str4;
  21: }
  22: 
  23: public final fn0 a() {
  24: fn0 fn0Var = new fn0();
  25: fn0Var.b = this.a;
  26: fn0Var.a = this.b;
  27: fn0Var.c = this.c;
  28: fn0Var.d = this.d;
  29: fn0Var.f = Long.valueOf(this.e);
  30: fn0Var.g = Long.valueOf(this.f);
  31: fn0Var.e = this.g;
  32: return fn0Var;
  33: }
  34: 
  35: public final boolean equals(Object obj) {
  36: if (obj == this) {
  37: return true;
  38: }
  39: if (!(obj instanceof gn0)) {
  40: return false;
  41: }
  42: gn0 gn0Var = (gn0) obj;
  43: String str = gn0Var.a;
  44: String str2 = this.a;
  45: if (str2 == null) {
  46: if (str != null) {
  47: return false;
  48: }
  49: } else if (!str2.equals(str)) {
  50: return false;
  51: }
  52: if (!s95.e(this.b, gn0Var.b)) {
  53: return false;
  54: }
  55: String str3 = gn0Var.c;
  56: String str4 = this.c;
  57: if (str4 == null) {
  58: if (str3 != null) {
  59: return false;
  60: }
  61: } else if (!str4.equals(str3)) {
  62: return false;
  63: }
  64: String str5 = gn0Var.d;
  65: String str6 = this.d;
  66: if (str6 == null) {
  67: if (str5 != null) {
  68: return false;
  69: }
  70: } else if (!str6.equals(str5)) {
  71: return false;
  72: }
  73: if (this.e != gn0Var.e \|\| this.f != gn0Var.f) {
  74: return false;
  75: }
  76: String str7 = gn0Var.g;
  77: String str8 = this.g;
  78: if (str8 == null) {
  79: return str7 == null;
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
~~~

## defpackage/sk2.java (88 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.os.Looper;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class sk2 {
   7: public static final /* synthetic */ zm9[] f;
   8: public final yi2 a;
   9: public final rp9 b;
  10: public final rp9 c;
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
  21: this.a = yi2Var;
  22: this.b = rp9Var;
  23: this.c = rp9Var2;
  24: this.d = rp9Var3;
  25: }
  26: 
  27: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
  28: public final Object a(d55 d55Var) {
  29: rk2 rk2Var;
  30: if (d55Var instanceof rk2) {
  31: rk2Var = (rk2) d55Var;
  32: int i = rk2Var.f;
  33: if ((i & Integer.MIN_VALUE) != 0) {
  34: rk2Var.f = i - Integer.MIN_VALUE;
  35: } else {
  36: rk2Var = new rk2(this, d55Var);
  37: }
  38: } else {
  39: rk2Var = new rk2(this, d55Var);
  40: }
  41: Object objA = rk2Var.d;
  42: ka5 ka5Var = ka5.a;
  43: int i2 = rk2Var.f;
  44: if (i2 == 0) {
  45: xnm.y(objA);
  46: if (Looper.getMainLooper().isCurrentThread()) {
  47: ((nvc) this.d.getValue()).getClass();
  48: f09.c0("CallsCredRepositoryTag", "Ok token was called from the main thread.", new IllegalStateException("Ok token was called from the main thread."));
  49: }
  50: long jF = ((hog) ((c74) this.b.getValue())).f();
  51: long jO = ((hog) ((c74) this.b.getValue())).o();
  52: if (jF >= jO) {
  53: fwc fwcVar = (fwc) this.c.getValue();
  54: rk2Var.f = 1;
  55: objA = fwcVar.a(rk2Var);
  56: if (objA == ka5Var) {
  57: return ka5Var;
  58: }
  59: } else {
  60: o1d o1dVar = f09.g;
  61: if (o1dVar != null) {
  62: c6a c6aVar = c6a.d;
  63: if (o1dVar.b(c6aVar)) {
  64: o1dVar.c(c6aVar, "CallsCredRepositoryTag", s95.p("Ok token will be expired in ", ".", jO), null);
  65: }
  66: }
  67: }
  68: return s1k.a;
  69: }
  70: if (i2 != 1) {
  71: k3g.o("call to 'resume' before 'invoke' with coroutine");
  72: return null;
  73: }
  74: xnm.y(objA);
  75: cqc cqcVar = (cqc) objA;
  76: c74 c74Var = (c74) this.b.getValue();
  77: String strH = cqcVar.h();
  78: hog hogVar = (hog) c74Var;
  79: zcg zcgVar = hogVar.E;
  80: zm9[] zm9VarArr = hog.i0;
  81: zcgVar.z(hogVar, zm9VarArr[27], strH);
  82: c74 c74Var2 = (c74) this.b.getValue();
  83: hog hogVar2 = (hog) c74Var2;
  84: hogVar2.G.z(hogVar2, zm9VarArr[29], Long.valueOf(cqcVar.i()));
  85: f09.p("CallsCredRepositoryTag", "Ok token updated.");
  86: return s1k.a;
  87: }
  88: }
~~~

## defpackage/mse.java (11 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class mse {
   5: public final x7g a;
   6: public final to b = new to(13);
   7: 
   8: public mse(x7g x7gVar) {
   9: this.a = x7gVar;
  10: }
  11: }
~~~

## defpackage/l7a.java (145 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.ArrayList;
   4: import java.util.HashMap;
   5: import java.util.List;
   6: import java.util.Map;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class l7a extends x6j implements s6a {
  10: public final cqe c;
  11: public final List d;
  12: public final List e;
  13: public final String f;
  14: public final long g;
  15: public final so4 h;
  16: public final HashMap i;
  17: public final long j;
  18: public final ArrayList k;
  19: public final boolean l;
  20: public final long m;
  21: public final int n;
  22: public final d7a o;
  23: 
  24: public l7a(cqe cqeVar, List list, List list2, String str, long j, so4 so4Var, HashMap map, long j2, ArrayList arrayList, boolean z, long j3, int i, d7a d7aVar) {
  25: this.c = cqeVar;
  26: this.d = list;
  27: this.e = list2;
  28: this.f = str;
  29: this.g = j;
  30: this.h = so4Var;
  31: this.i = map;
  32: this.j = j2;
  33: this.k = arrayList;
  34: this.l = z;
  35: this.m = j3;
  36: this.n = i;
  37: this.o = d7aVar;
  38: this.a = Math.abs(System.nanoTime() - j3) / 1000000;
  39: }
  40: 
  41: @Override // defpackage.s6a
  42: public final String a(boolean z, boolean z2) {
  43: String string;
  44: d0i d0iVar;
  45: d0i d0iVar2;
  46: so4 so4Var = this.h;
  47: if (so4Var != null && (d0iVar2 = so4Var.b) != null) {
  48: Map map = (Map) d0iVar2.b;
  49: if (map.containsKey("log-full")) {
  50: Object obj = map.get("log-full");
  51: z = Boolean.parseBoolean(obj != null ? obj.toString() : null);
  52: } else {
  53: z = false;
  54: }
  55: }
  56: if (so4Var != null && (d0iVar = so4Var.b) != null) {
  57: Map map2 = (Map) d0iVar.b;
  58: if (map2.containsKey("log-sensitive")) {
  59: Object obj2 = map2.get("log-sensitive");
  60: z2 = Boolean.parseBoolean(obj2 != null ? obj2.toString() : null);
  61: } else {
  62: z2 = false;
  63: }
  64: }
  65: StringBuilder sb = new StringBuilder("LOGIN.Response(login2Flags=");
  66: sb.append(this.o);
  67: sb.append(",profile=");
  68: sb.append(String.valueOf(this.c));
  69: sb.append(",token=");
  70: String str = this.f;
  71: sb.append(z2 ? str != null ? str.toString() : "NULL" : f09.N(str));
  72: sb.append(",time=");
  73: sb.append(this.g);
  74: sb.append(",chatMarker=");
  75: sb.append(this.j);
  76: sb.append(",videoChatHistory=");
  77: sb.append(this.l);
  78: sb.append(",contactInfos=");
  79: sb.append(g4a.z(this.e, z, z2));
  80: sb.append(",config=");
  81: sb.append(so4Var);
  82: sb.append(",messages=");
  83: HashMap map3 = this.i;
  84: if (z) {
  85: StringBuilder sb2 = new StringBuilder("{");
  86: for (Map.Entry entry : map3.entrySet()) {
  87: Object key = entry.getKey();
  88: Object value = entry.getValue();
  89: sb2.append(String.valueOf(key));
  90: sb2.append('=');
  91: sb2.append(g4a.R(value, z, z2));
  92: sb2.append(',');
  93: }
  94: sb2.append('}');
  95: string = sb2.toString();
  96: } else {
  97: string = String.valueOf(map3.size());
  98: }
  99: sb.append(string);
 100: sb.append(",chats=");
 101: sb.append(g4a.z(this.d, z, z2));
 102: sb.append(",calls=");
 103: sb.append(g4a.z(this.k, z, z2));
 104: sb.append(",updates=");
 105: return pq0.h(this.n, ",)", sb);
 106: }
 107: 
 108: public final boolean equals(Object obj) {
 109: if (this == obj) {
 110: return true;
 111: }
 112: if (!(obj instanceof l7a)) {
 113: return false;
 114: }
 115: l7a l7aVar = (l7a) obj;
 116: return g4a.c(this.c, l7aVar.c) && g4a.c(this.d, l7aVar.d) && g4a.c(this.e, l7aVar.e) && g4a.c(this.f, l7aVar.f) && this.g == l7aVar.g && g4a.c(this.h, l7aVar.h) && this.i.equals(l7aVar.i) && this.j == l7aVar.j && this.k.equals(l7aVar.k) && this.l == l7aVar.l && this.m == l7aVar.m && this.n == l7aVar.n && g4a.c(this.o, l7aVar.o);
 117: }
 118: 
 119: public final ArrayList h() {
 120: List list = this.e;
 121: ArrayList arrayList = new ArrayList();
 122: for (Object obj : list) {
 123: if (((ey4) obj) != dy4.t) {
 124: arrayList.add(obj);
 125: }
 126: }
 127: return arrayList;
 128: }
 129: 
 130: public final int hashCode() {
 131: cqe cqeVar = this.c;
 132: int iC = pq0.c(this.e, pq0.c(this.d, (cqeVar == null ? 0 : cqeVar.hashCode()) * 31, 31), 31);
 133: String str = this.f;
 134: int iH = s95.h((iC + (str == null ? 0 : str.hashCode())) * 31, 31, this.g);
 135: so4 so4Var = this.h;
 136: int iD = a15.d(this.n, s95.h(w7g.n(vw4.d(this.k, s95.h((this.i.hashCode() + ((iH + (so4Var == null ? 0 : so4Var.hashCode())) * 31)) * 31, 31, this.j), 31), 31, this.l), 31, this.m), 31);
 137: d7a d7aVar = this.o;
 138: return iD + (d7aVar != null ? d7aVar.hashCode() : 0);
 139: }
 140: 
 141: @Override // defpackage.mv0
 142: public final String toString() {
 143: return a(false, false);
 144: }
 145: }
~~~

## defpackage/c7j.java (14 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.concurrent.atomic.AtomicBoolean;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public class c7j {
   7: public static final b7j b = new b7j();
   8: public final AtomicBoolean a = new AtomicBoolean(false);
   9: 
  10: public Object a(q08 q08Var, x1j x1jVar) {
  11: Object objD;
  12: return (this.a.compareAndSet(false, true) && (objD = q08Var.d(x1jVar)) == ka5.a) ? objD : s1k.a;
  13: }
  14: }
~~~

## defpackage/k8a.java (904 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class k8a {
   5: public final rp9 A;
   6: public final rp9 B;
   7: public final rp9 C;
   8: public final rp9 D;
   9: public final rp9 E;
  10: public final rp9 F;
  11: public final rp9 G;
  12: public final r4i H;
  13: public final dmf I;
  14: public final String J;
  15: public final f0f a;
  16: public final ho7 b;
  17: public final yt0 c;
  18: public final s8a d;
  19: public final rp9 e;
  20: public final rp9 f;
  21: public final rp9 g;
  22: public final rp9 h;
  23: public final rp9 i;
  24: public final rp9 j;
  25: public final rp9 k;
  26: public final rp9 l;
  27: public final rp9 m;
  28: public final rp9 n;
  29: public final rp9 o;
  30: public final rp9 p;
  31: public final rp9 q;
  32: public final rp9 r;
  33: public final rp9 s;
  34: public final rp9 t;
  35: public final rp9 u;
  36: public final rp9 v;
  37: public final rp9 w;
  38: public final rp9 x;
  39: public final rp9 y;
  40: public final rp9 z;
  41: 
  42: public k8a(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9, rp9 rp9Var10, rp9 rp9Var11, rp9 rp9Var12, rp9 rp9Var13, rp9 rp9Var14, rp9 rp9Var15, rp9 rp9Var16, rp9 rp9Var17, rp9 rp9Var18, rp9 rp9Var19, rp9 rp9Var20, rp9 rp9Var21, rp9 rp9Var22, rp9 rp9Var23, rp9 rp9Var24, rp9
  43: this.a = f0fVar;
  44: this.b = ho7Var;
  45: this.c = yt0Var;
  46: this.d = s8aVar;
  47: this.e = rp9Var;
  48: this.f = rp9Var2;
  49: this.g = rp9Var3;
  50: this.h = rp9Var4;
  51: this.i = rp9Var5;
  52: this.j = rp9Var6;
  53: this.k = rp9Var7;
  54: this.l = rp9Var9;
  55: this.m = rp9Var10;
  56: this.n = rp9Var11;
  57: this.o = rp9Var12;
  58: this.p = rp9Var13;
  59: this.q = rp9Var14;
  60: this.r = rp9Var15;
  61: this.s = rp9Var16;
  62: this.t = rp9Var17;
  63: this.u = rp9Var18;
  64: this.v = rp9Var19;
  65: this.w = rp9Var20;
  66: this.x = rp9Var21;
  67: this.y = rp9Var22;
  68: this.z = rp9Var23;
  69: this.A = rp9Var24;
  70: this.B = rp9Var25;
  71: this.C = rp9Var8;
  72: this.D = rp9Var26;
  73: this.E = rp9Var27;
  74: this.F = rp9Var29;
  75: this.G = rp9Var28;
  76: r4i r4iVarC = az7.c(Boolean.TRUE);
  77: this.H = r4iVarC;
  78: this.I = new dmf(r4iVarC);
  79: this.J = k8a.class.getName();
  80: }
  81: 
  82: public static final String g(guf gufVar, huf hufVar) {
  83: StringBuilder sb = new StringBuilder("#");
  84: int i = gufVar.a;
  85: gufVar.a = i + 1;
  86: sb.append(i);
  87: sb.append('(');
  88: long jNanoTime = System.nanoTime();
  89: long j = jNanoTime - hufVar.a;
  90: hufVar.a = jNanoTime;
  91: qzd qzdVar = fe6.b;
  92: sb.append(fe6.x(az7.V(j, me6.b)));
  93: sb.append(')');
  94: return sb.toString();
  95: }
  96: 
  97: public final n83 a() {
  98: return (n83) this.j.getValue();
  99: }
 100: 
 101: public final n3a b() {
 102: return e().a;
 103: }
 104: 
 105: public final wi5 c() {
 106: return (wi5) this.h.getValue();
 107: }
 108: 
 109: public final k6j d() {
 110: return (k6j) this.y.getValue();
 111: }
 112: 
 113: public final dle e() {
 114: return (dle) this.g.getValue();
 115: }
 116: 
 117: /*  JADX ERROR: Type inference failed
 118: jadx.core.utils.exceptions.JadxOverflowException: Type inference error: updates count limit reached with updateSeq = 43541. Try increasing type updates limit count.
 119: at jadx.core.utils.ErrorsCounter.addError(ErrorsCounter.java:59)
 120: at jadx.core.utils.ErrorsCounter.error(ErrorsCounter.java:31)
 121: at jadx.core.dex.attributes.nodes.NotificationAttrNode.addError(NotificationAttrNode.java:19)
 122: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:79)
 123: */
 124: public final java.lang.Object f(long r54, defpackage.l7a r56, long r57, int r59, java.lang.String r60, defpackage.d55 r61) {
 125: /*
 126: Method dump skipped, instruction units count: 4354
 127: To view this dump add '--comments-level debug' option
 128: */
 129: throw new UnsupportedOperationException("Method not decompiled: defpackage.k8a.f(long, l7a, long, int, java.lang.String, d55):java.lang.Object");
 130: }
 131: 
 132: /* JADX WARN: Code duplicated, block: B:21:0x01af  */
 133: /* JADX WARN: Code duplicated, block: B:23:0x0201  */
 134: /* JADX WARN: Code duplicated, block: B:26:0x0214  */
 135: /* JADX WARN: Code duplicated, block: B:29:0x021b  */
 136: /* JADX WARN: Code duplicated, block: B:35:0x0236  */
 137: /* JADX WARN: Code duplicated, block: B:7:0x0019  */
 138: /* JADX WARN: Failed to calculate best type for var: r11v22 ??
 139: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v22 ??, new type: java.util.Iterator
 140: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 141: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 142: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 143: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 144: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 145: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 146: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 147: Caused by: java.lang.NullPointerException
 148: */
 149: /* JADX WARN: Failed to calculate best type for var: r11v22 ??
 150: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v22 ??, new type: java.util.Iterator
 151: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 152: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 153: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 154: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 155: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 156: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 157: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 158: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 159: Caused by: java.lang.NullPointerException
 160: */
 161: /* JADX WARN: Failed to calculate best type for var: r11v6 ??
 162: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v6 ??, new type: java.util.Iterator
 163: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 164: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 165: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 166: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 167: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 168: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 169: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 170: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 171: Caused by: java.lang.NullPointerException
 172: */
 173: /* JADX WARN: Failed to calculate best type for var: r11v6 ??
 174: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v6 ??, new type: java.util.Iterator
 175: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 176: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 177: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 178: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 179: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 180: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 181: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 182: Caused by: java.lang.NullPointerException
 183: */
 184: /* JADX WARN: Failed to calculate best type for var: r11v6 ??
 185: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v6 ??, new type: java.util.Iterator
 186: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 187: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 188: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 189: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 190: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 191: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 192: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 193: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 194: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 195: Caused by: java.lang.NullPointerException
 196: */
 197: /* JADX WARN: Failed to calculate best type for var: r11v6 ??
 198: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r11v6 ??, new type: java.util.Iterator
 199: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 200: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 201: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 202: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 203: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 204: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 205: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 206: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 207: Caused by: java.lang.NullPointerException
 208: */
 209: /* JADX WARN: Failed to calculate best type for var: r12v0 ??
 210: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v0 ??, new type: java.util.Iterator
 211: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 212: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 213: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 214: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 215: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 216: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 217: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 218: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 219: Caused by: java.lang.NullPointerException
 220: */
 221: /* JADX WARN: Failed to calculate best type for var: r12v0 ??
 222: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v0 ??, new type: java.util.Iterator
 223: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 224: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 225: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 226: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 227: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 228: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 229: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 230: Caused by: java.lang.NullPointerException
 231: */
 232: /* JADX WARN: Failed to calculate best type for var: r12v0 ??
 233: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v0 ??, new type: java.util.Iterator
 234: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 235: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 236: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 237: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 238: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 239: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 240: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 241: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 242: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 243: Caused by: java.lang.NullPointerException
 244: */
 245: /* JADX WARN: Failed to calculate best type for var: r12v0 ??
 246: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v0 ??, new type: java.util.Iterator
 247: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 248: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 249: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 250: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 251: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 252: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 253: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 254: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 255: Caused by: java.lang.NullPointerException
 256: */
 257: /* JADX WARN: Failed to calculate best type for var: r12v12 ??
 258: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v12 ??, new type: java.util.Iterator
 259: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 260: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 261: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 262: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 263: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 264: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 265: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 266: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 267: Caused by: java.lang.NullPointerException
 268: */
 269: /* JADX WARN: Failed to calculate best type for var: r12v12 ??
 270: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v12 ??, new type: java.util.Iterator
 271: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 272: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 273: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 274: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 275: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 276: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 277: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 278: Caused by: java.lang.NullPointerException
 279: */
 280: /* JADX WARN: Failed to calculate best type for var: r12v12 ??
 281: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v12 ??, new type: java.util.Iterator
 282: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 283: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 284: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 285: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 286: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 287: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 288: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 289: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 290: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 291: Caused by: java.lang.NullPointerException
 292: */
 293: /* JADX WARN: Failed to calculate best type for var: r12v12 ??
 294: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v12 ??, new type: java.util.Iterator
 295: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 296: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 297: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 298: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 299: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 300: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 301: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 302: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 303: Caused by: java.lang.NullPointerException
 304: */
 305: /* JADX WARN: Failed to calculate best type for var: r12v16 ??
 306: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v16 ??, new type: java.util.Iterator
 307: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 308: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 309: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 310: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 311: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 312: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 313: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 314: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 315: Caused by: java.lang.NullPointerException
 316: */
 317: /* JADX WARN: Failed to calculate best type for var: r12v16 ??
 318: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v16 ??, new type: java.util.Iterator
 319: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 320: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 321: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 322: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 323: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 324: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 325: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 326: Caused by: java.lang.NullPointerException
 327: */
 328: /* JADX WARN: Failed to calculate best type for var: r12v16 ??
 329: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v16 ??, new type: java.util.Iterator
 330: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 331: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 332: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 333: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 334: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 335: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 336: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 337: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 338: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 339: Caused by: java.lang.NullPointerException
 340: */
 341: /* JADX WARN: Failed to calculate best type for var: r12v16 ??
 342: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v16 ??, new type: java.util.Iterator
 343: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 344: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 345: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 346: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 347: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 348: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 349: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 350: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 351: Caused by: java.lang.NullPointerException
 352: */
 353: /* JADX WARN: Failed to calculate best type for var: r12v33 ??
 354: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v33 ??, new type: java.util.Iterator
 355: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 356: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 357: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 358: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 359: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 360: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 361: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 362: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 363: Caused by: java.lang.NullPointerException
 364: */
 365: /* JADX WARN: Failed to calculate best type for var: r12v33 ??
 366: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v33 ??, new type: java.util.Iterator
 367: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 368: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 369: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 370: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 371: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 372: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 373: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 374: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 375: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 376: Caused by: java.lang.NullPointerException
 377: */
 378: /* JADX WARN: Failed to calculate best type for var: r12v4 ??
 379: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v4 ??, new type: java.util.Iterator
 380: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 381: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 382: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 383: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 384: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 385: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 386: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 387: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 388: Caused by: java.lang.NullPointerException
 389: */
 390: /* JADX WARN: Failed to calculate best type for var: r12v4 ??
 391: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v4 ??, new type: java.util.Iterator
 392: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 393: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 394: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 395: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 396: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 397: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 398: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 399: Caused by: java.lang.NullPointerException
 400: */
 401: /* JADX WARN: Failed to calculate best type for var: r12v4 ??
 402: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v4 ??, new type: java.util.Iterator
 403: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 404: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 405: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 406: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 407: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 408: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 409: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 410: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 411: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 412: Caused by: java.lang.NullPointerException
 413: */
 414: /* JADX WARN: Failed to calculate best type for var: r12v4 ??
 415: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r12v4 ??, new type: java.util.Iterator
 416: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 417: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 418: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 419: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 420: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 421: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 422: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 423: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 424: Caused by: java.lang.NullPointerException
 425: */
 426: /* JADX WARN: Failed to calculate best type for var: r15v48 ??
 427: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r15v48 ??, new type: java.util.Iterator
 428: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 429: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 430: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 431: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 432: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 433: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 434: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 435: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 436: Caused by: java.lang.NullPointerException
 437: */
 438: /* JADX WARN: Failed to calculate best type for var: r15v48 ??
 439: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r15v48 ??, new type: java.util.Iterator
 440: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 441: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 442: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 443: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 444: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 445: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 446: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 447: Caused by: java.lang.NullPointerException
 448: */
 449: /* JADX WARN: Failed to calculate best type for var: r15v48 ??
 450: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r15v48 ??, new type: java.util.Iterator
 451: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 452: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 453: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 454: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 455: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 456: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 457: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 458: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 459: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 460: Caused by: java.lang.NullPointerException
 461: */
 462: /* JADX WARN: Failed to calculate best type for var: r15v48 ??
 463: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r15v48 ??, new type: java.util.Iterator
 464: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 465: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 466: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 467: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 468: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 469: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 470: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 471: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 472: Caused by: java.lang.NullPointerException
 473: */
 474: /* JADX WARN: Failed to calculate best type for var: r1v10 ??
 475: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r1v10 ??, new type: java.util.Iterator
 476: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 477: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 478: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 479: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 480: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 481: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 482: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
 483: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 484: Caused by: java.lang.NullPointerException
 485: */
 486: /* JADX WARN: Failed to calculate best type for var: r1v10 ??
 487: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r1v10 ??, new type: java.util.Iterator
 488: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 489: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 490: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 491: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 492: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 493: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 494: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 495: Caused by: java.lang.NullPointerException
 496: */
 497: /* JADX WARN: Failed to calculate best type for var: r1v10 ??
 498: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r1v10 ??, new type: java.util.Iterator
 499: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 500: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 501: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 502: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 503: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 504: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 505: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 506: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:678)
 507: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
 508: Caused by: java.lang.NullPointerException
 509: */
 510: /* JADX WARN: Failed to calculate best type for var: r1v10 ??
 511: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r1v10 ??, new type: java.util.Iterator
 512: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 513: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 514: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.calculateFromBounds(TypeInferenceVisitor.java:147)
 515: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.setBestType(TypeInferenceVisitor.java:125)
 516: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.lambda$runTypePropagation$2(TypeInferenceVisitor.java:103)
 517: at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
 518: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.runTypePropagation(TypeInferenceVisitor.java:103)
 519: at jadx.core.dex.visitors.typeinference.TypeInferenceVisitor.visit(TypeInferenceVisitor.java:75)
 520: Caused by: java.lang.NullPointerException
 521: */
 522: /* JADX WARN: Failed to calculate best type for var: r2v29 ??
 523: jadx.core.utils.exceptions.JadxRuntimeException: Type update failed for variable: r2v29 ??, new type: java.util.Iterator
 524: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:109)
 525: at jadx.core.dex.visitors.typeinference.TypeUpdate.apply(TypeUpdate.java:59)
 526: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.calculateFromBounds(FixTypesVisitor.java:159)
 527: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.setBestType(FixTypesVisitor.java:136)
 528: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.deduceType(FixTypesVisitor.java:241)
 529: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryDeduceTypes(FixTypesVisitor.java:224)
 530: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryInsertAdditionalMove(FixTypesVisitor.java:681)
~~~

Поздние сигнатуры: 897 public final java.lang.Object h(java.util.HashMap r39, defpackage.d55 r40) {

## defpackage/gh6.java (376 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.content.IntentFilter;
   4: import android.os.Bundle;
   5: import java.io.File;
   6: import java.util.List;
   7: import one.me.devmenu.logsviewer.IntegrityLogsViewerScreen;
   8: import one.me.webview.FaqWebViewWidget;
   9: import org.webrtc.PeerConnectionFactory;
  10: 
  11: /* JADX INFO: loaded from: classes2.dex */
  12: public final class gh6 extends x1j implements e18 {
  13: public final /* synthetic */ byte e;
  14: public boolean f;
  15: public final /* synthetic */ Object g;
  16: public Object h;
  17: 
  18: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  19: public gh6(gl8 gl8Var, jl8 jl8Var, boolean z, b55 b55Var) {
  20: super(2, b55Var);
  21: this.e = (byte) 17;
  22: this.h = gl8Var;
  23: this.g = jl8Var;
  24: this.f = z;
  25: }
  26: 
  27: private final Object A(Object obj) throws Throwable {
  28: boolean z = this.f;
  29: if (!z) {
  30: xnm.y(obj);
  31: nih nihVar = ((pt9) this.h).a;
  32: xv0 xv0Var = (xv0) this.g;
  33: long j = xv0Var.a;
  34: l6j l6jVar = xv0Var.b;
  35: String str = l6jVar.d;
  36: if (str == null) {
  37: str = l6jVar.c;
  38: }
  39: it9 it9Var = new it9(j, str);
  40: this.f = true;
  41: Object objB = nihVar.b(it9Var, this);
  42: ka5 ka5Var = ka5.a;
  43: if (objB == ka5Var) {
  44: return ka5Var;
  45: }
  46: } else {
  47: if (!z) {
  48: k3g.o("call to 'resume' before 'invoke' with coroutine");
  49: return null;
  50: }
  51: xnm.y(obj);
  52: }
  53: return s1k.a;
  54: }
  55: 
  56: private final Object B(Object obj) {
  57: k4a k4aVar = (k4a) this.g;
  58: wpe wpeVar = (wpe) this.h;
  59: boolean z = this.f;
  60: if (!z) {
  61: xnm.y(obj);
  62: j4a j4aVar = new j4a(k4aVar, new n00(0));
  63: IntentFilter intentFilter = new IntentFilter();
  64: intentFilter.addAction("action.LOCALE_CHANGED");
  65: intentFilter.addAction("action.CONFIGURATION_UPDATED");
  66: c45.P(k4aVar.e, j4aVar, intentFilter, null, 4);
  67: dv8 dv8Var = new dv8(k4aVar, j4aVar, (byte) 6);
  68: this.h = null;
  69: this.f = true;
  70: Object objH = jd0.h(wpeVar, dv8Var, this);
  71: ka5 ka5Var = ka5.a;
  72: if (objH == ka5Var) {
  73: return ka5Var;
  74: }
  75: } else {
  76: if (!z) {
  77: k3g.o("call to 'resume' before 'invoke' with coroutine");
  78: return null;
  79: }
  80: xnm.y(obj);
  81: }
  82: return s1k.a;
  83: }
  84: 
  85: private final Object C(Object obj) {
  86: boolean z = this.f;
  87: if (!z) {
  88: xnm.y(obj);
  89: i7a i7aVar = (i7a) this.h;
  90: l7a l7aVar = (l7a) this.g;
  91: this.f = true;
  92: Object objX = i7aVar.k(l7aVar, this);
  93: ka5 ka5Var = ka5.a;
  94: if (objX == ka5Var) {
  95: return ka5Var;
  96: }
  97: } else {
  98: if (!z) {
  99: k3g.o("call to 'resume' before 'invoke' with coroutine");
 100: return null;
 101: }
 102: xnm.y(obj);
 103: }
 104: return s1k.a;
 105: }
 106: 
 107: private final Object y(Object obj) {
 108: boolean z = this.f;
 109: try {
 110: if (!z) {
 111: xnm.y(obj);
 112: hh7 hh7Var = (hh7) ((ir9) this.g).f.getValue();
 113: this.h = null;
 114: this.f = true;
 115: Object objA = hh7Var.a(this);
 116: ka5 ka5Var = ka5.a;
 117: if (objA == ka5Var) {
 118: return ka5Var;
 119: }
 120: } else {
 121: if (!z) {
 122: k3g.o("call to 'resume' before 'invoke' with coroutine");
 123: return null;
 124: }
 125: xnm.y(obj);
 126: }
 127: } catch (Throwable unused) {
 128: }
 129: return s1k.a;
 130: }
 131: 
 132: private final Object z(Object obj) throws Throwable {
 133: ot9 ot9Var = (ot9) this.g;
 134: boolean z = this.f;
 135: if (!z) {
 136: xnm.y(obj);
 137: nih nihVar = ((pt9) this.h).a;
 138: jt9 jt9Var = new jt9(ot9Var.a, ot9Var.b, new Long(ot9Var.c), ot9Var.d, ot9Var.e, ot9Var.f, ot9Var.g, ot9Var.h);
 139: this.f = true;
 140: Object objB = nihVar.b(jt9Var, this);
 141: ka5 ka5Var = ka5.a;
 142: if (objB == ka5Var) {
 143: return ka5Var;
 144: }
 145: } else {
 146: if (!z) {
 147: k3g.o("call to 'resume' before 'invoke' with coroutine");
 148: return null;
 149: }
 150: xnm.y(obj);
 151: }
 152: return s1k.a;
 153: }
 154: 
 155: @Override // defpackage.e18
 156: public final Object invoke(Object obj, Object obj2) throws Exception {
 157: byte b = this.e;
 158: s1k s1kVar = s1k.a;
 159: switch (b) {
 160: case 0:
 161: return ((gh6) u((b55) obj2, (ri7) obj)).w(s1kVar);
 162: case 1:
 163: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 164: case 2:
 165: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 166: case 3:
 167: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 168: case 4:
 169: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 170: case 5:
 171: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 172: case 6:
 173: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 174: case 7:
 175: ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 176: return s1kVar;
 177: case 8:
 178: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 179: case 9:
 180: return ((gh6) u((b55) obj2, (wr4) obj)).w(s1kVar);
 181: case 10:
 182: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 183: case 11:
 184: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 185: case 12:
 186: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 187: case 13:
 188: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 189: case 14:
 190: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 191: case 15:
 192: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 193: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
 194: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 195: case 17:
 196: ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 197: return s1kVar;
 198: case 18:
 199: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 200: case 19:
 201: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 202: case 20:
 203: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 204: case 21:
 205: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 206: case 22:
 207: return ((gh6) u((b55) obj2, (dj9) obj)).w(s1kVar);
 208: case 23:
 209: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 210: case 24:
 211: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 212: case 25:
 213: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 214: case 26:
 215: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 216: case 27:
 217: return ((gh6) u((b55) obj2, (wpe) obj)).w(s1kVar);
 218: case 28:
 219: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 220: default:
 221: return ((gh6) u((b55) obj2, (ja5) obj)).w(s1kVar);
 222: }
 223: }
 224: 
 225: @Override // defpackage.hv0
 226: public final b55 u(b55 b55Var, Object obj) {
 227: byte b = this.e;
 228: Object obj2 = this.g;
 229: switch (b) {
 230: case 0:
 231: gh6 gh6Var = new gh6((lh6) obj2, b55Var, (byte) 0);
 232: gh6Var.h = obj;
 233: return gh6Var;
 234: case 1:
 235: return new gh6(obj2, this.h, b55Var, (byte) 1);
 236: case 2:
 237: return new gh6(obj2, this.h, b55Var, (byte) 2);
 238: case 3:
 239: return new gh6((byte) 3, b55Var, (j37) this.h, (a19) obj2, false);
 240: case 4:
 241: return new gh6((FaqWebViewWidget) obj2, b55Var, (byte) 4);
 242: case 5:
 243: gh6 gh6Var2 = new gh6((FaqWebViewWidget) obj2, b55Var, (byte) 5);
 244: gh6Var2.h = obj;
 245: return gh6Var2;
 246: case 6:
 247: return new gh6((byte) 6, b55Var, (n0b) this.h, (vo2) obj2, false);
 248: case 7:
 249: return new gh6((File) this.h, this.f, (wb7) obj2, b55Var);
 250: case 8:
 251: return new gh6((byte) 8, b55Var, (kc7) this.h, (List) obj2, false);
 252: case 9:
 253: gh6 gh6Var3 = new gh6((se7) obj2, b55Var, (byte) 9);
 254: gh6Var3.h = obj;
 255: return gh6Var3;
 256: case 10:
 257: return new gh6(obj2, this.h, b55Var, (byte) 10);
 258: case 11:
 259: return new gh6((byte) 11, b55Var, (zm7) this.h, (a19) obj2, false);
 260: case 12:
 261: return new gh6((byte) 12, b55Var, (bn7) this.h, (pm7) obj2, false);
 262: case 13:
 263: return new gh6((co7) obj2, b55Var, (byte) 13);
 264: case 14:
 265: return new gh6((byte) 14, b55Var, (tr7) this.h, (String) obj2, false);
 266: case 15:
 267: return new gh6((byte) 15, b55Var, (tb8) this.h, (Bundle) obj2, false);
 268: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
 269: return new gh6((yg8) obj2, b55Var, (byte) 16);
 270: case 17:
 271: return new gh6((gl8) this.h, (jl8) obj2, this.f, b55Var);
 272: case 18:
 273: gh6 gh6Var4 = new gh6((jl8) obj2, b55Var, (byte) 18);
 274: gh6Var4.h = obj;
 275: return gh6Var4;
 276: case 19:
 277: return new gh6((byte) 19, b55Var, (e09) this.h, (z28) obj2, false);
 278: case 20:
 279: return new gh6((byte) 20, b55Var, (s39) this.h, (r39) obj2, false);
 280: case 21:
 281: return new gh6((byte) 21, b55Var, (r6a) this.h, (IntegrityLogsViewerScreen) obj2, false);
 282: case 22:
 283: gh6 gh6Var5 = new gh6((fj9) obj2, b55Var, (byte) 22);
 284: gh6Var5.h = obj;
 285: return gh6Var5;
 286: case 23:
 287: gh6 gh6Var6 = new gh6((ir9) obj2, b55Var, (byte) 23);
 288: gh6Var6.h = obj;
 289: return gh6Var6;
 290: case 24:
 291: return new gh6((byte) 24, b55Var, (vr9) this.h, (r25) obj2, false);
 292: case 25:
 293: return new gh6((byte) 25, b55Var, (pt9) this.h, (ot9) obj2, false);
 294: case 26:
 295: return new gh6((byte) 26, b55Var, (pt9) this.h, (xv0) obj2, false);
 296: case 27:
 297: gh6 gh6Var7 = new gh6((k4a) obj2, b55Var, (byte) 27);
 298: gh6Var7.h = obj;
 299: return gh6Var7;
 300: case 28:
 301: return new gh6((byte) 28, b55Var, (i7a) this.h, (l7a) obj2, false);
 302: default:
 303: return new gh6((byte) 29, b55Var, (baa) this.h, (CharSequence) obj2, false);
 304: }
 305: }
 306: 
 307: /* JADX WARN: Code duplicated, block: B:201:0x0471  */
 308: /* JADX WARN: Code duplicated, block: B:209:0x048f  */
 309: /* JADX WARN: Code duplicated, block: B:211:0x0497  */
 310: /* JADX WARN: Code duplicated, block: B:212:0x0499  */
 311: /* JADX WARN: Code duplicated, block: B:216:0x04a7  */
 312: /* JADX WARN: Code duplicated, block: B:524:0x0502 A[SYNTHETIC] */
 313: /* JADX WARN: Code duplicated, block: B:525:0x04ce A[SYNTHETIC] */
 314: /* JADX WARN: Code duplicated, block: B:526:0x04ca A[SYNTHETIC] */
 315: /* JADX WARN: Code duplicated, block: B:527:0x04a5 A[SYNTHETIC] */
 316: /* JADX WARN: Code duplicated, block: B:528:0x04a3 A[SYNTHETIC] */
 317: /* JADX WARN: Multi-variable type inference failed */
 318: /* JADX WARN: Type inference failed for: r11v0, types: [b55] */
 319: /* JADX WARN: Type inference failed for: r11v53 */
 320: /*  JADX ERROR: JadxRuntimeException in pass: IfRegionVisitor
 321: jadx.core.utils.exceptions.JadxRuntimeException: Can't remove SSA var: r12v15 java.lang.Object, still in use, count: 2, list:
 322: (r12v15 java.lang.Object) from 0x0423: PHI (r12 I:??) = (r12v12 java.lang.Object), (r12v15 java.lang.Object) binds: [B:185:0x0422, B:534:0x0423] A[DONT_GENERATE, DONT_INLINE]
 323: (r12v15 java.lang.Object) from 0x0417: CHECK_CAST (mo7) (r12v15 java.lang.Object)
 324: at jadx.core.utils.InsnRemover.removeSsaVar(InsnRemover.java:164)
 325: at jadx.core.utils.InsnRemover.unbindResult(InsnRemover.java:129)
 326: at jadx.core.utils.InsnRemover.unbindInsn(InsnRemover.java:93)
 327: at jadx.core.dex.visitors.regions.TernaryMod.makeTernaryInsn(TernaryMod.java:132)
 328: at jadx.core.dex.visitors.regions.TernaryMod.processRegion(TernaryMod.java:67)
 329: at jadx.core.dex.visitors.regions.TernaryMod.enterRegion(TernaryMod.java:50)
 330: at jadx.core.dex.visitors.regions.DepthRegionTraversal.traverseInternal(DepthRegionTraversal.java:96)
 331: at jadx.core.dex.visitors.regions.DepthRegionTraversal.traverse(DepthRegionTraversal.java:27)
 332: at jadx.core.dex.visitors.regions.TernaryMod.process(TernaryMod.java:36)
 333: at jadx.core.dex.visitors.regions.IfRegionVisitor.process(IfRegionVisitor.java:44)
 334: at jadx.core.dex.visitors.regions.IfRegionVisitor.visit(IfRegionVisitor.java:30)
 335: */
 336: @Override // defpackage.hv0
 337: public final java.lang.Object w(java.lang.Object r22) throws java.lang.Exception {
 338: /*
 339: Method dump skipped, instruction units count: 3056
 340: To view this dump add '--comments-level debug' option
 341: */
 342: throw new UnsupportedOperationException("Method not decompiled: defpackage.gh6.w(java.lang.Object):java.lang.Object");
 343: }
 344: 
 345: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 346: public /* synthetic */ gh6(byte b, b55 b55Var, Object obj, Object obj2, boolean z) {
 347: super(2, b55Var);
 348: this.e = b;
 349: this.h = obj;
 350: this.g = obj2;
 351: }
 352: 
 353: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 354: public gh6(File file, boolean z, wb7 wb7Var, b55 b55Var) {
 355: super(2, b55Var);
 356: this.e = (byte) 7;
 357: this.h = file;
 358: this.f = z;
 359: this.g = wb7Var;
 360: }
 361: 
 362: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 363: public /* synthetic */ gh6(Object obj, b55 b55Var, byte b) {
 364: super(2, b55Var);
 365: this.e = b;
 366: this.g = obj;
 367: }
 368: 
 369: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
 370: public /* synthetic */ gh6(Object obj, Object obj2, b55 b55Var, byte b) {
 371: super(2, b55Var);
 372: this.e = b;
 373: this.g = obj;
 374: this.h = obj2;
 375: }
 376: }
~~~

## defpackage/er.java (905 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.List;
   4: import one.me.sdk.statistics.perf.utils.MissingMetricNameException;
   5: import one.me.sdk.statistics.perf.utils.PerfListenerException;
   6: 
   7: /* JADX INFO: loaded from: classes.dex */
   8: public final class er extends x1j implements e18 {
   9: public final /* synthetic */ byte e;
  10: public byte f;
  11: public Object g;
  12: public final /* synthetic */ Object h;
  13: 
  14: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  15: public /* synthetic */ er(Object obj, Object obj2, b55 b55Var, byte b) {
  16: super(2, b55Var);
  17: this.e = b;
  18: this.g = obj;
  19: this.h = obj2;
  20: }
  21: 
  22: /* JADX WARN: Code duplicated, block: B:123:0x023d  */
  23: /* JADX WARN: Code duplicated, block: B:125:0x0248  */
  24: /* JADX WARN: Code duplicated, block: B:126:0x025a  */
  25: /* JADX WARN: Code duplicated, block: B:128:0x0260  */
  26: /* JADX WARN: Code duplicated, block: B:131:0x0298  */
  27: /* JADX WARN: Code duplicated, block: B:137:0x02b8  */
  28: /* JADX WARN: Code duplicated, block: B:140:0x02d1  */
  29: /* JADX WARN: Code duplicated, block: B:147:0x02f0  */
  30: /* JADX WARN: Code duplicated, block: B:153:0x0316  */
  31: /* JADX WARN: Code duplicated, block: B:157:0x031f  */
  32: /* JADX WARN: Code duplicated, block: B:166:0x0345  */
  33: /* JADX WARN: Code duplicated, block: B:172:0x0369  */
  34: /* JADX WARN: Code duplicated, block: B:175:0x036f  */
  35: /* JADX WARN: Code duplicated, block: B:176:0x0372  */
  36: /* JADX WARN: Code duplicated, block: B:185:0x03b7  */
  37: /* JADX WARN: Code duplicated, block: B:191:0x03d0  */
  38: /* JADX WARN: Code duplicated, block: B:223:0x0470  */
  39: /* JADX WARN: Code duplicated, block: B:409:0x0321 A[SYNTHETIC] */
  40: /* JADX WARN: Code restructure failed: missing block: B:224:0x0472, code lost:
  41: 
  42: if (r2 == r0) goto L363;
  43: */
  44: /* JADX WARN: Code restructure failed: missing block: B:261:0x053d, code lost:
  45: 
  46: if (r2 == r0) goto L363;
  47: */
  48: /* JADX WARN: Code restructure failed: missing block: B:280:0x0597, code lost:
  49: 
  50: if (r2 == r0) goto L363;
  51: */
  52: /* JADX WARN: Code restructure failed: missing block: B:329:0x06a0, code lost:
  53: 
  54: if (r2 == r0) goto L363;
  55: */
  56: /* JADX WARN: Code restructure failed: missing block: B:362:0x0797, code lost:
  57: 
  58: if (r3.q(r1) == r0) goto L363;
  59: */
  60: /* JADX WARN: Multi-variable type inference failed */
  61: /* JADX WARN: Type inference failed for: r15v13 */
  62: /* JADX WARN: Type inference failed for: r15v6 */
  63: /* JADX WARN: Type inference failed for: r15v7, types: [aul] */
  64: /* JADX WARN: Type inference failed for: r2v27, types: [wud] */
  65: /* JADX WARN: Type inference failed for: r3v58 */
  66: /* JADX WARN: Type inference failed for: r3v59, types: [xsb] */
  67: /* JADX WARN: Type inference failed for: r3v69 */
  68: /* JADX WARN: Type inference failed for: r9v14 */
  69: /* JADX WARN: Type inference failed for: r9v15, types: [java.lang.String, rud] */
  70: /* JADX WARN: Type inference failed for: r9v16 */
  71: /* JADX WARN: Type inference fix 'apply assigned field type' failed
  72: java.lang.UnsupportedOperationException: ArgType.getObject(), call class: class jadx.core.dex.instructions.args.ArgType$UnknownArg
  73: at jadx.core.dex.instructions.args.ArgType.getObject(ArgType.java:596)
  74: at jadx.core.dex.attributes.nodes.ClassTypeVarsAttr.getTypeVarsMapFor(ClassTypeVarsAttr.java:35)
  75: at jadx.core.dex.nodes.utils.TypeUtils.replaceClassGenerics(TypeUtils.java:177)
  76: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.insertExplicitUseCast(FixTypesVisitor.java:397)
  77: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.tryFieldTypeWithNewCasts(FixTypesVisitor.java:359)
  78: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.applyFieldType(FixTypesVisitor.java:309)
  79: at jadx.core.dex.visitors.typeinference.FixTypesVisitor.visit(FixTypesVisitor.java:94)
  80: */
  81: /*
  82: Code decompiled incorrectly, please refer to instructions dump.
  83: */
  84: private final Object y(Object obj) {
  85: s1k s1kVar;
  86: String str;
  87: xsb xsbVar;
  88: x3c x3cVar;
  89: ?? r9;
  90: String str2;
  91: String str3;
  92: kig kigVar;
  93: long j;
  94: boolean zB;
  95: String str4;
  96: xsb xsbVarY;
  97: e4c e4cVar;
  98: e4c e4cVar2;
  99: Object[] objArr;
 100: int i;
 101: int i2;
 102: e4c e4cVar3;
 103: Object n4gVar;
 104: Throwable thA;
 105: e4c e4cVar4;
 106: Object obj2;
 107: String str5;
 108: o1d o1dVar;
 109: String str6;
 110: xsb xsbVar2;
 111: String str7;
 112: o1d o1dVar2;
 113: String name;
 114: String str8;
 115: PerfListenerException perfListenerException;
 116: o1d o1dVar3;
 117: wtd wtdVar;
 118: Object obj3;
 119: Object n4gVar2;
 120: Throwable thA2;
 121: int i3;
 122: int i4;
 123: String name2;
 124: String str9;
 125: PerfListenerException perfListenerException2;
 126: o1d o1dVar4;
 127: String str10;
 128: String str11;
 129: o1d o1dVar5;
 130: Object objD;
 131: ?? r15;
 132: ?? Y;
 133: aul aulVar;
 134: er erVar = this;
 135: c6a c6aVar = c6a.d;
 136: s1k s1kVar2 = s1k.a;
 137: c6a c6aVar2 = c6a.c;
 138: c6a c6aVar3 = c6a.f;
 139: ptd ptdVar = (ptd) erVar.g;
 140: ka5 ka5Var = ka5.a;
 141: byte b = erVar.f;
 142: if (b == 0) {
 143: xnm.y(obj);
 144: wud wudVar = (wud) erVar.h;
 145: boolean z = ptdVar instanceof aul;
 146: aul aulVar2 = z ? (aul) ptdVar : null;
 147: String strA = aulVar2 != null ? aulVar2.a() : null;
 148: xsb xsbVarY2 = strA != null ? f09.y(wudVar.c, strA) : null;
 149: String str12 = wudVar.b;
 150: if (xsbVarY2 != null) {
 151: o1d o1dVar6 = f09.g;
 152: if (o1dVar6 != null && o1dVar6.b(c6aVar)) {
 153: o1dVar6.c(c6aVar, str12, pq0.j(wud.y(xsbVarY2), ": ", String.valueOf(ptdVar)), null);
 154: }
 155: } else {
 156: o1d o1dVar7 = f09.g;
 157: if (o1dVar7 != null && o1dVar7.b(c6aVar)) {
 158: o1dVar7.c(c6aVar, str12, pq0.j(wudVar.z(strA), ": ", String.valueOf(ptdVar)), null);
 159: }
 160: }
 161: if (ptdVar instanceof wtl) {
 162: wud wudVar2 = (wud) erVar.h;
 163: aul aulVar3 = z ? (aul) ptdVar : null;
 164: String strA2 = aulVar3 != null ? aulVar3.a() : null;
 165: xsb xsbVarY3 = strA2 != null ? f09.y(wudVar2.c, strA2) : null;
 166: String str13 = wudVar2.b;
 167: if (xsbVarY3 != null) {
 168: o1d o1dVar8 = f09.g;
 169: if (o1dVar8 != null && o1dVar8.b(c6aVar2)) {
 170: o1dVar8.c(c6aVar2, str13, wud.y(xsbVarY3).concat(": Adding local properties"), null);
 171: }
 172: } else {
 173: o1d o1dVar9 = f09.g;
 174: if (o1dVar9 != null && o1dVar9.b(c6aVar2)) {
 175: o1dVar9.c(c6aVar2, str13, wudVar2.z(strA2).concat(": Adding local properties"), null);
 176: }
 177: }
 178: e4c e4cVar5 = ((wud) erVar.h).c;
 179: String strA3 = ((aul) ptdVar).a();
 180: kig kigVarC = ((wtl) ptdVar).c();
 181: xsb xsbVar3 = (xsb) e4cVar5.d(new lmj(strA3));
 182: if (xsbVar3 == null) {
 183: String str14 = h09.a;
 184: o1d o1dVar10 = f09.g;
 185: if (o1dVar10 != null && o1dVar10.b(c6aVar3)) {
 186: o1dVar10.c(c6aVar3, str14, "No metric for such traceId->".concat(lmj.a(strA3)), null);
 187: }
 188: } else {
 189: xsbVar3.g.l(kigVarC);
 190: }
 191: }
 192: if (ptdVar instanceof ytl) {
 193: wud wudVar3 = (wud) erVar.h;
 194: aul aulVar4 = z ? (aul) ptdVar : null;
 195: String strA4 = aulVar4 != null ? aulVar4.a() : null;
 196: xsb xsbVarY4 = strA4 != null ? f09.y(wudVar3.c, strA4) : null;
 197: String str15 = wudVar3.b;
 198: if (xsbVarY4 != null) {
 199: o1d o1dVar11 = f09.g;
 200: if (o1dVar11 != null && o1dVar11.b(c6aVar2)) {
 201: o1dVar11.c(c6aVar2, str15, wud.y(xsbVarY4).concat(": Clearing previous timeout jobs"), null);
 202: }
 203: } else {
 204: o1d o1dVar12 = f09.g;
 205: if (o1dVar12 != null && o1dVar12.b(c6aVar2)) {
 206: o1dVar12.c(c6aVar2, str15, wudVar3.z(strA4).concat(": Clearing previous timeout jobs"), null);
 207: }
 208: }
 209: aul aulVar5 = (aul) ptdVar;
 210: kf9 kf9Var = (kf9) ((wud) erVar.h).d.m(new lmj(aulVar5.a()));
 211: if (kf9Var != null) {
 212: kf9Var.m(null);
 213: }
 214: ((wud) erVar.h).i(aulVar5.a());
 215: }
 216: if (ptdVar instanceof ntd) {
 217: wud wudVar4 = (wud) erVar.h;
 218: ntd ntdVar = (ntd) ptdVar;
 219: e4c e4cVar6 = wudVar4.c;
 220: fk3 fk3Var = wudVar4.a.c;
 221: if (fk3Var instanceof ytd) {
 222: str2 = (String) va4.K0((List) fk3Var.b);
 223: } else {
 224: if (!(fk3Var instanceof xtd)) {
 225: k3g.l();
 226: return null;
 227: }
 228: String str16 = ntdVar.d;
 229: if (str16 != null) {
 230: s1kVar2 = s1kVar2;
 231: c6aVar2 = c6aVar2;
 232: str3 = str16;
 233: } else {
 234: str2 = (String) va4.K0((List) fk3Var.b);
 235: String str17 = ntdVar.a;
 236: MissingMetricNameException missingMetricNameException = new MissingMetricNameException(wudVar4.p(), str2);
 237: String str18 = wudVar4.b;
 238: o1d o1dVar13 = f09.g;
 239: if (o1dVar13 != null && o1dVar13.b(c6aVar3)) {
 240: o1dVar13.c(c6aVar3, str18, pq0.j(wudVar4.z(str17), ": ", vg9.y("Multi-metric registrar started without explicit name, falling back to '", str2, "'")), missingMetricNameException);
 241: }
 242: str3 = str2;
 243: }
 244: kigVar = ntdVar.b;
 245: j = ntdVar.c;
 246: zB = e4cVar6.b(new lmj(ntdVar.a));
 247: str4 = ntdVar.a;
 248: if (zB) {
 249: objD = e4cVar6.d(new lmj(str4));
 250: if (objD != null) {
 251: k3g.t("Required value was null.");
 252: return null;
 253: }
 254: xsb xsbVar4 = (xsb) objD;
 255: xsbVar4.f.b(new rxh(j));
 256: xsbVar4.g.l(kigVar);
 257: } else {
 258: lmj lmjVar = new lmj(str4);
 259: x3c x3cVarC = inc.c(new rxh(j));
 260: e4c e4cVar7 = new e4c(kigVar.e);
 261: e4cVar7.l(kigVar);
 262: qzd qzdVar = fe6.b;
 263: e4cVar6.o(lmjVar, new xsb(str3, str4, 0L, 0L, false, x3cVarC, e4cVar7));
 264: }
 265: xsbVarY = f09.y(wudVar4.c, ntdVar.a);
 266: if (xsbVarY == null) {
 267: str10 = ntdVar.a;
 268: str11 = wudVar4.b;
 269: o1dVar5 = f09.g;
 270: if (o1dVar5 != null && o1dVar5.b(c6aVar3)) {
 271: o1dVar5.c(c6aVar3, str11, wudVar4.z(str10).concat(": handleStartMetric: metric not found in storage right after start, skipping"), null);
 272: }
 273: } else {
 274: long[] jArr = lig.a;
 275: e4cVar = new e4c();
 276: e4cVar2 = new e4c();
 277: objArr = wudVar4.a.e.a;
 278: i2 = 0;
 279: for (i = r0.b; i2 < i; i = i3) {
 280: Object[] objArr2 = objArr;
 281: wtdVar = (wtd) objArr[i2];
 282: obj3 = lig.b;
 283: try {
 284: n4gVar2 = wtdVar.d(xsbVarY);
 285: } catch (Throwable th) {
 286: n4gVar2 = new n4g(th);
 287: }
 288: thA2 = p4g.a(n4gVar2);
 289: if (thA2 != null) {
 290: i3 = i;
 291: name2 = wtdVar.getClass().getName();
 292: i4 = i2;
 293: str9 = wudVar4.b;
 294: perfListenerException2 = new PerfListenerException(name2, thA2);
 295: o1dVar4 = f09.g;
 296: if (o1dVar4 != null && o1dVar4.b(c6aVar3)) {
 297: o1dVar4.c(c6aVar3, str9, "PerfListener callback failed, listener=".concat(name2), perfListenerException2);
 298: }
 299: } else {
 300: i3 = i;
 301: i4 = i2;
 302: }
 303: if (n4gVar2 instanceof n4g) {
 304: obj3 = n4gVar2;
 305: }
 306: e4cVar2.l((kig) obj3);
 307: i2 = i4 + 1;
 308: objArr = objArr2;
 309: }
 310: e4cVar3 = lig.b;
 311: try {
 312: n4gVar = wudVar4.d(xsbVarY);
 313: } catch (Throwable th2) {
 314: n4gVar = new n4g(th2);
 315: }
 316: thA = p4g.a(n4gVar);
 317: if (thA != null) {
 318: name = wudVar4.getClass().getName();
 319: str8 = wudVar4.b;
 320: e4cVar4 = e4cVar3;
 321: perfListenerException = new PerfListenerException(name, thA);
 322: o1dVar3 = f09.g;
 323: if (o1dVar3 != null && o1dVar3.b(c6aVar3)) {
 324: o1dVar3.c(c6aVar3, str8, "PerfListener callback failed, listener=".concat(name), perfListenerException);
 325: }
 326: } else {
 327: e4cVar4 = e4cVar3;
 328: }
 329: if (n4gVar instanceof n4g) {
 330: obj2 = e4cVar4;
 331: } else {
 332: obj2 = n4gVar;
 333: }
 334: e4cVar2.l((kig) obj2);
 335: e4cVar.l(e4cVar2);
 336: e4cVar.l(xsbVarY.g);
 337: str5 = wudVar4.b;
 338: o1dVar = f09.g;
 339: if (o1dVar != null && o1dVar.b(c6aVar)) {
 340: o1dVar.c(c6aVar, str5, pq0.j(wud.y(xsbVarY), ": ", "Local props in start of collect -> " + e4cVar), null);
 341: }
 342: e4c e4cVar8 = wudVar4.c;
 343: str6 = ntdVar.a;
 344: xsbVar2 = (xsb) e4cVar8.d(new lmj(str6));
 345: if (xsbVar2 == null) {
 346: str7 = h09.a;
 347: o1dVar2 = f09.g;
 348: if (o1dVar2 != null && o1dVar2.b(c6aVar3)) {
 349: o1dVar2.c(c6aVar3, str7, "No metric for such traceId->".concat(lmj.a(str6)), null);
 350: }
 351: } else {
 352: xsbVar2.g.g();
 353: xsbVar2.g.l(e4cVar);
 354: }
 355: }
 356: erVar = this;
 357: }
 358: str3 = str2;
 359: kigVar = ntdVar.b;
 360: j = ntdVar.c;
 361: zB = e4cVar6.b(new lmj(ntdVar.a));
 362: str4 = ntdVar.a;
 363: if (zB) {
 364: objD = e4cVar6.d(new lmj(str4));
 365: if (objD != null) {
 366: k3g.t("Required value was null.");
 367: return null;
 368: }
 369: xsb xsbVar5 = (xsb) objD;
 370: xsbVar5.f.b(new rxh(j));
 371: xsbVar5.g.l(kigVar);
 372: } else {
 373: lmj lmjVar2 = new lmj(str4);
 374: x3c x3cVarC2 = inc.c(new rxh(j));
 375: e4c e4cVar9 = new e4c(kigVar.e);
 376: e4cVar9.l(kigVar);
 377: qzd qzdVar2 = fe6.b;
 378: e4cVar6.o(lmjVar2, new xsb(str3, str4, 0L, 0L, false, x3cVarC2, e4cVar9));
 379: }
 380: xsbVarY = f09.y(wudVar4.c, ntdVar.a);
 381: if (xsbVarY == null) {
 382: str10 = ntdVar.a;
 383: str11 = wudVar4.b;
 384: o1dVar5 = f09.g;
 385: if (o1dVar5 != null) {
 386: o1dVar5.c(c6aVar3, str11, wudVar4.z(str10).concat(": handleStartMetric: metric not found in storage right after start, skipping"), null);
 387: }
 388: } else {
 389: long[] jArr2 = lig.a;
 390: e4cVar = new e4c();
 391: e4cVar2 = new e4c();
 392: objArr = wudVar4.a.e.a;
 393: i2 = 0;
 394: while (i2 < i) {
 395: Object[] objArr3 = objArr;
 396: wtdVar = (wtd) objArr[i2];
 397: obj3 = lig.b;
 398: n4gVar2 = wtdVar.d(xsbVarY);
 399: thA2 = p4g.a(n4gVar2);
 400: if (thA2 != null) {
 401: i3 = i;
 402: name2 = wtdVar.getClass().getName();
 403: i4 = i2;
 404: str9 = wudVar4.b;
 405: perfListenerException2 = new PerfListenerException(name2, thA2);
 406: o1dVar4 = f09.g;
 407: if (o1dVar4 != null) {
 408: o1dVar4.c(c6aVar3, str9, "PerfListener callback failed, listener=".concat(name2), perfListenerException2);
 409: }
 410: } else {
 411: i3 = i;
 412: i4 = i2;
 413: }
 414: if (n4gVar2 instanceof n4g) {
 415: obj3 = n4gVar2;
 416: }
 417: e4cVar2.l((kig) obj3);
 418: i2 = i4 + 1;
 419: objArr = objArr3;
 420: }
 421: e4cVar3 = lig.b;
 422: n4gVar = wudVar4.d(xsbVarY);
 423: thA = p4g.a(n4gVar);
 424: if (thA != null) {
 425: name = wudVar4.getClass().getName();
 426: str8 = wudVar4.b;
 427: e4cVar4 = e4cVar3;
 428: perfListenerException = new PerfListenerException(name, thA);
 429: o1dVar3 = f09.g;
 430: if (o1dVar3 != null) {
 431: o1dVar3.c(c6aVar3, str8, "PerfListener callback failed, listener=".concat(name), perfListenerException);
 432: }
 433: } else {
 434: e4cVar4 = e4cVar3;
 435: }
 436: if (n4gVar instanceof n4g) {
 437: obj2 = e4cVar4;
 438: } else {
 439: obj2 = n4gVar;
 440: }
 441: e4cVar2.l((kig) obj2);
 442: e4cVar.l(e4cVar2);
 443: e4cVar.l(xsbVarY.g);
 444: str5 = wudVar4.b;
 445: o1dVar = f09.g;
 446: if (o1dVar != null) {
 447: o1dVar.c(c6aVar, str5, pq0.j(wud.y(xsbVarY), ": ", "Local props in start of collect -> " + e4cVar), null);
 448: }
 449: e4c e4cVar10 = wudVar4.c;
 450: str6 = ntdVar.a;
 451: xsbVar2 = (xsb) e4cVar10.d(new lmj(str6));
 452: if (xsbVar2 == null) {
 453: str7 = h09.a;
 454: o1dVar2 = f09.g;
 455: if (o1dVar2 != null) {
 456: o1dVar2.c(c6aVar3, str7, "No metric for such traceId->".concat(lmj.a(str6)), null);
 457: }
 458: } else {
 459: xsbVar2.g.g();
 460: xsbVar2.g.l(e4cVar);
 461: }
 462: }
 463: erVar = this;
 464: } else {
 465: s1kVar2 = s1kVar2;
 466: c6aVar2 = c6aVar2;
 467: if (ptdVar instanceof ctd) {
 468: erVar = this;
 469: ?? r2 = (wud) erVar.h;
 470: ctd ctdVar = (ctd) ptdVar;
 471: erVar.g = ptdVar;
 472: erVar.f = (byte) 1;
 473: e4c e4cVar11 = r2.c;
 474: String str19 = ctdVar.a;
 475: xsb xsbVar6 = (xsb) e4cVar11.d(new lmj(str19));
 476: if (xsbVar6 == null) {
 477: String str20 = h09.a;
 478: o1d o1dVar14 = f09.g;
 479: if (o1dVar14 != null && o1dVar14.b(c6aVar3)) {
 480: o1dVar14.c(c6aVar3, str20, "No metric for such traceId->".concat(lmj.a(str19)), null);
 481: }
 482: } else {
 483: xsbVar6.f.b(new nxh(ctdVar.c, ctdVar.d, ctdVar.e, ctdVar.g));
 484: }
 485: if (f09.y(r2.c, ctdVar.a) != null) {
 486: r2.t();
 487: } else {
 488: String str21 = ctdVar.a;
 489: String str22 = r2.b;
 490: o1d o1dVar15 = f09.g;
 491: if (o1dVar15 != null && o1dVar15.b(c6aVar3)) {
 492: r9 = 0;
 493: o1dVar15.c(c6aVar3, str22, r2.z(str21).concat(": handleSpan: metric not found in storage, listeners not notified"), null);
 494: }
 495: if (ctdVar.f \|\| (objO = r2.o(ctdVar.a, r9, r9, erVar)) != ka5Var) {
 496: Object objO = s1kVar2;
 497: }
 498: }
 499: r9 = 0;
 500: if (ctdVar.f) {
 501: Object objO2 = s1kVar2;
 502: } else {
 503: Object objO3 = s1kVar2;
 504: }
 505: } else {
 506: erVar = this;
 507: if (ptdVar instanceof btd) {
 508: wud wudVar5 = (wud) erVar.h;
 509: btd btdVar = (btd) ptdVar;
 510: e4c e4cVar12 = wudVar5.c;
 511: String str23 = btdVar.a;
 512: long j2 = btdVar.c;
 513: xsb xsbVar7 = (xsb) e4cVar12.d(new lmj(str23));
 514: if (xsbVar7 == null) {
 515: String str24 = h09.a;
 516: o1d o1dVar16 = f09.g;
 517: if (o1dVar16 != null && o1dVar16.b(c6aVar3)) {
 518: o1dVar16.c(c6aVar3, str24, "No metric for such traceId->".concat(lmj.a(str23)), null);
 519: }
 520: } else {
 521: xsbVar7.f.b(new pxh(j2));
 522: }
 523: if (f09.y(wudVar5.c, btdVar.a) != null) {
 524: wudVar5.t();
 525: } else {
 526: String str25 = btdVar.a;
 527: String str26 = wudVar5.b;
 528: o1d o1dVar17 = f09.g;
 529: if (o1dVar17 != null && o1dVar17.b(c6aVar3)) {
 530: o1dVar17.c(c6aVar3, str26, wudVar5.z(str25).concat(": handleRetryBoundary: metric not found in storage, listeners not notified"), null);
~~~

Поздние сигнатуры: 776 public final Object invoke(Object obj, Object obj2) throws Throwable {; 815 public final b55 u(b55 b55Var, Object obj) {; 891 public final java.lang.Object w(java.lang.Object r28) throws java.lang.Throwable {

## defpackage/e7a.java (29 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class e7a extends d55 {
   5: public long d;
   6: public long e;
   7: public String f;
   8: public b7a g;
   9: public int h;
  10: public int i;
  11: public boolean j;
  12: public boolean k;
  13: public /* synthetic */ Object l;
  14: public final /* synthetic */ g7a m;
  15: public int n;
  16: 
  17: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  18: public e7a(g7a g7aVar, d55 d55Var) {
  19: super(d55Var);
  20: this.m = g7aVar;
  21: }
  22: 
  23: @Override // defpackage.hv0
  24: public final Object w(Object obj) {
  25: this.l = obj;
  26: this.n \|= Integer.MIN_VALUE;
  27: return this.m.a(0L, null, 0, null, false, false, this);
  28: }
  29: }
~~~

## defpackage/z7a.java (8 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public abstract class z7a extends yt6 {
   5: public z7a(Throwable th) {
   6: super(s1k.a, th);
   7: }
   8: }
~~~

## defpackage/e9a.java (13 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class e9a extends fk3 {
   5: public static final e9a c;
   6: public static final dn5 d;
   7: 
   8: static {
   9: e9a e9aVar = new e9a((byte) 2);
  10: c = e9aVar;
  11: d = fk3.e(e9aVar, ":logout", new String[0], kwm.d, 10);
  12: }
  13: }
~~~

## defpackage/k6a.java (37 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes3.dex */
   4: public final class k6a {
   5: public final int a;
   6: public final long b;
   7: public final long c;
   8: public final long d;
   9: 
  10: public k6a(int i, long j, long j2, long j3) {
  11: this.a = i;
  12: this.b = j;
  13: this.c = j2;
  14: this.d = j3;
  15: }
  16: 
  17: public final boolean equals(Object obj) {
  18: if (this == obj) {
  19: return true;
  20: }
  21: if (!(obj instanceof k6a)) {
  22: return false;
  23: }
  24: k6a k6aVar = (k6a) obj;
  25: return this.a == k6aVar.a && this.b == k6aVar.b && this.c == k6aVar.c && this.d == k6aVar.d;
  26: }
  27: 
  28: public final int hashCode() {
  29: return Long.hashCode(this.d) + s95.h(s95.h(Integer.hashCode(this.a) * 31, 31, this.b), 31, this.c);
  30: }
  31: 
  32: public final String toString() {
  33: StringBuilder sbS = a15.s(this.a, this.b, "ThrottleInfo(count=", ", totalIntervalMs=");
  34: s95.B(this.c, ", intervalMinMs=", ", intervalMaxMs=", sbS);
  35: return vg9.x(this.d, ")", sbS);
  36: }
  37: }
~~~

## defpackage/d5h.java (15 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class d5h extends u6j {
   5: @Override // defpackage.u6j
   6: public final short k() {
   7: cp5 cp5Var = tdd.c;
   8: return (short) 6;
   9: }
  10: 
  11: @Override // defpackage.u6j
  12: public final boolean o() {
  13: return false;
  14: }
  15: }
~~~

## defpackage/acc.java (1285 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.io.IOException;
   4: import java.util.ArrayList;
   5: import java.util.Collections;
   6: import java.util.Iterator;
   7: import java.util.List;
   8: import java.util.Locale;
   9: import java.util.Map;
  10: import java.util.concurrent.atomic.AtomicInteger;
  11: import me.leolin.shortcutbadger.BuildConfig;
  12: import net.jpountz.lz4.LZ4Exception;
  13: import ru.ok.tamtam.api.CorruptedInputDataException;
  14: import ru.ok.tamtam.api.SessionSenderUnexpectedException;
  15: import ru.ok.tamtam.api.UnknownOpcodeException;
  16: import ru.ok.tamtam.internal.MalformedPacketException;
  17: 
  18: /* JADX INFO: loaded from: classes.dex */
  19: public final class acc implements Runnable {
  20: public final /* synthetic */ byte a;
  21: public final /* synthetic */ bcc b;
  22: 
  23: public /* synthetic */ acc(bcc bccVar, byte b) {
  24: this.a = b;
  25: this.b = bccVar;
  26: }
  27: 
  28: public boolean a(fld fldVar) {
  29: bcc bccVar = this.b;
  30: if (bccVar.c.get() != 2 && !bccVar.d(fldVar, k7a.class)) {
  31: return false;
  32: }
  33: fldVar.b.c.f(new l6j("session.state", "session is in logged in state or login already in progress", null));
  34: return true;
  35: }
  36: 
  37: /* JADX WARN: Code duplicated, block: B:91:0x0271 A[Catch: all -> 0x0265, Exception -> 0x0268, IOException -> 0x026d, TRY_ENTER, TRY_LEAVE, TryCatch #2 {all -> 0x0265, blocks: (B:81:0x0231, B:83:0x0237, B:91:0x0271, B:92:0x0273, B:96:0x0293, B:98:0x02c7, B:107:0x0304, B:109:0x0327, B:113:0x034f, B:112:0x032d, B:114:0x0374), top: B:135:0x0
  38: /* JADX WARN: Code duplicated, block: B:94:0x0291  */
  39: /* JADX WARN: Code duplicated, block: B:95:0x0292  */
  40: public void b() {
  41: cld cldVar;
  42: eld eldVar;
  43: short s;
  44: short s2;
  45: short s3;
  46: eld eldVar2;
  47: u6j u6jVar;
  48: u6j u6jVar2;
  49: if (!this.b.l() \|\| this.b.v.isEmpty()) {
  50: return;
  51: }
  52: ArrayList arrayList = new ArrayList();
  53: AtomicInteger atomicInteger = new AtomicInteger();
  54: for (fld fldVar : this.b.v) {
  55: if (!this.b.l() \|\| this.b.k()) {
  56: f09.d0(this.b.a, "packet_sender, detect INACTIVE session or has NO connection", new Object[0]);
  57: break;
  58: }
  59: int i = fldVar.a;
  60: byte b = 2;
  61: if (i == 1 && (eldVar = fldVar.b) != null) {
  62: u6j u6jVar3 = eldVar.a;
  63: boolean z = u6jVar3 instanceof k7a;
  64: boolean z2 = u6jVar3 instanceof d9a;
  65: boolean z3 = u6jVar3 instanceof d5h;
  66: int iP = u6jVar3.p();
  67: cld cldVarA = null;
  68: if (iP == -1 \|\| iP == this.b.l.get()) {
  69: if (!z && !z2) {
  70: bcc bccVar = this.b;
  71: Iterator it = bccVar.v.iterator();
  72: while (true) {
  73: if (it.hasNext()) {
  74: eld eldVar3 = ((fld) it.next()).b;
  75: if (eldVar3 == null \|\| (u6jVar2 = eldVar3.a) == null \|\| !(u6jVar2 instanceof d9a)) {
  76: }
  77: } else {
  78: Iterator it2 = bccVar.u.entrySet().iterator();
  79: while (true) {
  80: if (it2.hasNext()) {
  81: eld eldVar4 = ((dld) ((Map.Entry) it2.next()).getValue()).b.b;
  82: if (eldVar4 == null \|\| (u6jVar = eldVar4.a) == null \|\| !(u6jVar instanceof d9a)) {
  83: }
  84: }
  85: }
  86: }
  87: f09.p(this.b.a, "Skipping " + fldVar.b.a.getClass().getName() + " because logout task in queue");
  88: }
  89: }
  90: if (fldVar.b.a.o() && this.b.c.get() != 2) {
  91: short sK = fldVar.b.a.k();
  92: cp5 cp5Var = tdd.c;
  93: if (sK != 5) {
  94: f09.p(this.b.a, "Skipping " + fldVar.b.a.getClass().getName() + " because need login");
  95: }
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
 106: }
 107: if (fldVar.e) {
 108: f09.d0(this.b.a, "packet_sender: task %s is cancelled", fldVar.b.a);
 109: } else {
 110: long jK = fe6.k(fldVar.c) - System.currentTimeMillis();
 111: bcc bccVar3 = this.b;
 112: if (jK > 0) {
 113: String str = bccVar3.a;
 114: o1d o1dVar = f09.g;
 115: if (o1dVar != null) {
 116: c6a c6aVar = c6a.d;
 117: if (o1dVar.b(c6aVar)) {
 118: vg9.J(vg9.B(jK, "Skipping ", fldVar.b.a.getClass().getName(), " because to early for queue, left "), "ms", o1dVar, c6aVar, str);
 119: }
 120: }
 121: } else {
 122: AtomicInteger atomicInteger2 = bccVar3.b;
 123: atomicInteger2.incrementAndGet();
 124: short sShortValue = atomicInteger2.shortValue();
 125: if (z) {
 126: try {
 127: try {
 128: try {
 129: if (a(fldVar)) {
 130: f09.d0(this.b.a, "Skipping " + fldVar.b.a.getClass().getName() + " because already login", new Object[0]);
 131: } else {
 132: try {
 133: dld dldVar = new dld(fldVar.b.c, fldVar, System.currentTimeMillis());
 134: this.b.u.put(Short.valueOf(sShortValue), dldVar);
 135: eldVar2 = fldVar.b;
 136: u6j u6jVar4 = eldVar2.a;
 137: if (eldVar2.b) {
 138: b = 0;
 139: }
 140: cldVarA = cld.a(u6jVar4, b, (short) 0);
 141: this.b.p.getClass();
 142: byte[] bArrC = cldVarA.c(sShortValue);
 143: s2 = sShortValue;
 144: try {
 145: this.b.n(l5a.c, fldVar.b.c.p(), s2, fldVar.b.a.k(), true, fldVar.b.a.toString(), null, bArrC.length);
 146: atomicInteger.set(this.b.l.get());
 147: this.b.K.b(bArrC);
 148: dldVar.d = bArrC.length;
 149: this.b.s.p.obtainMessage(3, fldVar.b.a.k(), bArrC.length).sendToTarget();
 150: } catch (IOException e) {
 151: e = e;
 152: s = s2;
 153: short s4 = s;
 154: this.b.m(l5a.d, fldVar.b.c.p(), s4, fldVar.b.a.k(), true, e.getMessage());
 155: fldVar.b.c.f(new g6j("send_io"));
 156: this.b.u.remove(Short.valueOf(s4));
 157: this.b.j(atomicInteger.get());
 158: this.b.s(e, false);
 159: arrayList.add(fldVar);
 160: this.b.v.removeAll(arrayList);
 161: arrayList.clear();
 162: } catch (Exception e2) {
 163: e = e2;
 164: this.b.m(l5a.d, fldVar.b.c.p(), s2, fldVar.b.a.k(), true, e.getMessage());
 165: s3 = s2;
 166: if (e instanceof ArrayIndexOutOfBoundsException) {
 167: f09.e0(this.b.a, e, "exception in LZ4, packet = " + e1n.c(cldVarA.b(s3), 0), new Object[0]);
 168: } else {
 169: f09.e0(this.b.a, e, "exception in LZ4, packet = " + e1n.c(cldVarA.b(s3), 0), new Object[0]);
 170: }
 171: fldVar.b.c.f(new g6j("send_error"));
 172: this.b.u.remove(Short.valueOf(s3));
 173: this.b.s(new SessionSenderUnexpectedException(e), false);
 174: }
 175: } catch (IOException e3) {
 176: e = e3;
 177: s2 = sShortValue;
 178: }
 179: }
 180: } catch (Throwable th) {
 181: arrayList.add(fldVar);
 182: throw th;
 183: }
 184: } catch (Exception e4) {
 185: e = e4;
 186: s2 = sShortValue;
 187: this.b.m(l5a.d, fldVar.b.c.p(), s2, fldVar.b.a.k(), true, e.getMessage());
 188: s3 = s2;
 189: if (((e instanceof ArrayIndexOutOfBoundsException) \|\| (e instanceof LZ4Exception)) && cldVarA != null) {
 190: f09.e0(this.b.a, e, "exception in LZ4, packet = " + e1n.c(cldVarA.b(s3), 0), new Object[0]);
 191: }
 192: fldVar.b.c.f(new g6j("send_error"));
 193: this.b.u.remove(Short.valueOf(s3));
 194: this.b.s(new SessionSenderUnexpectedException(e), false);
 195: arrayList.add(fldVar);
 196: }
 197: } catch (IOException e5) {
 198: e = e5;
 199: s = sShortValue;
 200: short s5 = s;
 201: this.b.m(l5a.d, fldVar.b.c.p(), s5, fldVar.b.a.k(), true, e.getMessage());
 202: fldVar.b.c.f(new g6j("send_io"));
 203: this.b.u.remove(Short.valueOf(s5));
 204: this.b.j(atomicInteger.get());
 205: this.b.s(e, false);
 206: arrayList.add(fldVar);
 207: this.b.v.removeAll(arrayList);
 208: arrayList.clear();
 209: }
 210: } else {
 211: dld dldVar2 = new dld(fldVar.b.c, fldVar, System.currentTimeMillis());
 212: this.b.u.put(Short.valueOf(sShortValue), dldVar2);
 213: eldVar2 = fldVar.b;
 214: u6j u6jVar5 = eldVar2.a;
 215: if (eldVar2.b) {
 216: b = 0;
 217: }
 218: cldVarA = cld.a(u6jVar5, b, (short) 0);
 219: this.b.p.getClass();
 220: byte[] bArrC2 = cldVarA.c(sShortValue);
 221: s2 = sShortValue;
 222: this.b.n(l5a.c, fldVar.b.c.p(), s2, fldVar.b.a.k(), true, fldVar.b.a.toString(), null, bArrC2.length);
 223: atomicInteger.set(this.b.l.get());
 224: this.b.K.b(bArrC2);
 225: dldVar2.d = bArrC2.length;
 226: this.b.s.p.obtainMessage(3, fldVar.b.a.k(), bArrC2.length).sendToTarget();
 227: }
 228: arrayList.add(fldVar);
 229: }
 230: }
 231: } else {
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
 242: this.b.m(l5a.e, 0L, cldVar.c, cldVar.d, true, BuildConfig.FLAVOR);
 243: atomicInteger.set(this.b.l.get());
 244: bcc bccVar4 = this.b;
 245: cld cldVar2 = fldVar.d;
 246: bccVar4.K.b(cldVar2.b(cldVar2.c));
 247: } catch (IOException e6) {
 248: bcc bccVar5 = this.b;
 249: l5a l5aVar = l5a.d;
 250: cld cldVar3 = fldVar.d;
 251: bccVar5.m(l5aVar, 0L, cldVar3.c, cldVar3.d, true, e6.getMessage());
 252: this.b.j(atomicInteger.get());
 253: this.b.s(e6, false);
 254: }
 255: arrayList.add(fldVar);
 256: } catch (Throwable th2) {
 257: arrayList.add(fldVar);
 258: throw th2;
 259: }
 260: }
~~~

Поздние сигнатуры: 279 public void c(byte[] bArr, cld cldVar, e6j e6jVar) throws Throwable {; 1028 public void d() throws Throwable {; 1195 public final void run() {

## defpackage/n4a.java (73 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.io.Serializable;
   4: 
   5: /* JADX INFO: loaded from: classes3.dex */
   6: public final class n4a implements Serializable {
   7: public static final n4a g = new n4a(1.401298464324817E-45d, 1.401298464324817E-45d, 0.0d, 0.0f, 0.0f, 0.0f);
   8: public final double a;
   9: public final double b;
  10: public final double c;
  11: public final float d;
  12: public final float e;
  13: public final float f;
  14: 
  15: public n4a(double d, double d2) {
  16: this.a = d;
  17: this.b = d2;
  18: this.c = 0.0d;
  19: this.d = 0.0f;
  20: this.e = 0.0f;
  21: this.f = 0.0f;
  22: }
  23: 
  24: public final boolean equals(Object obj) {
  25: if (this == obj) {
  26: return true;
  27: }
  28: if (obj != null && n4a.class == obj.getClass()) {
  29: n4a n4aVar = (n4a) obj;
  30: if (Double.compare(n4aVar.a, this.a) == 0 && Double.compare(n4aVar.b, this.b) == 0 && Double.compare(n4aVar.c, this.c) == 0 && Float.compare(n4aVar.d, this.d) == 0 && Float.compare(n4aVar.e, this.e) == 0 && Float.compare(n4aVar.f, this.f) == 0) {
  31: return true;
  32: }
  33: }
  34: return false;
  35: }
  36: 
  37: public final int hashCode() {
  38: long jDoubleToLongBits = Double.doubleToLongBits(this.a);
  39: long jDoubleToLongBits2 = Double.doubleToLongBits(this.b);
  40: int i = (((int) (jDoubleToLongBits ^ (jDoubleToLongBits >>> 32))) * 31) + ((int) (jDoubleToLongBits2 ^ (jDoubleToLongBits2 >>> 32)));
  41: long jDoubleToLongBits3 = Double.doubleToLongBits(this.c);
  42: int i2 = ((i * 31) + ((int) ((jDoubleToLongBits3 >>> 32) ^ jDoubleToLongBits3))) * 31;
  43: float f = this.d;
  44: int iFloatToIntBits = (i2 + (f != 0.0f ? Float.floatToIntBits(f) : 0)) * 31;
  45: float f2 = this.e;
  46: int iFloatToIntBits2 = (iFloatToIntBits + (f2 != 0.0f ? Float.floatToIntBits(f2) : 0)) * 31;
  47: float f3 = this.f;
  48: return iFloatToIntBits2 + (f3 != 0.0f ? Float.floatToIntBits(f3) : 0);
  49: }
  50: 
  51: public final String toString() {
  52: StringBuilder sb = new StringBuilder("LocationData{latitude=");
  53: sb.append(this.a);
  54: sb.append(", longitude=");
  55: sb.append(this.b);
  56: sb.append(", altitude=");
  57: sb.append(this.c);
  58: sb.append(", accuracy=");
  59: vg9.F(sb, this.d, ", bearing=", this.e, ", speed=");
  60: sb.append(this.f);
  61: sb.append("}");
  62: return sb.toString();
  63: }
  64: 
  65: public n4a(double d, double d2, double d3, float f, float f2, float f3) {
  66: this.a = d;
  67: this.b = d2;
  68: this.c = d3;
  69: this.d = f;
  70: this.e = f2;
  71: this.f = f3;
  72: }
  73: }
~~~

## defpackage/dtc.java (42 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class dtc {
   5: public final rp9 a;
   6: public final rp9 b;
   7: 
   8: public dtc(rp9 rp9Var, rp9 rp9Var2) {
   9: this.a = rp9Var;
  10: this.b = rp9Var2;
  11: }
  12: 
  13: public final dle a() {
  14: return (dle) this.a.getValue();
  15: }
  16: 
  17: public final boolean b() {
  18: String string;
  19: return (a().a.s() == -1 \|\| (string = a().d.d.getString("auth.token", null)) == null \|\| string.length() == 0) ? false : true;
  20: }
  21: 
  22: public final String c() {
  23: String string;
  24: if (a().a.s() != 0 && (string = a().d.d.getString("auth.token", null)) != null && string.length() != 0) {
  25: return a().d.d.getString("auth.token", null);
  26: }
  27: f09.d0(dtc.class.getName(), "Early return in peekToken cuz of prefs.client().userId == 0L \|\| prefs.auth().token.isNullOrEmpty()", new Object[0]);
  28: return null;
  29: }
  30: 
  31: public final void d(boolean z, boolean z2) {
  32: f09.p("dtc", "removeAccount");
  33: a().d.b();
  34: if (z) {
  35: ((l9a) this.b.getValue()).a(z2);
  36: }
  37: }
  38: 
  39: public final void e(String str) {
  40: a().d.e("auth.token", str);
  41: }
  42: }
~~~

## defpackage/qi0.java (5 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class qi0 extends a4 {
   5: }
~~~

## defpackage/e5h.java (62 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class e5h extends x6j {
   5: public String c;
   6: public int d;
   7: public t80 e;
   8: public String f;
   9: public Long g;
  10: public final int h;
  11: public boolean i;
  12: 
  13: public e5h(beb bebVar, int i) {
  14: super(bebVar);
  15: this.h = i;
  16: }
  17: 
  18: @Override // defpackage.x6j
  19: public final void c(beb bebVar, String str) {
  20: str.getClass();
  21: switch (str) {
  22: case "callsSeed":
  23: this.g = Long.valueOf(e0c.o0(bebVar, 0L));
  24: break;
  25: case "isVpn":
  26: this.i = e0c.g0(bebVar);
  27: break;
  28: case "reg-country-code":
  29: this.e = t80.g(bebVar);
  30: break;
  31: case "app-update-type":
  32: this.d = e0c.m0(bebVar, 0);
  33: break;
  34: case "location":
  35: this.c = e0c.r0(bebVar);
  36: break;
  37: case "recovery-url":
  38: this.f = e0c.r0(bebVar);
  39: break;
  40: default:
  41: bebVar.N();
  42: break;
  43: }
  44: }
  45: 
  46: @Override // defpackage.mv0
  47: public final String toString() {
  48: String str = this.c;
  49: int i = this.d;
  50: String strValueOf = String.valueOf(this.e);
  51: String str2 = this.f;
  52: Long l = this.g;
  53: boolean z = this.i;
  54: StringBuilder sbA = vg9.A(i, "{locationCountryCode='", str, "', appUpdateType=", ", regCountryCode=");
  55: w7g.D(sbA, strValueOf, ", recoveryUrl='", str2, "', callsSeed=");
  56: sbA.append(l);
  57: sbA.append(", isVpn=");
  58: sbA.append(z);
  59: sbA.append("}");
  60: return sbA.toString();
  61: }
  62: }
~~~

## defpackage/j6h.java (15 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class j6h {
   5: public final g7j a;
   6: 
   7: public j6h(h7j h7jVar) {
   8: g7j g7jVar = h7jVar instanceof g7j ? (g7j) h7jVar : null;
   9: this.a = g7jVar == null ? new g7j(h7jVar) : g7jVar;
  10: }
  11: 
  12: public final Thread a(Runnable runnable, String str) {
  13: return this.a.a(str).newThread(runnable);
  14: }
  15: }
~~~

## defpackage/f6h.java (174 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.os.Handler;
   4: import android.os.HandlerThread;
   5: import java.util.ArrayList;
   6: import java.util.concurrent.CopyOnWriteArraySet;
   7: import java.util.concurrent.locks.Lock;
   8: import java.util.concurrent.locks.ReentrantLock;
   9: 
  10: /* JADX INFO: loaded from: classes.dex */
  11: public final class f6h implements c6h {
  12: public final wag a;
  13: public final yw6 b;
  14: public final s8a c;
  15: public final yi1 d;
  16: public final long e;
  17: public final String f;
  18: public final rp9 g;
  19: public final rp9 h;
  20: public final rp9 i;
  21: public final ArrayList j;
  22: public final Object k;
  23: public final ArrayList l;
  24: public final CopyOnWriteArraySet m;
  25: public final String[] n;
  26: public final String[] o;
  27: public final Handler p;
  28: public volatile int q;
  29: public final r4i r;
  30: public final dmf s;
  31: public volatile byte t;
  32: public final f3c u;
  33: public final f4j v;
  34: public p2 w;
  35: 
  36: public f6h(wag wagVar, rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, yw6 yw6Var, s8a s8aVar, yi1 yi1Var, boolean z) {
  37: qzd qzdVar = fe6.b;
  38: long jU = az7.U(5, me6.f);
  39: this.a = wagVar;
  40: this.b = yw6Var;
  41: this.c = s8aVar;
  42: this.d = yi1Var;
  43: this.e = jU;
  44: String name = f6h.class.getName();
  45: this.f = name;
  46: this.g = rp9Var;
  47: this.h = rp9Var2;
  48: this.i = rp9Var3;
  49: this.j = new ArrayList(4);
  50: this.k = z ? new duf() : new ReentrantLock();
  51: this.l = new ArrayList(1);
  52: this.m = new CopyOnWriteArraySet();
  53: this.n = new String[]{"no_net", "disconnected", "connected", "logged_in"};
  54: this.o = new String[]{"disconnected", "connected", "logged_in"};
  55: r4i r4iVarC = az7.c(Integer.valueOf(this.q));
  56: this.r = r4iVarC;
  57: this.s = new dmf(r4iVarC);
  58: this.u = new f3c(tdd.Z3.a());
  59: this.v = new f4j((byte) 0);
  60: HandlerThread handlerThread = new HandlerThread("session-state");
  61: handlerThread.start();
  62: this.p = new Handler(handlerThread.getLooper(), new wz9(this, (byte) 2));
  63: ((ms4) rp9Var.getValue()).d(new g8c(this, (byte) 1));
  64: wagVar.e(new ky(this, (byte) 3));
  65: o1d o1dVar = f09.g;
  66: if (o1dVar == null) {
  67: return;
  68: }
  69: c6a c6aVar = c6a.d;
  70: if (o1dVar.b(c6aVar)) {
  71: o1dVar.c(c6aVar, name, "ctor, " + this, null);
  72: }
  73: }
  74: 
  75: public final void b(String str, e46 e46Var) {
  76: String str2 = this.f;
  77: o1d o1dVar = f09.g;
  78: if (o1dVar != null) {
  79: c6a c6aVar = c6a.d;
  80: if (o1dVar.b(c6aVar)) {
  81: o1dVar.c(c6aVar, str2, "onDisconnected for sessionId=" + str + " with reason=" + e46Var, null);
  82: }
  83: }
  84: this.p.obtainMessage(0, new e6h(str, e46Var)).sendToTarget();
  85: }
  86: 
  87: public final void c(b6h b6hVar) {
  88: f(new yr4(this, b6hVar, true, 1 == true ? 1 : 0));
  89: this.p.obtainMessage(10).sendToTarget();
  90: }
  91: 
  92: public final void d(b6h b6hVar) {
  93: f(new yr4(this, b6hVar, false, (byte) 1));
  94: this.p.obtainMessage(11).sendToTarget();
  95: }
  96: 
  97: public final void e() {
  98: int i;
  99: int i2 = 0;
 100: if (((ms4) this.g.getValue()).g()) {
 101: i = 1;
 102: if (this.t != 0) {
 103: if (this.t == 1) {
 104: i = 2;
 105: } else {
 106: if (this.t != 2) {
 107: k3g.o(w7g.E(this.t, "Unknown connection status="));
 108: return;
 109: }
 110: i = 3;
 111: }
 112: }
 113: } else {
 114: i = 0;
 115: }
 116: if (i != this.q) {
 117: this.q = i;
 118: String str = this.f;
 119: o1d o1dVar = f09.g;
 120: if (o1dVar != null) {
 121: c6a c6aVar = c6a.d;
 122: if (o1dVar.b(c6aVar)) {
 123: o1dVar.c(c6aVar, str, "updateState, " + this, null);
 124: }
 125: }
 126: while (i2 < this.j.size()) {
 127: int i3 = i2 + 1;
 128: b6h b6hVar = (b6h) this.j.get(i2);
 129: euf eufVar = new euf();
 130: f(new u6(this, b6hVar, eufVar, (byte) 13));
 131: if (!eufVar.a) {
 132: b6hVar.c(this.q);
 133: }
 134: i2 = i3;
 135: }
 136: r4i r4iVar = this.r;
 137: Integer numValueOf = Integer.valueOf(this.q);
 138: r4iVar.getClass();
 139: r4iVar.j(null, numValueOf);
 140: String str2 = this.f;
 141: o1d o1dVar2 = f09.g;
 142: if (o1dVar2 == null) {
 143: return;
 144: }
 145: c6a c6aVar2 = c6a.c;
 146: if (o1dVar2.b(c6aVar2)) {
 147: vg9.E("notifyListeners, sent ", this.n[this.q], o1dVar2, c6aVar2, str2);
 148: }
 149: }
 150: }
 151: 
 152: public final void f(o08 o08Var) {
 153: Object obj = this.k;
 154: if (obj instanceof duf) {
 155: ((duf) obj).a(o08Var);
 156: return;
 157: }
 158: if (!(obj instanceof ReentrantLock)) {
 159: k3g.o("Unexpected lock type");
 160: return;
 161: }
 162: Lock lock = (Lock) obj;
 163: lock.lock();
 164: try {
 165: o08Var.c();
 166: } finally {
 167: lock.unlock();
 168: }
 169: }
 170: 
 171: public final String toString() {
 172: return "SessionStateInfoImpl@" + Integer.toHexString(hashCode()) + "(connStatus=" + this.o[this.t] + ") -> " + this.n[this.q];
 173: }
 174: }
~~~

## defpackage/st5.java (59 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public final class st5 {
   5: public final q1a a;
   6: public final rp9 b;
   7: public final rp9 c;
   8: public final rp9 d;
   9: public final rp9 e;
  10: public final rp9 f;
  11: public final rp9 g;
  12: public final rp9 h;
  13: public final rp9 i;
  14: public final rp9 j;
  15: public final rp9 k;
  16: public final rp9 l;
  17: public final rp9 m;
  18: public volatile r1g n;
  19: public final z3j o;
  20: 
  21: public st5(rp9 rp9Var, rp9 rp9Var2, rp9 rp9Var3, rp9 rp9Var4, rp9 rp9Var5, rp9 rp9Var6, rp9 rp9Var7, rp9 rp9Var8, rp9 rp9Var9, rp9 rp9Var10, q1a q1aVar, rp9 rp9Var11, rp9 rp9Var12, vck vckVar) {
  22: this.a = q1aVar;
  23: this.b = rp9Var;
  24: this.c = rp9Var2;
  25: this.d = rp9Var3;
  26: this.e = rp9Var4;
  27: this.f = rp9Var5;
  28: this.g = rp9Var6;
  29: this.h = rp9Var7;
  30: this.i = rp9Var8;
  31: this.j = rp9Var9;
  32: this.k = rp9Var10;
  33: this.l = rp9Var11;
  34: this.m = rp9Var12;
  35: this.o = new z3j(new u6(vckVar, this, rp9Var2, (byte) 3));
  36: }
  37: 
  38: public final o1h a() {
  39: return (o1h) this.c.getValue();
  40: }
  41: 
  42: public final Object b(kgc kgcVar, x1j x1jVar) {
  43: boolean zD0 = ((dle) this.b.getValue()).a.d0();
  44: s1k s1kVar = s1k.a;
  45: if (zD0) {
  46: f09.d0("NotifListenerImpl", "internalOnNotifMessage: ignore! ok push disabled", new Object[0]);
  47: return s1kVar;
  48: }
  49: Object objA = a().a(kgcVar, x1jVar);
  50: return objA == ka5.a ? objA : s1kVar;
  51: }
  52: 
  53: public final void c(tdd tddVar, e18 e18Var) {
  54: r1g r1gVar = this.n;
  55: if (r1gVar != null) {
  56: nm9.J(r1gVar.h(), null, 0, new y30(e18Var, tddVar, null, (byte) 2), 3);
  57: }
  58: }
  59: }
~~~

## defpackage/o57.java (239 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.io.IOException;
   4: import java.net.Socket;
   5: import java.net.SocketTimeoutException;
   6: import java.util.Iterator;
   7: import java.util.Locale;
   8: import java.util.concurrent.ConcurrentHashMap;
   9: import java.util.concurrent.CopyOnWriteArrayList;
  10: import java.util.concurrent.atomic.AtomicInteger;
  11: import java.util.regex.Pattern;
  12: import ru.ok.android.onelog.impl.BuildConfig;
  13: 
  14: /* JADX INFO: loaded from: classes.dex */
  15: public final class o57 {
  16: public final p7c a;
  17: public final nt4 b;
  18: public final ru5 c;
  19: public final ks4 d;
  20: public final lr4 e;
  21: public final ConcurrentHashMap f;
  22: public final m66 g;
  23: public final mxf h;
  24: public final boolean i;
  25: public final yi1 j;
  26: public final ib0 k;
  27: public final zr4 l;
  28: public final CopyOnWriteArrayList m;
  29: 
  30: static {
  31: Pattern.compile("^(([0-9]\|[1-9][0-9]\|1[0-9]{2}\|2[0-4][0-9]\|25[0-5]).){3}([0-9]\|[1-9][0-9]\|1[0-9]{2}\|2[0-4][0-9]\|25[0-5])$");
  32: }
  33: 
  34: /* JADX WARN: Code duplicated, block: B:16:0x0031  */
  35: /* JADX WARN: Code duplicated, block: B:9:0x001d  */
  36: public o57(p7c p7cVar, ru5 ru5Var, nt4 nt4Var, m66 m66Var, mxf mxfVar, boolean z, yi1 yi1Var, boolean z2) {
  37: String str;
  38: yx9 yx9Var = p7cVar.e;
  39: dle dleVar = p7cVar.c;
  40: n3a n3aVar = dleVar.a;
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
  51: }
  52: }
  53: String strV = n3aVar2.V();
  54: if (strV == null) {
  55: yx9Var.getClass();
  56: str = "443";
  57: } else {
  58: str = strV.length() > 0 ? strV : null;
  59: if (str == null) {
  60: yx9Var.getClass();
  61: str = "443";
  62: }
  63: }
  64: ks4 ks4Var = new ks4(strU, str, n3aVar2.X());
  65: this.e = new lr4(new f4j((byte) 0));
  66: this.f = new ConcurrentHashMap();
  67: this.a = p7cVar;
  68: this.b = nt4Var;
  69: this.c = ru5Var;
  70: this.d = ks4Var;
  71: this.g = m66Var;
  72: this.h = mxfVar;
  73: this.i = z;
  74: this.j = yi1Var;
  75: ib0 ib0Var = new ib0();
  76: ib0Var.d = this;
  77: ib0Var.b = new f4j((byte) 3);
  78: ib0Var.a = this.i;
  79: ib0Var.c = this.g;
  80: this.k = ib0Var;
  81: me6 me6Var = me6.e;
  82: qzd qzdVar = fe6.b;
  83: this.l = new zr4(p7cVar, new f4j((byte) 2), z ? az7.U(1, me6Var) : az7.U(BuildConfig.COUNT_TO_UPLOAD, me6.d), z ? az7.U(10, me6Var) : az7.U(3, me6Var), az7.U(z ? 100 : 96, me6Var), z2);
  84: this.m = new CopyOnWriteArrayList();
  85: }
  86: 
  87: public static void a(Socket socket) {
  88: if (socket != null) {
  89: o1d o1dVar = f09.g;
  90: if (o1dVar != null) {
  91: c6a c6aVar = c6a.c;
  92: if (o1dVar.b(c6aVar)) {
  93: o1dVar.c(c6aVar, "o57", String.format(Locale.ROOT, "closeSocketSafely, %s", socket), null);
  94: }
  95: }
  96: try {
  97: socket.close();
  98: } catch (IOException e) {
  99: o1d o1dVar2 = f09.g;
 100: if (o1dVar2 == null) {
 101: return;
 102: }
 103: c6a c6aVar2 = c6a.f;
 104: if (o1dVar2.b(c6aVar2)) {
 105: o1dVar2.c(c6aVar2, "o57", String.format(Locale.ROOT, "closeSocketSafely, failed for %s", socket), e);
 106: }
 107: }
 108: }
 109: }
 110: 
 111: public final u34 b() {
 112: c6a c6aVar = c6a.c;
 113: o1d o1dVar = f09.g;
 114: if (o1dVar != null && o1dVar.b(c6aVar)) {
 115: ks4 ks4Var = this.d;
 116: String str = ks4Var.a;
 117: vg9.K(vg9.A(((Number) ks4Var.d.getValue()).intValue(), "createConnection -> to ", str, ":", ", with rbc="), this.i, o1dVar, c6aVar, "FastClient");
 118: }
 119: yaj yajVar = new yaj(this.k);
 120: n57 n57Var = new n57(yajVar);
 121: this.m.add(n57Var);
 122: try {
 123: try {
 124: ks4 ks4Var2 = this.d;
 125: String str2 = ks4Var2.a;
 126: int iIntValue = ((Number) ks4Var2.d.getValue()).intValue();
 127: qzd qzdVar = fe6.b;
 128: u34 u34VarB = yajVar.b(az7.U(15000, me6.d), str2, iIntValue);
 129: o1d o1dVar2 = f09.g;
 130: if (o1dVar2 != null) {
 131: c6a c6aVar2 = c6a.e;
 132: if (o1dVar2.b(c6aVar2)) {
 133: o1dVar2.c(c6aVar2, "FastClient", "<- createConnection, SUCCESS for " + u34VarB, null);
 134: }
 135: }
 136: this.l.c();
 137: if (this.i) {
 138: u34VarB.d = this.l;
 139: }
 140: this.m.remove(n57Var);
 141: return u34VarB;
 142: } catch (IOException e) {
 143: if (e.getCause() instanceof SocketTimeoutException) {
 144: o1d o1dVar3 = f09.g;
 145: if (o1dVar3 != null) {
 146: c6a c6aVar3 = c6a.f;
 147: if (o1dVar3.b(c6aVar3)) {
 148: o1dVar3.c(c6aVar3, "FastClient", "createConnection, reset dns after socket timeout", null);
 149: }
 150: }
 151: m66 m66Var = this.g;
 152: String str3 = this.d.a;
 153: String str4 = m66Var.e;
 154: o1d o1dVar4 = f09.g;
 155: if (o1dVar4 != null && o1dVar4.b(c6aVar)) {
 156: o1dVar4.c(c6aVar, str4, "resetHost, ".concat(str3), null);
 157: }
 158: wl8 wl8VarA = m66Var.a(str3);
 159: if (wl8VarA != null) {
 160: wl8VarA.b();
 161: }
 162: }
 163: this.l.b();
 164: throw e;
 165: }
 166: } catch (Throwable th) {
 167: this.m.remove(n57Var);
 168: throw th;
 169: }
 170: }
 171: 
 172: public final void c() {
 173: nt4 nt4Var = this.b;
 174: ((AtomicInteger) nt4Var.c).incrementAndGet();
 175: String name = nt4.class.getName();
 176: o1d o1dVar = f09.g;
 177: if (o1dVar == null) {
 178: return;
 179: }
 180: c6a c6aVar = c6a.d;
 181: if (o1dVar.b(c6aVar)) {
 182: ihk.k("tryNextRequestTimeout ", ((AtomicInteger) nt4Var.c).get(), o1dVar, c6aVar, name);
 183: }
 184: }
 185: 
 186: public final void d(boolean z) {
 187: vaj vajVar;
 188: Iterator it = this.m.iterator();
 189: while (it.hasNext()) {
 190: yaj yajVar = ((n57) it.next()).a;
 191: String str = yajVar.m;
 192: o1d o1dVar = f09.g;
 193: if (o1dVar != null) {
 194: c6a c6aVar = c6a.c;
 195: if (o1dVar.b(c6aVar)) {
 196: s95.F("setTryToConnect, ", z, o1dVar, c6aVar, str);
 197: }
 198: }
 199: boolean z2 = !z;
 200: if (z && (vajVar = (vaj) yajVar.h.get()) != null && ((o57) yajVar.a.d).a.a.g() && !vajVar.c && yajVar.d()) {
 201: synchronized (yajVar.c) {
 202: if (yajVar.d()) {
 203: if (yajVar.j.get() < yajVar.k.get()) {
 204: yajVar.l.set(true);
 205: yajVar.c.notifyAll();
 206: } else {
 207: z2 = true;
 208: }
 209: if (!z2) {
 210: String str2 = yajVar.m;
 211: o1d o1dVar2 = f09.g;
 212: if (o1dVar2 != null) {
 213: c6a c6aVar2 = c6a.f;
 214: if (o1dVar2.b(c6aVar2)) {
 215: o1dVar2.c(c6aVar2, str2, "setTryToConnect, force new connect", null);
 216: }
 217: }
 218: }
 219: }
 220: }
 221: }
 222: if (z2 && !yajVar.e.get()) {
 223: synchronized (yajVar.c) {
 224: if (yajVar.e.compareAndSet(false, true)) {
 225: yajVar.c.notifyAll();
 226: String str3 = yajVar.m;
 227: o1d o1dVar3 = f09.g;
 228: if (o1dVar3 != null) {
 229: c6a c6aVar3 = c6a.f;
 230: if (o1dVar3.b(c6aVar3)) {
 231: o1dVar3.c(c6aVar3, str3, "abort", null);
 232: }
 233: }
 234: }
 235: }
 236: }
 237: }
 238: }
 239: }
~~~

## defpackage/v6j.java (12 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.Arrays;
   4: import java.util.List;
   5: 
   6: /* JADX INFO: loaded from: classes.dex */
   7: public interface v6j {
   8: public static final List F0 = Arrays.asList("session.state", "proto.state", "proto.payload", "internal", "service.unavailable", "service.timeout", "proto.ver", "error.call.history.inconsistency", "errors.event.unavailable", "login.flood", "login.blocked");
   9: public static final jl9 G0 = new jl9();
  10: 
  11: long a(float f, int i, long j);
  12: }
~~~

## defpackage/i00.java (83 строк)

~~~java
   1: package defpackage;
   2: 
   3: import java.util.Collection;
   4: import java.util.Iterator;
   5: import java.util.Map;
   6: import java.util.Set;
   7: 
   8: /* JADX INFO: loaded from: classes.dex */
   9: public final class i00 extends uph implements Map {
  10: public c00 d;
  11: public e00 e;
  12: public g00 f;
  13: 
  14: @Override // java.util.Map
  15: public final Set entrySet() {
  16: c00 c00Var = this.d;
  17: if (c00Var != null) {
  18: return c00Var;
  19: }
  20: c00 c00Var2 = new c00(this);
  21: this.d = c00Var2;
  22: return c00Var2;
  23: }
  24: 
  25: public final boolean j(Collection collection) {
  26: Iterator it = collection.iterator();
  27: while (it.hasNext()) {
  28: if (!super.containsKey(it.next())) {
  29: return false;
  30: }
  31: }
  32: return true;
  33: }
  34: 
  35: public final boolean k(Collection collection) {
  36: int i = this.c;
  37: Iterator it = collection.iterator();
  38: while (it.hasNext()) {
  39: super.remove(it.next());
  40: }
  41: return i != this.c;
  42: }
  43: 
  44: @Override // java.util.Map
  45: public final Set keySet() {
  46: e00 e00Var = this.e;
  47: if (e00Var != null) {
  48: return e00Var;
  49: }
  50: e00 e00Var2 = new e00(this);
  51: this.e = e00Var2;
  52: return e00Var2;
  53: }
  54: 
  55: public final boolean l(Collection collection) {
  56: int i = this.c;
  57: for (int i2 = i - 1; i2 >= 0; i2--) {
  58: if (!collection.contains(f(i2))) {
  59: g(i2);
  60: }
  61: }
  62: return i != this.c;
  63: }
  64: 
  65: @Override // java.util.Map
  66: public final void putAll(Map map) {
  67: b(map.size() + this.c);
  68: for (Map.Entry entry : map.entrySet()) {
  69: put(entry.getKey(), entry.getValue());
  70: }
  71: }
  72: 
  73: @Override // java.util.Map
  74: public final Collection values() {
  75: g00 g00Var = this.f;
  76: if (g00Var != null) {
  77: return g00Var;
  78: }
  79: g00 g00Var2 = new g00(this);
  80: this.f = g00Var2;
  81: return g00Var2;
  82: }
  83: }
~~~

## defpackage/jn0.java (28 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public final class jn0 {
   5: public final Integer a;
   6: 
   7: public jn0(Integer num) {
   8: this.a = num;
   9: }
  10: 
  11: public final boolean equals(Object obj) {
  12: if (obj == this) {
  13: return true;
  14: }
  15: if (obj instanceof jn0) {
  16: return this.a.equals(((jn0) obj).a);
  17: }
  18: return false;
  19: }
  20: 
  21: public final int hashCode() {
  22: return this.a.hashCode() ^ 1000003;
  23: }
  24: 
  25: public final String toString() {
  26: return "ProductData{productId=" + this.a + "}";
  27: }
  28: }
~~~

## defpackage/pck.java (8 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes2.dex */
   4: public interface pck {
   5: Object g(vi viVar, b55 b55Var);
   6: 
   7: boolean p();
   8: }
~~~

## defpackage/i9g.java (300 строк)

~~~java
   1: package defpackage;
   2: 
   3: import com.google.protobuf.nano.InvalidProtocolBufferNanoException;
   4: import java.util.List;
   5: import java.util.Map;
   6: import java.util.concurrent.ConcurrentHashMap;
   7: import java.util.concurrent.atomic.AtomicInteger;
   8: import kotlin.NoWhenBranchMatchedException;
   9: import kotlin.collections.a;
  10: import org.webrtc.PeerConnectionFactory;
  11: import ru.ok.tamtam.nano.ProtoException;
  12: 
  13: /* JADX INFO: loaded from: classes.dex */
  14: public final class i9g {
  15: public final String a = i9g.class.getName();
  16: public final rp9 b;
  17: 
  18: public i9g(rp9 rp9Var) {
  19: this.b = rp9Var;
  20: }
  21: 
  22: public static rwd e(swd swdVar, byte[] bArr) throws e5f {
  23: try {
  24: switch (swdVar.ordinal()) {
  25: case 0:
  26: case 15:
  27: case 18:
  28: case 34:
  29: case 35:
  30: return null;
  31: case 1:
  32: return m3n.b(bArr);
  33: case 2:
  34: return u3n.b(bArr);
  35: case 3:
  36: return ken.a(bArr);
  37: case 4:
  38: return fen.b(bArr);
  39: case 5:
  40: return f09.R(bArr);
  41: case 6:
  42: return t6n.b(bArr);
  43: case 7:
  44: return c8n.c(bArr);
  45: case 8:
  46: return q3n.b(bArr);
  47: case 9:
  48: return n6n.b(bArr);
  49: case 10:
  50: return gxm.e(bArr);
  51: case 11:
  52: return o7n.b(bArr);
  53: case 12:
  54: laj lajVar = new laj();
  55: try {
  56: mcb.c(lajVar, bArr);
  57: d4h d4hVar = new d4h(lajVar.b, lajVar.c, lajVar.d, f0c.f(dx5.d, Integer.valueOf(lajVar.e)));
  58: f09.p(d4hVar.f, "parseFrom");
  59: return d4hVar;
  60: } catch (InvalidProtocolBufferNanoException e) {
  61: throw new ProtoException(e);
  62: }
  63: case 13:
  64: return a8n.a(bArr);
  65: case 14:
  66: return m7n.b(bArr);
  67: case PeerConnectionFactory.Options.ADAPTER_TYPE_LOOPBACK /* 16 */:
  68: return a4n.b(bArr);
  69: case 17:
  70: return s7n.b(bArr);
  71: case 19:
  72: return w7n.c(bArr);
  73: case 20:
  74: return ejn.b(bArr);
  75: case 21:
  76: return ugn.a(bArr);
  77: case 22:
  78: return o3n.a(bArr);
  79: case 23:
  80: return p6n.a(bArr);
  81: case 24:
  82: return y3n.a(bArr);
  83: case 25:
  84: return tkn.a(bArr);
  85: case 26:
  86: a3h.g.getClass();
  87: return jl9.o(bArr);
  88: case 27:
  89: return z5n.b(bArr);
  90: case 28:
  91: return swm.c(bArr);
  92: case 29:
  93: int i = d20.i;
  94: return iym.b(bArr);
  95: case 30:
  96: int i2 = j20.j;
  97: return kym.b(bArr);
  98: case 31:
  99: int i3 = n20.i;
 100: return oym.c(bArr);
 101: case PeerConnectionFactory.Options.ADAPTER_TYPE_ANY /* 32 */:
 102: int i4 = l20.k;
 103: return mym.b(bArr);
 104: case 33:
 105: return x6n.c(bArr);
 106: case 36:
 107: return com.k(bArr);
 108: case 37:
 109: return v5n.a(bArr);
 110: case 38:
 111: z9j z9jVar = new z9j();
 112: try {
 113: mcb.c(z9jVar, bArr);
 114: return new kc5(z9jVar.b, new os(z9jVar.c, z9jVar.d, z9jVar.e, z9jVar.f, z9jVar.g, (Map) e0c.C(z9jVar.h)));
 115: } catch (InvalidProtocolBufferNanoException e2) {
 116: throw new ProtoException(e2);
 117: }
 118: case 39:
 119: return pdn.b(bArr);
 120: case 40:
 121: return u7n.b(bArr);
 122: case 41:
 123: AtomicInteger atomicInteger = j4h.f;
 124: j9j j9jVar = new j9j((byte) 1);
 125: try {
 126: mcb.c(j9jVar, bArr);
 127: return new j4h(j9jVar.c, j9jVar.e, a.k0(j9jVar.d));
 128: } catch (InvalidProtocolBufferNanoException e3) {
 129: throw new ProtoException(e3);
 130: }
 131: case 42:
 132: ConcurrentHashMap concurrentHashMap = h2h.j;
 133: return ein.c(bArr);
 134: case 43:
 135: int i5 = n2h.i;
 136: return gin.b(bArr);
 137: case 44:
 138: int i6 = c2h.h;
 139: return din.c(bArr);
 140: case 45:
 141: return k44.t(bArr);
 142: case 46:
 143: return q8n.b(bArr);
 144: case 47:
 145: return s8n.a(bArr);
 146: case 48:
 147: String str = uc4.i;
 148: return rc4.d(bArr);
 149: case 49:
 150: return efn.a(bArr);
 151: case 50:
 152: return s8n.b(bArr);
 153: default:
 154: throw new NoWhenBranchMatchedException();
 155: }
 156: } catch (ProtoException e4) {
 157: throw new e5f(e4);
 158: }
 159: throw new e5f(e4);
 160: }
 161: 
 162: public final Object a(long j, d55 d55Var) {
 163: Object objK = az7.K(d55Var, b().a, false, true, new rj7(j, (byte) 8));
 164: s1k s1kVar = s1k.a;
 165: ka5 ka5Var = ka5.a;
 166: if (objK != ka5Var) {
 167: objK = s1kVar;
 168: }
 169: return objK == ka5Var ? objK : s1kVar;
 170: }
 171: 
 172: public final raj b() {
 173: return (raj) this.b.getValue();
 174: }
 175: 
 176: public final Object c(rwd rwdVar, long j, int i, d55 d55Var) {
 177: raj rajVarB = b();
 178: return az7.K(d55Var, rajVarB.a, false, true, new so((Object) rajVarB, (Object) new h8j(rwdVar.getId(), rwdVar.getType(), e9j.b, 0, j, i, rwdVar.l(), System.currentTimeMillis()), (byte) 25));
 179: }
 180: 
 181: public final List d(List list) {
 182: return j0h.T(j0h.K(new tsj(new q00(list, (byte) 1), new s14(1, this, i9g.class, "taskDbFromEntity", "taskDbFromEntity(Lone/me/sdk/tasks/db/TaskEntity;)Lone/me/sdk/tasks/db/TaskDb;", 0, (byte) 7))));
 183: }
 184: 
 185: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
 186: public final Object f(swd swdVar, d55 d55Var) {
 187: g9g g9gVar;
 188: if (d55Var instanceof g9g) {
 189: g9gVar = (g9g) d55Var;
 190: int i = g9gVar.g;
 191: if ((i & Integer.MIN_VALUE) != 0) {
 192: g9gVar.g = i - Integer.MIN_VALUE;
 193: } else {
 194: g9gVar = new g9g(this, d55Var);
 195: }
 196: } else {
 197: g9gVar = new g9g(this, d55Var);
 198: }
 199: Object objK = g9gVar.e;
 200: int i2 = g9gVar.g;
 201: if (i2 == 0) {
 202: xnm.y(objK);
 203: raj rajVarB = b();
 204: g9gVar.d = this;
 205: g9gVar.g = 1;
 206: objK = az7.K(g9gVar, rajVarB.a, true, false, new g4h(rajVarB, swdVar));
 207: ka5 ka5Var = ka5.a;
 208: if (objK == ka5Var) {
 209: return ka5Var;
 210: }
 211: } else {
 212: if (i2 != 1) {
 213: k3g.o("call to 'resume' before 'invoke' with coroutine");
 214: return null;
 215: }
 216: this = g9gVar.d;
 217: xnm.y(objK);
 218: }
 219: return this.d((List) objK);
 220: }
 221: 
 222: /* JADX WARN: Code duplicated, block: B:7:0x0013  */
 223: public final Object g(long j, d55 d55Var) {
 224: h9g h9gVar;
 225: if (d55Var instanceof h9g) {
 226: h9gVar = (h9g) d55Var;
 227: int i = h9gVar.f;
 228: if ((i & Integer.MIN_VALUE) != 0) {
 229: h9gVar.f = i - Integer.MIN_VALUE;
 230: } else {
 231: h9gVar = new h9g(this, d55Var);
 232: }
 233: } else {
 234: h9gVar = new h9g(this, d55Var);
 235: }
 236: Object objK = h9gVar.d;
 237: int i2 = h9gVar.f;
 238: if (i2 == 0) {
 239: xnm.y(objK);
 240: raj rajVarB = b();
 241: h9gVar.f = 1;
 242: objK = az7.K(h9gVar, rajVarB.a, true, false, new rj7(j, rajVarB, (byte) 7));
 243: ka5 ka5Var = ka5.a;
 244: if (objK == ka5Var) {
 245: return ka5Var;
 246: }
 247: } else {
 248: if (i2 != 1) {
 249: k3g.o("call to 'resume' before 'invoke' with coroutine");
 250: return null;
 251: }
 252: xnm.y(objK);
 253: }
 254: h8j h8jVar = (h8j) objK;
 255: if (h8jVar != null) {
 256: return i(h8jVar);
 257: }
 258: return null;
 259: }
 260: 
~~~

Поздние сигнатуры: 261 public final Object h(int i, d55 d55Var) {; 270 public final g8j i(h8j h8jVar) {

## defpackage/f4j.java (64 строк)

~~~java
   1: package defpackage;
   2: 
   3: import android.os.SystemClock;
   4: 
   5: /* JADX INFO: loaded from: classes.dex */
   6: public final class f4j extends q2 {
   7: public final /* synthetic */ byte d;
   8: 
   9: /* JADX WARN: Illegal instructions before constructor call */
  10: public f4j(byte b) {
  11: this.d = b;
  12: me6 me6Var = me6.d;
  13: switch (b) {
  14: case 2:
  15: super(me6Var);
  16: break;
  17: case 3:
  18: super(me6Var);
  19: break;
  20: default:
  21: super(me6Var);
  22: break;
  23: }
  24: }
  25: 
  26: @Override // defpackage.q2
  27: public final long U0() {
  28: switch (this.d) {
  29: case 0:
  30: return System.currentTimeMillis();
  31: case 1:
  32: return System.nanoTime();
  33: case 2:
  34: return SystemClock.elapsedRealtime();
  35: default:
  36: return SystemClock.uptimeMillis();
  37: }
  38: }
  39: 
  40: public final long V0() {
  41: byte b = this.d;
  42: me6 me6Var = me6.d;
  43: switch (b) {
  44: case 0:
  45: qzd qzdVar = fe6.b;
  46: return az7.V(System.currentTimeMillis(), me6Var);
  47: case 1:
  48: qzd qzdVar2 = fe6.b;
  49: return az7.V(System.nanoTime(), me6.b);
  50: case 2:
  51: qzd qzdVar3 = fe6.b;
  52: return az7.V(SystemClock.elapsedRealtime(), me6Var);
  53: default:
  54: qzd qzdVar4 = fe6.b;
  55: return az7.V(SystemClock.uptimeMillis(), me6Var);
  56: }
  57: }
  58: 
  59: /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
  60: public /* synthetic */ f4j(me6 me6Var) {
  61: super(me6Var);
  62: this.d = (byte) 1;
  63: }
  64: }
~~~

## defpackage/o6a.java (6 строк)

~~~java
   1: package defpackage;
   2: 
   3: /* JADX INFO: loaded from: classes.dex */
   4: public interface o6a {
   5: Object f(Object obj, String str);
   6: }
~~~

