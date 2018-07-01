import telebot
import json

token = "599427472:AAHhsx10cntdNyWMbKP4eJ6iysg9utBzemA"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет!":
        bot.send_message(message.chat.id, "Привет) Как дела?")
    elif message.text == "Запиши меня":
        data = {'First Name': message.from_user.first_name,
                'Second Name': message.from_user.last_name}
    else:
        bot.send_message(message.chat.id, "Ты не умеешь правильно здороваться!")


bot.polling(none_stop=True, interval=0)

