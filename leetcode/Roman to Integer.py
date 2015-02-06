"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

algorithm: scan in reversed order

about the Roman numerals: just baidu it!
"""
__author__ = 'phoenix'

class Solution:
    # @return an integer1100
    def romanToInt(self, s):
        roman2decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new_s = []
        num_now = 0
        result = 0
        for chars in s:
            new_s.append(roman2decimal.get(chars))
        for index in range(len(new_s)-1, -1, -1):
            if new_s[index] >= num_now:
                num_now = new_s[index]
                result += num_now
            else:
                num_now = new_s[index]
                result -= num_now
        return result


if __name__ == '__main__':
    o = Solution()
    print(o.romanToInt('MMMCMXCIX'))