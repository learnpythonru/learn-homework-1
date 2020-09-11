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
    marks = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4b', 'scores': [5,4,3,1,5,4]},
      {'school_class': '5a', 'scores': [2,3,5,1,4,3,2]},
      {'school_class': '5b', 'scores': [4,5,2,4,3,3,4,2,5]},
    ]  
    
    mark_num = 0
    ttl_marks = 0
    for mark in marks:
      mark_num += len(mark['scores'])
      ttl_marks += sum(mark['scores'])
      
    school_average = ttl_marks / mark_num
    print(f'Средняя оценка по школе: {school_average}')


    for cl_mark in marks:
      t = sum(cl_mark["scores"])/len(cl_mark["scores"])
      print(f'Средняя оценка класса "{cl_mark["school_class"]}": {t}')
        
if __name__ == "__main__":
    main()
