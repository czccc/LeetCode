#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = 1
        queue = [root]
        pre = root
        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                return ans
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node == pre:
                ans += 1
                if queue:
                    pre = queue[-1]
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
        cls._func = Solution().minDepth

    def test_1(self):
        args = [TreeNode.build([3, 9, 20, null, null, 15, 7])]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
