"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        temp = result = ListNode(9999)
        lists = [x for x in lists if x is not None]
        while len(lists) > 0:
            index = 0
            for i in range(len(lists)):
                if lists[i].val < lists[index].val:
                    index = i
            temp.next = lists[index]
            temp = temp.next
            if lists[index].next is None:
                lists[index: index+1] = []
            else:
                lists[index] = lists[index].next
        return result.next
"""
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

23: Merge k Sorted Lists
https://oj.leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

===Comments by Dabay===

递归：每次把lists折半，分别处理左右两个子lists，然后merge。和归并排序的算法一样。
时间复杂度为NlgN
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def merge(node1, node2):
            head = node = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next
            if node1:
                node.next = node1
            elif node2:
                node.next = node2
            return head.next

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge(lists[0], lists[1])

        node1 = self.mergeKLists(lists[:len(lists)/2])
        node2 = self.mergeKLists(lists[len(lists)/2:])
        return merge(node1, node2)


def main():
    s = Solution()
    ln1 = ListNode(1)
    ln1.next = ListNode(10)
    ln2 = ListNode(2)
    ln2.next = ListNode(20)
    node = s.mergeKLists([ln1, ln2])
    while node:
        print("%s->" % node.val)
        node = node.next
    print("None")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
