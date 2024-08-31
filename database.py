from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase

class Base(DeclarativeBase): pass

class Activist(Base):
    __tablename__ = 'Activist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    activistTypeId = Column(Integer, ForeignKey('ActivistType.id'), nullable=False)

class ActivistType(Base):
    __tablename__ = 'ActivistType'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Admin(Base):
    __tablename__ = 'Admin'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class AttendingClassHours(Base):
    __tablename__ = 'AttendingClassHours'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    isVisited = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)

class DegreeOfKinship(Base):
    __tablename__ = 'DegreeOfKinship'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Dormitory(Base):
    __tablename__ = 'Dormitory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    room = Column(Integer, nullable=False)

class Event(Base):
    __tablename__ = 'Event'
    id = Column(Integer, primary_key=True, autoincrement=True)
    eventTypeId = Column(Integer, ForeignKey('EventType.id'), nullable=False)
    targent = Column(String(100), nullable=False)
    result = Column(String(1000), nullable=False)
    date = Column(Date, nullable=False)
    groupId = Column(Integer, ForeignKey('Group.id'), nullable=False)
    workPlanReportId = Column(Integer, ForeignKey('WorkPlanReport.id'), nullable=False)

class EventType(Base):
    __tablename__ = 'EventType'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class Group(Base):
    __tablename__ = 'Group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(Integer, nullable=False)
    mentorId = Column(Integer, ForeignKey('Mentor.personId'), nullable=False)
    specificationId = Column(Integer, ForeignKey('Specification.id'), nullable=False)
    isByuget = Column(Boolean, nullable=False)
    recruitmentYear = Column(String(2), nullable=False)

class GroupSocialStatus(Base):
    __tablename__ = 'GroupSocialStatus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    socialStatusId = Column(Integer, ForeignKey('SocialStatus.id'), nullable=False)
    editDate = Column(Date, nullable=False)

class HobbieType(Base):
    __tablename__ = 'HobbieType'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class IndividualWorkWithParrent(Base):
    __tablename__ = 'IndividualWorkWithParrent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    parrentId = Column(Integer, ForeignKey('Parrent.personId'), nullable=False)
    topic = Column(String(1000), nullable=False)
    result = Column(String(1000), nullable=False)

class IndividualWorkWithStudent(Base):
    __tablename__ = 'IndividualWorkWithStudent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    topic = Column(String(1000), nullable=False)
    result = Column(String(1000), nullable=False)

class Mentor(Base):
    __tablename__ = 'Mentor'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    category = Column(String(6), nullable=False)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class MentorObservationList(Base):
    __tablename__ = 'MentorObservationList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    characteristic = Column(String(1000), nullable=False)

class Parrent(Base):
    __tablename__ = 'Parrent'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    degreeOfkinshipId = Column(Integer, ForeignKey('DegreeOfKinship.id'), nullable=False)
    phone = Column(String(12), nullable=False)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)

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

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    passportSerial = Column(String(4), nullable=False)
    passportNumber = Column(String(6), nullable=False)
    SNILS = Column(String(11), nullable=False)
    INN = Column(String(12), nullable=False)
    gender = Column(Boolean, nullable=False)
    phone = Column(String(12), nullable=False)
    registrationAddress = Column(String(100), nullable=False)
    livingAddress = Column(String(100), nullable=False)

class SocialStatus(Base):
    __tablename__ = 'SocialStatus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Specification(Base):
    __tablename__ = 'Specification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    qualification = Column(String(50), nullable=False)
    nameReduction = Column(String(3), nullable=False)
    qualificationReduction = Column(String(2))

class Student(Base):
    __tablename__ = 'Student'
    personId = Column(Integer, ForeignKey('Person.id'), primary_key=True)
    isRemoved = Column(Boolean, nullable=False)
    dateRemoved = Column(Date)

class StudentHobbie(Base):
    __tablename__ = 'StudentHobbie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    hobbieTypeId = Column(Integer, ForeignKey('HobbieType.id'), nullable=False)
    isInColledge = Column(Boolean, nullable=False)

class StudentInGroup(Base):
    __tablename__ = 'StudentInGroup'
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('Student.personId'), nullable=False)
    groupId = Column(Integer, ForeignKey('Group.id'), nullable=False)
    date = Column(Date, nullable=False)

class WorkPlanReport(Base):
    __tablename__ = 'WorkPlanReport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target = Column(String(1000), nullable=False)
    jobAnalysisReport = Column(String(1000), nullable=False)
    semesterNumber = Column(String(1), nullable=False)
    learningYear = Column(String(21), nullable=False)

# Создание движка
engine = create_engine('postgresql://postgres:1@localhost:5434/MentorJournal')

# Создание таблиц
Base.metadata.create_all(engine)