"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

__author__ = 'phoenix'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def build_tree(self, num, start, end):
        if start > end:
            return None
        mid = int((start + end) / 2)
        left_child = self.build_tree(num, start, mid - 1)
        parent = TreeNode(num[mid])
        parent.left = left_child
        parent.right = self.build_tree(num, mid + 1, end)
        return parent

    def sortedListToBST(self, head):
        list_num = []
        while head is not None:
            list_num.append(head.val)
            head = head.next
        return self.build_tree(list_num, 0, len(list_num) - 1)