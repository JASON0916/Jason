"""
Write a function that takes an unsigned integer and returns the number of ’1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
"""
__author__ = 'phoenix'


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        while n >= 2:
            if n % 2 == 1:
                num += 1
            n = int(n/2)
        num += n
        return num


if __name__ == '__main__':
    o = Solution()
    print(o.hammingWeight(8))