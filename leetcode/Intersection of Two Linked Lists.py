"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""
__author__ = 'phoenix'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        tempa = headA
        tempb = headB
        vala = []
        valb = []
        while tempa is not None:
            vala.append(tempa.val)
            tempa = tempa.next
        while tempb is not None:
            valb.append(tempb.val)
            tempb = tempb.next
        min_root = headA
        if len(vala) >= len(valb):
            del(vala[0: len(vala) - len(valb)])
            min_root = headB
        else:
            del(valb[0: len(valb) - len(vala)])
        for i in range(len(vala)):
            if vala[i] == valb[i]:
                while min_root is not None:
                    if min_root.val == vala[i]:
                        return min_root
                    else:
                        min_root = min_root.next
            else:
                continue
        return None


if __name__ == '__main__':
    list1 = [1,3,5,6,7,8,9,10]
    list2 = [2,4,6,7,8,9,10]
    a = A = ListNode(list1[0])
    b = B = ListNode(list2[0])
    for i in range(1, len(list1)):
        a.next = ListNode(list1[i])
        a = a.next
    for i in range(1, len(list2)):
        b.next = ListNode(list2[i])
        b = b.next
    o = Solution()
    C = o.getIntersectionNode(A, B)
    if C is not None:
        print(C.val)