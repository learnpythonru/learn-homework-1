"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    class_list = [{'school_class': '4a', 'scores': [3,4,4,5,2,5]}, 
                  {'school_class': '4b', 'scores': [5,5,5,5,3]}, 
                  {'school_class': '4c', 'scores': [2,3,5,5,4,4,2]}]
    total_summ = 0
    count_students = 0
    for s_class in class_list:
      class_summ = 0
      for score in s_class['scores']:
        class_summ += score
        total_summ += score
      s_class['mean'] = round(class_summ / len(s_class['scores']), 2)
      count_students += len(s_class['scores'])
      print(f"Средняя оценка для класса {s_class['school_class']}: {s_class['mean']}")
    print(f"Средняя оценка для школы: {round(total_summ / count_students , 2)}")




if __name__ == "__main__":
    main()
