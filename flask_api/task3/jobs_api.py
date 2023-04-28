import flask

from flask import jsonify, make_response
from db_session import global_init, create_session
from jobs import Job


global_init("task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

blueprint = flask.Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


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
