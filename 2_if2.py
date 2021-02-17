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

def main():

    def check_strings(first_string, second_string):
        if first_string != str or second_string != str:
            return 0
        elif first_string == second_string: 
            return 1
        elif first_string != second_string and len(first_string) > len(second_string):
            return 2
        elif first_string != second_string and second_string == 'learn':
            return 3
        else: 
            return 'Unknown result'

    print(check_strings('hello', 4))
    print(check_strings('hello', 'hello')
    
if __name__ == "__main__":
    main()
