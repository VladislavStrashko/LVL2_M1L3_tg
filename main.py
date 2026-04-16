mport telebot
from bot_logic import gen_pass, coin_flip, random_emoji

TOKEN = "  "

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(20)
    bot.reply_to(message, f"Вот твой пароль: {password}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = coin_flip()
    bot.reply_to(message, f"Монетка подброшена. Выпало: {result}")

@bot.message_handler(commands=['emoji'])
def send_emoji(message):

    emoji = random_emoji()
    bot.reply_to(message, f"Вот твой случайный смайлик: {emoji}")

@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):

    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):

    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):

    bot.reply_to(message, message.text)

bot.polling()
