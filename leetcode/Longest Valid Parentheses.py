"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
__author__ = 'phoenix'

"""
my solution failed at 160/229
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0
        stack = []
        num = 0
        num_list = []
        for i in range(len(s)):
            if s[i] == '(':
                if len(stack) > 0:
                    num_list.append(num)
                stack.append(s[i])
            elif len(stack) > 0 and s[i] == ')':
                num += 2
                stack.pop()
            else:
                num_list.append(num)
                num = 0
        if len(num_list) == 0:
            return num
        else:
            if len(stack) != 0:
                num_list.append(num - num_list[1-len(stack)])
            else:
                num_list.append(num)
            return max(num_list)
"""


class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        #解题思路：返回括号串中合法括号串的长度。使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，而是未匹配左括号的索引！
        max_Len = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        max_Len = max(max_Len, i - last)
                    else:
                        max_Len = max(max_Len, i - stack[-1])
        return max_Len

if __name__ == '__main__':
    o = Solution()
    parenteses = '(((()(()'
    print(o.longestValidParentheses(parenteses))