#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = end = dummy
        length = 0
        while end.next:
            length += 1
            end = end.next
        k %= length
        for _ in range(length - k):
            p = p.next
        end.next = dummy.next
        dummy.next = p.next
        p.next = None
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
        cls._func = Solution().rotateRight

    def test_1(self):
        args = [ListNode.build([1, 2, 3, 4, 5]), 2]
        ans = ListNode.build([4, 5, 1, 2, 3])
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [ListNode.build([0, 1, 2]), 4]
        ans = ListNode.build([2, 0, 1])
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
