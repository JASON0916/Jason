# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        tail, body, pre = head, head.next, head.next.next
        tail.next = None
        while pre is not None:            
            body.next = tail
            tail = body
            body = pre
            pre = pre.next
        body.next = tail
        return body

if __name__ == '__main__':
    a,b,c = ListNode(1), ListNode(2), ListNode(3)
    a.next = b
    b.next = c
    res = Solution().reverseList(a)
    while res is not None:
        print(res.val)
        res = res.next