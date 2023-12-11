from conf.db import session
from conf.models import Student, Teacher, Group, Subject, Score

from my_select import (
    choose_group,
    choose_student,
    choose_subject,
    choose_teacher,
    choose_scores,
)

from datetime import datetime
import calendar


def user_input(field):
    return input(f"Enter {field}\n>>> ")


def input_date():
    def try_get_int_input(field):
        try:
            num = int(user_input(field))
        except ValueError:
            print("You entered not integer")

        return num

    # Enter Year
    while True:
        year = try_get_int_input("Year")

        if year > 0 and year <= datetime.now().year:
            break

        print("You entered not correct year")

    # Enter Month
    while True:
        month = try_get_int_input("Month")
        if month > 0 and month <= 12:
            break

        print("You entered not correct month")

    # Enter Day
    while True:
        day = try_get_int_input("Day")

        is_correct = True

        if day <= 0 and day > 31:
            is_correct = False
        if calendar.isleap(year) and day >= 29:
            is_correct = False
        if not calendar.isleap(year) and day >= 28:
            is_correct = False

        if is_correct:
            break

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


def update_student():
    student_id = choose_student()

    student = session.query(Student).filter_by(id=student_id).first()

    new_first_name = user_input("First name")
    if new_first_name:
        student.first_name = new_first_name

    new_last_name = user_input("Last name")
    if new_last_name:
        student.last_name = new_last_name

    new_group_id = choose_group()
    if new_group_id:
        student.group_id = new_group_id

    session.commit()


def update_teacher():
    teacher_id = choose_teacher()

    teacher = session.query(Teacher).filter_by(id=teacher_id).first()

    new_first_name = user_input("First name")
    if new_first_name:
        teacher.first_name = new_first_name

    new_last_name = user_input("Last name")
    if new_last_name:
        teacher.last_name = new_last_name

    session.commit()


def update_group():
    group_id = choose_group()

    group = session.query(Group).filter_by(id=group_id).first()

    new_group_name = user_input("Group name")
    if new_group_name:
        group.group_name = new_group_name

    session.commit()


def update_subject():
    subject_id = choose_subject()

    subject = session.query(Subject).filter_by(id=subject_id).first()

    new_subject_name = user_input("Subject name")
    if new_subject_name:
        subject.subject_name = new_subject_name

    session.commit()


def update_score():
    score_id = choose_scores()

    score = session.query(Score).filter_by(id=score_id).first()

    new_student_id = choose_student()
    if new_student_id:
        score.student_id = new_student_id

    new_subject_id = choose_subject()
    if new_subject_id:
        score.subject_id = new_subject_id

    new_score = user_input("Score")
    if new_score:
        score.score = new_score

    print("Enter date (format):")
    new_data_of = input_date()
    if new_data_of:
        score.data_of = new_data_of

    session.commit()


def delete_student():
    student_id = choose_student()
    student = session.query(Student).filter_by(id=student_id).first()
    session.delete(student)
    session.commit()


def delete_teacher():
    teacher_id = choose_teacher()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    session.delete(teacher)
    session.commit()


def delete_group():
    group_id = choose_group()
    group = session.query(Group).filter_by(id=group_id).first()
    session.delete(group)
    session.commit()


def delete_subject():
    subject_id = choose_subject()
    subject = session.query(Subject).filter_by(id=subject_id).first()
    session.delete(subject)
    session.commit()


def delete_score():
    score_id = choose_scores()
    score = session.query(Score).filter_by(id=score_id).first()
    session.delete(score)
    session.commit()
