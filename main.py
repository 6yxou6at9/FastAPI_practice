from fastapi import FastAPI, Request
from api import user_api
from api import test_api
from api.user_api import user_router
from api.test_api import test_router
from database import Base, engine


app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="MyFirstAPI")
app.include_router(user_router)
app.include_router(test_router)
Base.metadata.create_all(engine)

@app.get('/')
async def main(request: Request):
    return 'Gryth'