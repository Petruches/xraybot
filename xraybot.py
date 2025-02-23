import telebot
import psutil


#parsbot 
bot = telebot.TeleBot('7939669010:AAEG8-KmNSVoisckbRFYM36Kq2-HkXJZWrU')


@staticmethod
def status() -> bool:
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == "rsyslogd":
            return proc.is_running()


def info() -> str:
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == "rsyslogd":
            return str(proc)


@bot.message_handler(commands=["status"])
def get_status(message):
    if status() == True:
        bot.send_message(message.chat.id, "Запущен")
    else:
        bot.send_message(message.chat.id, "Остановлен")


@bot.message_handler(commands=["allstatus"])
def all_status(message):
    bot.send_message(message.chat.id, info())


if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
