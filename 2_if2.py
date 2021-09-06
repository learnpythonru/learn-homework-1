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
    def get_data_from_input(value1,value2):
        for value in (value1,value2):
            try:
                float(value)
                return 0
            except :
                if  value1==value2:
                    return 1
                else:
                    if len(value1) > len(value2) and value2 != 'learn':
                        return 2
                    elif value2 == 'learn':
                        return 3
                    elif 'learn' in value2.lower().strip():
                        return 4    
                    else: 
                        return 'Not defined case'     

    input1=input('Введите строку 1: ')
    input2=input('Введите строку 2: ')
    print(get_data_from_input(input1,input2))

if __name__ == "__main__":
    main()
