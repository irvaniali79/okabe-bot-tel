import telebot
import random
import khayyam
import qrcode

bot = telebot.TeleBot('2140486942:AAFJgBA0y10ZHkbM-7VIIfUm6B3-WMBnsAk')
number=0


@bot.message_handler(commands=['start'])
def register(message):
    bot.reply_to(message, "Welcome to my bot " +  message.from_user.first_name +  " !")
   
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""
    Wellcome\n
    /start\n
    Guess game\n
    /game \n
    maximum of array \n
    /max\n
    position of maximum number of array\n
    /maxindex\n
    how old are you? \n
    /age\n
    Sentence2voice\n
    /voice\n
    Text2QRcode\n
    /qrcode\n
    Guide\n
    /help\n
    """)

@bot.message_handler(commands=['game'])
def game(message):
    global number
    number = random.randint(0,100)
    bot.reply_to(message,"Guess a number Please between 0 to 100 ") 
    bot.register_next_step_handler(message , geuess)

def geuess(message):
    if int(message.text) > number:
        bot.reply_to(message, "greater!")
        bot.register_next_step_handler(message , geuess)
    elif int(message.text) < number :
        bot.reply_to(message, "smaller!")
        bot.register_next_step_handler(message , geuess)
    elif int(message.text) == number:
        bot.reply_to(message, "you guess right")

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

@bot.message_handler(commands=['age'])
def age(message):
    bot.reply_to(message,"Please enter your birth date ,use seprator \'/\' like 1379/12/22 ") 
    bot.register_next_step_handler(message ,agecalculator)

def agecalculator(message):
    date = message.text.split('/')
    dif = JalaliDatetime.now()-JalaliDatetime(date[0],date[1],date[2])
    bot.reply_to(message,dif)


@bot.message_handler(commands=['qrcode'])
def text2qrcode(message):
  bot.reply_to(message,"Enter your text :") 
  bot.register_next_step_handler(message ,toqrcode)

def toqrcode(message):
    img = qrcode.make(message.text) 
    img.save('qrcode.png')
    photo = open('qrcode.png', 'rb')
    bot.send_photo(message.chat.id, photo)

bot.infinity_polling()