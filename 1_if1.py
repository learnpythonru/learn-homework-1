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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Please enter your age: '))

    def employment(age=int(age)):
        if 3 < age < 7:
            return 'You will be in kindergarten.'
        if 7 <= age < 18:
            return 'You will be in school.'
        if 18 <= age < 24:
            return 'You will be in college.'
        if 24 <= age < 65:
            return 'You must work, sry dude.'
        else:
            print('Sorry, your age is not in correct range of ages.')
            age = int(input('Please enter your age: '))
            return employment(age)

    your_job = employment(age)
    print(your_job)


if __name__ == "__main__":
    main()
