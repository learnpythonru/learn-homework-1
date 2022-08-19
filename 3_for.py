"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
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
