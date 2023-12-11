from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(120))


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(120))
    teacher_id = Column(
        Integer, ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    group_id = Column(
        Integer, ForeignKey("groups.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    student_id = Column(
        Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    subject_id = Column(
        Integer, ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    score = Column(Integer)
    data_of = Column(Date, nullable=False)
