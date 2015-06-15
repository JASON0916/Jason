__author__ = 'phoenix'
"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        def recursion(root):
            if root is None:
                return
            else:
                root.right, root.left = root.left, root.right
                recursion(root.left)
                recursion(root.right)
        recursion(root)
        return root