def threeSsum(nums):
    triplets = []
    nums.sort()
    # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)-2):
        if i == 0 or (i > 0 and nums[i] != nums[i-1]):
            low = i + 1
            high = len(nums)-1
            sum = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == sum:
                    triplets.append([nums[i], nums[low], nums[high]])
                    # here we check for duplicates and if the next number is duplicate then increase the pointer
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    # else increase the pinter to move on to the next item
                    low += 1
                    high -= 1
                # if the sum of low and high is greater than the sum, then we should decrease the counter of high
                elif nums[low] + nums[high] > sum:
                    high -= 1
                # else if the sum of low and high is less than the sum, then we have to increase the counter of low
                else:
                    low += 1
    return triplets


print(threeSsum([-1, 0, 1, 2, -1, -4]))
