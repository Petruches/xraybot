import telebot
import psutil
import sys


bot = telebot.TeleBot(sys.argv[1])

service: str = "rsyslogd"


@staticmethod
def status() -> bool:
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == service:
            return proc.is_running()


@staticmethod
def info() -> str:
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == service:
            return str(proc)


@staticmethod
def restart_xray() -> str:
    import os, time
    os.system('systemctl restart xray')
    time.sleep(2)
    if status() == True:
        return "Рестарт успешен"
    else:
        return "Ошибка"


@bot.message_handler(commands=["restart"])
def restart(message):
    bot.send_message(message.chat.id, restart_xray())


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
