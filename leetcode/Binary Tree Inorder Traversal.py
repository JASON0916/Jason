__author__ = 'phoenix'
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        stack, pointer = [], root
        res = []
        while True:
            while pointer is not None:
                stack.append(pointer)
                pointer = pointer.left
            if len(stack) > 0:
                pointer = stack.pop()
                res.append(pointer.val)
                pointer = pointer.right
            if len(stack) == 0 and pointer is None:
                break
        return res


if __name__ == '__main__':
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    print(Solution().inorderTraversal(a))