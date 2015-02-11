"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the min_numimum element.

You may assume no duplicate exists in the array.
"""

__author__ = 'phoenix'


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findmin(self, num):
        min_num = num[0]
        start, end = 0, len(num) - 1
        while start <= end:
            mid = int((start + end)/2)
            if num[mid] >= min_num:
                start = mid + 1
            else:
                min_num = num[mid]
                end = mid
        return min_num


if __name__ == '__main__':
    o = Solution()
    print(o.findmin([2, 3, 1]))