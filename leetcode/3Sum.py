"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

__author__ = 'phoenix'

"""

This is a horrible algorithm, although it is admitted by the oj.

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        numbers = sorted(num)
        result = []
        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                temp = - numbers[i] - numbers[j]
                if temp in numbers[j+1: len(numbers)]:
                    a = [numbers[i], numbers[j], temp]
                    if a not in result:
                        result.append(a)
        return result
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    # @algorithm http://en.wikipedia.org/wiki/3SUM
    # exclude the duplicated answer in the process of start & end
    def threeSum(self, num):
        numbers = sorted(num)
        length = len(numbers)
        result = []
        for i in range(length-2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            a = numbers[i]
            start, end = i + 1, length - 1
            while start < end:
                b = numbers[start]
                c = numbers[end]
                if a + b + c == 0:
                    temp = [a, b, c]
                    start += 1
                    while start < end and numbers[start] == numbers[start - 1]:
                        start += 1
                    result.append(temp)
                elif a + b + c < 0:
                    start += 1
                else:
                    end -= 1
        return result