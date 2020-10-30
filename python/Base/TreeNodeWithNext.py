# Definition for a binary tree node.
class TreeNodeWithNext(object):
    def __init__(self, x=0, left=None, right=None, next=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right and self.next == self.next

    def __str__(self):
        return str(TreeNodeWithNext.flat(self))

    def __repr__(self):
        return str(TreeNodeWithNext.flat(self))

    @staticmethod
    def print(node, enable=True):
        pass

    @staticmethod
    def build(node_list):
        if not node_list or node_list[0] is None:
            return None
        root = TreeNodeWithNext(node_list[0])
        queue = [root]
        for i in range(1, len(node_list), 2):
            node = queue.pop(0)
            if node_list[i]:
                node.left = TreeNodeWithNext(node_list[i])
                queue.append(node.left)
            if i + 1 < len(node_list) and node_list[i + 1]:
                node.right = TreeNodeWithNext(node_list[i + 1])
                queue.append(node.right)
        return root

    @staticmethod
    def flat(root):
        ret = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append(None)
        while ret[-1] is None:
            ret.pop()
        return ret

    @staticmethod
    def flatOfNext(root):
        ret = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                ret.append(node.val)
                if not node.next:
                    ret.append(None)
                queue.append(node.left)
                queue.append(node.right)
        return ret


# TEST ONLY
import unittest

class TreeNodeWithNextTest(unittest.TestCase):

    def test_init(self):
        p = TreeNodeWithNext(0)
        self.assertEqual(p.val, 0)
        p.val = 1
        self.assertEqual(p.val, 1)
        self.assertEqual(p.left, None)
        self.assertEqual(p.right, None)

    def test_eq(self):
        p = TreeNodeWithNext(0)
        q = TreeNodeWithNext(1)
        self.assertEqual(p == q, False)
        q.val = 0
        self.assertEqual(p == q, True)
        p.left = TreeNodeWithNext(1)
        self.assertEqual(p == q, False)
        q.left = TreeNodeWithNext(1)
        self.assertEqual(p == q, True)

    def test_build(self):
        node_list = [0, 1, 2, None, None, 3, 4]
        l1 = TreeNodeWithNext.build(node_list)
        l2 = p = TreeNodeWithNext(0)
        p.left = TreeNodeWithNext(1)
        p.right = TreeNodeWithNext(2)
        p = p.right
        p.left = TreeNodeWithNext(3)
        p.right = TreeNodeWithNext(4)
        self.assertTrue(l1 == l2)

    def test_none_build(self):
        node_list = []
        l1 = TreeNodeWithNext.build(node_list)
        self.assertEqual(l1, None)

    def test_flat(self):
        node_list = [0, 1, 2, None, None, 3, 4]
        l1 = TreeNodeWithNext.build(node_list)
        self.assertEqual(TreeNodeWithNext.flat(l1), node_list)

    def test_flatOfNext(self):
        node_list = [0, 1, 2, None, None, 3, 4]
        ans = [0, None, 1, 2, None, 3, 4, None]
        l1 = TreeNodeWithNext.build(node_list)
        self.assertEqual(TreeNodeWithNext.flat(l1), node_list)

    # def test_print(self):
    #     result = "Linked Node: 0 -> 1 -> 2 -> 3 -> 4"
    #     node_list = [0, 1, 2, 3, 4]
    #     l1 = TreeNodeWithNext.build(node_list)
    #     self.assertEqual(TreeNodeWithNext.print(l1, enable=False), result)

    # def test_none_print(self):
    #     result = "Linked Node: None"
    #     node_list = []
    #     l1 = TreeNodeWithNext.build(node_list)
    #     self.assertEqual(TreeNodeWithNext.print(l1, enable=False), result)


if __name__ == "__main__":
    unittest.main("TreeNodeWithNext", verbosity=2)
