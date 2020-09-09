#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#
'''

'''

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def char2int(s):
            return ord(s) - ord('a')

        if not needle:
            return 0
        nh = len(haystack)
        nn = len(needle)
        if nh < nn:
            return -1
        base = 26
        modulus = 2**31
        needle_hash = 0
        haystack_hash = 0
        for i in range(nn):
            needle_hash = (needle_hash * base + char2int(needle[i])) % modulus
            haystack_hash = (haystack_hash * base + char2int(haystack[i])) % modulus
        if needle_hash == haystack_hash:
            return 0
        base_mul = pow(base, nn, modulus)
        for i in range(1, nh - nn + 1):
            haystack_hash = (haystack_hash * base - char2int(haystack[i - 1]) * base_mul + char2int(haystack[i + nn - 1])) % modulus
            if haystack_hash == needle_hash:
                return i
        return -1
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().strStr

    def test_1(self):
        args = ["hello", "ll"]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = ["hello", "la"]
        ans = -1
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = ["hello", ""]
        ans = 0
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

    def get_next(self, needle):
        next = [0 for _ in range(len(needle))]
        i = 1
        j = 0
        while i < len(needle):
            # j = next[i - 1]
            if needle[i] == needle[j]:
                j += 1
                next[i] = j
                i += 1
            elif j:
                j = next[j - 1]
            else:
                next[i] = j
                i += 1

class Solution2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution2().strStr

    def test_1(self):
        args = ["hello", "ll"]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = ["hello", "la"]
        ans = -1
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = ["hello", ""]
        ans = 0
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
