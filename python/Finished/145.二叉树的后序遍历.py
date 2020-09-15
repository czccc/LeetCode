#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        stack = []
        pre = None
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != pre:
                    p = p.right
                    stack.append(p)
                    p = p.left
                else:
                    p = stack.pop()
                    ans.append(p.val)
                    pre = p
                    p = None
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
        cls._func = Solution().postorderTraversal

    def test_1(self):
        args = [TreeNode.build([1, null, 2, 3])]
        ans = [3, 2, 1]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
