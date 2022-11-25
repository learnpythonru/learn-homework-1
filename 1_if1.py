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
def what_you_gonna_do(age: int) -> str:
    if age <= 5:
        return 'Тебе нужно в детский сад!'
    if age <= 17:
        return 'Тебе бы в школе учиться!'
    if age <= 23:
        return 'Привет студент!'
    if age <= 125:
       return 'Привет работяга!'
    return 'Привет вампир!'
      

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    while True:
      try:
          user_age = abs(int(input("Введите ваш возраст: "))) # а вдруг нажмет -15
      except ValueError:
          print('Вы ввели не число! Попробуйте ещё раз.')
          continue
      else:
        result = what_you_gonna_do(user_age)
        print(result)
        break

if __name__ == "__main__":
    main()
