def line_comp(str1,str2):

    # не строки
    if isinstance(str1,int) and isinstance(str2,int):
        return 0

    # строки одинаковые
    elif str1 == str2:
        return 1

    # строки разные и первая длиннее
    elif str1 != str2 and len(str1) > len(str2):
        return 2

    # строки разные и вторая строка 'learn'
    elif str1 != str2 and str2 == 'learn':
        return 3

def main():
    if __name__ == "__main__":
        main()

print(f'Не строки: {line_comp(1,22)}')

print(f'строки одинаковые: {line_comp("asd","asd")}')

print(f'строки разные и первая длиннее: {line_comp("asds","asd")}')

print(f'строки разные и вторая строка "learn": {line_comp("asd","learn")}')
