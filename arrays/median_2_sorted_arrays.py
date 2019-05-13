import unittest



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

class Test(unittest.TestCase):
    def test_me(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1,3], [2]), 2.0)
        self.assertEqual(s.findMedianSortedArrays([1,2], [3,4]), 2.5)

if __name__ == '__main__':
    unittest.main()