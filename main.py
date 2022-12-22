import logging
from aiogram import types, executor, Bot, Dispatcher
from tokapi import TOKEN
from function import chek_up

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_up(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Assalom alaykum {name}")


@dp.message_handler(commands=['help'])
async def helpMe(message: types.Message):
    await message.reply("Bot ishlatish uchun so'z yuboring!!!")


@dp.message_handler()
async def work(message: types.Message):
    word = message.text
    result = chek_up(word)
    if result['awailable']:
        response = f"✅{word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(response)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)