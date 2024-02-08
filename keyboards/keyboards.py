from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Girls profiles 👩🏼👩🏻‍🦰❤️")
        ],
        [
            KeyboardButton(text="Terms of use", url="https://www.camcontacts.com/terms.html")
        ],
        [
            KeyboardButton(text="How does it work?")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)