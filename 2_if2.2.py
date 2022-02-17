
def main():

    def strings(first_string, second_string):
        if isinstance(first_string, str) and isinstance(second_string, str):
            return 'Строка'
        elif not isinstance(first_string, str) and not isinstance(second_string, str):
            return '0'
        elif first_string == second_string:
            return '1'
        elif first_string != second_string and len(first_string) > len(second_string):
            return '2'
        elif first_string != second_string and second_string =='learn':
            return '3'

    print(strings(first_string = 'Home', second_string = 'learn'))
    print(strings(first_string = 1, second_string = 2))
    print(strings(first_string = , second_string = ))

if __name__ == "__main__":
    main()