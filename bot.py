import telebot

TOKEN = "8700332266:AAHQ-oN_zvcl9TOwUso7uj8RJRg65UclQuM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام، خوش آمدی به ربات Toker ❤️")

bot.infinity_polling()
