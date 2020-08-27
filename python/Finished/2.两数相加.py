#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

from Base.ListNode import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        p = ret
        r = 0
        while(r or l1 or l2):
            a1 = 0 if not l1 else l1.val
            l1 = None if not l1 else l1.next
            a2 = 0 if not l2 else l2.val
            l2 = None if not l2 else l2.next
            s = a1 + a2 + r
            r = s // 10
            p.next = ListNode(s % 10)
            p = p.next
        return ret.next
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().addTwoNumbers

    def test_1(self):
        l1 = ListNode.build([1, 9, 9])
        l2 = ListNode.build([9, 0, 1])
        l3 = ListNode.build([0, 0, 1, 1])
        self.assertEqual(self._func(l1, l2), l3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
