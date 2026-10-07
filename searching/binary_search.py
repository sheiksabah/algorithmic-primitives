# Binary search 

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
    return -1
    
print(binary_search([2, 5, 8, 12, 16, 23, 38], 23))
