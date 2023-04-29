import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Job(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    jobTitle = sqlalchemy.Column(sqlalchemy.String)
    teamLeaderId = sqlalchemy.Column(sqlalchemy.Integer)
    workSize = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    isFinished = sqlalchemy.Column(sqlalchemy.Boolean)
    nameOfCreator = sqlalchemy.Column(sqlalchemy.String)