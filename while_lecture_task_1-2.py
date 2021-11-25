people = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

"""
#1. 
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
#2.
def get_name():
    name = input('Напишите какое-нибудь имя: ').capitalize()
    if name in people:
        find_person(name)
    else:
        print(f'{name} отсутствует в списке')

def find_person(name):

    #if name not in people:
    #    print(f'{name} отсутствует в списке')

    while True:    
        if people[0] != name:
            #print(f"Ой, это {people[0]}")
            people.pop(0)
        else:
            print(f"{name} нашелся")
            break

#find_person("Оля")
#find_person("Петя")
#find_person("Даша")
get_name()