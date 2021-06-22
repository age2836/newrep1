from config import TOKEN
from info import infos
from opens import opens
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as otvet
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


nomer = 0
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    name = message.from_user.first_name
    global nomer
    await bot.send_message(message.from_user.id, '<b>😎 Привет,' + str(name) + '!\nВведи свой город</b>', parse_mode=types.ParseMode.HTML)
    nomer = 0

@dp.message_handler()
async def process_message(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Отлично, твой город " + str(message.text) + "\nКто ты?</b>", parse_mode=types.ParseMode.HTML, reply_markup=otvet.otvet)

@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    global nomer
    if call.data == "boy":
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Выбери свой возраст</b>", parse_mode=types.ParseMode.HTML, reply_markup=otvet.otvet1)
    if call.data == "kto":
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Выберите кого будем искать?</b>", parse_mode=types.ParseMode.HTML, reply_markup=otvet.otvet2)

    if call.data == "1":
        print(nomer)
        nomer += 1
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_photo(call.message.chat.id, opens[nomer], infos[nomer], reply_markup=otvet.otvet3)
        print(nomer)


    if call.data == "down":
        if nomer == 34:
            nomer += 1
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            await bot.send_photo(call.message.chat.id, opens[nomer], infos[nomer], reply_markup=otvet.otvet5)
            print(nomer)
        else:
            nomer += 1
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            await bot.send_photo(call.message.chat.id, opens[nomer], infos[nomer], reply_markup=otvet.otvet4)
            print(nomer)



    if call.data == "up":
        if nomer == 2:
            nomer -= 1
            print(nomer)
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            await bot.send_photo(call.message.chat.id, opens[nomer], infos[nomer], reply_markup=otvet.otvet3)
        else:
            nomer -= 1
            print(nomer)
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            await bot.send_photo(call.message.chat.id, opens[nomer], infos[nomer], reply_markup=otvet.otvet4)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
