import unittest
from practical_2 import winner


class TestE(unittest.TestCase):
    def testE1(self):
        list1 = [10]
        list2 = [5]
        result = winner(list1,list2)
        self.assertEqual(result,"MAXI: WIN")

    def testE2(self):
        list1 = [10]
        list2 = [10]
        result = winner(list1,list2)
        self.assertEqual(result,"Equal Energy!")



    def testE3(self):
        list1 = [5]
        list2 = [10]
        result = winner(list1,list2)
        self.assertEqual(result,"MAXI: LOSE")


if __name__ == '__main__':
    unittest.main()