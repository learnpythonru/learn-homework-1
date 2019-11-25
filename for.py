"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def average_mark(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum/len(scores) 

def increment():
    """
    Создать список из десяти целых чисел.
    Вывести на экран каждое число, увеличенное на 1.
    """
    inc_list: list = [10, 35, 50, 13, 5, 92, 12, 4, 32, 23]
    inc: str = ''
    for num in inc_list:
        inc += str(num + 1)+' '
    print(f"Инкрементированный список: {inc}") 

def vert_string():
    """
    Ввести с клавиатуры строку.
    Вывести эту же строку вертикально: по одному символу на строку консоли.
    """
    user_string = input('Ведите строку: ')
    for char in user_string:
        print(char)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    increment()
    vert_string()
    
    school = [{'school_class': '4a', 'scores': [3,5,4,4,3]},
              {'school_class': '4b', 'scores': [4,2,3,4,5]}
             ]     
    global_scores = []
    
    for score in school:
        global_scores += score['scores']  # Объединяем все данные из scores
        # Средний бал по каждому классу    
        score['average_scores'] = average_mark(score['scores'])
        print(f"Средний бал по классу {score['school_class']} : {score['average_scores']}")
    # Средний бал по всей школе
    all_average_scores = average_mark(global_scores)
    print(f"Средний бал по всей школе : {all_average_scores}")    

if __name__ == "__main__":
    main()
