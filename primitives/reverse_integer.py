# Reverse a signed 32 bit integer.
import unittest

class Solution(object):
    def reverse(self, x):
        """
        Algo:
        1. Reverse string 
        2. If reversed string has - sign as last char, remove that and put it in the beginning.
        3. If reversed string's int value overflows size of 32 bit signed int then return 0.
        """
        re_string = str(x)[::-1]
        if re_string[-1] == '-':
            re_string = re_string[-1]+re_string[0:-1]
        output = int(re_string)

        if output > 2**31 or output < -2**31:
            output = 0
        return(output)



class Test(unittest.TestCase):
    def testme(self):
        s = Solution()
        self.assertEqual(s.reverse(1534236469), 0)
        self.assertEqual(s.reverse(0), 0)
        self.assertEqual(s.reverse(123), 321)
        self.assertEqual(s.reverse(-123), -321)
        self.assertEqual(s.reverse(120), 21)
        

if __name__ == "__main__":
    unittest.main()