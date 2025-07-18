from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = TeleBot("7828546240:AAFO_-dgTpbDQiUXRsx3CTj1FlZdRsUD11Q")

@bot.message_handler(commands=["start"])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text="Открыть Mini App", web_app=WebAppInfo(url="https://studio.firebase.google.com/studio-13031746"))
    markup.add(btn)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы открыть приложение:", reply_markup=markup)

bot.infinity_polling()
