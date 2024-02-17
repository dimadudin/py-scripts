def power_set(input_set):
    if not input_set:
        return [[]]
    res = []
    sub_list = power_set(input_set[1:])
    for sub in sub_list:
        res.append([input_set[0]] + sub)
        res.append(sub)
    return res
