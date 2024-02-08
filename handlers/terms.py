from aiogram import Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

async def terms_btn():
    url = "https://www.camcontacts.com/terms.html?sidk=1ede3fc6182b210ca9422c5ac91ca4e6c350964"
    inline_keyboard = [
        [InlineKeyboardButton(text=f"Terms and Conditions", url=f"{url}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

async def terms_info(message: Message, bot: Bot):
    try:
        keyboard = await terms_btn()
        await bot.send_message(message.from_user.id, f"Click to read the information", reply_markup=keyboard)
    except Exception as error:
        with open('errors.txt', 'a') as error_file:
            error_message = f"Ошибка показа terms info - {error}\n"
            error_file.write(error_message)
        print(f"Ошибка показа terms info - {error}")