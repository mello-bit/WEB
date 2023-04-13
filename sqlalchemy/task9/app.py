import db_session
from db_session import global_init, create_session
from users import User, Jobs


nameOfDb = input()
global_init(nameOfDb)
db_sess = create_session()


users = db_sess.query(User).filter(User.address.like(
    '%1%'), User.age < 21).all()
for user in users:
    user.address = "module_3"

db_sess.commit()
