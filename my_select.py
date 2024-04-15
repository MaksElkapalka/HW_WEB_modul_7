from conf.conect_db import session
from conf.models import Teacher, Student, Grade, Subject, Group
from sqlalchemy import desc, func


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    result = (
        session.query(
            Student.first_name,
            Student.last_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    print(result)


# Знайти студента із найвищим середнім балом з певного предмета.
def select_2():
    subject_name = session.query(Subject.name).first()[0]

    result = (
        session.query(
            Student.first_name,
            Student.last_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )
    print(f"Subject {subject_name} --> {result}")


# Знайти середній бал у групах з певного предмета.
def select_3():
    subject_name = session.query(Subject.name).first()[0]

    result = (
        session.query(
            Group.name.label("group_name"),
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    print(result)


# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
    print(result)


# Знайти які курси читає певний викладач.
def select_5():
    teacher_id = session.query(Teacher.id).first()[0]
    result = (
        session.query(Subject.name).join(Teacher).filter(Teacher.id == teacher_id).all()
    )
    print(result)


# Знайти список студентів у певній групі.
def select_6():
    group_name = session.query(Group.name).first()[0]
    result = (
        session.query(Student.first_name, Student.last_name)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )
    print(f'"{group_name}" {result}')


# Знайти оцінки студентів у окремій групі з певного предмета
def select_7():
    subject_id = session.query(Subject.id).first()[0]
    group_id = session.query(Group.id).first()[0]

    results = (
        session.query(Student.first_name, Student.last_name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .order_by(Student.last_name)
        .all()
    )

    for first_name, last_name, grade in results:
        print(f"Student: {first_name} {last_name}, Grade: {grade}")


# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8():
    teacher = session.query(Teacher.id, Teacher.first_name, Teacher.last_name).first()

    avg_grade = (
        session.query(func.avg(Grade.grade))
        .join(Subject)
        .filter(Subject.teacher_id == teacher[0])
        .scalar()
    )

    print(f"Average grade given by {teacher[1]} {teacher[2]}: {avg_grade}")


#  Знайти список курсів, які відвідує певний студент.
def select_9():
    student = session.query(Student.id, Student.first_name, Student.last_name).first()
    results = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student[0])
        .distinct()
        .all()
    )

    print(
        f"Student {student[1]} {student[2]} attends subjects: {[result[0] for result in results]}"
    )


#  Список курсів, які певному студенту читає певний викладач.
def select_10():
    student = session.query(Student.id, Student.first_name, Student.last_name).first()
    teacher = session.query(Teacher.id, Teacher.first_name, Teacher.last_name).first()

    results = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Subject.teacher_id == teacher[0])
        .filter(Student.id == student[0])
        .distinct()
        .all()
    )

    result = [course[0] for course in results]

    print(result)


if __name__ == "__main__":
    # select_1()
    select_2()
    # select_3()
    # select_4()
    # select_5()
    # select_6()
    # select_7()
    # select_8()
    # select_9()
    # select_10()
