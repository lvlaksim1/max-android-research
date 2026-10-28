# Подтверждённые сведения менеджера

## Назначение проекта
- Состояние: исследовательский репозиторий для воспроизводимого изучения Android-приложения MAX `ru.oneme.app` по предоставленному APK и журналам, не исходный код приложения.
- source: `.context/project/identity.md`, `.context/project/architecture.md`
- authority: verified-repository

## Эталонный образец и границы доказанности
- Состояние, записанное на 15.10.2026: проектные сведения фиксируют образец MAX 26.35.1 (6867) с SHA-256 `e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc` и размещение в GitHub Release; новая проверка выпуска и бинарного файла этим обновлением менеджера не проводилась.
- source: `.context/current/state.md`, `.context/project/constraints.md`
- authority: verified-repository; historical project status

## Подтверждённая граница исследования
- Зафиксированные результаты статического анализа и опубликованные инструменты не являются доказательством фактической серверной авторизации или реальных сетевых запросов. Динамический анализ требует отдельного наблюдения и проверки.
- source: `.context/current/state.md`, `.context/project/goals.md`
- authority: verified-repository

## Хранение и конфиденциальность
- Исходный APK не изменяется и не включается в историю Git; публичный репозиторий содержит только допустимые небольшие материалы, без личных данных, переписки и токенов.
- source: `.context/project/constraints.md`
- authority: owner-directive recorded in repository; verified-repository
