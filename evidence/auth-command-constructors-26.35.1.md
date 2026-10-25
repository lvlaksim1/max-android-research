# MAX 26.35.1 — классы, создающие команды входа

Статический поиск конструкторов команд в декомпилированном APK.
Названия методов и условные ветви могут быть искажены JADX.
Источник: оригинал с SHA-256 e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc

## AUTH_REQUEST — super(tdd.l)
Найдено классов: 1

### defpackage/aj0.java
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

## AUTH_CONFIRM — super(tdd.u)
Найдено классов: 0

## AUTH — super(tdd.m)
Найдено классов: 0

## LOGIN — super(tdd.n)
Найдено классов: 1

### defpackage/k7a.java
```java
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
```

## LOGIN2 — super(tdd.o)
Найдено классов: 1

### defpackage/a7a.java
```java
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
```

