"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def employment(age: str) -> str:
    try:
        age = float(age)
    except ValueError:
        return 'ValueError: age should be a number'
    if age >= 65:
        return 'retiree'
    elif 24 <= age < 65:
        return 'employed'
    elif 18 <= age < 24:
        return 'student'
    elif 7 <= age < 18:
        return 'schoolchild'
    elif 3 <= age < 7:
        return 'kindergartner'
    elif 0 <= age < 3:
        return 'baby'
    else:
        return 'age could not be a negative number'

def main():
    age = input("Please, enter person's age\n")
    print(employment(age))

if __name__ == "__main__":
    main()
