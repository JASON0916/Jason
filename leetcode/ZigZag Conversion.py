"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

__author__ = 'phoenix'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        i = 0
        word = ''
        result = ['' for i in range(0, nRows)]
        gap = nRows - 2
        while i < len(s):
            j = 0
            while i < len(s) and j < nRows:
                result[j] += s[i]
                i += 1
                j += 1
            j = gap
            while i < len(s) and j > 0:
                result[j] += s[i]
                i += 1
                j -= 1
        for words in result:
            word += words
        return word

if __name__ == "__main__":
    o = Solution()
    print(o.convert("A", 2))