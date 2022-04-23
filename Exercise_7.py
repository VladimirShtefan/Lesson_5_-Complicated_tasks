def validate(options=None):
    if options is None:
        options = {'h': 0, 'w': 0}
    return (157 <= options['h'] <= 175) & (50 <= options['w'] <= 70)


def validate_list(candidates):
    candidates_allow = []
    for human in candidates:
        try:
            assert validate(human)
            candidates_allow.append(human)
        except AssertionError:
            continue
    return candidates_allow


print(validate_list([
    {'name': 'Юрий', 'h': 157, 'w': 60},
    {'name': 'Олег', 'h': 177, 'w': 65},
    {'name': 'Юлия', 'h': 165, 'w': 57},
    {'name': 'Аркадий', 'h': 174, 'w': 59},
]))
