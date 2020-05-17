# code review done by https://github.com/adityakamble49
import unittest


class SearchRotatedSortedArray:

    def search(self, nums, target):
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


class SearchRotatedSortedArrayTest(unittest.TestCase):

    def setUp(self):
        # Test Data
        self.test_input = [
            [[4, 5, 6, 7, 0, 1, 2], 0],
            [[4, 5, 6, 7, 0, 1, 2], 1],
            [[4, 5, 6, 7, 0, 1, 2], 2],
            [[4, 5, 6, 7, 0, 1, 2], 3],
        ]

        self.test_output = [
            4,
            5,
            6,
            -1
        ]

        self.test_range = range(len(self.test_input))
        # self.test_range = [4]

        # Tester Object
        self.searchin = SearchRotatedSortedArray()

    def test_remove_k_digits(self):
        for i in self.test_range:
            self.assertEqual(self.test_output[i],
                             self.searchin.search(self.test_input[i][0],
                                                  self.test_input[i][1]))


if __name__ == '__main__':
    unittest.main()
