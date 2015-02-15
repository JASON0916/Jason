__author__ = 'phoenix'

"""
algorithm: http://bookshadow.com/weblog/2014/12/22/leetcode-majority-element/

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = candidate = 0
        for nums in num:
            if count == 0:
                candidate = nums
                count = 1
            else:
                if candidate == nums:
                    count += 1
                else:
                    count -= 1
        return candidate