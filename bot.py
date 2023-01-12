from aiogram import Dispatcher, Bot, executor, types

TOKEN_API = '5596150170:AAFyzFBYilB9ZMvA4sKMnV29i3HVEJqY1Cw'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
