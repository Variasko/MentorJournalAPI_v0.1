from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, create_engine, inspect, text
import psycopg2
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase

class Base(DeclarativeBase): pass

class Activist(Base):
    __tablename__ = 'Activist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    activistTypeId = Column(Integer, ForeignKey('ActivistType.id'), nullable=False)

    student = relationship("Student", back_populates="activists")
    activistType = relationship("ActivistType", back_populates="activists")

class ActivistType(Base):
    __tablename__ = 'ActivistType'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    activists = relationship("Activist", back_populates="activistType")

class Admin(Base):
    __tablename__ = 'Admin'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    login = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)

    person = relationship("Person", back_populates="admin")

class AttendingClassHours(Base):
    __tablename__ = 'AttendingClassHours'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    isVisited = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="attendingClassHours")

class DegreeOfKinship(Base):
    __tablename__ = 'DegreeOfKinship'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    parrents = relationship("Parrent", back_populates="degreeOfKinship")

class Dormitory(Base):
    __tablename__ = 'Dormitory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    room = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="dormitories")

class Event(Base):
    __tablename__ = 'Event'
    id = Column(Integer, primary_key=True, autoincrement=True)
    eventTypeId = Column(Integer, ForeignKey('EventType.id'), nullable=False)
    targent = Column(String(100), nullable=False)
    result = Column(String(1000), nullable=False)
    date = Column(Date, nullable=False)
    groupId = Column(Integer, ForeignKey('Group.id'), nullable=False)
    workPlanReportId = Column(Integer, ForeignKey('WorkPlanReport.id'), nullable=False)

    eventType = relationship("EventType", back_populates="events")
    group = relationship("Group", back_populates="events")
    workPlanReport = relationship("WorkPlanReport", back_populates="events")

class EventType(Base):
    __tablename__ = 'EventType'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    events = relationship("Event", back_populates="eventType")

class Group(Base):
    __tablename__ = 'Group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(Integer, nullable=False)
    mentorId = Column(Integer, ForeignKey('Mentor.personId'), nullable=False)
    specificationId = Column(Integer, ForeignKey('Specification.id'), nullable=False)
    isByuget = Column(Boolean, nullable=False)
    recruitmentYear = Column(String(2), nullable=False)

    mentor = relationship("Mentor", back_populates="groups")
    specification = relationship("Specification", back_populates="groups")
    events = relationship("Event", back_populates="group")
    studentInGroups = relationship("StudentInGroup", back_populates="group")
    parrentConferences = relationship("ParrentConference", back_populates="group")

class GroupSocialStatus(Base):
    __tablename__ = 'GroupSocialStatus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    socialStatusId = Column(Integer, ForeignKey('SocialStatus.id'), nullable=False)
    editDate = Column(Date, nullable=False)

    student = relationship("Student", back_populates="groupSocialStatuses")
    socialStatus = relationship("SocialStatus", back_populates="groupSocialStatuses")

class HobbieType(Base):
    __tablename__ = 'HobbieType'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    studentHobbies = relationship("StudentHobbie", back_populates="hobbieType")

class IndividualWorkWithParrent(Base):
    __tablename__ = 'IndividualWorkWithParrent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    parrentId = Column(Integer, ForeignKey('Parrent.personId'), nullable=False)
    topic = Column(String(1000), nullable=False)
    result = Column(String(1000), nullable=False)

    parrent = relationship("Parrent", back_populates="individualWorkWithParrents")

class IndividualWorkWithStudent(Base):
    __tablename__ = 'IndividualWorkWithStudent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    topic = Column(String(1000), nullable=False)
    result = Column(String(1000), nullable=False)

    student = relationship("Student", back_populates="individualWorkWithStudents")

class Mentor(Base):
    __tablename__ = 'Mentor'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    category = Column(String(6), nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)

    person = relationship("Person", back_populates="mentor")
    groups = relationship("Group", back_populates="mentor")

class MentorObservationList(Base):
    __tablename__ = 'MentorObservationList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    characteristic = Column(String(1000), nullable=False)

    student = relationship("Student", back_populates="mentorObservationLists")

class Parrent(Base):
    __tablename__ = 'Parrent'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    degreeOfkinshipId = Column(Integer, ForeignKey('DegreeOfKinship.id'), nullable=False)
    phone = Column(String(12), nullable=False)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)

    person = relationship("Person", back_populates="parrents")
    degreeOfKinship = relationship("DegreeOfKinship", back_populates="parrents")
    student = relationship("Student", back_populates="parrents")
    individualWorkWithParrents = relationship("IndividualWorkWithParrent", back_populates="parrent")

class ParrentConference(Base):
    __tablename__ = 'ParrentConference'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    present = Column(Integer, nullable=False)
    absent = Column(Integer, nullable=False)
    goodAbsentReason = Column(Integer, nullable=False)
    target = Column(String(1000), nullable=False)
    result = Column(String(1000), nullable=False)
    groupId = Column(Integer, ForeignKey('Group.id'), nullable=False)

    group = relationship("Group", back_populates="parrentConferences")

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    passportSerial = Column(String(4), nullable=False, unique=True)
    passportNumber = Column(String(6), nullable=False, unique=True)
    SNILS = Column(String(11), nullable=False, unique=True)
    INN = Column(String(12), nullable=False, unique=True)
    gender = Column(Boolean, nullable=False)
    phone = Column(String(12), nullable=False, unique=True)
    registrationAddress = Column(String(100), nullable=False)
    livingAddress = Column(String(100), nullable=False)

    admin = relationship("Admin", back_populates="person", uselist=False)
    mentor = relationship("Mentor", back_populates="person", uselist=False)
    parrents = relationship("Parrent", back_populates="person")
    student = relationship("Student", back_populates="person", uselist=False)

class SocialStatus(Base):
    __tablename__ = 'SocialStatus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    groupSocialStatuses = relationship("GroupSocialStatus", back_populates="socialStatus")

class Specification(Base):
    __tablename__ = 'Specification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    qualification = Column(String(50), nullable=False)
    nameReduction = Column(String(3), nullable=False)
    qualificationReduction = Column(String(2))

    groups = relationship("Group", back_populates="specification")

class Student(Base):
    __tablename__ = 'Student'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    isRemoved = Column(Boolean, nullable=False)
    dateRemoved = Column(Date)

    person = relationship("Person", back_populates="student")
    activists = relationship("Activist", back_populates="student")
    attendingClassHours = relationship("AttendingClassHours", back_populates="student")
    dormitories = relationship("Dormitory", back_populates="student")
    groupSocialStatuses = relationship("GroupSocialStatus", back_populates="student")
    individualWorkWithStudents = relationship("IndividualWorkWithStudent", back_populates="student")
    mentorObservationLists = relationship("MentorObservationList", back_populates="student")
    parrents = relationship("Parrent", back_populates="student")
    studentHobbies = relationship("StudentHobbie", back_populates="student")
    studentInGroups = relationship("StudentInGroup", back_populates="student")

class StudentHobbie(Base):
    __tablename__ = 'StudentHobbie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    hobbieTypeId = Column(Integer, ForeignKey('HobbieType.id'), nullable=False)
    isInColledge = Column(Boolean, nullable=False)

    student = relationship("Student", back_populates="studentHobbies")
    hobbieType = relationship("HobbieType", back_populates="studentHobbies")

class StudentInGroup(Base):
    __tablename__ = 'StudentInGroup'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    groupId = Column(Integer, ForeignKey('Group.id'), nullable=False)
    date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="studentInGroups")
    group = relationship("Group", back_populates="studentInGroups")

class TableEditedHistory(Base):
    __tablename__ = 'TableEditedHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tableName = Column(String(50), nullable=False)
    attributeEdited = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    attributeBefore = Column(String(1000), nullable=False)
    attributeAfter = Column(String(1000), nullable=False)

class WorkPlanReport(Base):
    __tablename__ = 'WorkPlanReport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target = Column(String(1000), nullable=False)
    jobAnalysisReport = Column(String(1000), nullable=False)
    semesterNumber = Column(String(1), nullable=False)
    learningYear = Column(String(21), nullable=False)

    events = relationship("Event", back_populates="workPlanReport")

# Создание движка
engine = create_engine('postgresql+psycopg2://postgres:1@localhost:5434/MentorJournal', echo=True)

# Создание таблиц
Base.metadata.create_all(engine)

inspector = inspect(engine)

# Функция для генерации и выполнения SQL-команд
def generate_and_execute_sql():
    # Создание функции триггера
    trigger_function_sql = """
CREATE OR REPLACE FUNCTION log_table_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO public."TableEditedHistory" ("tableName", "attributeEdited", date, "attributeBefore", "attributeAfter")
        VALUES (TG_TABLE_NAME, TG_ARGV[0], CURRENT_DATE, OLD, NEW);
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO public."TableEditedHistory" ("tableName", "attributeEdited", date, "attributeBefore", "attributeAfter")
        VALUES (TG_TABLE_NAME, TG_ARGV[0], CURRENT_DATE, OLD, NULL);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
"""
    try:
        # Подключение к базе данных с помощью psycopg2
        conn = psycopg2.connect(
            dbname='MentorJournal',
            user='postgres',
            password='1',
            host='localhost',
            port='5434'
        )
        cursor = conn.cursor()

        # Выполнение SQL-команды для создания функции триггера
        cursor.execute(trigger_function_sql)
        conn.commit()

        # Генерация и выполнение триггеров для всех таблиц и их атрибутов
        tables = inspector.get_table_names()
        for table in tables:
            columns = inspector.get_columns(table)
            for column in columns:
                column_name = column['name']
                trigger_name = f"log_{table}_changes_{column_name}"
                trigger_sql = f"""
CREATE TRIGGER {trigger_name}
AFTER UPDATE OR DELETE ON public."{table}"
FOR EACH ROW EXECUTE FUNCTION log_table_changes('{column_name}');
"""
                cursor.execute(trigger_sql)
                conn.commit()

        # Закрытие соединения
        cursor.close()
        conn.close()

    except psycopg2.OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
    except Exception as e:
        print(f"Ошибка выполнения SQL-команд: {e}")

# Генерация и выполнение SQL-команд
generate_and_execute_sql()