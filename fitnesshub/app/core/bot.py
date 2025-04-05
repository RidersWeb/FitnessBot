import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

logging = logging.getLogger(__name__)

# Загружаем переменные из .env
load_dotenv()

# 1. Инициализация бота и диспетчера
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

# 2. Создаём роутер
router = Router()

# 3. Регистрируем хендлеры в роутере
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой фитнес-бот.")

# 4. Подключаем роутер к диспетчеру
dp.include_router(router)

# 5. Запускаем бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())