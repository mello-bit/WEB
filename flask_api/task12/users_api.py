import flask
import hashlib

from flask import jsonify, make_response, request
from db_session import global_init, create_session
from users import User
import requests


salt = '5gz'
global_init("task12.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

blueprint = flask.Blueprint(
    "users_api",
    __name__,
    template_folder="templates"
)


def checkPasswordSimilarity(dbPassword, incomingPassword):
    hashedIncomingPassword = hashlib.md5(
        (incomingPassword + salt).encode())

    return dbPassword == hashedIncomingPassword.hexdigest()


@blueprint.route('/api/users/<int:userId>/map')
def showUserCity(userId):
    api_key = "5d666306-8732-43c4-a011-a9cc7afada11"
    staticMapApi = "https://static-maps.yandex.ru/1.x/?"
    geocoderApi = "https://geocode-maps.yandex.ru/1.x/?"
    currentUser = db_sess.query(User).filter(User.id == userId).first()
    cityGeocode = requests.get(
        f"{geocoderApi}apikey={api_key}&geocode={currentUser.cityFrom}&results=1&format=json"
    )
    if not cityGeocode:
        print(cityGeocode)
        return jsonify({"error": "Bad city geocoder"})

    geo = cityGeocode.json()
    pos = geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    pos = ','.join(pos.split())
    
    req = requests.get(
        f"{staticMapApi}ll={pos}&l=sat&z=11"
    )
    
    if not req:
        return jsonify({"error": "Bad city geocoder"})
    
    with open("flask_api/task12/static/map.jpg", "wb") as f:
        f.write(req.content)
    
    
    return jsonify({
        "userNickname": currentUser.nickname,
        "userCity": currentUser.cityFrom,
        "map": 'map.jpg',
        "pos": pos
    })


@blueprint.route('/api/users')
def getAllUsers():
    users = db_sess.query(User).all()
    allUsers = []

    for user in users:
        allUsers.append(user.to_dict())

    return jsonify(allUsers)



@blueprint.route('/api/users/<int:userId>')
def getUserById(userId):
    user = db_sess.query(User).filter(User.id == userId).first()

    if not user:
        return jsonify({
            "error": "not found"
        })

    return jsonify({
        "user": user.to_dict()
    })


@blueprint.route('/api/users', methods=["POST"])
def createUser():
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 ["id", "nickname", "email", "jobsList", "password"]):
        return jsonify({"error": "Bad request"})
    print(request.json)
    if isinstance(request.json["id"], int) and request.json["id"] >= 1:

        print("Меня ищут")
        userWithIncomingId = db_sess.query(User).filter(
            (User.nickname == request.json["nickname"]) | (User.id == request.json["id"])).first()
        
        print("Меня нашли")
        if userWithIncomingId is None:
            print("Я внутри ифа")
            hashedPassword = hashlib.md5(
                (request.json["password"] + salt).encode())
            user = User(
                id=request.json["id"],
                nickname=request.json["nickname"],
                email=request.json["email"],
                jobsList=request.json["jobsList"],
                password=hashedPassword.hexdigest(),
            )
            print("User был создан")
            db_sess.add(user)
            print("User был добавлен")
            db_sess.commit()
            print("User был закоммичен")
            return jsonify({"success": "ok"})
        
        return jsonify({"error": "Id already exists or nickname already exists"})

    return jsonify({"error": "Bad request(wrong id)"})


@blueprint.route('/api/users', methods=["PATCH"])
def editUser():
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 ["nickname", "email", "jobsList", "password"]):
        return jsonify({"error": "Bad request"})

    if isinstance(request.json["id"], int) and request.json["id"] >= 1:

        userWithIncomingId = db_sess.query(User).filter(
            User.id == request.json["id"]).first()

        if userWithIncomingId is not None and \
                checkPasswordSimilarity(userWithIncomingId.password, request.json["password"]):
                    
            hashedPassword = hashlib.md5((request.json["password"] + salt).encode())
            
            userWithIncomingId.id = request.json["id"]
            userWithIncomingId.nickname=request.json["nickname"]
            userWithIncomingId.email=request.json["email"]
            userWithIncomingId.jobsList=request.json["jobsList"]
            userWithIncomingId.password = hashedPassword.hexdigest()
            
            db_sess.commit()
            return jsonify({"success": "ok"})

        return jsonify({"error": "Id isn't in db"})

    return jsonify({"error": "Bad request(wrong id)"})


@blueprint.route('/api/users/<userId>/<userPassword>', methods=["DELETE"])
def deleteUserById(userId, userPassword):
    
    try:
        userId = int(userId)

        if isinstance(userId, int) and userId >= 1:
            user = db_sess.query(User).filter(User.id == userId).first()
            if not checkPasswordSimilarity(user.password, userPassword):
                return jsonify({"error": "Wrong user password"})
            
            if not user:
                return jsonify({"error": "Not found"})

            db_sess.delete(user)
            db_sess.commit()

            return jsonify({"success": "ok"})
        
        return jsonify({"error": "Bad password"})
    except Exception as e:
        return jsonify({"error": "Bad Id in request"})

