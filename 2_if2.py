def main():
    string1 = input("Первая строка: ")
    string2 = input("Вторая строка: ")
    print(string_ent(string1, string2))


def string_ent(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string1 != string2 and str(string2) == "learn":
        return 3
    pass


if __name__ == "__main__":
    main()
