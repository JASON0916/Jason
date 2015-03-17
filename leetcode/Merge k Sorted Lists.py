"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        temp = result = ListNode(9999)
        lists = [x for x in lists if x is not None]
        while len(lists) > 0:
            val = [i.val for i in lists]
            index = val.index(max(val))
            temp.next = lists[index]
            temp = temp.next
            if lists[index].next is None:
                lists[index: index+1] = []
            else:
                lists[index] = lists[index].next
        return result.next


if __name__ == '__main__':
    a = [None]
    o = Solution()
    c = o.mergeKLists(a)
    while c is not None:
        print(c.val)
        c = c.next