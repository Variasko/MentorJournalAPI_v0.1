import datetime as dt

from sqlalchemy.orm import Session

from database import engine, WorkPlanReport

"""from fastapi import FastAPI
from sqlalchemy.orm import Session
from synonyms_pars import *
from database import *"""

"""def get_student_by_group(group: str):
    with Session(autoflush=False, bind=engine) as db:
        result = []

        groups = db.query(Group).all()
        students = db.query(Student).all()
        studInGroups = db.query(StudentInGroup).all()

        for studInGroup in studInGroups:
            for student in students:
                for grou in groups:
                    if (f'{grou.specification.nameReduction}-{grou.course}{grou.recruitmentYear}{grou.specification.qualificationReduction}' == group):
                        if (grou.id == studInGroup.groupId
                        and student.personId == studInGroup.studentId):
                            result.append({"id":student.personId,
                                           "isRemoved":student.isRemoved,
                                           "dateRemoved":student.dateRemoved})
        return {'students':result}

print(get_student_by_group("ИСП-421п"))"""

"""from sqlalchemy.orm import Session

def get_student_by_group(group: str):
    with Session(autoflush=False, bind=engine) as db:
        # Разбиваем строку group на компоненты
        spec_reduction = group[:3]
        course = int(group[4])
        recruitment_year = group[5:7]
        qual_reduction = group[7]

        # Находим группу по компонентам
        group_query = db.query(Group).join(Specification).filter(
            Specification.nameReduction == spec_reduction,
            Group.course == course,
            Group.recruitmentYear == recruitment_year,
            Specification.qualificationReduction == qual_reduction
        ).first()

        if not group_query:
            return {'students': []}

        result = []

        # Находим студентов в этой группе
        students = db.query(Student).join(StudentInGroup).filter(
            StudentInGroup.groupId == group_query.id
        ).all()

        for i in students:
            result.append({
                'id':i.personId,
                'isRemoved':i.isRemoved,
                'dateRemoved':i.dateRemoved
            })
        return {'students':result}"""