import telebot

#parsbot 
bot = telebot.TeleBot('7939669010:AAEG8-KmNSVoisckbRFYM36Kq2-HkXJZWrU')


@bot.message_handler(commands=["status"])
def start_message(message):
    bot.send_message(message.chat.id, f"Привет чат\nВаше сообщение: {message.id}")


if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
