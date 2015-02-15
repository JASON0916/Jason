"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

__author__ = 'phoenix'

"""
memory limit exceeded on leetcode
I don't know why
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

    def show(self, root):
        if root is None:
            return
        self.show(root.left)
        print(root.val)

        self.show(root.right)


if __name__ == '__main__':
    o = Solution()
    o.show(o.buildTree([1,2,3,4,5,6,7,8], [3,4,2,5,1,7,6,8]))