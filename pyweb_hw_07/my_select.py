from conf.db import session
from conf.models import Student, Teacher, Group, Subject, Score

from sqlalchemy import func, desc, and_


def choose_student():
    students = session.query(Student).all()

    for student in students:
        print(f"{student.id}. {student.fullname}")

    return int(input("Choose number of student: \n>>> "))


def choose_teacher():
    teachers = session.query(Teacher).all()

    for teacher in teachers:
        print(f"{teacher.id}. {teacher.fullname}")

    return int(input("Choose number of teacher: \n>>> "))


def choose_group():
    groups = session.query(Group).all()

    for group in groups:
        print(f"{group.id}. {group.group_name}")

    return int(input("Choose number of group: \n>>> "))


def choose_subject():
    subjects = session.query(Subject).all()

    for subject in subjects:
        print(f"{subject.id}. {subject.subject_name}")

    return int(input("Choose number of subject: \n>>> "))


def select_1():
    print(
        "--- Select 1 ---\nЗнайти 5 студентів із найбільшим середнім балом з усіх предметів."
    )
    students = []

    result = (
        session.query(
            Student.id,
            Student.fullname,
            func.round(func.avg(Score.score), 2).label("avg_score"),
        )
        .select_from(Score)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_score"))
        .limit(5)
    )
    columns = ["id", "fullname", "avg_score"]
    for student in result:
        s = [dict(zip(columns, (student.id, student.fullname, student.avg_score)))]
        students.append(s)

    return students


def select_2():
    print(
        "--- Select 2 ---\nЗнайти студента із найвищим середнім балом з певного предмета."
    )
    num_subject = choose_subject()

    students = (
        session.query(
            Student.id,
            Subject.subject_name,
            Student.fullname,
            func.round(func.avg(Score.score), 2).label("avg_score"),
        )
        .select_from(Score)
        .join(Student)
        .join(Subject)
        .group_by(Subject.subject_name, Student.id)
        .order_by(desc("avg_score"))
        .filter(Subject.id == num_subject)
        .limit(1)
    )
    for s in students:
        columns = ["subject", "id", "student", "avg_score"]
        student = [dict(zip(columns, (s.subject_name, s.id, s.fullname, s.avg_score)))]

    return student


def select_3():
    print("--- Select 3 ---\nЗнайти середній бал у групах з певного предмета.")
    num_subject = choose_subject()

    response = (
        session.query(
            Subject.subject_name,
            Group.group_name,
            func.round(func.avg(Score.score), 2).label("avg_score"),
        )
        .select_from(Score)
        .join(Student)
        .join(Subject)
        .join(Group)
        .group_by(Subject.subject_name, Group.group_name)
        .order_by(desc("avg_score"))
        .filter(Subject.id == num_subject)
        .all()
    )
    result = []
    columns = ["subject", "group", "avg_score"]
    for g in response:
        r = [dict(zip(columns, (g.subject_name, g.group_name, g.avg_score)))]
        result.append(r)

    return result


def select_4():
    print("--- Select 4 ---\nЗнайти середній бал на потоці (по всій таблиці оцінок).")

    response = (
        session.query(
            func.round(func.avg(Score.score), 2).label("avg_score"),
        )
        .select_from(Score)
        .all()
    )
    result = []
    columns = ["avg_score"]
    for g in response:
        r = [dict(zip(columns, (g.avg_score,)))]
        result.append(r)

    return result


def select_5():
    print("--- Select 5 ---\nЗнайти які курси читає певний викладач.")
    num_teacher = choose_teacher()

    response = (
        session.query(
            Teacher.fullname,
            Subject.subject_name,
        )
        .select_from(Subject)
        .join(Teacher)
        .group_by(Teacher.fullname, Subject.subject_name)
        .filter(Teacher.id == num_teacher)
        .all()
    )
    result = []
    columns = ["teacher", "subject"]
    for g in response:
        r = [dict(zip(columns, (g.fullname, g.subject_name)))]
        result.append(r)

    return result


def select_6():
    print("--- Select 6 ---\nЗнайти список студентів у певній групі.")
    num_group = choose_group()

    response = (
        session.query(
            Group.group_name,
            Student.fullname,
        )
        .select_from(Student)
        .join(Group)
        .group_by(Group.group_name, Student.fullname)
        .filter(Group.id == num_group)
        .all()
    )
    result = []
    columns = ["group", "student"]
    for g in response:
        r = [dict(zip(columns, (g.group_name, g.fullname)))]
        result.append(r)

    return result


def select_7():
    print(
        "--- Select 7 ---\nЗнайти оцінки студентів у окремій групі з певного предмета."
    )
    num_subject = choose_subject()
    num_group = choose_group()

    response = (
        session.query(
            Subject.subject_name,
            Group.group_name,
            Student.fullname,
            Score.score,
        )
        .select_from(Score)
        .join(Subject)
        .join(Student)
        .join(Group)
        .group_by(Subject.subject_name, Group.group_name, Student.fullname, Score.score)
        .filter(and_(Subject.id == num_subject, Group.id == num_group))
        .all()
    )
    result = []
    columns = ["subject", "group", "student", "score"]
    for g in response:
        r = [
            dict(
                zip(
                    columns,
                    (g.subject_name, g.group_name, g.fullname, g.score),
                )
            )
        ]
        result.append(r)

    return result


def select_8():
    print(
        "--- Select 8 ---\nЗнайти середній бал, який ставить певний викладач зі своїх предметів."
    )
    num_teacher = choose_teacher()

    response = (
        session.query(
            Teacher.fullname,
            Subject.subject_name,
            func.round(func.avg(Score.score), 2).label("avg_score"),
        )
        .select_from(Score)
        .join(Subject)
        .join(Teacher)
        .group_by(Teacher.fullname, Subject.subject_name)
        .filter(Teacher.id == num_teacher)
        .all()
    )
    result = []
    columns = ["teacher", "subject", "avg_score"]
    for g in response:
        r = [
            dict(
                zip(
                    columns,
                    (g.fullname, g.subject_name, g.avg_score),
                )
            )
        ]
        result.append(r)

    return result


def choose_select(number):
    match number:
        case "1":
            return select_1()
        case "2":
            return select_2()
        case "3":
            return select_3()
        case "4":
            return select_4()
        case "5":
            return select_5()
        case "6":
            return select_6()
        case "7":
            return select_7()
        case "8":
            return select_8()
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case _:
            pass


def main_select(number):
    result = choose_select(number)

    if result:
        for row in result:
            print(row)
    else:
        print("Something wrong")


if __name__ == "__main__":
    main_select(1)
