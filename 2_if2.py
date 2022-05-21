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

def check_strings(str1, str2):
    if (str(type(str1)) != "<class 'str'>") or (str(type(str2)) != "<class 'str'>"):
        return 0
    elif str1 == str2:
        return 1
    else:
        if str2 == 'learn':
            return 3
        elif len(str1) > len(str2):
            return 2
        else:
            return f"Attention!'{str2}' is longer than '{str1}'"
    
  


def main():

    print(check_strings(3, '5')) # 0
    print(check_strings(3, True)) # 0
    print(check_strings('learn', 'learn')) # 1
    print(check_strings('learnnn', 'lear')) # 2
    print(check_strings('learnnn', 'learn')) # 3
    print(check_strings('lear', 'learns')) # Attention!'learns' is longer than 'lear'
    print(check_strings('lear', 'learn')) # 3

if __name__ == "__main__":
    main()
