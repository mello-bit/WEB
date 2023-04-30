import requests

from db_session import global_init, create_session
from users import User


global_init("../../task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

urlForGettingAllUsers = "http://localhost:5001/api/users"
urlForGettingOneUser = "http://localhost:5001/api/users/"
urlForAddingUser = "http://localhost:5001/api/users"
urlForDeletingUser = "http://localhost:5001/api/users/"
urlForUpdatingUser = "http://localhost:5001/api/users"


def checkGettingAllUser():
    req = requests.get(urlForGettingAllUsers).json()
    allUsers = db_sess.query(User).all()
    isEverythingOkay = True

    for r, all in zip(req, allUsers):
        for key, val in r.items():
            user = all.to_dict()
            if user[key] != val:
                isEverythingOkay = False

    if isEverythingOkay:
        return "Все хорошо, все пользователи на месте"
    return "Плохо, пользователей не хватает. Нужно проверить код :)"


def checkGettingOneUser(id):
    req = requests.get(f"{urlForGettingOneUser}{id}").json()
    user = db_sess.query(User).get(id)
    isEverythingOkay = True

    if not user or not req:
        print(req)
        return "Параметр id был передан неверно"

    user = user.to_dict()

    for key, val in req["user"].items():
        if user[key] != val:
            isEverythingOkay = False

    if isEverythingOkay:
        print(req)
        return "Все хорошо, этот пользователь правильный"

    return "Плохо, что-то не соответствует. Пользователь из бд и из url отличаются"


def checkAddUser(id, nickname="QBoff", email="k@gmail.com",
                jobsList="1, 2, 3", password="123"):

    resOfPost = requests.post(urlForAddingUser, json={
        "id": id,
        "nickname": nickname,
        "email": email,
        "jobsList": jobsList,
        "password": password,
    }).json()

    print(resOfPost)


def checkOfDeleteUser(id, password):
    resOfDelete = requests.delete(
        f"{urlForDeletingUser}{id}/{password}").json()

    print(resOfDelete)


def checkOfUpdateUser(id, nickname="QBoff", email="kaaa@gmail.com",
                     jobsList="1, 2, 3, 67", password="123"):
    resOfUpdate = requests.patch(f"{urlForUpdatingUser}", json={
        "id": id,
        "nickname": nickname,
        "email": email,
        "jobsList": jobsList,
        "password": password,
    }).json()

    print(resOfUpdate)


if __name__ == '__main__':
    print(checkGettingAllUser())
    print(checkGettingOneUser(id=5))
    checkAddUser(id=5, nickname="QB")
    checkAddUser(id=6,nickname="QBoffffffffffff", password="1234")
    checkAddUser(id=7,nickname="QBOFFFFFFFFFFFFFFF", password="234")
    checkOfDeleteUser(id=5, password="123")
    checkOfUpdateUser(id=7, nickname="Ann", password="234")
    
    