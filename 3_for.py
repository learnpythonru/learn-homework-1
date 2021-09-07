"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    school = [{'school_class':'4a','scores': [3,4,5,2,2]},
    {'school_class':'5b','scores': [5,4,3,5,4]},
    {'school_class':'6c','scores':[3,4,2,3,4]}]
    len_all = 0
    sum_all = 0
    for n in range(len(school)):
        sum_class = 0
        for i in school[n]['scores']:
            sum_class += i
            sum_all += i
        len_all += len(school[n]['scores'])
        len_class = len (school[n]['scores'])    
        avg_class = sum_class / len_class
        print(f'Средняя оценка в классе {school[n]["school_class"]} : {avg_class}')
    avg_all = sum_all / len_all
    print(f'Средняя оценка в школе: {avg_all:.2f}')

 
if __name__ == "__main__":
    main()
