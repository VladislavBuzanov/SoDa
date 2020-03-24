# -*- coding: utf-8 -*-
import telebot

import service.image_service as image
import service.text_service as text
from server import Config

bot = telebot.TeleBot(Config.token)


# connecting to proxy
# apihelper.proxy = {Config.connection_type:Config.proxy}
# Сервис, который будет искать продукт по названию, и выкидывать ответ, исходя из этой информации.
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    text.handle_text(message.text)


@bot.message_handler(content_types=['photo'])
def response_image(message):
    try:

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # print(file_info)
        # print(file_info.file_path)
        src = Config.images_path + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        # bot.reply_to(message, "Фото добавлено")
        bot.reply_to(message, image.handle_image(src)[0])

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling(none_stop=True, interval=0)
