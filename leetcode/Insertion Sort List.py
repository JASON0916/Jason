"""
Sort a linked list using insertion sort.
"""
__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
test cases may be wrong
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        fh = ListNode(0)
        fh.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = fh
                while pre.next.val < cur.next.val:
                    pre = pre.next
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
            else:
                cur = cur.next
        return fh.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(1)
    d = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    o = Solution()
    t = a
    while t is not None:
        print(t.val)
        t = t.next
    o.insertionSortList(a)
    while a is not None:
        print(a.val)
        a = a.next