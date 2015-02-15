"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

__author__ = 'phoenix'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        pointer = A[0]
        i = 1
        while i < len(A):
            if A[i] == pointer:
                A[i:i+1] = []
            else:
                pointer = A[i]
                i += 1
        return len(A)


if __name__ == '__main__':
    A = [1, 1]
    o = Solution()
    print(o.removeDuplicates(A), '\n')
    print(A)