import unittest


class Solution:
    def singleNonDuplicate(self, nums):
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


class singleNonDuplicateTest(unittest.TestCase):

    def setUp(self):
        # Test Data
        self.test_input = [
            [1, 1, 2, 3, 3, 4, 4, 8, 8],
            [1, 1, 3, 3, 4, 4, 5, 8, 8],
            [1, 1, 3, 3, 4, 4, 6, 8, 8],
            [3,3,7,7,10,11,11],
            [1, 1, 3, 3, 4, 4, 8],
            [1, 1, 3, 3, 4, 4, 8, 8, 9],
            [1, 1, 3, 3, 4, 4, 8, 8, 10],
        ]

        self.test_output = [
            2,
            5,
            6,
            10,
            8,
            9,
            10
        ]

        self.test_range = range(len(self.test_input))
        # self.test_range = [4]

        # Tester Object
        self.singleElement = Solution()

    def test_singleNonDuplicate(self):
        for i in self.test_range:
            self.assertEqual(self.test_output[i],
                             self.singleElement.singleNonDuplicate(self.test_input[i]))


if __name__ == '__main__':
    unittest.main()
