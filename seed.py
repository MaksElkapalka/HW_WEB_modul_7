from datetime import datetime
import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.conect_db import session
from conf.models import Teacher, Student, Group, Subject, Grade


fake = Faker("uk-UA")


def insert_groups():
    list_groups = ["Group A", "Group B", "Group C"]
    for g in list_groups:
        group = Group(name=g)
        session.add(group)


def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        session.add(teacher)


def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(6):
        teacher = random.choice(teachers)
        subject = Subject(name=fake.word(), teacher=teacher)
        session.add(subject)


def insert_students():
    groups = session.query(Group).all()
    for _ in range(30):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=random.choice(groups),
        )
        session.add(student)


def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")

    for student in students:
        for subject in subjects:
            for _ in range(20):
                mark = random.randint(1, 100)
                grade = Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    grade=mark,
                    date=fake.date_between(start_date=start_date),
                )
                session.add(grade)


if __name__ == "__main__":
    try:
        # Видалення всіх записів з таблиць
        session.query(Grade).delete()
        session.query(Student).delete()
        session.query(Subject).delete()
        session.query(Teacher).delete()
        session.query(Group).delete()
        session.commit()

        insert_groups()
        session.commit()

        insert_teachers()
        session.commit()

        insert_subjects()
        session.commit()

        insert_students()
        session.commit()

        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
