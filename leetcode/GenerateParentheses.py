"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

__author__ = 'phoenix'


class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        def generate(res, string, left, right, n):
            if left == n and right == n:
                res.append(string)
            if left < n:
                generate(res, string + '(', left + 1, right, n)
            if right < left:
                generate(res, string + ')', left, right + 1, n)

        result = []
        parenthesis = ''
        generate(result, parenthesis, 0, 0, n)
        return result


if __name__ == '__main__':
    o = Solution()
    print(o.generateParenthesis(2))
