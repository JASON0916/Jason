__author__ = 'phoenix'
from time import clock
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count



if __name__ == '__main__':
    start = clock()
    print(Solution().rangeBitwiseAnd(5, 7))
    end = clock()
    print("time: %f" % (end-start))