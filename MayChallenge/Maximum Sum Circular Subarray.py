class Solution:
    def maxSubarraySumCircular(self, A):

        max_kadane = self.kadane(A)
        cirSum = 0

        for i in range(len(A)):
            cirSum += A[i]
            A[i] = -A[i]

        cirSum = cirSum + self.kadane(A)

        if cirSum > max_kadane and cirSum != 0:
            return cirSum
        else:
            return max_kadane

    def kadane(self, A):
        max_curr = max_sum = A[0]
        for i in range(1, len(A)):
            max_curr = max(A[i], max_curr + A[i])
            max_sum = max(max_sum, max_curr)
        return max_sum


maxSub = Solution()

print(maxSub.maxSubarraySumCircular([1,-2,3,-2]))
print(maxSub.maxSubarraySumCircular([-2,-3,-1]))
print(maxSub.maxSubarraySumCircular([2,-2,2,7,8,0]))
print(maxSub.maxSubarraySumCircular([5,-3,5]))
