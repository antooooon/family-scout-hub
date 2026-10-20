from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.db.init import db_init
from app.telegram.client import client
from app.telegram.registration import register_handlers
from app.web.endpoints.channels import router as channel_router
from app.web.endpoints.keywords import router as keyword_router

# noinspection
import app.telegram.handlers


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logging.getLogger("telethon").setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):

    await db_init()

    try:
        await client.start()
        await register_handlers()
        # print("Telegram client started")
        logging.info("Telegram client started")
        yield
    finally:
        await client.disconnect()
        # print("Telegram client disconnected")
        logging.info("Telegram client disconnected")


app = FastAPI(
    title="Telegram Monitor API",
    lifespan=lifespan
)

app.include_router(keyword_router)
app.include_router(channel_router)


# Декоратор @asynccontextmanager из модуля contextlib в Python позволяет создавать
# асинхронные менеджеры контекста с помощью обычной асинхронной функции-генератора
# (async def), без необходимости писать громоздкие классы с методами
# __aenter__() и __aexit__()

# lifespan — механизм FastAPI для управления ресурсами при запуске и остановке приложения.
