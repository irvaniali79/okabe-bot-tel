import telebot
import random
from khayyam import JalaliDatetime
import qrcode
import gtts

bot = telebot.TeleBot('2140486942:AAFJgBA0y10ZHkbM-7VIIfUm6B3-WMBnsAk')
number=0

btn=None


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
    Text2voice\n
    /voice\n
    Text2QRcode\n
    /qrcode\n
    Guide\n
    /help\n
    """)

@bot.message_handler(commands=['game'])
def game(message):
    global number,btn
    number = random.randint(0,100)
    bot.reply_to(message,"Guess a number Please between 0 to 100 ") 
    btn = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    content = telebot.types.KeyboardButton('new game')
    btn.add(content)
    bot.register_next_step_handler(message , geuess)
    btn=None
    
def geuess(message):

    if message.text=='new game':
        game(bot.send_message(message.chat.id,""))
    elif int(message.text) > number:
        bot.reply_to(message, "samller!")
        bot.register_next_step_handler(message , geuess)
    elif int(message.text) < number :
        bot.reply_to(message, "greater!")
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
    bot.reply_to(message,dif[0]/365)


@bot.message_handler(commands=['qrcode'])
def text2qrcode(message):
    bot.reply_to(message,"Enter your text :") 
    bot.register_next_step_handler(message ,toqrcode)

def toqrcode(message):
    img = qrcode.make(message) 
    img.save(f"qrcode_{message.chat.id}.png")
    photo = open(f"qrcode_{message.chat.id}.png", 'rb')
    bot.send_photo(message.chat.id, photo)
    
@bot.message_handler(commands=['voice'])
def voice(message):
    bot.reply_to(message,"please enter your text :") 
    bot.register_next_step_handler(message , text2voice)

def text2voice(message):
    voiceobj = gtts.gTTS(text=message.text ,  lang= 'en', slow=False)
    voiceobj.save(f"voice_{message.chat.id}.ogg")
    voiceobj = open(f"voice_{message.chat.id}.ogg", 'rb')
    bot.send_voice(message.chat.id,voiceobj)

bot.infinity_polling()