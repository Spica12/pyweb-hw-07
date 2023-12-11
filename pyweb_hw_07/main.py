import argparse

from conf.db import create_database, drop_database
from seeds.init import init_random_data

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
select = arguments.get("select")


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


def main():
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


if __name__ == "__main__":
    main()
