from .PyVar import *
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(TreeNode.flat(self))

    def __repr__(self):
        return str(TreeNode.flat(self))

    @staticmethod
    def print(node, enable=True):
        pass

    @staticmethod
    def build(node_list):
        if not node_list or node_list[0] == null:
            return None
        root = TreeNode(node_list[0])
        queue = [root]
        for i in range(1, len(node_list), 2):
            node = queue.pop(0)
            if node_list[i]:
                node.left = TreeNode(node_list[i])
                queue.append(node.left)
            if i + 1 < len(node_list) and node_list[i + 1]:
                node.right = TreeNode(node_list[i + 1])
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
                ret.append(null)
        while ret[-1] is null:
            ret.pop()
        return ret


# TEST ONLY
import unittest

class TreeNodeTest(unittest.TestCase):

    def test_init(self):
        p = TreeNode(0)
        self.assertEqual(p.val, 0)
        p.val = 1
        self.assertEqual(p.val, 1)
        self.assertEqual(p.left, None)
        self.assertEqual(p.right, None)

    def test_eq(self):
        p = TreeNode(0)
        q = TreeNode(1)
        self.assertEqual(p == q, False)
        q.val = 0
        self.assertEqual(p == q, True)
        p.left = TreeNode(1)
        self.assertEqual(p == q, False)
        q.left = TreeNode(1)
        self.assertEqual(p == q, True)

    def test_build(self):
        node_list = [0, 1, 2, null, null, 3, 4]
        l1 = TreeNode.build(node_list)
        l2 = p = TreeNode(0)
        p.left = TreeNode(1)
        p.right = TreeNode(2)
        p = p.right
        p.left = TreeNode(3)
        p.right = TreeNode(4)
        self.assertTrue(l1 == l2)

    def test_none_build(self):
        node_list = []
        l1 = TreeNode.build(node_list)
        self.assertEqual(l1, None)

    def test_flat(self):
        node_list = [0, 1, 2, null, null, 3, 4]
        l1 = TreeNode.build(node_list)
        self.assertEqual(TreeNode.flat(l1), node_list)

    # def test_print(self):
    #     result = "Linked Node: 0 -> 1 -> 2 -> 3 -> 4"
    #     node_list = [0, 1, 2, 3, 4]
    #     l1 = TreeNode.build(node_list)
    #     self.assertEqual(TreeNode.print(l1, enable=False), result)

    # def test_none_print(self):
    #     result = "Linked Node: None"
    #     node_list = []
    #     l1 = TreeNode.build(node_list)
    #     self.assertEqual(TreeNode.print(l1, enable=False), result)


if __name__ == "__main__":
    unittest.main("TreeNode", verbosity=2)
