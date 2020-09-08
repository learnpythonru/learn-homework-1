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
    age = input('Введите ваш возраст:') 

    def your_destiny(age):

      
      #функция для добавления правильного окончания к возрасту:
      def age_ending(age):

        if len(str(age)) == 1 and int(age) == 0:
          return 'лет'
        if len(str(age)) == 1 and int(age) == 1:
          return 'год'
        elif len(str(age)) == 1 and 2 <= int(age) <= 4:
          return 'года'
        elif len(str(age)) == 1 and 5 <= int(age) <= 9:
          return 'лет'
        elif 2 <= len(str(age)) and 10 <= int(age) <= 20:
          return 'лет'
        elif 2 <= len(str(age)):
          return age_ending(int(age)%10)

      if age.isdigit() or type(age) == int:
        if 1 <= int(age) <= 5:
          return print(f'Ваш полный возраст: {age} {age_ending(age)}.\nВам суждено учиться в детском саду')
        elif 5 < int(age) <= 17:
          return print(f'Вашage  полный возраст: {age} {age_ending(age)}.\nВам суждено учиться в школе')
        elif 17 < int(age) <= 150:
          return print(f'Ваш полный возраст: {age} {age_ending(age)}.\nВам суждено учиться в ВУЗе или работать')
        elif int(age) > 150:
          return print(f'Ваш полный возраст: {age} {age_ending(age)}.\nУкажите ваш настоящий возраст!')
        elif int(age) == 0:
          return print(f'Ваш полный возраст: {age} {age_ending(age)}.\nВаша судьба неопределена')
      else:
        return print('Возраст указан неверно. Должно быть целое и положительное число')
    your_destiny(age)

if __name__ == "__main__":
    main()
