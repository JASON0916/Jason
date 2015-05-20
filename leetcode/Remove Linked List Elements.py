"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
    	while head is not None and head.val == val:
    		head = head.next
    	res = head
    	if head is None:
    		return head
    	while head.next is not None:
    		if head.next.val == val:
    			head.next = head.next.next
    		else:
    			head = head.next
    	return res


if __name__ == '__main__':
	a = ListNode(1)
	
	print(Solution().removeElements(a,1))