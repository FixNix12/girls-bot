from aiogram import Bot
from aiogram.types import Message, FSInputFile
import asyncio
from keyboards.keyboards import start_keyboards


async def start_bot(message: Message, bot: Bot):
    try:

        msg9 = ("Together with our bot you will be able to get the attention of the most beautiful girls 👭👭👭\n\n"
                "Play video 👇")
        await bot.send_message(message.from_user.id, msg9)
        await asyncio.sleep(2)

        video_note_path = 'media/girls.mp4'

        my_video = FSInputFile(video_note_path)


        await bot.send_video_note(chat_id=message.from_user.id,
                                  video_note=my_video, reply_markup=start_keyboards)



    except Exception as error:
        with open('errors.txt', 'a') as error_file:
            error_message = f"Ошибка при старте бота - {error}\n"
            error_file.write(error_message)
        print(f"Ошибка при старте бота - {error}")