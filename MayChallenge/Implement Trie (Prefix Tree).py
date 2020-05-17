import unittest


class TreeNode:
    def __init__(self, v):
        self.value = v
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True


# Your Trie object will be instantiated and called as such:


obj = Trie()
obj.insert('aditya')
param_2 = obj.search('aditya')
param_3 = obj.startsWith('di')


class TrieTest(unittest.TestCase):

    def setUp(self):
        # Test Data
        self.test_input = [
            ['aditya', 'aditya', 'di'],
            ['aditya', 'sid', 'adi'],
        ]

        self.test_output = [
            [True, False],
            [False, True]
        ]
        self.test_range = range(len(self.test_input))
        # self.test_range = [4]

        # Tester Object
        self.searchin = Trie()

    def test_trie(self):
        for i in self.test_range:
            self.searchin.insert(self.test_input[i][0])
            self.assertEqual(self.test_output[i][0],
                             self.searchin.search(self.test_input[i][1]))
            self.assertEqual(self.test_output[i][1],
                             self.searchin.search(self.test_input[i][2]))


if __name__ == '__main__':
    unittest.main()
