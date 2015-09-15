#!/usr/bin/env python
# coding=utf-8
"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_list = [0]*(n+1)
        num_list[1] = 1
        for i in range(2, n+1):
            res = 99999999999999999
            j = 1
            while j*j <= i:
                if j*j == i:
                    res = 1
                    break
                res = min(res, num_list[i-j*j]+1)
                j+=1
            num_list[i] = res
        return num_list[n]
    
if __name__ == '__main__':
    print Solution().numSquares(13)
