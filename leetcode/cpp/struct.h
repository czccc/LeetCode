#ifndef _LEETCODE_STRUCT_H_
#define _LEETCODE_STRUCT_H_

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x = 0) : val(x), left(nullptr), right(nullptr) {}
};

#endif