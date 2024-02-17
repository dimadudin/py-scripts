def exponential_growth(n, factor, days):
    n_ = n
    res = [n_]
    for _ in range(days):
        n_ *= factor
        res.append(n_)
    return res
