import db_session
from db_session import global_init, create_session
from users import User, Jobs


nameOfDb = input()
global_init(nameOfDb)
db_sess = create_session()


jobs = db_sess.query(Jobs).filter(
    Jobs.work_size < 20, Jobs.is_finished == 0).all()

for job in jobs:
    print(job)
