import argparse

from conf.db import create_database, drop_database
from seeds.init import init_random_data
from my_select import main_select

parser = argparse.ArgumentParser(description="Student&Teacher&Score")

parser.add_argument(
    "--action", "-a", help="Command: init, create, read, update, delete, random, "
)
parser.add_argument(
    "--model", "-m", help="DATABASE, Student, Group, Teacher, Subject, Score"
)
parser.add_argument("--select", "-s", help="Choose number of select")
parser.add_argument("--init", help="Create new DB (If DB exists, it will be drop)")

arguments = vars(parser.parse_args())
print(arguments)

action = arguments.get("action")
model = arguments.get("model")
number_select = arguments.get("select")


def parse_create_argument():
    match model.lower():
        case "database":
            create_database()


def parse_read_argument():
    match model.lower():
        case "database":
            print("This action is not supported for the database")


def parse_update_argument():
    match model.lower():
        case "database":
            print("This action is not supported for the database.")


def parse_delete_argument():
    match model.lower():
        case "database":
            drop_database()


def get_help():
    message = (
        "\nAll supported command in this app:",
        "--action create -model database        - create new database",
        "--action drop -model database          - drop exist database",
        "--action random                        - insert random data to database",
        "--select 1                             - Знайти 5 студентів із найбільшим середнім балом з усіх предметів.",
        "--select 2                             - Знайти студента із найвищим середнім балом з певного предмета."
        "--select 3                             - Знайти середній бал у групах з певного предмета.",
        "--select 4                             - Знайти середній бал на потоці (по всій таблиці оцінок).",
        "--select 5                             - Знайти які курси читає певний викладач.",
        "--select 6                             - Знайти список студентів у певній групі.",
        "--select 7                             - Знайти оцінки студентів у окремій групі з певного предмета.",
        "--select 8                             - Знайти середній бал, який ставить певний викладач зі своїх предметів.",
        "--select 9                             - Знайти список курсів, які відвідує певний студент.",
        "10) Список курсів, які певному студенту читає певний викладач.",
        "11) Додатковий. Середній бал, який певний викладач ставить певному студентові.",
        "12) Додатковий. Оцінки студентів у певній групі з певного предмета на останньому занятті.",
    )

    for row in message:
        print(row)


def main():
    if action:
        match action.lower():
            case "create":
                parse_create_argument()
            case "read":
                pass
            case "update":
                pass
            case "delete":
                parse_delete_argument()
            case "random":
                init_random_data()
            case "init":
                pass
            case "help":
                get_help()

    elif number_select:
        main_select(number_select)


if __name__ == "__main__":
    print("--- PyWEB Homework-07 ---")

    main()

    print("---  ---")
