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
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""
    Wellcome\n
    /start\n
    Guess game\n
    /game \n
    how old are you? \n
    /age\n
    Sentence2voice\n
    /voice\n
    maximum of array \n
    /max\n
    position of maximum number of array\n
    /maxindex\n
    Text2QRcode\n
    /qrcode\n
    Guide\n
    /help\n
    """)


@bot.message_handler(commands=['max'])
def getarray(message):
    arr=bot.send_message(message.chat.id,'Enter your array for example :1 2 3 4')
    bot.register_next_step_handler(arr,max_array)
    
def max_array(message):    
    numbers=list(map(int,message.text.split()))
    bot.send_message(message.chat.id,max(numbers))

@bot.message_handler(commands=['maxindex'])
def getarray(message):
    arr=bot.send_message(message.chat.id,'Enter your array for example :1 2 3 4')
    bot.register_next_step_handler(arr,max_index_array)
    
def max_index_array(message):    
    numbers=list(map(int,message.text.split()))
    bot.send_message(message.chat.id,numbers.index(max(numbers)))



bot.infinity_polling()