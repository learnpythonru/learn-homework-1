people = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

"""
while True:
    if people.pop(0) == 'Валера':
        print('Валера нашелся')
        break


while True:
    if people[0] != 'Валера':
        print(f"Ой, это {people[0]}")
        people.pop(0)
    else:
        print("Валера нашелся")
        break
"""

def find_person(name):
    while True:    
        if name not in people:
            print(f'{name} отсутствует в списке')
            break
        elif people[0] != name:
            #print(f"Ой, это {people[0]}")
            people.pop(0)
        else:
            print(f"{name} нашелся")
            break


find_person("Петя")
find_person("Даша")
find_person("Оля")