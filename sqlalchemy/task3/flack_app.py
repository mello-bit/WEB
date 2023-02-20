import db_session
from users import User


db_session.global_init("blogs.db")
db_sess = db_session.create_session()
ll = {
    "surname": "Scott",
    "name": "Ridley",
    "age": 21,
    "position": "captain",
    "sreciality": "research engineer",
    "address": "module 1",
    "email": "scott_chief@mars.org"
}

for i in range(0, 4):
    if i != 0:
        user = User()
        user.surname = ll["surname"] + str(i)
        user.name = ll["name"] + str(i)
        user.age = ll["age"] + i
        user.position = ll["position"] + str(i)
        user.speciality = ll["sreciality"] + str(i)
        user.address = ll["address"] + str(i)
        user.email = ll["email"] + str(i)
    else:
        user = User()
        user.surname = ll["surname"]
        user.name = ll["name"]
        user.age = ll["age"]
        user.position = ll["position"]
        user.speciality = ll["sreciality"]
        user.address = ll["address"]
        user.email = ll["email"]
    
    db_sess.add(user)

db_sess.commit()
