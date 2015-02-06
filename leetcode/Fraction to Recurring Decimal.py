"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.
"""

__author__ = 'phoenix'

"""
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        result = str(numerator / denominator)
        if len(result) < 18:
            return result
        else:
            for i in range(len(result) - 1, 1, -1):
                if result[i] == result[i - 1]:
                    result = result[:i]
                else:
                    result = result[:i] + '(' + result[i] + ')'
        return result
"""

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):.
        neg = numerator != 0 and numerator >> 31 != denominator >> 31 #otherwise 0, -5 = -0
        numerator = abs(numerator)
        denominator = abs(denominator)
        result = ""
        remainder = numerator%denominator
        quotient = numerator//denominator
        result += str(quotient)+"."
        #start dealing with decimalpart
        remainders = {}
        decimalpart = ""
        curposition = 0
        while remainder not in remainders and remainder != 0:
            remainders[remainder] = curposition
            curposition += 1
            numerator = remainder*10
            remainder = numerator%denominator
            quotient = numerator//denominator
            decimalpart += str(quotient)

        if remainder == 0:
            result += decimalpart
            if result[-1] == ".":   #"0."case
                result = result[:-1]
        else:
            start = remainders[remainder]
            result = result + decimalpart[:start] + "(" + decimalpart[start:] +")"
        return "-"+result if neg else result


if __name__ == '__main__':
    a = 1
    b = 5
    o = Solution()
    print(o.fractionToDecimal(a, b))