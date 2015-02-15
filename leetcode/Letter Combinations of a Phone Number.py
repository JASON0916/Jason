"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

__author__ = 'phoenix'


class Solution:
    # @return a list of strings, [s1, s2]
    def combination(self, list1, list2):
        if list1 == []:
            return list2
        else:
            return [x+y for x in list1 for y in list2]

    def letterCombinations(self, digits):
        if digits == "":
            return [""]
        digit2str = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        o = Solution()
        res = []
        for i in range(len(digits)):
                res = o.combination(res, digit2str.get(digits[i]))
        return res


if __name__ == '__main__':
    stri = "23"
    a = Solution()
    print(a.letterCombinations(stri))