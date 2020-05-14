# code review done by https://github.com/adityakamble49
def removeKdigits(num, k):
    length = len(num)
    stack = []
    string = []
    counter = 0
    i = 0

    if k == length:
        return '0'

    while i < length:
        while counter < k and len(stack) > 0 and stack[-1] > num[i]:
            stack.pop()
            counter += 1
        stack.append(num[i])
        i += 1

    while counter < k:
        stack.pop()
        counter += 1

    for i in range(len(stack)):
        char = stack[i]
        string.append(char)

    string = ''.join(string)
    string = string.lstrip('0')

    return string


print(removeKdigits("1432219", 3))  # Output: "1219" Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

print(removeKdigits("20200", 1))  # output - 200
