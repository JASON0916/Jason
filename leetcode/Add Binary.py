"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100"
"""

__author__ = 'phoenix'


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(str(int(a, 2) + int(b, 2))))[2:]

"""
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length_a = len(a)
        length_b = len(b)
        if length_a > length_b:
            b = '0' * (length_a - length_b) + b
            length = length_a
        else:
            a = '0' * (length_b - length_a) + a
            length = length_b
        a = a[::-1]
        b = b[::-1]
        Sum = ''
        carry = 0
        for i in xrange(length):
            tmp = ord(a[i]) - 48 + ord(b[i]) - 48 + carry
            Sum += str(tmp % 2)
            carry = tmp / 2
        if carry == 1:
            Sum += '1'
        return Sum[::-1]
"""