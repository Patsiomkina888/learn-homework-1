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
        # "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        "items_sold": [363, 500],
    },
    {
        "product": "Xiaomi Mi11",
        "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
    },
    {
        "product": "Samsung Galaxy 21",
        "items_sold": [343, 390]
        # "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
    },
]

# total_sum = 0
# for item in phone_sales:
#     item_sum = 0

#     for quantity in item["items_sold"]:
#         item_sum += quantity
#     item_avg = round(item_sum / len(item["items_sold"]), 2)

#     print(f'Суммарное количество продаж для {item["product"]} составляет {item_sum}')
#     item_avg = round(item_sum / len(item["items_sold"]), 2)
#     print(f'Среднее количество продаж для {item["product"]} составляет {item_avg}')

#     total_sum += item_sum
# print(f"Суммарное количество продаж составляет {total_sum}")
# avg_total_sum = round(total_sum / len(phone_sales), 2)
# print(f"Среднее количество продаж составляет {avg_total_sum}")


def get_average(sum, list_of_items):
    return round(sum / len(list_of_items), 2)


def sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number
    return sum


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
