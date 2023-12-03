"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

import ephem
import datetime

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


# PROXY = {
#     "proxy_url": "socks5://t2.learn.python.ru:1080",
#     "urllib3_proxy_kwargs": {"username": PROXY_USERNAME, "password": PROXY_PASSWORD},
# }


def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(
        "Привет, дорогой пользователь! Ты вызвал команду /start. Ай-да молодец!"
    )


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def planet_constellation(update, context):
    user_text = update.message.text  # например, user_text = Mars
    command_and_planet_list = user_text.split()
    try:
        planet_name = command_and_planet_list[1].lower()
    except IndexError:
        update.message.reply_text(f"{user_text} содержит невалидное название планеты")
        return

    logging.info("earth", dir(ephem))
    planet = ""
    planet_dict = {
        "mercury": ephem.Mercury(),
        "venus": ephem.Venus(),
        "mars": ephem.Mars(),
        "jupiter": ephem.Jupiter(),
        "saturn": ephem.Saturn(),
        "uranus": ephem.Uranus(),
        "neptune": ephem.Neptune(),
    }
    if planet_name in planet_dict.keys():
        planet = planet_dict[planet_name]
    elif planet_name == "earth":
        update.message.reply_text(f"Земля не находится в созвездии")
    else:
        update.message.reply_text(f"Введите валидное имя планеты")
    current_date = datetime.datetime.now()
    planet.compute(current_date)
    constellation = ephem.constellation(planet)

    update.message.reply_text(f"{planet_name} находится в созвездии {constellation}")


def main():
    mybot = Updater(
        settings.API_KEY,
        # request_kwargs=PROXY,
        use_context=True,
    )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
