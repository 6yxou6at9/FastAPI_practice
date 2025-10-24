from sqlalchemy import desc
from database import get_db
from database.models import User, Results, Question, UserAnswer

# Функции для добавления вопросов, получения топ 10 пользователей, для получения первых 20 вопросов

def create_question_db(question, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Question(question=question, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return True

def get_top_10_users_db():
    db = next(get_db())
    get_top_users = db.query(Results).order_by(desc(Results.correct_answers)).all()
    return get_top_users

def get_20_questions_db():
    db = next(get_db())
    get_questions = db.query(Question).all()[0:20]
    return get_questions

