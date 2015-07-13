__author__ = 'phoenix'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


if __name__ == '__main__':
    a, b, c, d, e, f, g = [TreeNode(i) for i in [3, 5, 1, 6, 2, 0, 8]]
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    print Solution().lowestCommonAncestor(a, b, c).val