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


def check_occupation_by_age(age):
    if 0 < age < 7:
        return 'kindergarten'
    elif 7 <= age < 16:
        return 'school'
    elif 16 <= age < 25:
        return "college"
    elif 25 <= age < 65:
        return "work"
    else:
        raise Exception('You\'re are too young or too old')


def main():
    try:
        age = int(input("Please enter your age : "))
        occupation = check_occupation_by_age(age)
        print(f'Your occupation is {occupation}')
    except ValueError:
        print('Invalid input, please enter correct age as an integer value')
    except Exception as e:
        print(e.args[0])


if __name__ == "__main__":
    main()
