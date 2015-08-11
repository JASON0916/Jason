__author__ = 'phoenix'
"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        res, m = 0, 1
        while m <= n:
            a, b = int(n/m), n%m
            res += int((a+8)/10)*m + (a%10 == 1)*(b+1)
            m *= 10
        return res


if __name__ == '__main__':
    print Solution().countDigitOne(1)