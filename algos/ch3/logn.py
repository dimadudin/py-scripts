def binary_search(target, arr):
    l, h = 0, len(arr)-1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] < target:
            l = mid+1
        else:
            h = mid-1
    if l != len(arr) and arr[l] == target:
        return True
    else:
        return False

