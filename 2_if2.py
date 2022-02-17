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
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    str1 = input('Первая строчка: ') 
    str2 = input('Вторая строчка: ')
    if not isinstance(str1, str) and not isinstance(str2, str):
      print ('0')
    elif str1 == str2:
      print ('1')
    elif str1 != str2 or len(str1) > len(str2):
      print ('2')
    elif str1 != str2 or str2 == 'learn':
      print ('3')

    
if __name__ == "__main__":
    print(main(2, 1))
    print(main('Привет', 'Привет'))
    print(main('Приветы', 'Привет'))
    print(main('Привет', 'learn'))