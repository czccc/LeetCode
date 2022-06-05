#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().containsDuplicate

    def test_1(self):
        args = [[1, 2, 3, 1]]
        ans = True
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
