import flask

from flask import jsonify, make_response, request
from db_session import global_init, create_session
from jobs import Job


global_init("task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

blueprint = flask.Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


@blueprint.route('/api/jobs/<jobId>', methods=["DELETE"])
def deleteJobById(jobId):

    try:
        jobId = int(jobId)
        if isinstance(jobId, int) and jobId >= 1:
            job = db_sess.query(Job).filter(Job.id == int(jobId)).first()

            if not job:
                return jsonify({"error": "Not found"})

            db_sess.delete(job)
            db_sess.commit()

            return jsonify({"success": "ok"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Bad Id in request"})


@blueprint.app_errorhandler(404)
@blueprint.app_errorhandler(400)
@blueprint.route('/api/jobs/<int:jobId>')
def getNewsById(jobId, error=None):
    job = db_sess.query(Job).get(jobId)

    if not job:
        return make_response(jsonify({
            "error": "not found"
        }), error)

    return jsonify({
        "job": job.to_dict()
    })


@blueprint.route('/api/jobs')
def showAllJobs():
    allJobs = []

    for job in db_sess.query(Job).all():
        allJobs.append(job.to_dict())

    return jsonify(
        allJobs
    )


@blueprint.route('/api/jobs', methods=["POST"])
def createJob():
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 ["id", "jobTitle", "teamLeaderId", "workSize", "collaborators", "isFinished", "nameOfCreator"]):
        return jsonify({"error": "Bad request"})

    if isinstance(request.json["id"], int) and request.json["id"] >= 1:

        jobWithEntryId = db_sess.query(Job).filter(
            Job.id == request.json["id"]).first()

        if jobWithEntryId is None:
            job = Job(
                id=request.json["id"],
                jobTitle=request.json["jobTitle"],
                teamLeaderId=request.json["teamLeaderId"],
                workSize=request.json["workSize"],
                collaborators=request.json["collaborators"],
                isFinished=request.json["isFinished"],
                nameOfCreator=request.json["nameOfCreator"]
            )

            db_sess.add(job)
            db_sess.commit()
            return jsonify({"success": "ok"})

        return jsonify({"error": "Id already exists"})

    return jsonify({"error": "Bad request(wrong id)"})
