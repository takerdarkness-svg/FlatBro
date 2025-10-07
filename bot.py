import os
import telebot

# Отримай токен у @BotFather і встав сюди або в змінну оточення BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВСТАВ_СВІЙ_ТОКЕН_СЮДИ")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я бот для моніторингу квартир 🏠")

# Простий цикл, щоб бот працював постійно
if __name__ == "__main__":
    bot.infinity_polling()
