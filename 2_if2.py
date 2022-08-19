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
first_str = 'fff'
second_str = 'learn'

def chack_type():

	if isinstance(first_str, str) and isinstance(second_str, str):
		if first_str == second_str:
			return 1
		elif first_str != second_str and len(first_str) > len(second_str):
			return 2
		elif first_str != second_str and second_str == 'learn':
			return 3
	else:
		return 0

print(chack_type())

if __name__ == "__main__":
    main()
