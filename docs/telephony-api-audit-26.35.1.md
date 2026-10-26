# MAX 26.35.1 — проверка получения номера SIM из APK

Проверен оригинал `base.apk` (e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc); исходных Java: **24272**.
Проверка статическая, без запуска, сетевых запросов или изменения SIM.

## Сводка вызовов и ссылок

| Маркер | Найдено строк |
|---|---:|
| `getLine1Number` | 0 |
| `getPhoneNumber(` | 1 |
| `getSimSerialNumber` | 0 |
| `getSubscriberId` | 0 |
| `getNetworkOperator(` | 4 |
| `getNetworkOperatorName(` | 5 |
| `getSimOperator(` | 2 |
| `getSimOperatorName(` | 0 |
| `getSimState(` | 0 |
| `SubscriptionManager` | 0 |
| `TelephonyManager` | 28 |
| `getActiveSubscriptionInfo` | 0 |
| `getDefaultSubscriptionId` | 0 |
| `READ_PHONE_NUMBERS` | 0 |
| `READ_PHONE_STATE` | 3 |
| `TelephonyCallback` | 5 |
| `CarrierPrivileges` | 0 |
| `MobileId` | 24 |

## Найденные обращения (по 12 на маркер)

### `getPhoneNumber(`

- `defpackage/n3a.java:10` — `public static final /* synthetic */ zm9[] g1 = {new c4c(n3a.class, "phoneCode", "getPhoneCode()Ljava/lang/String;"), a15.f(luf.a, n3a.class, "phoneNumber", "getPhoneNumber()Ljava/lang/String;"), new c`

### `getNetworkOperator(`

- `defpackage/lb6.java:673` — `n4gVar = telephonyManager != null ? telephonyManager.getNetworkOperator() + ':' + telephonyManager.getNetworkOperatorName() : null;`
- `defpackage/t5a.java:232` — `n4gVar = telephonyManager != null ? telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName() : null;`
- `defpackage/yr0.java:96` — `n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();`
- `defpackage/yr0.java:180` — `n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();`

### `getNetworkOperatorName(`

- `defpackage/lb6.java:673` — `n4gVar = telephonyManager != null ? telephonyManager.getNetworkOperator() + ':' + telephonyManager.getNetworkOperatorName() : null;`
- `defpackage/t5a.java:232` — `n4gVar = telephonyManager != null ? telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName() : null;`
- `defpackage/tul.java:111` — `String networkOperatorName = telephonyManager != null ? telephonyManager.getNetworkOperatorName() : null;`
- `defpackage/yr0.java:96` — `n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();`
- `defpackage/yr0.java:180` — `n4gVar = telephonyManager.getNetworkOperator() + ":" + telephonyManager.getNetworkOperatorName();`

### `getSimOperator(`

- `defpackage/ey2.java:122` — `h8lVarC.p("mcc_mnc", ((TelephonyManager) context.getSystemService("phone")).getSimOperator());`
- `defpackage/ey2.java:142` — `h8lVarC.p("mcc_mnc", ((TelephonyManager) context2.getSystemService("phone")).getSimOperator());`

### `TelephonyManager`

- `defpackage/esd.java:11` — `import android.telephony.TelephonyManager;`
- `defpackage/esd.java:701` — `TelephonyManager telephonyManager = (TelephonyManager) systemService2;`
- `defpackage/eug.java:12` — `import android.telephony.TelephonyManager;`
- `defpackage/eug.java:4269` — `switch (((TelephonyManager) context.getSystemService("phone")).getDataNetworkType()) {`
- `defpackage/ey2.java:8` — `import android.telephony.TelephonyManager;`
- `defpackage/ey2.java:122` — `h8lVarC.p("mcc_mnc", ((TelephonyManager) context.getSystemService("phone")).getSimOperator());`
- `defpackage/ey2.java:142` — `h8lVarC.p("mcc_mnc", ((TelephonyManager) context2.getSystemService("phone")).getSimOperator());`
- `defpackage/lb6.java:6` — `import android.telephony.TelephonyManager;`
- `defpackage/lb6.java:672` — `TelephonyManager telephonyManager = systemService instanceof TelephonyManager ? (TelephonyManager) systemService : null;`
- `defpackage/o4n.java:6` — `import android.telephony.TelephonyManager;`
- `defpackage/o4n.java:13` — `TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService("phone");`
- `defpackage/sgk.java:15` — `import android.telephony.TelephonyManager;`
- Остальные 16 строк не приведены

### `READ_PHONE_STATE`

- `defpackage/esd.java:707` — `if ((networkInfo == null \|\| !networkInfo.isConnected()) && context.checkPermission("android.permission.READ_PHONE_STATE", Process.myPid(), Process.myUid()) == 0) {`
- `defpackage/eug.java:4266` — `String[] strArr = {"android.permission.READ_PHONE_STATE", "android.permission.READ_BASIC_PHONE_STATE"};`
- `defpackage/hwd.java:23` — `public static final String[] j = {"android.permission.CAMERA", "android.permission.RECORD_AUDIO", "android.permission.READ_PHONE_STATE"};`

### `TelephonyCallback`

- `android/telephony/TelephonyCallback.java:4` — `public /* synthetic */ class TelephonyCallback {`
- `defpackage/k9c.java:3` — `import android.telephony.TelephonyCallback;`
- `defpackage/k9c.java:7` — `public final class k9c extends TelephonyCallback implements TelephonyCallback.DisplayInfoListener {`
- `defpackage/o4n.java:16` — `telephonyManager.registerTelephonyCallback(m9cVar.a, k9cVar);`
- `defpackage/o4n.java:17` — `telephonyManager.unregisterTelephonyCallback(k9cVar);`

### `MobileId`

- `defpackage/a8l.java:637` — `bj9 bj9Var4 = new bj9("WebAppVerifyMobileId", mj9Var4.b(jol.Companion.serializer(), jolVar), true);`
- `defpackage/ajk.java:33` — `StringBuilder sb = new StringBuilder("VerifyMobileIdResponseInfo(code=");`
- `defpackage/dol.java:22` — `arrayList.add("WebAppVerifyMobileId");`
- `defpackage/dol.java:34` — `return (str.equals("WebAppVerifyMobileId") && (objF = f(str2, (d55) b55Var)) == ka5.a) ? objF : s1kVar;`
- `defpackage/dol.java:42` — `if (str.equals("WebAppVerifyMobileId")) {`
- `defpackage/e11.java:9` — `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0010\t\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\n\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0004\n\u0002\u00`
- `defpackage/e11.java:40` — `public final long healthStatsMobileIdleMs;`
- `defpackage/e11.java:83` — `long j24 = (i3 & 512) != 0 ? e11Var.healthStatsMobileIdleMs : j8;`
- `defpackage/e11.java:179` — `public final long getHealthStatsMobileIdleMs() {`
- `defpackage/e11.java:180` — `return this.healthStatsMobileIdleMs;`
- `defpackage/e11.java:203` — `return this.sliceTime == e11Var.sliceTime && this.utime == e11Var.utime && this.stime == e11Var.stime && this.cutime == e11Var.cutime && this.cstime == e11Var.cstime && this.batteryPercent == e11Var.b`
- `defpackage/e11.java:219` — `return Boolean.hashCode(this.isBackgroundActivityDisabled) + w7g.n((zoe.h(this.processes) + pzm.a(pzm.a(pzm.a(pzm.a(pzm.a(pzm.a(pzm.a(pzm.a(a15.d(this.temperature, a15.d(this.batteryPercent, pzm.a(pzm`
- Остальные 12 строк не приведены

## Интерпретация

- Ссылки на API и строки ещё не доказывают использование конкретного пути во время привязки устройства.
- Возвращённый Android API номер SIM не является доказательством владения номером или успешной проверки Mobile ID.
- Проверка доверенного устройства может проводиться через мобильного оператора вне локального чтения номера.
- В отчёте нет сетевых токенов, пользовательских номеров, кодов подтверждения и рекомендаций по обходу привязки.

Источники: официальный Android API `SubscriptionManager.getPhoneNumber` и справка MAX по Mobile ID.
