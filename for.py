"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
        {'school_class': '4a', 'scores': [5,5,5,5,5]},
        {'school_class': '4b', 'scores': [4,4,4,4,4]},
        {'school_class': '4c', 'scores': [3,3,3,3,3]},
        {'school_class': '4d', 'scores': [1,2,3,4,5]}
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    i = 0
    j = 0
    summa_school = 0

    for j in range(len(school)):
        summa_class = 0

        for i in range(len(school[j]["scores"])):   
            summa_class += school[j]["scores"][i]
            diff1 = summa_class/len(school[j]["scores"])
        print(diff1)
        summa_school += diff1/4

    print(summa_school)

if __name__ == "__main__":
    main()
