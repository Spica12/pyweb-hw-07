import sys
import os


# Отримати шлях до поточного каталогу (де розташований поточний файл)
current_dir = os.path.dirname(__file__)

# Отримати шлях до кореневого каталогу (вище на один рівень)
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Додати кореневий каталог до системи шляхів Python для можливості імпорту з модулів db та models
sys.path.append(root_dir)


import random
from faker import Faker

from conf.models import Student, Group, Teacher, Subject, Score
from conf.db import session

from sqlalchemy.exc import SQLAlchemyError


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
MAX_SCORES = 20

SUBJECTS = [
    "Mathematic",
    "Computer Science",
    "Software",
    "Farm Management",
    "Agriculture",
    "Astronomy",
    "Chemistry",
    "Biology",
    "Physics",
    "Geography",
]

fake = Faker("uk-Ua")


def insert_groups():
    first_letter_for_group = ["M", "E", "C", "D", "B"]
    second_letter_for_group = ["a", "f", "b", "c"]

    print("Insert groups into database:")
    for _ in range(NUMBER_GROUPS):
        random_first_letter = random.choice(first_letter_for_group)
        random_second_letter = random.choice(second_letter_for_group)
        group_name = f"{random_first_letter}0{random_second_letter}"

        group = Group(group_name=group_name)
        session.add(group)

        print(f"Added group {group.group_name} .")


def insert_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=random.randint(1, NUMBER_GROUPS),
        )
        session.add(student)

        print(f"Added student {student.fullname}.")


def insert_teacher():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        session.add(teacher)

        print(f"Added teacher {teacher.fullname}.")


def insert_subject():
    for _ in range(NUMBER_SUBJECTS):
        subject = Subject(
            subject_name=random.choice(SUBJECTS),
            teacher_id=random.randint(1, NUMBER_TEACHERS),
        )
        session.add(subject)

        print(f"Added subject {subject.subject_name}.")


def insert_scores():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for _ in range(MAX_SCORES):
            score = Score(
                student_id=student.id,
                subject_id=random.choice(subjects).id,
                score=random.randint(1, 99),
                data_of=fake.date_between(start_date="-5y"),
            )
            session.add(score)
        print(f"Added score for {student.fullname}.")


if __name__ == "__main__":
    try:
        # Добавляємо рандомно групи
        # insert_groups()

        # Добавляємо рандомно студентів
        # insert_students()

        # Добавляємо рандомно вчителя
        # insert_teacher()

        # Добавляємо рандомно предмет
        # insert_subject()

        # Добавляємо рандомно оцінки для кожного студента
        insert_scores()

    except SQLAlchemyError as err:
        print(err)
        session.rollback
        print("Data wasn't saved into database")

    finally:
        session.commit()
        print("Data was saved into database")
        session.close()
