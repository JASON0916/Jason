"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
__author__ = 'phoenix'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.__list = []

        def recursion(r, l):
            if r is None:
                return
            recursion(r.left, l)
            l.append(r.val)
            recursion(r.right, l)
        recursion(root, self.__list)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.__list) != 0:
            return True

    # @return an integer, the next smallest number
    def next(self):
        res = self.__list[0]
        self.__list = self.__list[1:]
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

"""
my solution sucks! that's one kind of good solutions.

class BSTIterator:
  # @param root, a binary search tree's root node
  def __init__(self, root):
    self.stack = []
    self.pushLeft(root)
  # @return a boolean, whether we have a next smallest number
  def hasNext(self):
    return self.stack
  # @return an integer, the next smallest number
  def next(self):
    top = self.stack.pop()
    self.pushLeft(top.right)
    return top.val
  def pushLeft(self, node):
    while node:
      self.stack.append(node)
      node = node.left
"""

if __name__ == '__main__':
    [a, b, c, d, e, f, g] = [TreeNode(i) for i in range(1, 8)]
    d.right = f
    d.left = b
    b.left = a
    b.right = c
    f.left = e
    f.right = g
    i, v = BSTIterator(d), []
    while i.hasNext():
        v.append(i.next())
    print(v)