from conf.db import session
from conf.models import Student, Teacher, Group, Subject, Score

from sqlalchemy import func, desc

from pprint import pprint


def select_1():
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


if __name__ == "__main__":
    print("--- Select 1 ---")
    result = select_1()
    pprint(result)
