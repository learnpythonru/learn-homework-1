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


def get_input() -> int:

    try:
        age = int(input('Введите возраст: '))
    except ValueError as err:
      print(f'{err} Возраст должен быть целым числом')

    assert age > 0, 'Возраст должен быть больше нуля'
    assert age < 122, 'Возраст слишком большой'
    
    return age


def stage_of_life(age: int) -> str:
    if age <= 6: return 'Учиться в детском саду'
    if age >= 7 and age <= 17: return 'Учиться в школе'
    if age >= 18 and age <= 24: return 'Учиться в ВУЗе'
    if age >= 25 and age <= 64: return 'Работает'
    if age >= 65: return 'Пенсионер'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    age = get_input()
    work = stage_of_life(age)
    print(work)

if __name__ == "__main__":
    main()
