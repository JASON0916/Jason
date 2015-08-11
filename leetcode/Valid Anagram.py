__author__ = 'phoenix'
"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        def serialize(s, dict1):
            for alphabets in s:
                if dict1.get(alphabets) is None:
                    dict1[alphabets] = 1
                else:
                    dict1[alphabets] += 1
            return dict1
        if serialize(s, {}) != serialize(t, {}):
            return False
        else:
            return True


if __name__ == '__main__':
    print Solution().isAnagram('a', 'b')