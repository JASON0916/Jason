"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'phoenix'


class Solution:
    # @return a string
    def intToRoman(self, num):
        unit_plc = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
        ten_plc = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
        hundred_plc = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
        thousand_plc = {'1': 'M', '2': 'MM', '3': 'MMM'}
        plcs = [unit_plc, ten_plc, hundred_plc, thousand_plc]
        list_num = list(str(num))
        length = len(list_num)
        plcs = plcs[0:length]
        result = ''
        for i in range(0, length):
            result += plcs[length - 1 - i].get(list_num[i])
        return result
if __name__ == '__main__':
    o = Solution()
    print(o.intToRoman(10))