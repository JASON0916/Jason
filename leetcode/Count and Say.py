"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

__author__ = 'phoenix'


class Solution:
    # @return a string
    def read(self, string):
        num_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        res = ''
        for i in range(len(string)):
            num_dict[string[i]] += 1
            if i+1 < len(string) and string[i] == string[i+1]:
                continue
            else:
                res += str(num_dict[string[i]]) + string[i]
                num_dict[string[i]] = 0
        return res

    def countAndSay(self, n):
        temp = '1'
        o = Solution()
        for i in range(n-1):
            temp = o.read(temp)
        return temp


if __name__ == '__main__':
    a = Solution()
    print(a.countAndSay(4))