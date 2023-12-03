"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    while True:
        answer = input("Kaк дела? ")
        if answer == "Хорошо":
            print("Ну и отлично!")
            break
        else:
            print("Рад, что у тебя {}".format(answer))


if __name__ == "__main__":
    hello_user()
