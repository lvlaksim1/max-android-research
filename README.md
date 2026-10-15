# MAX Android Research

Исследование Android-приложения **MAX** (`ru.oneme.app`), независимое от разработчика приложения.

## Исходный образец

| Параметр | Значение |
| --- | --- |
| Исходный файл | `base.apk` |
| Версия | 26.35.1 |
| Номер сборки | 6867 |
| Размер | 133 730 048 байт |
| SHA-256 | `e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc` |
| Минимальный Android API | 26 |
| Целевой Android API | 37 |

**Полный исходный APK опубликован как вложение выпуска GitHub:** [base.apk — точный исследовательский образец](https://github.com/lvlaksim1/max-android-research/releases/download/apk-26.35.1-6867/base.apk). GitHub проверил и сообщил размер 133 730 048 байт и SHA-256 `e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc`. Двоичный APK хранится в **Releases**, а не в истории Git: прямое добавление файла больше 100 МиБ в обычный Git запрещено самим GitHub. Это единственное разрешённое владельцем исключение для хранения большого исследовательского образца.

## Содержимое

- `docs/static-analysis-26.35.1.md` — первичный статический отчёт, границы доказанности.
- `evidence/sample.json` — идентификатор исследованного APK.
- `evidence/network-indicators.md` — обнаруженные в статическом анализе сетевые признаки, не подтверждённые реальными соединениями.
- `app-extract/` — небольшие текстовые файлы, действительно присутствующие в исследованном APK (с сохранением относительного пути).
- `tools/apk_inventory.py` — проверка контрольной суммы, список файлов и безопасная локальная распаковка полного APK.
- `tools/axml_events.py` — получение упорядоченных элементов из двоичного манифеста Android или другого двоичного XML.
- `tools/dex_index.py` — извлечение структурных счётчиков и отобранных сетевых строк из DEX.
- `scripts/check_repository_storage.py` — ограничение размера по политике repo-factory.

## Как восстановить файлы приложения

Скачать полный исследовательский образец из закреплённого выпуска, затем распаковать локально:

```bash
mkdir -p work
curl -fL "https://github.com/lvlaksim1/max-android-research/releases/download/apk-26.35.1-6867/base.apk" -o work/base.apk
python3 tools/apk_inventory.py work/base.apk --index work/files.json --extract work/apk-unpacked
python3 tools/axml_events.py work/base.apk AndroidManifest.xml > work/manifest-events.json
python3 tools/axml_events.py work/base.apk res/xml/network_security_config.xml > work/network-security-events.json
python3 tools/dex_index.py work/base.apk > work/dex-index.json
```

Точное совпадение SHA-256 проверяется программой `apk_inventory.py`. Альтернативно загрузить файл командой `gh release download apk-26.35.1-6867 --pattern base.apk --dir work`.

Предыдущий вариант с локальным файлом `base.apk` также допускается, если его SHA-256 точно совпадает с эталоном.

Прежние команды ниже приведены как вариант работы с локальным `base.apk`:

```bash
python3 tools/apk_inventory.py base.apk --index work/files.json --extract work/apk-unpacked
python3 tools/axml_events.py base.apk AndroidManifest.xml > work/manifest-events.json
python3 tools/axml_events.py base.apk res/xml/network_security_config.xml > work/network-security-events.json
python3 tools/dex_index.py base.apk > work/dex-index.json
```

Первая команда проверяет SHA-256 исходного образца, создаёт перечень всех файлов и распаковывает их в локальный каталог. Файлы `work/` не публикуются в Git. Для работы скриптов достаточно Python 3.10+ (внешние библиотеки не требуются).

**Ограничения:** статический разбор не доказывает фактического обмена с перечисленными серверами, порядка входа или способа доставки уведомлений. Подтверждение требует отдельной записи реального запуска. Не добавляйте в публичный репозиторий токены, приватные переписки и сведения об учётных записях.

## Политика хранения

Репозиторий создан посредством [repo-factory](https://github.com/lvlaksim1/repo-factory) с профилем `project-manager`. Правила хранения фабрики продолжают действовать: не более 5 МиБ на отслеживаемый Git-файл; никакие исполняемые APK/DEX/SO не добавляются в историю Git. Для одного эталонного образца владелец разрешил исключение **в виде вложения GitHub Release**. Дополнительные копии и устаревшие версии APK не публикуются.

Текущий этап: базовое исследование структуры APK; полный неизменённый эталон доступен в выпуске для углублённого анализа.
