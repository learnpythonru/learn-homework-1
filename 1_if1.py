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
    age = int(input("Введите возраст: "))
    if age <= 0:
      print("Not exist")
    elif 0 < age < 7:
      print("Посещение дет.сада")
    elif 7 <= age < 18:
      print("Учеба в школе")
    elif 18 <= age < 24:
      print("Учеба в ВУЗе") 
    else: 
      print("Работа")

if __name__ == "__main__":
    main()
