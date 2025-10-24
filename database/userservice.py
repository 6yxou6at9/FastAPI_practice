from statistics import correlation

from database import get_db
from database.models import User, Results, Question, UserAnswer

#Создание пользователя
def create_user_db(name, phone_number):
    db = next(get_db())
    new_user = User(name=name, phone_number=phone_number)
    db.add(new_user)
    db.commit()
    return True

#Для получения всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users

#ДЛя получения определенного пользователя по айди
def get_exact_user_id_db(uid):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=uid).first()
    if exact_user:
        return exact_user
    return False

def save_user_answer_db(uid, qid, user_answer):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=qid).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False
        user_answer_db = UserAnswer(uid=uid, qid=qid, answer=user_answer, correctness=correctness)
        db.add(user_answer_db)
        if correctness:
            user_result = db.query(Results).filter_by(uid=uid).first()
            if user_result:
                user_result.correct_answers += 1
            else:
                new_result = Results(uid=uid, correct_answers=1)
                db.add(new_result)
                db.commit()
            return True
        db.commit()
    return False

def get_exact_user_result_db (uid):
    db = next(get_db())
    user_result = db.query(Results).filter_by(uid=uid).first()
    if user_result:
        return user_result
    return False