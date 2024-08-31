import telebot

token = "7403077161:AAH3jblk9q4Fo2UJPG5q4FhIukrNQqk5KXc"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def sendxd(message):
    bot.reply_to(message, "HOLA CRACK")

bot.polling()