"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
__author__ = 'phoenix'

"""
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483847
        sign_dividend = True if dividend >= 0 else False
        sign_divisor = True if divisor >= 0 else False
        res = 0
        dividend_n, divisor_n = abs(dividend), abs(divisor)
        while dividend_n >= divisor_n:
            dividend_n -= divisor_n
            res += 1
        if sign_dividend == sign_divisor:
            return res
        else:
            return -res
"""
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483847
        sign_dividend = True if dividend >= 0 else False
        sign_divisor = True if divisor >= 0 else False
        res, cur = 0, 0
        dividend_n, divisor_n = abs(dividend), abs(divisor)
        while dividend_n >> 1 >= divisor_n:
            cur += 1
            divisor_n <<= 1
        while cur >= 0:
            if dividend_n >= divisor_n:
                res += 1 << cur
                dividend_n -= divisor_n
            divisor_n >>= 1
            cur -= 1
        if res > 2147483847:
            return 2147483847
        if sign_dividend == sign_divisor:
            return res
        else:
            return -res

if __name__ == '__main__':
    print(Solution().divide(-2147483648, -1))
    # fuck the last test case!!!