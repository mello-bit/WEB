import db_session
from db_session import global_init, create_session
from users import User


nameOfDb = input()
global_init(nameOfDb)
db_sess = create_session()


users = db_sess.query(User).filter(User.address.like('%1%'),
                                   User.speciality.notlike('%engineer%'),
                                   User.position.notlike('%engineer%')).all()

for user in users:
    print(user.id)
