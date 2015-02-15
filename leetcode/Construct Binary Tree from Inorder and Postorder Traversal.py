"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

__author__ = 'phoenix'

"""
also memory limit exceeded
i have to say that the algorithm is correct for CPP version is accepted
fuck
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

    def show(self, root):
        if root is None:
            return
        self.show(root.left)
        print(root.val)

        self.show(root.right)


if __name__ == '__main__':
    o = Solution()
    o.show(o.buildTree([1,2,3,4], [2,4,3,1]))