import db_session
from db_session import global_init, create_session
from users import User, Jobs

from sqlalchemy import desc


nameOfDb = input()
global_init(nameOfDb)
db_sess = create_session()


jobs = db_sess.query(Jobs).order_by(desc(Jobs.collaborators)).all()

mem = 0
for i in range(len(jobs)):
    if i == 0:
        mem = len(jobs[i].collaborators)
        continue

    if mem != len(jobs[i].collaborators):
        break

    currentId = jobs[i].team_leader
    user = db_sess.query(User).filter(User.id == currentId).first()

    print(user.surname, user.name)
