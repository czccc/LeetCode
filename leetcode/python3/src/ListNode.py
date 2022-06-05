# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class TListNode(ListNode):
    def __init__(self, val=0, next=None) -> None:
        super().__init__(val, next)

    def __str__(self):
        return TListNode.string(self)

    def __repr__(self):
        return TListNode.string(self)

    @staticmethod
    def eq(l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return True
        elif l1 and not l2 or l2 and not l1:
            return False
        else:
            return l1.val == l2.val and TListNode.eq(l1.next, l2.next)

    @staticmethod
    def string(node):
        ss = "List: "
        if not node:
            ss += "None"
        else:
            ss += str(node.val)
            p = node.next
            while p:
                ss += " -> " + str(p.val)
                p = p.next
        return ss

    @staticmethod
    def build(node_list):
        if not node_list:
            return None
        p = head = TListNode(0)
        for val in node_list:
            p.next = TListNode(val)
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


class TListNodeTest(unittest.TestCase):
    def test_init(self):
        p = TListNode(0)
        self.assertEqual(p.val, 0)
        p.val = 1
        self.assertEqual(p.val, 1)
        self.assertEqual(p.next, None)

    def test_eq(self):
        p = TListNode(0)
        q = TListNode(1)
        self.assertEqual(TListNode.eq(p, q), False)
        q.val = 0
        self.assertEqual(TListNode.eq(p, q), True)
        p.next = TListNode(1)
        self.assertEqual(TListNode.eq(p, q), False)
        q.next = TListNode(1)
        self.assertEqual(TListNode.eq(p, q), True)

    def test_build(self):
        node_list = [0, 1, 2, 3, 4]
        l1 = TListNode.build(node_list)
        l2 = p = TListNode(0)
        p.next = TListNode(1)
        p = p.next
        p.next = TListNode(2)
        p = p.next
        p.next = TListNode(3)
        p = p.next
        p.next = TListNode(4)
        self.assertTrue(TListNode.eq(l1, l2))

    def test_none_build(self):
        node_list = []
        l1 = TListNode.build(node_list)
        self.assertEqual(l1, None)

    def test_flat(self):
        node_list = [0, 1, 2, 3, 4]
        l1 = TListNode.build(node_list)
        self.assertTrue(TListNode.flat(l1) == node_list)

    def test_print(self):
        result = "List: 0 -> 1 -> 2 -> 3 -> 4"
        node_list = [0, 1, 2, 3, 4]
        l1 = TListNode.build(node_list)
        self.assertEqual(TListNode.string(l1), result)

    def test_none_print(self):
        result = "List: None"
        node_list = []
        l1 = TListNode.build(node_list)
        self.assertEqual(TListNode.string(l1), result)


if __name__ == "__main__":
    unittest.main("ListNode", verbosity=2)
