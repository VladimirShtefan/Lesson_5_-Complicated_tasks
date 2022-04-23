def print_time(seconds_):
    hours = seconds_//3600
    minutes = seconds_//60 - hours*60
    seconds = seconds_ - minutes*60 - hours*3600
    result = ''
    if hours != 0:
        result += f'{hours} ч '
    if minutes != 0:
        result += f'{minutes} м '
    return result + f'{seconds} с'


print(print_time(int(input())))
