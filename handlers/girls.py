from aiogram import Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, FSInputFile
from utils.database import Database
import os
import asyncio

async def keyboard_btn(girl_name, girl_link):
    inline_keyboard = [
        [InlineKeyboardButton(text=f"Meet {girl_name}", url=f"{girl_link}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

async def info_girl(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    girls = db.get_girls_info()
    try:
        for girl in girls:
            girl_id = girl[0]
            girl_name = girl[1]
            girl_description = girl[2]
            girl_link = girl[3]

            keyboard = await keyboard_btn(girl_name, girl_link)

            girl_information = (f'{girl_name}\n\n'
                                f'{girl_description}\n\n')

            girl_photo = db.get_image_path(girl_id)
            media_group = [InputMediaPhoto(media=FSInputFile(photo[0])) for photo in girl_photo]


            if media_group:
                await bot.send_media_group(message.from_user.id, media_group)

            # Отправляем информацию о девушке
            await bot.send_message(message.from_user.id, girl_information, reply_markup=keyboard)
            await asyncio.sleep(2)
    except Exception as error:
        with open('errors.txt', 'a') as error_file:
            error_message = f"Ошибка при попытке показать анкеты - {error}\n"
            error_file.write(error_message)
        print(f"Ошибка при попытке показать анкеты - {error}")

# Дальше идет код для инициализации и запуска бота
