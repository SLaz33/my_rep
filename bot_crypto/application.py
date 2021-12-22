import telebot
from config import TOKEN, exchanger
from extensions import Convertor, APIException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def help(message: telebot.types.Message):
    text_start = 'Привет! Я - бот, который умеет конвертировать валюты.\n' \
                 '/help - получить параметры ввода\n' \
                 r'/values - получить список доступных валют'
    bot.send_message(message.chat.id, text_start)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text_help = 'Для того, чтобы начать работу,\n' \
                ' отправьте боту команду в следующем формате:\n' \
                '<название валюты, цену которой вы хотите узнать>\n' \
                '<название валюты, в которой отобразить цену>\n' \
                '<количество валюты>'
    bot.send_message(message.chat.id, text_help)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text_values = 'Доступные валюты:'
    for _ in exchanger.keys():
        text_values = '\n'.join((text_values, _))
    bot.send_message(message.chat.id, text_values)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    values = list(map(str.lower, values))
    try:
        result = Convertor.get_price(values)
    except APIException as i:
        bot.reply_to(message, i)
    except Exception as e:
        bot.reply_to(message, e)
    else:
        answer = f'{values[2]} {exchanger[values[0]]} по текущему курсу равно {result} {exchanger[values[1]]}'
        bot.reply_to(message, answer)


bot.polling(none_stop=True, interval=0)
