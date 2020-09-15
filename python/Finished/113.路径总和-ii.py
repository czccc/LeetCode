#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        ans = []
        for x in self.pathSum(root.left, sum - root.val):
            ans.append([root.val] + x)
        for x in self.pathSum(root.right, sum - root.val):
            ans.append([root.val] + x)
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
        cls._func = Solution().pathSum

    def test_1(self):
        args = [TreeNode.build([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]), 22]
        ans = [
            [5, 4, 11, 2],
            [5, 8, 4, 5]
        ]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
