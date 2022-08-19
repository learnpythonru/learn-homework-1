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
school_classes = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '3б', 'scores': [3,2,2,2,2]},
{'school_class': '7а', 'scores': [5,4,3,5,5]}]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
avg_school = 0
counter = 0

for cls in school_classes:

	avg_class = (sum(cls['scores'])) / len(cls['scores'])
	avg_school += avg_class
	counter += 1
	print(cls['school_class'], avg_class)

avg_school = round(avg_school / counter, 2)
print(avg_school)

if __name__ == "__main__":
    main()
