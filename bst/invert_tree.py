
import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ds.binary_tree import BinaryTree

# O(n) time, O(lg n) space - due to recursion
def invertBinaryTree(tree):
    if tree is None:
        return 
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swap(tree):
    tree.left, tree.right = tree.right, tree.left

test1 = BinaryTree(1)
invertedTest1 = BinaryTree(1)

test2 = BinaryTree(1).insert([2])
invertedTest2 = BinaryTree(1).invertedInsert([2])

test3 = BinaryTree(1).insert([2, 3])
invertedTest3 = BinaryTree(1).invertedInsert([2, 3])

test4 = BinaryTree(1).insert([2, 3, 4])
invertedTest4 = BinaryTree(1).invertedInsert([2, 3, 4])

test5 = BinaryTree(1).insert([2, 3, 4, 5])
invertedTest5 = BinaryTree(1).invertedInsert([2, 3, 4, 5])

test6 = BinaryTree(1).insert([2, 3, 4, 5, 6])
invertedTest6 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6])

test7 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
invertedTest7 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7])

test8 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8])
invertedTest8 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8])

test9 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
invertedTest9 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])

test10 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
invertedTest10 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9, 10])

test11 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
invertedTest11 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        invertBinaryTree(test1)
        self.assertTrue(test1, invertedTest1)

    def test_case_2(self):
        invertBinaryTree(test2)
        self.assertTrue(test2.__eq__(invertedTest2))

    def test_case_3(self):
        invertBinaryTree(test3)
        self.assertTrue(test3.__eq__(invertedTest3))

    def test_case_4(self):
        invertBinaryTree(test4)
        self.assertTrue(test4.__eq__(invertedTest4))

    def test_case_5(self):
        invertBinaryTree(test5)
        self.assertTrue(test5.__eq__(invertedTest5))

    def test_case_6(self):
        invertBinaryTree(test6)
        self.assertTrue(test6.__eq__(invertedTest6))

    def test_case_7(self):
        invertBinaryTree(test7)
        self.assertTrue(test7.__eq__(invertedTest7))

    def test_case_8(self):
        invertBinaryTree(test8)
        self.assertTrue(test8.__eq__(invertedTest8))

    def test_case_9(self):
        invertBinaryTree(test9)
        self.assertTrue(test9.__eq__(invertedTest9))

    def test_case_10(self):
        invertBinaryTree(test10)
        self.assertTrue(test10.__eq__(invertedTest10))

    def test_case_11(self):
        invertBinaryTree(test11)
        self.assertTrue(test11.__eq__(invertedTest11))


if __name__ == "__main__":
	unittest.main()
