"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        pre, cur = 0, 1
        while abs(pre-cur) > 0.0001:
            pre = cur
            cur = pre/2 + x/(2*pre)
        return int(cur)


if __name__ == '__main__':
    print(Solution().mySqrt(1))