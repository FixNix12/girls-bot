from aiogram import Bot
from aiogram.types import Message, FSInputFile
import asyncio
from keyboards.keyboards import start_keyboards


async def help_message(message: Message, bot: Bot):
    try:
        msg1 = "Video Chat Window - How does it work?"
        msg2 = "Let's take a close look at our video chat window so we're 100% sure you get the maximum out of each video session."
        msg3 = "Here follows a description of each feature available on the video chat page:"
        msg4 = "1. Mute: To turn the Chathost's sound on or off"
        msg5 = "2. Video size: This gives you the option to change your video viewing dimensions. The options available are small, large, full window and full screen. When you are in full screen mode, the text remains visible for a few seconds and then disappears to allow you to fully enjoy the show. Furthermore, the option to send a message is disabled whilst in full screen. To re-enable it simply hit the escape button to return to the full window display, and from here you can type and send messages as normal."
        msg6 = "3. Cam2Cam: This allows you to send your webcam image to the Chathost (to disable this option click Stop Cam2Cam)"
        msg7 = "4. Switch Session: This gives you the option of going into a One2One session, where you can have an exclusive and private show without interruption. This option is automatically disabled if the Chathost has other viewers in her room."
        msg8 = "5. End Session: This ends your current video session."
        msg9 = "6. Cam2Cam Settings: This allows you to get help, mute or un-mute your microphone, change your audio settings and change your webcam settings."
        msg10 = "7. Message Dialog box and Sending Options. You have the option to add emoticons, write and send messages, change the text size and change the text bar location (between the top and bottom of the screen). Furthermore, you have the option to change your message settings from send to all to send private to the chathost."

        image_help = "media/help/help.png"

        help_img = FSInputFile(image_help)

        await bot.send_message(message.from_user.id, msg1)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg2)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg3)
        await asyncio.sleep(1)
        await bot.send_photo(message.from_user.id, help_img)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg4)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg5)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg6)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg7)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg8)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg9)
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, msg10, reply_markup=start_keyboards)
        await asyncio.sleep(1)
    except Exception as error:
        with open('errors.txt', 'a') as error_file:
            error_message = f"Ошибка показа help info - {error}\n"
            error_file.write(error_message)
        print(error_message)