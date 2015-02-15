"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

__author__ = 'phoenix'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
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

    def sortedArrayToBST(self, num):
        return self.build_tree(num, 0, len(num) - 1)
