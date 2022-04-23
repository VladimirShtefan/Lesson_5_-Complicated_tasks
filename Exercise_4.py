def search_number(user_input):
    symbol_list = ['+', '-', '(', ')']
    for symbol in symbol_list:
        if symbol in user_input:
            user_input = user_input.replace(symbol, '')
    return [True for word in user_input.split(' ') if word.isdigit()]


print('Введен номер телефона' if search_number(input()) else 'Номер телефона не встречается')
