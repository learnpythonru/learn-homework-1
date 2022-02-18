def main():
    def strings(first_string, second_string):
        if first_string and second_string:
            if first_string == second_string:
                return '1'
            elif first_string != second_string and len(first_string) > len(second_string):
                return '2'
            elif first_string != second_string and second_string =='learn':
                return '3'
            elif isinstance(first_string, str) and isinstance(second_string, str):
                return 'Строка'
        else:
            return '0'

    print(strings(first_string = 'Home', second_string = 'learn'))
    print(strings(first_string = 'Home', second_string = 'Home'))
    print(strings(first_string = 'Home', second_string = 'Apple'))
    print(strings(first_string = True, second_string = False))




if __name__ == "__main__":
    main()           
















