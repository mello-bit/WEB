from db_session import global_init, create_session
from users import User
from jobs import Job
from flask import Flask, render_template, redirect
from forms import LoginForm, SignUpForm, AddJobs
from flask_login import LoginManager, login_user
import hashlib
import jobs_api
import users_api


global_init("task8.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['salt'] = '5gz'
nickname = None
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/')
def showJobsList():
    jobs = db_sess.query(Job).all()

    if nickname is not None:
        return render_template('jobs.html', jobs=jobs, nickname=nickname)

    return redirect('/sign_up')


@app.route('/edit/<jobTitle>/<teamLeaderId>/<workSize>/<collaborators>/<isFinished>/<nameOfCreator>/', methods=["GET", "POST"])
def edit(jobTitle, teamLeaderId, workSize, collaborators, isFinished, nameOfCreator):
    if nickname == None:
        return redirect('/sign_up')

    captainName = db_sess.query(User).filter(User.id == 1).first()
    if nameOfCreator != nickname and nickname != captainName.nickname:
        return redirect('/')

    addJob = AddJobs()

    if addJob.validate_on_submit():
        try:
            currentJob = db_sess.query(Job).filter(Job.nameOfCreator == nickname).update({
                "jobTitle": str(addJob.jobTitle.data),
                "teamLeaderId": int(addJob.teamLeaderId.data),
                "workSize": int(addJob.workSize.data),
                "collaborators": str(addJob.collaborators.data),
                "isFinished": bool(addJob.isFinished.data),
                "nameOfCreator": str(nickname)
            })
            db_sess.commit()

            return redirect('/')
        except Exception:
            return render_template('jobsForm.html', titleOfPage="Edit Job", form=addJob,
                                   currentJobTitle=jobTitle,
                                   currentTeamLeaderId=teamLeaderId,
                                   currentWorkSize=workSize,
                                   currentCollaborator=collaborators, nickname=nickname, message="Isn't valid data")

    return render_template('jobsForm.html', titleOfPage="Edit Job", form=addJob,
                           currentJobTitle=jobTitle,
                           currentTeamLeaderId=teamLeaderId,
                           currentWorkSize=workSize,
                           currentCollaborator=collaborators, nickname=nickname)
    
    
@app.route('/edit/<jobTitle>/<teamLeaderId>/<workSize>/<collaborators>/<isFinished>/<nameOfCreator>/<id>', methods=["GET", "POST"])
def delete(jobTitle, teamLeaderId, workSize, collaborators, isFinished, nameOfCreator, id):
    if nickname == None:
        return redirect('/sign_up')

    captainName = db_sess.query(User).filter(User.id == 1).first()
    if nameOfCreator != nickname and nickname != captainName.nickname:
        return redirect('/')

    db_sess.query(Job).filter(Job.id == id).delete()
    db_sess.commit()

    return redirect('/')
    


@app.route('/add_job', methods=["GET", "POST"])
def addJob():

    if nickname is None:
        return redirect('/sign_up')
    addJob = AddJobs()

    if addJob.validate_on_submit():
        try:
            
            job = Job(
                jobTitle=addJob.jobTitle.data,
                teamLeaderId=int(addJob.teamLeaderId.data),
                workSize=int(addJob.workSize.data),
                collaborators=addJob.collaborators.data,
                isFinished=addJob.isFinished.data,
                nameOfCreator=nickname
            )
        except Exception:
            return render_template('jobsForm.html', titleOfPage="Add New Job",
                                   title="Добавление работы",
                                   form=addJob, nickname=nickname,
                                   message="Isn't valid data!!")

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')

    if nickname is not None:
        return render_template('jobsForm.html', titleOfPage="Add New Job", title="Добавление работы", form=addJob, nickname=nickname)

    return render_template('jobsForm.html', titleOfPage="Add New Job", title="Добавление работы", form=addJob)


@app.route('/login', methods=["GET", "POST"])
def login():
    global nickname

    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        user = db_sess.query(User).filter(
            User.email == loginForm.email.data).first()
        if user:
            databasePassword = user.password

            if databasePassword == \
                    hashlib.md5((loginForm.password.data + app.config['salt']).encode()).hexdigest():

                login_user(user, remember=loginForm.remember_me.data)
                nickname = user.nickname
                return redirect('/')

        return render_template('login.html', message="Неправильный логин или пароль", form=loginForm, nickname=nickname)

    if nickname is not None:
        return render_template('login.html', title="Авторизация", form=loginForm, nickname=nickname)

    return render_template('login.html', title="Авторизация", form=loginForm)


@app.route('/sign_up', methods=["GET", "POST"])
def signUp():
    global nickname

    signUpForm = SignUpForm()
    print("SignUp")

    if signUpForm.is_submitted():
        databasePassword = hashlib.md5(
            (signUpForm.password.data + app.config['salt']).encode())

        ne = db_sess.query(User).filter(
            User.nickname == signUpForm.nickname.data).all()
        repEmail = db_sess.query(User).filter(User.email == signUpForm.email.data).all()
        if len(ne) == 0 and len(repEmail) == 0:
            user = User(email=signUpForm.email.data,
                        password=databasePassword.hexdigest(),
                        jobsList=signUpForm.jobsList.data,
                        nickname=signUpForm.nickname.data)
        else:
            print("This nickname has already been creating")
            return render_template('signUp.html', title="Авторизация", form=signUpForm, message="Такой nickname уже есть :)")

        print(user, 1)
        db_sess.add(user)
        db_sess.commit()
        print(user, 2)
        nickname = user.nickname
        # return render_template('signUp.html', message="Everything is ok", form=signUpForm, nickname=nickname)
        return redirect('/')

    if nickname is not None:
        return render_template('signUp.html', title="Авторизация", form=signUpForm, nickname=nickname)

    return render_template('signUp.html', title="Авторизация", form=signUpForm)


@app.route('/logout')
def logout():
    global nickname

    nickname = None
    return redirect('/')


if __name__ == '__main__':
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run(debug=True, port=5001)
