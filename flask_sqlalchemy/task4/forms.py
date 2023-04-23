from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    

class SignUpForm(FlaskForm):
    nickname = StringField('Имя')
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    jobsList = StringField('Введите список ваших работ :)', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')
    
    
class AddJobs(FlaskForm):
    email = EmailField('Введите вашу почту', validators=[DataRequired()])
    nameOfJob = StringField('Название вашей работы', validators=[DataRequired()])
    experience = StringField('Каков ваш опыт на данной работе', validators=[DataRequired()])
    description = StringField('Напишите что вы делаете на работе', validators=[DataRequired()])
    likeIt = BooleanField('Нравится ли вам работа или нет')
    submit = SubmitField('Добавить работу')