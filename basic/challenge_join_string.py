def join_strings(strings):
    n = len(strings)
    res = ""
    if n > 0:
        for i in range(n - 1):
            res += strings[i] + ","
        res += strings[n - 1]
    return res
