__author__ = 'phoenix'
from time import clock
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        def sum_digits(num):
            res = 0
            g = lambda x: x**2
            while num != 0:
                res += g(num % 10)
                num = int(num/10)
            return res

        ans_list = []
        sum_n = sum_digits(n)
        while sum_n not in ans_list:
            ans_list.append(sum_n)
            sum_n = sum_digits(sum_n)
            if sum_n == 1:
                return True
        return False


if __name__ == '__main__':
    start = clock()
    print(Solution().isHappy(18))
    end = clock()
    print("time: %f" % (end - start))