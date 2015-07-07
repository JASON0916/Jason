__author__ = 'phoenix'
"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        bitmask = 0x01
        if n <= 0:
            return False
        while n&bitmask != 1:
            n >>= 1
        if n > 1:
            return False
        elif n == 1:
            return True
