from fastapi import FastAPI
from routes import auth
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(auth.router)

register_tortoise(
    app,
    db_url="mysql://root:Doraemon31@127.0.0.1:3306/nebula_db",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)