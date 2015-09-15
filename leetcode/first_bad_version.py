#!/usr/bin/env python
# coding=utf-8
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(n):
    if n == 2:
        return False
    elif n==1:
        return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return -1
        left, right = 1, n
        while left+1 < right:
            test_item = left+(right-left)/2
            if isBadVersion(test_item) is True:
                right = test_item
            else:
                left = test_item
        if isBadVersion(left):
            return left
        elif isBadVersion(right):
            return right

if __name__ == '__main__':
    print Solution().firstBadVersion(2)

