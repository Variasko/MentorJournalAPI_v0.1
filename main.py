from fastapi import FastAPI
from sqlalchemy.orm import Session
from synonyms_pars import *
from database import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_synonym/{word}")
async def get_synonym(word: str):
    return get_synonyms(word)


@app.get("/get_mentor/{login}/{password}")
async def get_mentor_by_login_and_password(login: str, password: str):
    with Session(autoflush=False, bind=engine) as db:
        try:
            mentor = db.query(Mentor).filter(Mentor.login == login,
                                             Mentor.password == password).first()
            return mentor
        except Exception as e:
            mentor = Mentor()
            return mentor


@app.get("/get_admin/{login}/{password}")
async def get_admin_by_login_and_password(login: str, password: str):
    with Session(autoflush=False, bind=engine) as db:
        try:
            admin = db.query(Admin).filter(Admin.login == login,
                                           Admin.password == password).first()
            return admin
        except Exception as e:
            admin = Admin()
            return admin


@app.get("/get_all_students")
async def get_all_students():
    with Session(autoflush=False, bind=engine) as db:
        students = db.query(Student).all()
        return {"students": students}


@app.get('/get_all_social_status')
async def get_all_social_status():
    with Session(autoflush=False, bind=engine) as db:
        social_status = db.query(SocialStatus).all()
        return {"social_status": social_status}
@app.get('/get_student_by_group/{group}')
async def get_student_by_group(group: str):
    with Session(autoflush=False, bind=engine) as db:
        # Разбиваем строку group на компоненты
        spec_reduction = group[:3]
        course = int(group[4])
        recruitment_year = group[5:7]
        qual_reduction = group[7] if len(group) > 7 else None

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
        return {'students':result}

@app.get('/get_persons')
async def get_persons():
    with Session(autoflush=False, bind=engine) as db:
        persons = db.query(Person).all()
        return {"persons": persons}

@app.post("/add_admin/{id}/{login}/{password}")
async def add_admin(id: int, login: str, password: str):
    with Session(autoflush=False, bind=engine) as db:
        new_admin = Admin(personId=id, login=login, password=password)
        db.add(new_admin)
        db.commit()
        return {
            'status': 'success'
        }

@app.post('/add_mentor/{id}/{category}/{login}/{password}')
async def add_mentor(id: int, category: str, login: str, password: str):
    with Session(autoflush=False, bind=engine) as db:
        new_mentor = Mentor(personId=id, category=category, login=login, password=password)
        db.add(new_mentor)
        db.commit()
        return {
            'status': 'success'
        }

@app.post('/add_student/{id}/{isRemoved}/{dateRemoved}')
async def add_student(id: int, isRemoved: bool, dateRemoved: str = None):
    with Session(autoflush=False, bind=engine) as db:
        new_student = Student(personId=id, isRemoved=isRemoved, dateRemoved=dateRemoved)
        db.add(new_student)
        db.commit()
        return {
            'status': 'success'
        }

@app.post('/add_person/{surname}/{name}/{patronymic}/{passportSerial}/{passportNumber}/{SNILS}/{INN}/{gender}/{phone}/{registrationAddress}/{livingAddress}')
async def add_person(surname: str, name: str, patronymic: str, passportSerial: str, passportNumber: str, SNILS: str,
                      INN: str, gender: bool, phone: str, registrationAddress: str, livingAddress: str):
    with Session(autoflush=False, bind=engine) as db:
        new_person = Person(surname=surname, name=name, patronymic=patronymic, passportSerial=passportSerial,
                            passportNumber=passportNumber, SNILS=SNILS, INN=INN, gender=gender, phone=phone,
                            registrationAddress=registrationAddress, livingAddress=livingAddress)
        db.add(new_person)
        db.commit()
        return {
            'status': 'success'
        }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="192.168.0.102", port=8020)
