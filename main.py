from aiogram import  Bot, Dispatcher, F
import asyncio
import logging
from dotenv import load_dotenv
import os
from aiogram.filters import Command
from handlers.start import start_bot
from handlers.help import help_message
from utils.commands import set_commands
from handlers.girls import info_girl
from handlers.terms import terms_info


from utils.database import Database



#загрузка данных и файла env (для безопасности)
load_dotenv()

#получение токена используемого бота
token = os.getenv('BOT_TOKEN')

#chat_id главного администратора для дальнейшего уведомления
admin_id = os.getenv('ADMIN_ID')

#экземпляр бота
bot = Bot(token=token, parse_mode='HTML')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#объявление диспетчера
dp = Dispatcher()


#запуск бота и приветствие

dp.message.register(start_bot, Command(commands='start'))

dp.message.register(info_girl, F.text == 'Girls profiles 👩🏼👩🏻‍🦰❤️')

dp.message.register(help_message, F.text == 'How does it work?')

dp.message.register(terms_info, F.text == 'Terms of use')



logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


async def start():
    db = Database(os.getenv('DATABASE_NAME'))
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())