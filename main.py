import telebot
from telebot import types

bot = telebot.TeleBot('6709225571:AAHYbX6g7xiua34ezCJooPhCh630LjN7ZUA')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 ку")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой помощник умскул!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 ку':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Ссылка на вебинар')
        btn2 = types.KeyboardButton('Наш сайт Умскул')
        btn3 = types.KeyboardButton('Наш телеграм бот')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)


    elif message.text == 'Ссылка на вебинар':
        bot.send_message(message.from_user.id, 'Видео.\n \nСсылка на вебинар по ' + '[ссылке](https://youtu.be/WqGCbO4QW9k)', parse_mode='Markdown')

    elif message.text == 'Наш сайт Умскул':
        bot.send_message(message.from_user.id, 'Наш сайт Умскул тут ' + '[ссылке](https://umschool.net/)', parse_mode='Markdown')

    elif message.text == 'Наш телеграм бот':
        bot.send_message(message.from_user.id, 'Наш телеграм бот для вашей задачи ' + '[ссылке](https://t.me/PythonUM_homework)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) 