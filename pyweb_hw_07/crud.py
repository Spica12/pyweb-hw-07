from conf.db import session
from conf.models import Student, Teacher, Group, Subject, Score

from my_select import choose_group, choose_student, choose_subject, choose_teacher

from datetime import datetime
import calendar


def user_input(field):
    return input(f"Enter {field}\n>>> ")


def input_date():
    def try_input(field):
        try:
            num = int(user_input("Year"))
        except ValueError:
            print("You entered not integer")
            
        return num

    # Enter Year
    while True:
        year = try_input("Year")
        if year > 0 and year <= datetime.now().year:
            break
        else:
            print("You entered not correct year")

    # Enter Month
    while True:
        month = try_input("Month")

        if month > 0 and month <= 12:
            break
        else:
            print("You entered not correct month")

    # Enter Day
    while True:
        day = try_input("Day")

        is_correct = True

        if day <= 0 and day > 31:
            is_correct = False
        if calendar.isleap(year) and day >= 29:
            is_correct = False
        if not calendar.isleap(year) and day >= 28:
            is_correct = False

        if is_correct:
            break
        else:
            print("You entered not correct day")

    return datetime(year=year, month=month, day=day)


def create_student():
    first_name = user_input("First name")
    last_name = user_input("Last name")
    group_id = choose_group()

    student = Student(first_name=first_name, last_name=last_name, group_id=group_id)

    session.add(student)
    session.commit()
    print(f"Added student{student.fullname}")
    session.close()


def create_teacher():
    first_name = user_input("First name")
    last_name = user_input("Last name")

    teacher = Teacher(first_name=first_name, last_name=last_name)

    session.add(teacher)
    session.commit()
    print(f"Added teacher {teacher.fullname}")
    session.close()


def create_group():
    group_name = user_input("Group name")

    group = Group(group_name=group_name)

    session.add(group)
    session.commit()
    print(f"Added group {group.group_name}")
    session.close()


def create_subject():
    subject_name = user_input("Subject name")
    teacher_id = choose_teacher()

    subject = Subject(subject_name=subject_name, teacher_id=teacher_id)

    session.add(subject)
    session.commit()
    print(f"Added subject {subject.subject_name}")
    session.close()


def create_score():
    student_id = choose_student()
    subject_id = choose_subject()
    score_ = user_input("Score")
    print("Enter date (format):")
    data_of = input_date()

    score = Score(
        student_id=student_id, subject_id=subject_id, score=score_, data_of=data_of
    )

    session.add(score)
    session.commit()
    print(f"Added score {score.score}")
    session.close()
