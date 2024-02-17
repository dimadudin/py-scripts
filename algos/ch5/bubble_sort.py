def bubble_sort(nums):
    for j in range(len(nums)):
        for i in range(len(nums) - 1 - j):
            if nums[i + 1] < nums[i]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
    return nums
