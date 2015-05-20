"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def convert(self, s):
        record = {}
        for index in range(len(s)):
            if record.get(s[index]) is None:
                record[s[index]] = [index]
            else:
                record[s[index]].append(index)
        return record.values()

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        elif sorted(Solution().convert(s)) == sorted(Solution().convert(t)):
            return True
        else:
            return False


if __name__ == '__main__':
    a, b = 'add', 'egg'
    print(Solution().isIsomorphic(a,b))