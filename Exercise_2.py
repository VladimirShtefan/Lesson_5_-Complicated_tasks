def string_selection(string_):
    split_string_ = [word.lower() for word in string_.split()]
    try:
        index_start = split_string_.index('старт')
    except ValueError:
        return 'нет слова старт'
    try:
        return ' '.join(split_string_[index_start+1: split_string_.index('стоп')])
    except ValueError:
        return ' '.join(split_string_[index_start+1::])


print(string_selection(input('Введите строку: ')))
