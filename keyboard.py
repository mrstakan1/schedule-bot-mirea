from telebot import types

#Main menu buttons
week_parity_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
week_parity_select.row("📅Чётная неделя", "📅Нечётная неделя")

#Even week button
even_week = types.ReplyKeyboardMarkup(resize_keyboard=True)
even_week.row("Пн📅", "Вт📅", "Ср📅")
even_week.row("Чт📅", "Пт📅", "Сб📅")
even_week.row("MAIN MENU📲")

#Odd week button
odd_week = types.ReplyKeyboardMarkup(resize_keyboard=True)
odd_week.row("Пн📅", "Вт📅", "Ср📅")
odd_week.row("Чт📅", "Пт📅", "Сб📅")
odd_week.row("MAIN MENU📲")

#Back to main menu
back_to_main_menu= types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_main_menu.row('MAIN MENU📲')


