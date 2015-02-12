"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param head, a ListNode
    # @return nothing
    # fuck! what does 'in-place' mean!? even this is accepted????
    def reorderList(self, head):
        if head is None:
            return
        temp = head
        node_list = []
        while temp is not None:
            node_list.append(temp)
            temp = temp.next
        left, right = 0, len(node_list) - 1
        while left < right:
            node_list[left].next = node_list[right]
            left += 1
            node_list[right].next = node_list[left]
            right -= 1
        node_list[left].next = None
"""

class Solution:
    # @param head, a ListNode
    # @return nothing
    # that's the appropriate algorithm
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        tmp_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tmp_head
    def reorderList(self, head):
        if head is None:
            return
        slow = fast = head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next