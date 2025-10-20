from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


#User, Question, Answer, Result

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(64), nullable=False)
    phone_number = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, autoincrement=True, primary_key=True)
    question = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

class UserAnswer(Base):
    __tablename__ = 'user_answers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    uid = Column(Integer, ForeignKey('users.id'))
    qid = Column(Integer, ForeignKey('questions.id'))
    answer = Column(String, nullable=False)
    correctness = Column(Boolean, default=True)
    reg_date = Column(DateTime, default=datetime.now())
    user_fk = relationship("User", lazy='subquery')
    question_fk = relationship('Question', lazy='subquery')

class Results(Base):
    __tablename__ = 'results'

    id = Column(Integer, autoincrement=True, primary_key=True)
    uid = Column(Integer, ForeignKey('users.id'))
    correct_answers = Column(Integer, default=0)
    user_fk = relationship("User", lazy='subquery')