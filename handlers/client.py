from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


async def start_command(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}!')


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Это должно быть ответом на сообщение')


async def quiz_1(message: types.message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Cколько весит самая крупная жемчужина в мире?"
    answers = [
        "60 килограмм",
        "47 килограмм",
        "21 килограмм",
        "34 килограмм"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        explanation='Очень тяжелый крч',
        type='quiz',
        correct_option_id=3,
        open_period=15,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
