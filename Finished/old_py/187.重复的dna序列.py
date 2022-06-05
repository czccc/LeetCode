#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mod = 1 << 20
        nums = set()
        char2num = {"A": 0, "C": 1, "G": 2, "T": 3}
        ans = []
        ans_num = set()
        cur = 0
        for i in range(0, len(s)):
            cur = ((cur << 2) + char2num[s[i]]) % mod
            if i >= 9:
                if cur in nums and cur not in ans_num:
                    ans.append(s[i - 9:i + 1])
                    ans_num.add(cur)
                else:
                    nums.add(cur)
        return ans
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().findRepeatedDnaSequences

    def test_1(self):
        args = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"]
        ans = ["AAAAACCCCC", "CCCCCAAAAA"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
