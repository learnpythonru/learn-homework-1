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
def persons_task(age):
    if age < 3 and age > 0:
      return 'baby with her mom all time'
    elif age < 7:
      return 'Kindergarten'
    elif age < 17:
      return 'School'
    elif age < 22:
      return 'Higher education'
    elif age >= 22 and age < 200:
      return 'Work'
    else:
      return 'Please inpute correct age'



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
      age = int(input('Please type your age '))
      answer = persons_task(age)
      print(answer)
    except ValueError:
      print('Пожалуйста введите возраст цифрами')



if __name__ == "__main__":
    main()
