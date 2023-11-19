"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):   
  try:
    if max_discount <= 20:
      total_price = price - (price * discount / 100)
      return total_price
  except TypeError:
      try:                                                 # Есть вопрос!!! надо ли для защиты
        price = float(price)                               # Для защиты от дурака сделать тут функцию
        discount = float(discount)                         # abs()? просто по условию я отцательных не увидел
        max_discount = int(max_discount)                   # Но есть ощущение что это было бы правильно
        total_price = price - (price * discount / 100)
        return total_price
      except ValueError:
        if price.isalpha() or discount.isalpha() or max_discount.isalpha():
          return 'Не подходящий тип данных!'
   
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
