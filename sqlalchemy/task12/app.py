import db_session
from db_session import global_init, create_session
from users import User, Jobs, Department


nameOfDb = input()
global_init(nameOfDb)
db_sess = create_session()

users = db_sess.query(Department).filter(Department.id == 1).all()

for user in users:

    # так работает быстрее чем через list(map(int, ...))
    listOfIds = [int(id) for id in user.members.split(', ')]

    for id in listOfIds:
        currentUser = db_sess.query(User).filter(User.id == id).first()
        totalWorkSize = 0

        jobsWithThisId = db_sess.query(Jobs).filter(
            Jobs.collaborators.like(f'%{id}%')).all()
        for job in jobsWithThisId:
            totalWorkSize += job.work_size

        if totalWorkSize > 25:
            print(currentUser.surname, currentUser.name)
