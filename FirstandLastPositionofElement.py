def searchRange(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            left_idx = i
            break
    else:
        return [-1, -1]

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            right_idx = i
            break

    if len(nums) == 1 and target == nums[0]:
        return [0, 0]

    return [left_idx, right_idx]


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([1,3], 1))
