from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node with next pointer.
class TreeNodeWithNext:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TTreeNode(TreeNode):
    def __init__(self, val):
        super().__init__(val)

    def __str__(self):
        return "Tree: " + str(TreeNode.flat(self))

    def __repr__(self):
        return str(TreeNode.flat(self))

    @staticmethod
    def eq(t1: Optional[TreeNode], t2: Optional[TreeNode]):
        if not t1 and not t2:
            return True
        elif t1 and not t2 or t2 and not t1:
            return False
        else:
            return (
                t1.val == t2.val
                and TTreeNode.eq(t1.left, t2.left)
                and TTreeNode.eq(t2.right, t2.right)
            )

    @staticmethod
    def build(node_list):
        if not node_list or node_list[0] is None:
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
                ret.append(None)
        while ret[-1] is None:
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
        node_list = [0, 1, 2, None, None, 3, 4]
        t1 = TreeNode.build(node_list)
        t2 = p = TreeNode(0)
        p.left = TreeNode(1)
        p.right = TreeNode(2)
        p = p.right
        p.left = TreeNode(3)
        p.right = TreeNode(4)
        self.assertTrue(t1 == t2)

    def test_none_build(self):
        node_list = []
        t1 = TreeNode.build(node_list)
        self.assertEqual(t1, None)

    def test_flat(self):
        node_list = [0, 1, 2, None, None, 3, 4]
        t1 = TreeNode.build(node_list)
        self.assertEqual(TreeNode.flat(t1), node_list)

    # def test_print(self):
    #     result = "Linked Node: 0 -> 1 -> 2 -> 3 -> 4"
    #     node_list = [0, 1, 2, 3, 4]
    #     t1 = TreeNode.build(node_list)
    #     self.assertEqual(TreeNode.print(t1, enable=False), result)

    # def test_none_print(self):
    #     result = "Linked Node: None"
    #     node_list = []
    #     t1 = TreeNode.build(node_list)
    #     self.assertEqual(TreeNode.print(t1, enable=False), result)


if __name__ == "__main__":
    unittest.main("TreeNode", verbosity=2)
