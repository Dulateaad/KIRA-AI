from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = TeleBot("@kira_ai_style_bot")

@bot.message_handler(commands=["start"])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text="Открыть Mini App", web_app=WebAppInfo(url="https://studio--studio-4612461108-2107c.us-central1.hosted.app")) 
    markup.add(btn)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы открыть приложение:", reply_markup=markup)

bot.infinity_polling()

