def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(min_idx + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
