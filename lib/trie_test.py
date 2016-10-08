import unittest
import trie


class TreeTest(unittest.TestCase):

    def testInsert(self):
        t = trie.PrefixTree()
        word = 'ABC'
        t.Insert(word)
        node = t.root
        for char in word:
            self.assertIn(char, node.children)
            node = node.children[char]

    def testSearchByPrefix(self):
        t = trie.PrefixTree()
        t.Insert('ABC')
        t.Insert('ABB')
        t.Insert('ADC')
        t.Insert('AAB')
        actual = t.SearchByPrefix('AB')
        self.assertItemsEqual(actual, ['ABC', 'ABB'])

    def testSearchByPrefixNoResults(self):
        t = trie.PrefixTree()
        t.Insert('ABC')
        t.Insert('ABB')
        t.Insert('ADC')
        t.Insert('AAB')
        actual = t.SearchByPrefix('XXX')
        self.assertItemsEqual(actual, [])


if __name__ == "__main__":
    unittest.main()
