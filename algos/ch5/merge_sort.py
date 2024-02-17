def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid_i = len(nums) // 2
    first = merge_sort(nums[:mid_i])
    second = merge_sort(nums[mid_i:])
    return merge(first, second)


def merge(first, second):
    res = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1
    while i < len(first):
        res.append(first[i])
        i += 1
    while j < len(second):
        res.append(second[j])
        j += 1
    return res
