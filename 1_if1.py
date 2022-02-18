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
    

    def should_to_do(age):
        if age < 6:
            return "User should study in kindergarten"
        if age < 18:
            return "User should study in school"
        if age < 22:
            return "User should study in university"
        return "User must have a job already!"

    try:
        age = int(input("Insert the user's age > "))
        to_do = should_to_do(age)
        print(to_do)
    except ValueError:
        print("It can't be an age!")

    
if __name__ == "__main__":
    main()
