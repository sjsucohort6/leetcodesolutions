import unittest

class Solution:
    def reverseBits(self, n):
        """
        Algo:
        1. get last bit from int
        2. append to a list
        3. convert the list to string of bits
        4. convert the string to int passing base as 2 (for binary)
        """
        list = []
        for i in range(0,32):
            last_bit = n & 0x01
            list.append(last_bit)
            n >>= 1
        s = "".join(str(x) for x in list)
        return int(s, 2)


class Test (unittest.TestCase):
    def testme(self):
        s = Solution()
        self.assertEqual(s.reverseBits(43261596), 964176192)
        self.assertEqual(s.reverseBits(4294967293), 3221225471)

if __name__ == "__main__":
    unittest.main()