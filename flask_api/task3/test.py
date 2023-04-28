import requests

from db_session import global_init, create_session
from jobs import Job


global_init("task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

urlForGettingAllJobs = "http://localhost:5001/api/jobs"
urlForGettingOneJob = "http://localhost:5001/api/jobs/"


def checkGettingAllJobs():
    req = requests.get(urlForGettingAllJobs).json()
    allJobs = db_sess.query(Job).all()
    isEverythingOkay = True

    for r, all in zip(req, allJobs):
        for key, val in r.items():
            job = all.to_dict()
            if job[key] != val:
                isEverythingOkay = False

    if isEverythingOkay:
        return "Все хорошо, все работы на месте"
    return "Плохо, работ не хватает. Нужно проверить код :)"


def checkGettingOneJob(id):
    req = requests.get(f"{urlForGettingOneJob}{id}").json()
    job = db_sess.query(Job).get(id)
    isEverythingOkay = True

    if not job or not req:
        return "Параметр id был передан неверно"

    job = job.to_dict()

    for key, val in req["job"].items():
        if job[key] != val:
            isEverythingOkay = False

    if isEverythingOkay:
        return "Все хорошо, это работа правильная"

    return "Плохо, что-то не соответствует. Работа из бд и из url отличаются"


if __name__ == '__main__':
    print(checkGettingAllJobs())
    print(checkGettingOneJob(2))
    print(checkGettingOneJob(20))
    print(checkGettingOneJob("20"))
