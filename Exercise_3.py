def search_bracket(user_string):
    list_open_bracket = []
    list_close_bracket = []
    for number_symbol in range(len(user_string)):
        if user_string[number_symbol] == '(':
            list_open_bracket.append(number_symbol)
        elif user_string[number_symbol] == ')':
            list_close_bracket.append(number_symbol)
    if not list_open_bracket or not list_close_bracket:
        return 'Не верно'
    if len(list_open_bracket) == len(list_close_bracket):
        if list_open_bracket[0] < list_close_bracket[0]:
            if list_close_bracket[len(list_close_bracket)-1] > list_open_bracket[len(list_open_bracket)-1]:
                return 'Верно'
    return 'Не верно'


print(search_bracket(input()))
