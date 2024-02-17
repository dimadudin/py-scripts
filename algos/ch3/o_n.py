def find_max(nums):
    if not nums:
        return 0
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max
