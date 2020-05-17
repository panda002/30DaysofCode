# code review done by https://github.com/adityakamble49
import unittest


class SearchRotatedSortedArray:

    def search(self, nums, target) -> int:
        nums.sort()
        if target in nums:
            return nums.index(target)

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
            0,
            1,
            2,
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
