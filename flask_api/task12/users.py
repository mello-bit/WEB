import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, unique=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    jobsList = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    cityFrom = sqlalchemy.Column(sqlalchemy.String)
    
