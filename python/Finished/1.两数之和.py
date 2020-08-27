#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, x in enumerate(nums):
            if target - x not in d:
                d[x] = i
            else:
                return [d[target - x], i]


# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().twoSum

    def test_1(self):
        args = [[2, 7, 11, 15], 9]
        ans = [0, 1]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
