"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def check_parameters_strings(string1:str, string2:str):
   if not isinstance(string1, str) or not isinstance(string2, str):
      return 0
   else:
      if string1 == string2:
         return 1
      else:
        if len(string1)>len(string2):
          return 2
        if string2 == 'learn':
          return 3

   
   
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    string1 = 1
    string2 = 2
    print(check_parameters_strings(string1,string2))    

    string1 = "python"
    string2 = "python"
    print(check_parameters_strings(string1,string2)) 

    string1 = "python3"
    string2 = "python"
    print(check_parameters_strings(string1,string2))  


    string1 = "py"
    string2 = "learn"
    print(check_parameters_strings(string1,string2))  

if __name__ == "__main__":
    main()
