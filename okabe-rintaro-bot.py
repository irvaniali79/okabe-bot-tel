import telebot
import random

bot = telebot.TeleBot('2140486942:AAFJgBA0y10ZHkbM-7VIIfUm6B3-WMBnsAk')


@bot.message_handler(commands=['start'])
def register(message):
    bot.reply_to(message, "Welcome to my bot " +  message.from_user.first_name +  " !")

@bot.message_handler(commands=['game'])
def game(message):
    num=random.randint(0,100)
    markup = telebot.types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "guess my number:", reply_markup=markup)
    

bot.infinity_polling()