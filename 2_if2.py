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
# this is test data
strings0 = ['greaterstring', 'lower']
strings1 = ['lower', 'greaterstring']
strings2 = [True, 'string']
strings3 = ['string', False]
strings4 = [123, '']
strings5 = ['']
strings6 = []
strings7 = ['equal', 'equal']
strings8 = ['hi', 'learn']
strings9 = ['verylongstring', 'learn']

# print the list of eguments and their types - just for debug
def testStrings(list):
  for each in list:
    if type(each) is str:
      print(f'The argument of {list} position {list.index(each)} is string')
    else:
      print(f'The argument of {list} at position {list.index(each)} is not a valid string')
      return 0

# added 4th option for the case if second string is greater
# added 5th option if we don't have one or all of strings
def compareStrings(list):
  try:
    testStrings(list)
        
    if list[0] == list[1]:
      print('The lengths of strings are equal ')
      return 1
    elif len(list[0]) > len(list[1]) and list[1] != 'learn':
      print('The length of the first string is greater')
      return 2
    elif list[0] != list[1] and list[1] == 'learn':
      print('THe lengths are diff and the second string is "learn"')
      return 3
    else:
      print('The second string is greater')
      return 4
    
  except TypeError:
    print('Value of string is invalid')
    return 0
  except IndexError:
    print('Missing arguments to compare strings')
    return 5
  
def defineTheLongestString(list):
  if list[0] == list[1]:
    return('none of them - they are equal')
  else:
    try:
     return(max(list , key = len))
    except TypeError:
     print('The argument is not a string')
    except ValueError:
     print('The list of strings is empty')

def main():
#  uncomment the blocks of code you need to test functions

#  case 0 
#  print(compareStrings(strings2))
#  print(f'The longest string is {defineTheLongestString(strings2)}')
#  print(compareStrings(strings3))
#  print(f'The longest string is {defineTheLongestString(strings3)}')
#  print(compareStrings(strings4))
#  print(f'The longest string is {defineTheLongestString(strings4)}')

#  case 1
 print(compareStrings(strings7))
 print(f'The longest string is {defineTheLongestString(strings7)}')

#  case 2
#  print(compareStrings(string0))
#  print(f'The longest string is {defineTheLongestString(string0)}')

#  case 3
#  print(compareStrings(strings8))
#  print(f'The longest string is {defineTheLongestString(strings8)}')
#  print(compareStrings(strings9))
#  print(f'The longest string is {defineTheLongestString(strings9)}')

#  case 4
#  print(compareStrings(strings1))
#  print(f'The longest string is {defineTheLongestString(strings1)}')

#  case 5
#  print(compareStrings(strings5))
#  print(f'The longest string is {defineTheLongestString(strings5)}')
#  print(compareStrings(strings6))
#  print(f'The longest string is {defineTheLongestString(strings6)}')
  
if __name__ == "__main__":
    main()
