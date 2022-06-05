#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = q = dummy
        while q.next:
            k = q.next
            if k.val < x:
                q.next = k.next
                k.next = p.next
                p.next = k
                if p == q:
                    q = q.next
                p = p.next
            else:
                q = q.next
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
        cls._func = Solution().partition

    def test_1(self):
        args = [ListNode.build([1, 4, 3, 2, 5, 2]), 3]
        ans = ListNode.build([1, 2, 2, 4, 3, 5])
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
