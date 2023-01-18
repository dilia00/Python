import telebot
import metods 
import io
import time
from telebot import types
import requests
from random import randint

number = None
is_started = False

token = "5624431164:AAEDYftBG9WaNr6QWKHumR8DlHBNXlbFBwE"
bot = telebot.TeleBot(token, parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('играть')
itembtn2 = types.KeyboardButton('котик')
itembtn3 = types.KeyboardButton('погода')
itembtn4 = types.KeyboardButton('файл')
itembtn5 = types.KeyboardButton('регистрация')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    metods.logger(message)
    bot.reply_to(message, f"Привет, {message.from_user.first_name}", reply_markup=markup)

@bot.message_handler(commands=['alert'])
def send_alert(message):
    metods.logger(message)
    with open("users.txt", "r", encoding="utf-8") as data:
        users_id = data.readlines()
        for id in users_id:
            try:
                bot.send_message(id[:-1], "Оповещение")
            except telebot.apihelper.ApiTelegramException:
                print(f"Сщщбщение пользователю {id[:-1]} отправить не удалось")

	

    
@bot.message_handler(content_types=["text"])
def hello_user(message):
    global is_started
    global number
    if is_started:
        if message.text.isdigit():
            input_number = int(message.text)
            if input_number > number:
                bot.send_message(message.from_user.id, "Меньше!")
            elif input_number < number:
                bot.send_message(message.from_user.id, "Больше!")
            elif input_number == number:
                is_started = False
                bot.send_message(message.from_user.id, f"Ура! Ты выиграл! Я загадал число {number}.")
        else:
            bot.send_message(message.from_user.id, "Введи просто число")
    else:
        metods.logger(message)
        if message.text == "регистрация":
            user_id = str(message.from_user.id) + "\n"
            data = open("users.txt", "r+", encoding="utf-8")
            try:
                lines = data.readline()
                if user_id not in lines:
                    data.writelines(str(message.from_user.id) + "\n")
                    bot.send_message(message.from_user.id, "Регистрация прошла успешно!")
                else:
                    bot.send_message(message.from_user.id, "Данный аккаунт уже зарегистрирован")
            except io.UnsupportedOperation:
                data.writelines(str(message.from_user.id) + "\n")
                bot.send_message(message.from_user.id, "Регистрация прошла успешно!")
            data.close()
        elif message.text == "играть":
                number = randint(1, 1000)
                is_started = True
                bot.send_message(message.from_user.id, "я загадал чисто от 1 до 1000, попробуй его отгадать. Введи первое число.")
        elif message.text == "погода":
                r = requests.get("https://wttr.in/?0T")
                bot.send_message(message.from_user.id, r.text)
        elif message.text == "котик":
            r = f"https://cataas.com/cat?t=${time.time()}"
            bot.send_photo(message.from_user.id, r)
        elif message.text == "файл":
            data = open("users.txt", encoding="utf-8")
            bot.send_message(message.from_user.id, data)
            data.close()
        else:
            bot.reply_to(message, "Не понимаю. Введите /start или /help")    

bot.infinity_polling()