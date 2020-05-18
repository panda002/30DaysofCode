def firstMissingPositive(nums):
    n = len(nums)
    a = set()
    if n == 0:
        return 1
    for i in range(1, n + 2):
        a.add(i)
    for i in a:
        if i not in nums and i != 0:
            return i


print(firstMissingPositive([]))
print(firstMissingPositive([1]))
print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))
