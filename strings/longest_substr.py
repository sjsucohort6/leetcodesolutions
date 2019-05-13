import unittest

# Given a string, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    """
    Algo: Sliding window approach
    1. 2 pointers, start and cur.
    2. start stays at first letter being scanned, cur moves forward from start until a repeating char is found.
    3. a dict is used to keep letters already found with their position as value.
    4. scanning continues until max_len is less than remaining chars to be scanned.
    Time complexity: O(n)
    Space complexity: O(n) worst case
    """
    max_len = 0
    for start in range(0, len(s)):
        map = {}
        if max_len < len(s) - start:
            for cur in range(start, len(s)):
                if s[cur] not in map:
                    map[s[cur]] = cur
                    max_len = max(max_len, len(map))
                else:
                    break
    return max_len

class Test(unittest.TestCase):
    def test_me(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(lengthOfLongestSubstring(''), 0)
        self.assertEqual(lengthOfLongestSubstring('b'), 1)
        self.assertEqual(lengthOfLongestSubstring('dvdf'), 3)
        self.assertEqual(lengthOfLongestSubstring("ohomm"), 3)
        self.assertEqual(lengthOfLongestSubstring("anviaj"), 5)

if __name__ == '__main__':
    unittest.main()