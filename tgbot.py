import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7342365714:AAGqE40tU7SE5SMT_jpUlqpYS8GuILMwCrw")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
  await message.reply("Hello!")


await dp.start_polling(bot)
