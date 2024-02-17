def remove_nonints(nums):
    res = []
    for num in nums:
        if type(num) == int:
            res.append(num)
    return res
