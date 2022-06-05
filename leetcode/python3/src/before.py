from typing import List, Optional

null = None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


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
