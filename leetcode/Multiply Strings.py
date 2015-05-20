__author__ = 'phoenix'
"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        str_len1, str_len2 = len(num1), len(num2)
        res = "0" * (str_len1 + str_len2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(str_len2):
            multiflag = addflag = 0
            for j in range(str_len1):
                temp1 = int(num1[j]) * int(num2[i]) + multiflag
                multiflag = int(temp1/10)
                temp1 %= 10
                temp2 = int(res[i+j]) + addflag + temp1
                addflag = int(temp2/10)
                res = res[:i+j] + str(temp2 % 10) + res[i+j+1:]
            temp = str(int(res[i+str_len1]) + multiflag + addflag)
            res = res[:i+str_len1] + temp + res[i+str_len1+1:]

        return str(int(res[::-1]))


if __name__ == '__main__':
    print(Solution().multiply("9133", "0"))