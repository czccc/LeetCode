#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        p = dummy.next
        while p and p.next:
            if p.val == p.next.val:
                while p and p.next and p.val == p.next.val:
                    p = p.next
                p = p.next
                pre.next = p
            else:
                pre = pre.next
                p = p.next
        return dummy.next

# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().deleteDuplicates

    def test_1(self):
        args = [ListNode.build([1, 2, 3, 3, 4, 4, 5])]
        ans = ListNode.build([1, 2, 5])
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
