def lidar(data=None, position=2):
    line_0 = False
    line_1 = False
    line_2 = False
    if data is None:
        return 'Остановиться'
    for string in data.keys():
        line_0 += data[string][0]
        line_1 += data[string][1]
        line_2 += data[string][2]
    if (position == 1 and not line_0) or (position == 2 and not line_1) or (position == 3 and not line_2):
        return 'Оставаться на текущей полосе'
    elif (position == 1 and not line_1) or (position == 2 and not line_2):
        return 'Перестроиться направо'
    elif (position == 2 and not line_0) or (position == 3 and not line_1):
        return 'Перестроиться налево'
    else:
        return 'Остановиться'


print(lidar({
   2: [False, False, False],
   1: [False, False, False],
   0: [False, True, False],
}))
