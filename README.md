# О проекте

Данный проект предназначен для автоматизированной проверки корректности работы веб-сервиса
[DNS](https://www.dns-shop.ru/).

Так же имеется пример автотеста мобильного приложения
["Конвертер"](https://play.google.com/store/apps/details?id=com.techsial.android.unitconverter&hl=ru).

# Структура проекта

- data - модули, содержащие данные веб-страниц
- pages - модули, содержащие методы для работы с веб-страницами
- conftest - модуль, содержащий предусловия автотестов
- test_smoke - модуль, содержащий тела UI тестов
- test_api - модуль, содержащий тела API тестов
- test_mobile - модуль, содержащий тела тестов мобильного приложения

# Установка

1. Установить python.
2. Установить любое IDE, например,
   [PyCharm Community](https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows).
3. Скачать веб-драйвер [Chrome](https://chromedriver.chromium.org/downloads).
4. Добавить веб-драйвер в переменное окружение PATH.
5. Открыть проект в IDE.
6. Установить зависимости.  
   В терминале прописать команду:
   `pip install -r requirements.txt`.

Проект готов к запуску.

Для запуска теста мобильного приложения дополнительно необходимо:

1. Скачать [apk](https://disk.yandex.ru/d/4NEVxAlHTC2GMA) приложения.
2. В файле configuration_data.py в словаре CAPABILITIES для ключа "appium:app" значение "PATH_APK"   
   заменить на путь до apk приложения.
2. Установить [Android Studio](https://developer.android.com/studio).
3. Установить [Appium Server](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4).
4. Добавить ANDROID_HOME (путь по-умолчанию: C:\Users\USER_NAME\AppData\Local\Android\Sdk)  
   и JAVA_HOME (путь по-умолчанию: C:\Program Files\Java\jdk-version) в переменное окружение PATH.  
   В случае отсутствия Java JDK можно скачать его с данного
   [сайта](https://www.oracle.com/cis/java/technologies/downloads/).

# Запуск

Для запуска тестов мобильного приложения необходимо в Android Studio запустить эмуляцию Pixel 4 Android Version 12.0,  
затем запустить Appium Server с локальным хостом 127.0.0.1 и портом 4723.

Для простого запуска проекта необходимо в терминале прописать команду:  
`pytest`.

Для параллельного запуска проекта в несколько потоков необходимо в терминале прописать команду:  
`pytest -n COUNT`, где `COUNT` - число потоков.

Для сохранения отчетов о прохождении тестов необходимо в терминале прописать команду:  
`pytest --alluredir=ПУТЬ`, где `ПУТЬ` - это путь до директории, где будут сохранены отчеты.

Для просмотра сохраненных отчетов необходимо в терминале прописать команду:  
`allure serve ПУТЬ`, где `ПУТЬ` - это путь до директории, где сохранены отчеты.