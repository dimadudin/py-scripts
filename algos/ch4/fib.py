def fib(n):
    __i = 0
    _i = 1
    i = _i
    for _ in range(n - 1):
        i = __i + _i
        __i = _i
        _i = i
    if n == 0:
        return __i
    else:
        return i
