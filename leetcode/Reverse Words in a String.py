"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""

__author__ = 'phoenix'


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_list = s.split()
        res = ""
        for i in range(len(s_list) - 1, -1, -1):
            res += s_list[i] + " "
        return res[:len(res) - 1]


if __name__ == '__main__':
    string = "the sky is blue"
    o = Solution()
    print(o.reverseWords(string))