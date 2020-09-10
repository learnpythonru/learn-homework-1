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

#функция для добавления правильного окончания к возрасту:
def age_ending(age_input):
  age_int = int(age_input)%10
  if age_int == 0 or 5 <= age_int<= 9 or 10 <= age_int <= 20:
    return 'лет'
  if age_int == 1:
    return 'год'
  if 2 <= age_int <= 4:
    return 'года'
  
def get_age_status(age_input):
  if age_input.isdigit():
    age_input = int(age_input)
    if 1 <= age_input <= 5:
      return f'Ваш полный возраст: {age_input} {age_ending(age_input)}.\nВы должны учиться в детском саду.'
    elif 5 < age_input <= 17:
      return f'Ваш  полный возраст: {age_input} {age_ending(age_input)}.\nВы должны учиться в школе.'
    elif 17 < age_input <= 150:
      return f'Ваш полный возраст: {age_input} {age_ending(age_input)}.\nВы должны учиться в ВУЗе или работать.'
    elif age_input > 150:
      return f'Ваш полный возраст: {age_input} {age_ending(age_input)}.\nУкажите ваш настоящий возраст!.'
    elif age_input == 0:
      return f'Ваш полный возраст: {age_input} {age_ending(age_input)}.\nВы должны вырасти, чтобы пойти учиться в детский сад.'
  else:
    return ('Возраст указан неверно. Должно быть целое и положительное число.')

def main():
    age_input = input('\nВведите ваш возраст:\n') 
    print(get_age_status(age_input))

if __name__ == "__main__":
    main()
