"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def get_summ(num_one, num_two):
  try:
    num_one = int(num_one)
    try:
      num_two = int(num_two)
      x = int(num_one) + int(num_two)
      return x
    except ValueError:
      return f'{num_two} нельзя привести к целому числу'
  except ValueError:
    return f'{num_one} нельзя привести к целому числу'
      
    
if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
