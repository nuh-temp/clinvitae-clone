import unittest
import utils


class TreeTest(unittest.TestCase):

	def testInsert(self):
		t = utils.PrefixTree()
		t.Insert('ABC')

unittest.main()