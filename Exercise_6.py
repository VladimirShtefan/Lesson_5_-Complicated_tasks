def surrender_of_money(sum_, nominal_):
    dict_nominal = {}
    list_nominal = sorted(list(map(int, nominal_.split(','))), reverse=True)
    for nominal in list_nominal:
        temp_sum = sum_ // nominal
        dict_nominal[nominal] = temp_sum
        sum_ -= temp_sum * nominal
    return dict_nominal


try:
    print(surrender_of_money(int(input('Введите сумму: ')), input('Введите номиналы через запятую: ')))
except ValueError:
    print('Не верный ввод')
