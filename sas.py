import unittest


class RemoveKDigits:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        number_list = [int(x) for x in num]
        result_stack = []
        tries = 0
        i = 0

        while i < len(number_list):
            while tries < k and len(result_stack) > 0 and result_stack[-1] > number_list[i]:
                result_stack.pop()
                tries += 1
            result_stack.append(number_list[i])
            i += 1

        while tries < k:
            result_stack.pop()
            tries += 1

        # Final String
        result_str = []
        for digit in result_stack:
            result_str.append(str(digit))

        final_str = ''.join(result_str)
        final_str = final_str.lstrip('0')

        if final_str == "":
            return "0"

        return final_str


class RemoveKDigitsTest(unittest.TestCase):

    def setUp(self):
        # Test Data
        self.test_input = [
            ["1432219", 3],
            ["10200", 1],
            ["10", 2],
            ["10", 1],
            ["5337", 2],
            ["1111111", 3],
            ["1234567890", 9],
        ]

        self.test_output = [
            "1219",
            "200",
            "0",
            "0",
            "33",
            "1111",
            "0"
        ]

        self.test_range = range(len(self.test_input))
        # self.test_range = [4]

        # Tester Object
        self.remove_k_digits = RemoveKDigits()

    def test_remove_k_digits(self):
        for i in self.test_range:
            self.assertEqual(self.test_output[i],
                             self.remove_k_digits.removeKdigits(self.test_input[i][0],
                                                                self.test_input[i][1]))


if __name__ == '__main__':
    unittest.main()