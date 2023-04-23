import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase
from flask_login import UserMixin


class Job(SqlAlchemyBase, UserMixin):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    nameOfJob = sqlalchemy.Column(sqlalchemy.String)
    experience = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    likeIt = sqlalchemy.Column(sqlalchemy.Boolean)
