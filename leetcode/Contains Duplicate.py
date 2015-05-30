"""
Given an array of integers, find if the array contains any duplicates. Your function should return true

if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        cdict = {}
        for num in nums:
            if cdict.get(num) is None:
                cdict[num] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([2, 1]))