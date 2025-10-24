from fastapi import APIRouter
from database.userservice import (create_user_db, get_exact_user_result_db, get_all_users_db, save_user_answer_db, get_exact_user_id_db)

user_router = APIRouter(prefix='/user', tags=["User API"])


@user_router.post('/create_user')
async def create_user(name, phone_number):
    result = create_user_db(name=name, phone_number=phone_number)
    return {'status': 1, "message": f"Пользователь создан {result}"}

@user_router.get('/get_all_users')
async def get_all_users():
    result = get_all_users_db()
    return {"status":1, "message": f"{result}"}

@user_router.get('/get_exact_user_id')
async def get_exact_user_id(id):
    result = get_exact_user_id_db(uid=id)
    return {"status":1, "message": result}

@user_router.post('/save_user_answer')
async def save_user_answer(uid, qid, user_answer):
    result = save_user_answer_db (uid=uid, qid=qid, user_answer=user_answer)
    return {"status":1, 'message': f'Ответ пользователя {result} сохранен'}

@user_router.get('/get_exact_user_result')
async def get_exact_user_result(uid):
    result = get_exact_user_result_db(uid=uid)
    return {"status":1, 'message': result}