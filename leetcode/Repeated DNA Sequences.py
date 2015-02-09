"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

__author__ = 'phoenix'

"""

idiot solution1: time limit exceeded

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        res = []
        for i in range(len(s) - 10):
            if s[i: i+10] in s[i+10:]:
                res.append(s[i: i+10])
        return res
"""


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict1 = {}
        res = []
        for i in range(len(s) - 9):
            string = hash(s[i: i+10])
            temp = dict1.get(string)
            if temp is None:
                dict1[string] = 1
            else:
                dict1[string] += 1
                if dict1[string] == 2:
                    res += [s[i: i+10]]
        return res

if __name__ == '__main__':
    o = Solution()
    print(o.findRepeatedDnaSequences("AAAAAAAAAAAA"))