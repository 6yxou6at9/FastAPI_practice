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
def get_exact_user_id():
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=uid).first()
    if exact_user:
        return exact_user
    return False