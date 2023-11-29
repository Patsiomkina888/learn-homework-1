"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def two_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif str1 != str2:
            if str2 == "learn":
                return 3
            elif len(str1) > len(str2):
                return 2
            else:
                return 0

    else:
        return 0


if __name__ == "__main__":
    print(two_strings("check", 25))  # 0
    print(two_strings("check", "check"))  # 1
    print(two_strings("double check", "check"))  # 2
    print(two_strings("double check", "learn"))  # 3
    print(two_strings("double check", "double checkdouble check"))  # 0
