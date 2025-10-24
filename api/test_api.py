from fastapi import APIRouter
from database.testservice import (create_question_db, get_20_questions_db, get_top_10_users_db)

test_router = APIRouter(prefix='/test', tags=["Test API"]) #НЕ УВЕРЕН

@test_router.post('/create_question_db')
async def create_question_db(question, v1, v2, v3, v4, correct_answer):
    result = create_question_db(question=question, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    return {'status': 1, 'message': f'Вопрос {result} создан'}

@test_router.get('/get_20_questions_db')
async def get_20_questions_db():
    result = get_20_questions_db()
    return {'status': 1, 'message': result}

@test_router.get('/get_top_10_users_db')
async def get_top_10_users_db():
    result = get_top_10_users_db()
    return {'status': 1, 'message': result}