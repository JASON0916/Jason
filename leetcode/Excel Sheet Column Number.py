"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        length = len(s)
        result = 0
        if length == 0:
            return 0
        for chars in s:
            dig = ord(chars) - 65
            result = result * 26 + dig
        return result