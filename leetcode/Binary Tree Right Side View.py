"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
"""
__author__ = 'phoenix'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def recursion(self, next_l, res):
        if len(next_l) == 0:
            return
        temp = []
        temp_l = []
        for node in next_l:
            temp.append(node.val)
            if node.right is not None:
                temp_l.append(node.right)
            if node.left is not None:
                temp_l.append(node.left)
        res.append(temp)
        self.recursion(temp_l, res)

    def rightSideView(self, root):
        if root is None:
            return []
        res_l = []
        self.recursion([root], res_l)
        return [x[0] for x in res_l]


if __name__ == '__main__':
    root = TreeNode(1)
    a, b, c, d = TreeNode(2), TreeNode(3), TreeNode(5), TreeNode(4)
    root.left = a
    root.right = b
    b.left = c
    b.right = d
    print(Solution().rightSideView(None))