"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""
__author__ = 'phoenix'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        lr, ll = 0, 0
        tempr, templ = root, root
        while tempr is not None:
            lr += 1
            tempr = tempr.right
            if templ is not None:
                ll += 1
                templ = templ.left

        if lr == ll:
            return pow(2, ll)-1
        else:
            return self.countNodes(root.right)+self.countNodes(root.left)+1