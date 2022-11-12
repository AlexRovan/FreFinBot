import telebot

bot = telebot.TeleBot('5617670899:AAF-ikXKqNVnxR5DFkx2dOafi6bUVJnM3qM')


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    add_category_btn = telebot.types.InlineKeyboardButton('Добавить категорию', callback_data='add_category')
    add_cash_btn = telebot.types.InlineKeyboardButton('Добавить расход', callback_data='add_cash')
    markup.add(add_category_btn, add_cash_btn)

    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name}({message.from_user.username}) с id={message.from_user.id}',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "add_category":
        bot.send_message(call.message.chat.id, 'add_category')
    elif call.data == "add_cash":
        bot.send_message(call.message.chat.id, 'add_cash')


bot.polling(none_stop=True)
