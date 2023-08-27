#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.cn/problems/longest-univalue-path/description/
#
# algorithms
# Medium (47.70%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    83.2K
# Total Submissions: 174.5K
# Testcase Example:  '[5,4,5,1,1,null,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
#
# The length of the path between two nodes is represented by the number of
# edges between them.
#
#
# Example 1:
#
#
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 5).
#
#
# Example 2:
#
#
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 4).
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
#
#
#


from leetcode.before import *


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        pass


# @lc code=end


from leetcode.after import *


class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().twoSum

    def test_1(self):
        args = [[2, 7, 11, 15], 9]
        ans = [0, 1]
        ret = self._func(*args)
        self.assertEqual(ret, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
