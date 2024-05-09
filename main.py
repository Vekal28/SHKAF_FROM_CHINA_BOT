import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token="7143916813:AAEWNi0ScjlvdYlRrnwycR3WDVQ9W0GCmg4")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Бот выключен")