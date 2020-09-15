#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        L = len(nums)
        root = TreeNode(nums[L // 2])
        root.left = self.sortedArrayToBST(nums[:L // 2])
        root.right = self.sortedArrayToBST(nums[L // 2 + 1:])
        return root
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().sortedArrayToBST

    def test_1(self):
        args = [[-10, -3, 0, 5, 9]]
        ans = TreeNode.build([0, -3, 9, -10, null, 5])
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
