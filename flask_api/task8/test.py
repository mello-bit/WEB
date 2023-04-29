import requests

from db_session import global_init, create_session
from jobs import Job


global_init("../../task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

urlForGettingAllJobs = "http://localhost:5001/api/jobs"
urlForGettingOneJob = "http://localhost:5001/api/jobs/"
urlForAddingJob = "http://localhost:5001/api/jobs"
urlForDeletingJob = "http://localhost:5001/api/jobs/"


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


def checkAddJob(id, jobTitle="First job from POST request",
                teamLeaderId=1, workSize=200, collaborators="13", isFinished=True, nameOfCreator="Dany Kiper"):
    resOfPost = requests.post(urlForAddingJob, json={
        "id": id,
        "jobTitle": jobTitle,
        "teamLeaderId": teamLeaderId,
        "workSize": workSize,
        "collaborators": collaborators,
        "isFinished": isFinished,
        "nameOfCreator": nameOfCreator
    }).json()

    print(resOfPost)
    

def checkOfDeleteJob(id):
    resOfDelete = requests.delete(f"{urlForDeletingJob}{id}").json()
    
    print(resOfDelete)


if __name__ == '__main__':
    checkOfDeleteJob(id=11)  # тест корректного запроса на удаления
    checkOfDeleteJob(id=90)  # тест некорректного запроса на удаления
    checkOfDeleteJob(id="900")  # тест некорректного запроса на удаления
    checkOfDeleteJob(id="ghghgh")  # тест некорректного запроса на удаления
    
    print(checkGettingAllJobs())