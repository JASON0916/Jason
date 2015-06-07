"""
Implement pow(x, n).
"""
__author__ = 'phoenix'


class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if 0 < n <= 1:
            return x
        else:
            return x**n


if __name__ == '__main__':
    print(Solution().myPow(-0.44895, 0))