# Hamming distance between 2 integers is the number of 
# positions at which the corresponding bits are different.

import unittest

def find_hamming_distance(x, y):
    """
    Algo:
    1. Get last bits of x and y and XOR them. XOR is 1 if bits are dis-similar.
    2. Right shift until both x and y are 0.
    3. Keep incrementing the result count.
    """
    result = 0
    while x > 0 or y > 0:
        result += (x & 0x01) ^ (y & 0x01)
        x >>= 1
        y >>= 1
    return result



class Test (unittest.TestCase):
    def testme(self):
        self.assertEqual(find_hamming_distance(1,4), 2)


if __name__ == "__main__":
    unittest.main()