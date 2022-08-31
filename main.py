import telebot
from config import TOKEN
import keyboard as kb

bot = telebot.TeleBot(TOKEN)

#Bot start
@bot.message_handler(commands=['start', 'restart'])
def start_msg(message):
    bot.send_message(
    message.chat.id, 
    text = '', 
    reply_markup=kb.main_menu,
    parse_mode='html'
    )

#Bot commands

@bot.message_handler(content_types=['text'])
def idk():
    pass
