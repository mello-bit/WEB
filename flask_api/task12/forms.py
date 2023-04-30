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
    cityFrom = StringField('Введите город, где вы родились', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')
    
    
class AddJobs(FlaskForm):
    jobTitle = EmailField('Job Title', validators=[DataRequired()])
    teamLeaderId = StringField('Team Leader ID', validators=[DataRequired()])
    workSize = StringField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    isFinished = BooleanField('Is Finished?')
    submit = SubmitField('Submit')