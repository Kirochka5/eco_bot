import telebot, os, random, requests
from logic import *  
 # Инициализация бота с использованием его токена
bot = telebot.TeleBot("")
    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
@bot.message_handler(commands=['recycle'])
def recycle_info(message):
    bot.reply_to(message,recycling())    

@bot.message_handler(commands=['sort'])
def sorting_info(message):
    bot.reply_to(message,sorting())    

@bot.message_handler(commands=['motive'])
def send_mem(message):
    mem_r = random.choice(os.listdir('images'))
    with open(f'images/{mem_r}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

    


# Запуск бота
bot.polling()