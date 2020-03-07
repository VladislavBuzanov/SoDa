# -*- coding: utf-8 -*-
import telebot
import service.text_service as text
import service.image_service as image

bot = telebot.TeleBot("980191188:AAGcx1XaNFobSuQRCIWNJehgSsqzo5hIz6Y")


# Сервис, который будет искать продукт по названию, и выкидывать ответ, исходя из этой информации.
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    text.handle_text(message.text)


@bot.message_handler(content_types=['photo'])
def response_image(img):
    print("OPA")
    file = bot.get_file(img.json['photo'][-1]['file_id'])
    print(type(file))
    file.download()
    image.handle_image(file)


bot.polling(none_stop=True, interval=0)
