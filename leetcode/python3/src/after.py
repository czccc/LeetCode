from .before import *

import unittest


class TListNode:
    def __init__(self, head: Optional[ListNode] = None) -> None:
        self.head = head

    def __str__(self) -> str:
        return "List: " + str(TListNode.flat(self.head))

    def __repr__(self) -> str:
        return "List: " + str(TListNode.flat(self.head))

    def from_list(self, node_list) -> None:
        self.head = TListNode.build(node_list)

    def to_list(self) -> List[int]:
        return TListNode.flat(self.head)

    @staticmethod
    def eq(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
        if not l1 and not l2:
            return True
        elif l1 and not l2 or l2 and not l1:
            return False
        else:
            return l1.val == l2.val and TListNode.eq(l1.next, l2.next)

    @staticmethod
    def build(node_list: List[int]) -> Optional[ListNode]:
        if not node_list:
            return None
        p = head = ListNode(0)
        for val in node_list:
            p.next = ListNode(val)
            p = p.next
        return head.next

    @staticmethod
    def flat(node: Optional[ListNode]) -> List[int]:
        ret = []
        p = node
        while p:
            ret.append(p.val)
            p = p.next
        return ret


class TTreeNode:
    def __init__(self, head: Optional[TreeNode] = None):
        self.head = head

    def __str__(self) -> str:
        return "Tree: " + str(TTreeNode.flat(self.head))

    def __repr__(self) -> str:
        return "Tree: " + str(TTreeNode.flat(self.head))

    def from_list(self, node_list) -> None:
        self.head = TTreeNode.build(node_list)

    def to_list(self) -> List[int]:
        return TTreeNode.flat(self.head)

    @staticmethod
    def eq(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
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
    def build(node_list: List[int]) -> Optional[TreeNode]:
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
    def flat(root: Optional[TreeNode]) -> List[int]:
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


class TTreeNodeWithNext:
    def __init__(self, head: Optional[TreeNodeWithNext] = None) -> None:
        self.head = head

    def __str__(self) -> str:
        return "Tree: " + str(TTreeNodeWithNext.flat(self.head))

    def __repr__(self) -> str:
        return "Tree: " + str(TTreeNodeWithNext.flat(self.head))

    def from_list(self, node_list) -> None:
        self.head = TTreeNodeWithNext.build(node_list)

    def to_list(self) -> List[int]:
        return TTreeNodeWithNext.flat(self.head)

    @staticmethod
    def eq(t1: Optional[TreeNodeWithNext], t2: Optional[TreeNodeWithNext]) -> None:
        if not t1 and not t2:
            return True
        elif t1 and not t2 or t2 and not t1:
            return False
        else:
            return (
                t1.val == t2.val
                and TreeNodeWithNext.eq(t1.left, t2.left)
                and TreeNodeWithNext.eq(t2.right, t2.right)
                and TTreeNodeWithNext.eq(t1.next, t2.next)
            )

    @staticmethod
    def build(node_list: List[int]) -> Optional[TreeNodeWithNext]:
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
    def flat(root: Optional[TreeNodeWithNext]) -> List[int]:
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
