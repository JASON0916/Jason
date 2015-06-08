"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        p, q, i = head, head, 0
        while i < k and q is not None:
            q = q.next
            i += 1
            if q is None and i <= k:
                k %= i
                i = 0
                q = head
                if k == 0:
                    return head
        while q.next is not None:
            q = q.next
            p = p.next
        tmp = p.next
        p.next = None
        q.next = head
        return tmp

if __name__ == '__main__':
    list_node = [ListNode(i+1) for i in range(5)]
    for i in range(4):
        list_node[i].next = list_node[i+1]
    head = Solution().rotateRight(list_node[0], 1)
    while head is not None:
        print(head.val)
        head = head.next