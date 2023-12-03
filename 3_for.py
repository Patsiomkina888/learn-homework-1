"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров

"""

phone_sales = [
    {
        "product": "iPhone 12",
        "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
    },
    {
        "product": "Xiaomi Mi11",
        "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
    },
    {
        "product": "Samsung Galaxy 21",
        # "items_sold": [343, 390]
        "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
    },
]


def get_average(prouct_sum, list_of_items):
    return round(prouct_sum / len(list_of_items), 2)


def prouct_sum(list_of_numbers):
    prouct_sum = 0
    for number in list_of_numbers:
        prouct_sum += number
    return prouct_sum


total_sum = 0
for item in phone_sales:
    item_sum = sum(item["items_sold"])
    print(f'Суммарное количество продаж для {item["product"]} составляет {item_sum}')
    item_avg = get_average(item_sum, item["items_sold"])
    print(f'Среднее количество продаж для {item["product"]} составляет {item_avg}')
    total_sum += item_sum
print(f"Суммарное количество продаж составляет {total_sum}")
avg_total_sum = get_average(total_sum, phone_sales)
print(f"Среднее количество продаж составляет {avg_total_sum}")
