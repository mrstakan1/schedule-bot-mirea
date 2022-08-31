from email import message
import telebot
from config import TOKEN
import keyboard as kb
from text import *

bot = telebot.TeleBot(TOKEN)

#Bot start
@bot.message_handler(commands=['start', 'restart'])
def start_msg(message):
    bot.send_message(
    message.chat.id, 
    text = '<b> Выбери четность недели⤵️ </b>', 
    reply_markup=kb.week_parity_select,
    parse_mode='html'
    )

#Bot commands

@bot.message_handler(content_types=['text'])
def week_parity_selection(message):
    if message.text == "📅Чётная неделя":
        msg = bot.send_message(
            message.chat.id,
            text = '<b> Выбери день недели⤵️ </b>',
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == '📅Нечётная неделя':
        msg = bot.send_message(
            message.chat.id,
            text = '<b> Выбери день недели⤵️ </b>',
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    else:
        msg = bot.send_message(
            message.chat.id,
            text = '<b> ❗️Я не понимаю Вас, попробуйте еще раз. </b>',
            reply_markup=kb.week_parity_select,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, week_parity_selection)
        
def even_week_schedule(message):
    if message.text == 'Пн📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_monday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'Вт📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_tuesday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'Ср📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_wednesday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'Чт📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_thursday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'Пт📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_friday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'Сб📅':
        msg = bot.send_message(
            message.chat.id,
            text = even_saturday,
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    elif message.text == 'MAIN MENU📲':
        msg = bot.send_message(
            message.chat.id,
            text = '<b>❗️Вы перешли в главное меню.</b>',
            reply_markup=kb.week_parity_select,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, week_parity_selection)
    else:
        msg = bot.send_message(
            message.chat.id,
            text = '<b> ❗️Я не понимаю Вас, попробуйте еще раз.</b>',
            reply_markup=kb.even_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, even_week_schedule)
    
def odd_week_schedule(message):
    if message.text == 'Пн📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_monday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'Вт📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_tuesday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'Ср📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_wednesday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'Чт📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_thursday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'Пт📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_friday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'Сб📅':
        msg = bot.send_message(
            message.chat.id,
            text = odd_saturday,
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)
    elif message.text == 'MAIN MENU📲':
        msg = bot.send_message(
            message.chat.id,
            text = '<b>❗️Вы перешли в главное меню.</b>',
            reply_markup=kb.week_parity_select,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, week_parity_selection)
    else:
        msg = bot.send_message(
            message.chat.id,
            text = '<b>❗️Я не понимаю Вас, попробуйте еще раз.</b>',
            reply_markup=kb.odd_week,
            parse_mode='html'
        )
        bot.register_next_step_handler(msg, odd_week_schedule)


bot.infinity_polling()
