def binary_search(data, followers):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["followers"] < followers:
            low = mid + 1
        elif data[mid]["followers"] > followers:
            high = mid - 1
        else:
            return data[mid]["name"]
    return None
