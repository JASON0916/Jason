__author__ = 'phoenix'
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
"""


class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        res = []
        def recursion(root, res):
            if len(res) == k or root is None:
                return
            recursion(root.left, res)
            if len(res) < k:
                res.append(root.val)
            recursion(root.right, res)
        recursion(root, res)
        print(res)
        return res[-1]