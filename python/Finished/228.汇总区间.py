#
# @lc app=leetcode.cn id=228 lang=python
#
# [228] 汇总区间
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        start = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != cur + 1:
                if start == cur:
                    ans.append("{}".format(start))
                else:
                    ans.append("{}->{}".format(start, cur))
                start = cur = nums[i]
            else:
                cur += 1
        if start == cur:
            ans.append("{}".format(start))
        else:
            ans.append("{}->{}".format(start, cur))
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
        cls._func = Solution().summaryRanges

    def test_1(self):
        args = [[0, 1, 2, 4, 5, 7]]
        ans = ["0->2", "4->5", "7"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [[0, 2, 3, 4, 6, 8, 9]]
        ans = ["0", "2->4", "6", "8->9"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
