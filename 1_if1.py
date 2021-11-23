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

def guess_business(age):
    try:
        age = int(age)
        if 0 < age < 7:
            return 'Kindergarten'
        elif 7 <= age <= 17:
            return 'School'
        elif 18 < age < 23:
            return 'University'
        elif age >= 23:
            return 'Job'
        else:
            raise ValueError('Wrong age')
    except (ValueError, TypeError):
        return 'Wrong age'

def main():
    age = input('Enter your age: ')
    result = guess_business(age)
    print(result)

if __name__ == "__main__":
    main()
