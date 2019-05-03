import unittest

# Given a string, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    """
    Algo:
    1. 2 pointers, start and end - end pointer scans the string forward and moves until there is 
    no matching char found in a map of chars. 
    2. When a matching char is found in a map, the start pointer is reset to the char before where end stops.
    3. Before resetting the start pointer, measure length of non-repeating char string as end - start.
    4. Maintain a max len and reset the counter everytime a length is found that is greater.
    """
    max_len = 0
    char_map = {}
    start = 0
    for i in range(0, len(s)):
        ch = s[i]
        if ch not in char_map:
            char_map[ch] = i
        else:
            cur_len = len(char_map)
            start = i 
            char_map = {}
            char_map[s[start-1]] = i-1
            char_map[s[start]] = i
            max_len = max(cur_len, max_len)
    return max(max_len, len(char_map))

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


# Tests
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring(''))
# print(lengthOfLongestSubstring('b'))
# print(lengthOfLongestSubstring('dvdf'))
# print(lengthOfLongestSubstring("ohomm"))
# print(lengthOfLongestSubstring("anviaj"))