## Python WEB Homework-07 "ORM SQLAlchemy"

1) У командному рядку запустити Docker контейнер, де замість ```some-postgres```та ```mysecretpassword``` придумати свою назву контейнера та пароль до БД:

```
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

2) Реалізувати модель **SQLAlchemy**, для таблиць:
    - Таблиця Студентів;
    - Таблиця Груп;
    - Таблиця Викладачів;
    - Таблиця Предметів із вказівкою викладача, який читає предмет;
    - Таблиця Оцінок з предметів для кожного студента із зазначенням коли оцінку отримано.

3) Створити за допомогою ```alembic``` міграції у базі даних.

4) Написати скріпт ```seed.py``` та заповнити отриману базу даних за допомогою пакета ```Faker```, використовувая механізм сесії ```SQLAlchemy```:
    - 30-50 випадкових студентів;
    - 3 групи;
    - 5-8 предметів;
    - 3-5 викладача;
    - до 20 оцінок у кожного студента з усіх предметів;

5) Оформити окремий файл ```my_select.py``` де будуть 12 функцій від ```select_1``` до ```select_12```. Зробити вибірки з отриманої бази даних:

    1) Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2) Знайти студента із найвищим середнім балом з певного предмета.
    3) Знайти середній бал у групах з певного предмета.
    4) Знайти середній бал на потоці (по всій таблиці оцінок).
    5) Знайти які курси читає певний викладач.
    6) Знайти список студентів у певній групі.
    7) Знайти оцінки студентів у окремій групі з певного предмета.
    8) Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9) Знайти список курсів, які відвідує певний студент.
    10) Список курсів, які певному студенту читає певний викладач.
    11) Додатковий. Середній бал, який певний викладач ставить певному студентові.
    12) Додатковий. Оцінки студентів у певній групі з певного предмета на останньому занятті.

6) Додатково реалізувати повноцінну **CLI** програму для **CRUD** операцій із базою даних. Використовуйте для цього модуль ```argparse``` :
    - Команда ```--action``` або ```-a``` - для операцій **CRUD**
        - ```create``` - для **створення** запису;
        - ```read``` - для **читання** запису;
        - ```update``` - для **оновлення** запису;
        - ```delete``` - для **видалення** запису;
        - ```random``` - для **рандомного** наповнення бази даних ;

    - Команда ```--model``` або ```-a``` - для вказівки над якою моделлю проводиться операція.
        - ```Student``` - для моделі **Студент**;
        - ```Teacher``` - для моделі **Вчитель**;
        - ```Group``` - для моделі **Група**;
        - ```Student``` - для моделі **Студент**;
        - ```Student``` - для моделі **Студент**;

    - Команда ```--select``` або ```-s``` - для вказівки який запит необхідно виконати.
        - ```help``` - вивести **інформацію про всі можливі запити**;
        - ```1-12``` - вивести **запит №1**, де цифра - це номер запиту;
