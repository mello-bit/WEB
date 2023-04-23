from db_session import global_init, create_session
from users import User
from jobs import Job
from flask import Flask, render_template, redirect
from forms import LoginForm, SignUpForm, AddJobs
from flask_login import LoginManager, login_user
import hashlib


global_init("task5.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['salt'] = '5gz'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/')
def showJobsList():
    jobs = db_sess.query(Job).all()

    return render_template('jobs.html', jobs=jobs)


@app.route('/add_job', methods=["GET", "POST"])
def addJob():
    addJob = AddJobs()

    if addJob.validate_on_submit():
        job = Job(
            jobTitle=addJob.jobTitle.data,
            teamLeaderId=addJob.teamLeaderId.data,
            workSize=addJob.workSize.data,
            collaborators=addJob.collaborators.data,
            isFinished=addJob.isFinished.data
        )

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')

    return render_template('jobsForm.html', title="Добавление работы", form=addJob)


@app.route('/login', methods=["GET", "POST"])
def login():
    global jobs
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        user = db_sess.query(User).filter(
            User.email == loginForm.email.data).first()
        databasePassword = user.password
        if user and databasePassword == \
                hashlib.md5((loginForm.password.data + app.config['salt']).encode()).hexdigest():
                    
            login_user(user, remember=loginForm.remember_me.data)
            print(user.nickname)
            jobs = user.jobsList
            print(jobs)
            return redirect('/')

        return render_template('login.html', message="Неправильный логин или пароль", form=loginForm)

    return render_template('login.html', title="Авторизация", form=loginForm)


@app.route('/sign_up', methods=["GET", "POST"])
def signUp():
    signUpForm = SignUpForm()
    print("SignUp")

    if signUpForm.is_submitted():
        databasePassword = hashlib.md5(
            (signUpForm.password.data + app.config['salt']).encode())
        user = User(email=signUpForm.email.data,
                    password=databasePassword.hexdigest(),
                    jobsList=signUpForm.jobsList.data,
                    nickname=signUpForm.nickname.data)

        print(user, 1)
        db_sess.add(user)
        db_sess.commit()
        print(user, 2)

        return render_template('signUp.html', message="Everything is ok", form=signUpForm)

    return render_template('signUp.html', title="Авторизация", form=signUpForm)


if __name__ == '__main__':
    app.run(debug=True)
