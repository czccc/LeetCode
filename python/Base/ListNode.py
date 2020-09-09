# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next

    def __str__(self):
        return ListNode.print(self, False)

    def __repr__(self):
        return ListNode.print(self, False)

    @staticmethod
    def print(node, enable=True):
        ss = "Linked Node: "
        if not node:
            ss += "None"
        else:
            ss += str(node.val)
            p = node.next
            while p:
                ss += " -> " + str(p.val)
                p = p.next
        if enable:
            print(ss)
        return ss

    @staticmethod
    def build(node_list):
        if not node_list:
            return None
        p = head = ListNode(0)
        for val in node_list:
            p.next = ListNode(val)
            p = p.next
        return head.next

    @staticmethod
    def flat(node):
        ret = []
        p = node
        while p:
            ret.append(p.val)
            p = p.next
        return ret


# TEST ONLY
import unittest

class ListNodeTest(unittest.TestCase):

    def test_init(self):
        p = ListNode(0)
        self.assertEqual(p.val, 0)
        p.val = 1
        self.assertEqual(p.val, 1)
        self.assertEqual(p.next, None)

    def test_eq(self):
        p = ListNode(0)
        q = ListNode(1)
        self.assertEqual(p == q, False)
        q.val = 0
        self.assertEqual(p == q, True)
        p.next = ListNode(1)
        self.assertEqual(p == q, False)
        q.next = ListNode(1)
        self.assertEqual(p == q, True)

    def test_build(self):
        node_list = [0, 1, 2, 3, 4]
        l1 = ListNode.build(node_list)
        l2 = p = ListNode(0)
        p.next = ListNode(1)
        p = p.next
        p.next = ListNode(2)
        p = p.next
        p.next = ListNode(3)
        p = p.next
        p.next = ListNode(4)
        self.assertTrue(l1 == l2)

    def test_none_build(self):
        node_list = []
        l1 = ListNode.build(node_list)
        self.assertEqual(l1, None)

    def test_flat(self):
        node_list = [0, 1, 2, 3, 4]
        l1 = ListNode.build(node_list)
        self.assertTrue(ListNode.flat(l1) == node_list)

    def test_print(self):
        result = "Linked Node: 0 -> 1 -> 2 -> 3 -> 4"
        node_list = [0, 1, 2, 3, 4]
        l1 = ListNode.build(node_list)
        self.assertEqual(ListNode.print(l1, enable=False), result)

    def test_none_print(self):
        result = "Linked Node: None"
        node_list = []
        l1 = ListNode.build(node_list)
        self.assertEqual(ListNode.print(l1, enable=False), result)


if __name__ == "__main__":
    unittest.main("ListNode", verbosity=2)
