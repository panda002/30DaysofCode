def searchRange(nums, target):
    result = []

    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result


print(searchRange([2,2],2))
print(searchRange([1],0))
print(searchRange([1],1))
print(searchRange([1, 3],1))
