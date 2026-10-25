# MAX 26.35.1: указатель кода авторизации

Автоматический статический разбор точного APK с помощью JADX.
Это перечень кандидатов, а НЕ подтверждённая последовательность сетевых запросов.

SHA-256: e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc
Обработано файлов Java: 24272
Файлов-кандидатов: 299

## Частота маркеров

| Маркер | Совпадений |
|---|---:|
| InputPhoneScreen | 176 |
| ConfirmPhoneScreen | 160 |
| AUTH_OTP | 2 |
| AUTH_CHECK_CALL | 1 |
| AUTH_CALL_OUT | 2 |
| AUTH_BY_TRACK | 1 |
| AUTH_QR_APPROVE | 1 |
| AUTH_CHECK_PASSWORD | 1 |
| AUTH_2FA | 21 |
| api2.oneme.ru | 10 |
| api-tg.oneme.ru | 4 |
| api/v3/ws | 1 |
| tokenRefresh | 3 |
| refreshToken | 9 |
| accessToken | 7 |
| refresh_token | 0 |
| access_token | 0 |
| verifyOtp | 0 |
| checkOtp | 0 |
| requestOtp | 0 |
| sendOtp | 0 |
| verifyCode | 4 |
| requestCode | 22 |
| AuthRepository | 0 |
| AuthApi | 1 |
| AuthService | 9 |
| AuthRequest | 5 |
| AuthResponse | 2 |
| LoginRequest | 0 |
| LoginResponse | 1 |
| Authorization | 14 |
| Bearer | 0 |
| sessionToken | 7 |

## Приоритет ручного разбора

| Приоритет | Путь Java-файла | Маркеры |
|---:|---|---|
| 81 | defpackage/rkg.java | AUTH_2FA, AUTH_CALL_OUT, AUTH_OTP |
| 75 | one/me/settings/twofa/creation/TwoFACreationScreen.java | AUTH_2FA |
| 45 | defpackage/tdd.java | AUTH_2FA, AUTH_BY_TRACK, AUTH_CHECK_CALL, AUTH_CHECK_PASSWORD, AUTH_QR_APPROVE |
| 33 | one/me/login/inputphone/InputPhoneScreen.java | InputPhoneScreen |
| 30 | one/me/settings/twofa/password/TwoFACheckPassScreen.java | AUTH_2FA |
| 27 | defpackage/hb3.java | accessToken |
| 22 | one/me/login/confirm/ConfirmPhoneScreen.java | ConfirmPhoneScreen |
| 22 | one/me/login/confirmcallout/ConfirmPhoneCallOutScreen.java | AUTH_CALL_OUT |
| 20 | defpackage/k79.java | InputPhoneScreen |
| 20 | defpackage/n79.java | InputPhoneScreen |
| 20 | defpackage/sv2.java | ConfirmPhoneScreen |
| 20 | defpackage/vp4.java | ConfirmPhoneScreen |
| 20 | defpackage/yp4.java | ConfirmPhoneScreen |
| 19 | com/vk/push/authsdk/ipc/AuthService.java | AuthService |
| 18 | defpackage/kz.java | AuthService |
| 18 | defpackage/ojm.java | accessToken, refreshToken, tokenRefresh |
| 18 | defpackage/oq6.java | AuthService |
| 18 | defpackage/oxj.java | AUTH_2FA |
| 18 | defpackage/wpc.java | refreshToken |
| 18 | defpackage/x36.java | AuthService |
| 18 | defpackage/y1l.java | AuthService |
| 15 | defpackage/i79.java | InputPhoneScreen |
| 14 | ru/ok/android/externcalls/sdk/AuthRequiredException.java | Authorization |
| 13 | one/me/android/initialization/AccountInitializer.java | имя файла |
| 13 | one/me/android/media/service/OneMeMediaSessionService.java | имя файла |
| 13 | one/me/login/LoginScreen.java | имя файла |
| 13 | one/me/login/restrict/RestrictLoginScreen.java | имя файла |
| 13 | one/me/main/accountswitcher/AccountSwitcherBottomSheet.java | имя файла |
| 13 | one/me/net/ssl/api/InvalidSslSessionException.java | имя файла |
| 13 | one/me/sdk/login/LoginException.java | имя файла |
| 13 | one/me/sdk/net/ssl/tm/ApiTrustManager$UnacceptableAuthTypeCertificateException.java | имя файла |
| 13 | one/me/sdk/tasks/login/LoginException.java | имя файла |
| 13 | one/me/sdk/vendor/SystemServicesManager$PushTokenGeneratedListener.java | имя файла |
| 13 | one/me/settings/AccountActionsBottomSheet.java | имя файла |
| 13 | one/me/settings/devices/hintdialog/QrAuthHintBottomSheet.java | имя файла |
| 13 | one/me/settings/privacy/ui/ForgotPinCodeDialog.java | имя файла |
| 13 | ru/ok/android/api/core/ApiLoginException.java | имя файла |
| 13 | ru/ok/android/api/session/ApiRecreateSessionException.java | имя файла |
| 13 | ru/ok/android/api/session/ApiSessionChangedException.java | имя файла |
| 13 | ru/ok/android/externcalls/sdk/exceptions/ConversationNotPreparedException.java | имя файла |
| 13 | ru/ok/android/externcalls/sdk/sessionroom/exceptions/SessionRoomException.java | имя файла |
| 13 | ru/ok/android/externcalls/sdk/sessionroom/exceptions/SessionRoomInactiveException.java | имя файла |
| 13 | ru/ok/android/externcalls/sdk/sessionroom/exceptions/SessionRoomNotAdminException.java | имя файла |
| 13 | ru/ok/android/onelog/OneLogSessionEventNumbering.java | имя файла |
| 13 | ru/ok/tamtam/api/SessionSendLimitException.java | имя файла |
| 13 | ru/ok/tamtam/api/SessionSenderUnexpectedException.java | имя файла |
| 13 | ru/ok/tamtam/api/SessionTamErrorException.java | имя файла |
| 13 | ru/ok/tamtam/exception/SessionStateAnonException.java | имя файла |
| 13 | ru/ok/tamtam/login/LoginEventsByBus.java | имя файла |
| 13 | ru/ok/tamtam/models/stickers/StickerAuthorType.java | имя файла |
| 12 | defpackage/l79.java | InputPhoneScreen |
| 12 | defpackage/o79.java | InputPhoneScreen |
| 12 | defpackage/wi3.java | AUTH_OTP, ConfirmPhoneScreen |
| 10 | android/hardware/biometrics/BiometricPrompt$AuthenticationCallback.java | имя файла |
| 10 | android/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback.java | имя файла |
| 10 | android/hardware/camera2/CameraExtensionSession$StateCallback.java | имя файла |
| 10 | android/support/v4/media/session/MediaSessionCompat$ResultReceiverWrapper.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/CaptureSessionOnClosedNotCalledQuirk.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/CaptureSessionStuckQuirk.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/CloseCaptureSessionOnVideoQuirk.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/ConfigureSurfaceToSecondarySessionFailQuirk.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/DisableAbortCapturesOnStopWithSessionProcessorQuirk.java | имя файла |
| 10 | androidx/camera/camera2/compat/quirk/FinalizeSessionOnCloseQuirk.java | имя файла |
| 10 | androidx/media3/datasource/HttpDataSource$CleartextNotPermittedException.java | имя файла |
| 10 | androidx/media3/exoplayer/drm/DefaultDrmSession$UnexpectedDrmSessionException.java | имя файла |
| 10 | androidx/media3/exoplayer/drm/DefaultDrmSessionManager$MissingSchemeDataException.java | имя файла |
| 10 | androidx/media3/exoplayer/drm/DrmSession$DrmSessionException.java | имя файла |
| 10 | androidx/media3/session/MediaSessionService.java | имя файла |
| 10 | com/facebook/imagepipeline/platform/PreverificationHelper.java | имя файла |
| 10 | com/google/android/gms/auth/GoogleAuthException.java | имя файла |
| 10 | com/google/android/gms/auth/UserRecoverableAuthException.java | имя файла |
| 10 | com/google/android/gms/auth/api/accounttransfer/AccountTransferException.java | имя файла |
| 10 | com/google/android/gms/auth/api/signin/GoogleSignInAccount.java | имя файла |
| 10 | com/google/android/gms/auth/api/signin/SignInAccount.java | имя файла |
| 10 | com/vk/push/core/auth/Auth.java | имя файла |
| 10 | com/vk/push/core/auth/AuthTokenResult.java | имя файла |
| 10 | com/vk/push/core/auth/AuthorizedResult.java | имя файла |
| 10 | com/vk/push/core/push/InvalidateTokenResult.java | имя файла |
| 10 | com/vk/push/core/push/IsPushTokenExistResult.java | имя файла |
| 10 | com/vk/push/pushsdk/work/TokensHealthCheckWorker.java | имя файла |
| 10 | com/vk/push/pushsdk/work/scheduler/DeleteTokensFromServerWorker.java | имя файла |
| 10 | defpackage/bwb.java | AuthApi, AuthRequest |
| 10 | defpackage/m79.java | InputPhoneScreen |
| 10 | defpackage/wbi.java | AuthRequest, refreshToken |
| 10 | one/video/calls/sdk/net/signaling/wt/nal/internal/WebTransportSocket$openSession$1$1.java | имя файла |
| 10 | org/webrtc/CallSessionFileRotatingLogSink.java | имя файла |
| 10 | org/webrtc/Camera1Session.java | имя файла |
| 10 | org/webrtc/Camera2Session.java | имя файла |
| 10 | org/webrtc/CameraSession.java | имя файла |
| 10 | org/webrtc/SessionDescription.java | имя файла |
| 10 | ru/rustore/sdk/core/exception/RuStoreUserUnauthorizedException.java | имя файла |
| 10 | ru/rustore/sdk/pushclient/internal/work/DeletePushTokenIfNoHostsWorker.java | имя файла |
| 9 | com/google/android/gms/auth/api/signin/GoogleSignInOptions.java | AuthRequest, refreshToken |
| 9 | defpackage/gn0.java | refreshToken |
| 9 | defpackage/hg7.java | refreshToken |
| 9 | defpackage/p0b.java | api/v3/ws |
| 9 | defpackage/p73.java | accessToken |
| 9 | defpackage/qzb.java | accessToken |
| 9 | defpackage/sm0.java | refreshToken |
| 9 | defpackage/tp4.java | ConfirmPhoneScreen |
| 9 | defpackage/ug9.java | accessToken |
| 9 | defpackage/up4.java | ConfirmPhoneScreen |
| 9 | defpackage/zjn.java | refreshToken |
| 8 | defpackage/ty3.java | InputPhoneScreen |
| 7 | one/me/location/map/pick/PickLocationScreen.java | requestCode |
| 6 | defpackage/eb1.java | InputPhoneScreen |
| 5 | defpackage/aq4.java | ConfirmPhoneScreen |
| 5 | defpackage/u9m.java | Authorization |
| 5 | defpackage/wp4.java | ConfirmPhoneScreen |
| 5 | defpackage/zp4.java | ConfirmPhoneScreen |
| 5 | one/me/chats/picker/contacts/ContactsPickerScreen.java | requestCode |
| 5 | one/me/sdk/permissionhost/PermissionBottomSheet.java | requestCode |
| 5 | one/me/webapp/rootscreen/WebAppRootScreen.java | requestCode |
| 4 | defpackage/dr.java | InputPhoneScreen |
| 4 | defpackage/f60.java | ConfirmPhoneScreen |
| 4 | defpackage/ka9.java | ConfirmPhoneScreen, InputPhoneScreen |
| 4 | defpackage/so.java | InputPhoneScreen |
| 4 | defpackage/sx3.java | api2.oneme.ru |
| 4 | one/me/calls/ui/ui/incoming/CallIncomingScreen.java | requestCode |
| 4 | one/me/informer/ui/InformerBottomSheet.java | requestCode |
| 4 | one/me/pinbars/PinBarsWidget.java | requestCode |
| 4 | one/me/selfservice/ui/vendorautolock/VendorAutolockRationaleDialog.java | requestCode |
| 3 | defpackage/yj3.java | InputPhoneScreen |
| 3 | defpackage/yx9.java | api-tg.oneme.ru |
| 3 | one/me/login/a.java | имя файла |
| 3 | one/me/login/avatar/RegistrationAvatarScreen.java | имя файла |
| 3 | one/me/login/inputname/InputNameScreen.java | имя файла |
| 3 | one/me/login/inputphone/a.java | имя файла |
| 3 | one/me/login/neuroavatars/NeuroAvatarPickerBottomSheet.java | имя файла |
| 3 | one/me/login/neuroavatars/NeuroAvatarsScreen.java | имя файла |
| 3 | one/me/login/neuroavatars/RegistrationNeuroAvatarsScreen.java | имя файла |
| 3 | ru/ok/tamtam/login/a.java | имя файла |
| 3 | ru/ok/tamtam/login/b.java | имя файла |
| 2 | androidx/fragment/app/strictmode/GetTargetFragmentRequestCodeUsageViolation.java | requestCode |
| 2 | defpackage/g91.java | Authorization |
| 2 | defpackage/ki0.java | verifyCode |
| 2 | defpackage/ll.java | requestCode |
| 2 | defpackage/o57.java | api2.oneme.ru |
| 2 | defpackage/qv7.java | requestCode |
| 2 | defpackage/wz7.java | InputPhoneScreen |
| 2 | defpackage/x49.java | InputPhoneScreen |
| 2 | defpackage/xla.java | sessionToken |
| 1 | defpackage/a6l.java | AuthRequest |
| 1 | defpackage/an8.java | Authorization |
| 1 | defpackage/b28.java | sessionToken |
| 1 | defpackage/bqc.java | verifyCode |
| 1 | defpackage/c6l.java | AuthRequest |
| 1 | defpackage/cp5.java | verifyCode |
| 1 | defpackage/d6l.java | AuthResponse |
| 1 | defpackage/dp5.java | api2.oneme.ru |

## Ограничения

Одни названия, строки или их количество не устанавливают назначение сервера, порядок обмена или формат токенов.
Для этого нужно проследить вызывающие функции и поля сериализации, затем проверить журнал реального входа.

