def search_bracket(user_string):
    user_list = list(user_string)
    while True:
        if '(' in user_list and ')' in user_list:
            if user_list.count('(') == user_list.count(')'):
                return 'Верно'
            else:
                return 'Не верно'
        else:
            return 'Не верно'


print(search_bracket(input()))
