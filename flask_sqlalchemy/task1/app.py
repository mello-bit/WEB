from db_session import global_init, create_session
from users import User
from flask import Flask, render_template, redirect
from forms import LoginForm, SignUpForm
from flask_login import LoginManager, login_user


global_init("alpha.db")  # bd лежит в папке WEB т.к venv тоже лежит в WEB
db_sess = create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=["GET", "POST"])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        user = db_sess.query(User).filter(
            User.email == loginForm.email.data).first()

        if user and user.check_password(loginForm.password.data):
            login_user(user, remember=loginForm.remember_me.data)
            return redirect('/')

        return render_template('login.html', message="Неправильный логин или пароль", form=loginForm)

    return render_template('login.html', title="Авторизация", form=loginForm)


@app.route('/sign_up', methods=["GET", "POST"])
def signUp():
    signUpForm = SignUpForm()
    print("SignUp")

    if signUpForm.is_submitted():
        user = User(email=signUpForm.email.data,
                    password=signUpForm.password.data,
                    nickname=signUpForm.nickname.data)

        print(user, 1)
        db_sess.add(user)
        db_sess.commit()
        print(user, 2)

        return render_template('signUp.html', message="Everything is ok", form=signUpForm)

    return render_template('signUp.html', title="Авторизация", form=signUpForm)


if __name__ == '__main__':
    app.run()
