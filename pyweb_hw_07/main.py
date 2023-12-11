import argparse

from conf.db import create_database, drop_database
from crud import (create_group, create_score, create_student, create_subject,
                  create_teacher, delete_group, delete_score, delete_student,
                  delete_subject, delete_teacher, update_group, update_score,
                  update_student, update_subject, update_teacher)
from my_select import (main_select, read_all_groups, read_all_scores,
                       read_all_students, read_all_subjects, read_all_teachers)
from seeds.init import init_random_data

parser = argparse.ArgumentParser(
    description="All supported command:\n"
    "--action create --model database       - create new database\n"
    "--action create --model student        - add new student into database\n"
    "--action create --model teacher        - add new teacher into database\n"
    "--action create --model group          - add new group into database\n"
    "--action create --model subject        - add new subject into database\n"
    "--action create --model score          - add new score into database\n"
    "--action read --model student          - read all students from database\n"
    "--action read --model teacher          - read all teachers from database\n"
    "--action read --model group            - read all groups from database\n"
    "--action read --model subject          - read all subjects from database\n"
    "--action read --model score            - read all scores from database\n"
    "--action update --model student        - update record student in database\n"
    "--action update --model teacher        - update record in database\n"
    "--action update --model group          - update record group in database\n"
    "--action update --model subject        - update record subject in database\n"
    "--action update --model score          - update record score in database\n"
    "--action delete -model database        - drop exist database\n"
    "--action delete --model student        - delete student from database\n"
    "--action delete --model teacher        - delete teacher from database\n"
    "--action delete --model group          - delete group from database\n"
    "--action delete --model subject        - delete subject from database\n"
    "--action delete --model score          - delete score from database\n"
    "\n"
    "ATTENTION: After created new database need to enter 'alembic upgrade head'",
    formatter_class=argparse.RawTextHelpFormatter,
)

parser.add_argument("--action", "-a")
parser.add_argument("--model", "-m")
parser.add_argument("--select", "-s")

arguments = vars(parser.parse_args())

action = arguments.get("action")
model = arguments.get("model")
number_select = arguments.get("select")


def parse_create_argument():
    match model.lower():
        case "database":
            create_database()
        case "student":
            create_student()
        case "teacher":
            create_teacher()
        case "group":
            create_group()
        case "subject":
            create_subject()
        case "score":
            create_score()
        case _:
            print("You entered not correct arguments")


def parse_read_argument():
    match model.lower():
        case "database":
            print("This action is not supported for the database")
        case "students":
            read_all_students()
        case "teachers":
            read_all_teachers()
        case "groups":
            read_all_groups()
        case "subjects":
            read_all_subjects()
        case "scores":
            read_all_scores()
        case _:
            print("You entered not correct arguments")


def parse_update_argument():
    match model.lower():
        case "database":
            print("This action is not supported for the database.")
        case "student":
            update_student()
        case "teacher":
            update_teacher()
        case "group":
            update_group()
        case "subject":
            update_subject()
        case "score":
            update_score()
        case _:
            print("You entered not correct arguments")


def parse_delete_argument():
    match model.lower():
        case "database":
            drop_database()
        case "student":
            delete_student()
        case "teacher":
            delete_teacher()
        case "group":
            delete_group()
        case "subject":
            delete_subject()
        case "score":
            delete_score()
        case _:
            print("You entered not correct arguments")


def main():
    if action:
        match action.lower():
            case "create":
                parse_create_argument()
            case "read":
                parse_read_argument()
            case "update":
                parse_update_argument()
            case "delete":
                parse_delete_argument()
            case "random":
                init_random_data()
            case _:
                print("This action is not supported for the database")

    elif number_select:
        main_select(number_select)
    else:
        print("To get all commands enter 'main.py --help'")


if __name__ == "__main__":
    print("--- PyWEB Homework-07 ---")

    main()

    print("---  ---")
