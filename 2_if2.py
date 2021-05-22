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
def compare(a, b):
  if not (isinstance(a, str) and isinstance(b, str)):
    return 0
  if a == b:
    return 1
  if a != b and len(a) > len(b):
    return 2
  if a != b and b == 'learn':
    return 3
  
def main():
    print(compare(123, 'ads'))
    print(compare('qwerty', 'qwerty'))
    print(compare('asdfghjkl', 'qwer'))
    print(compare('fdas', 'learn'))
    print(compare('fds', 'adfasdfsas'))
    
if __name__ == "__main__":
    main()
