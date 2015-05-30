__author__ = 'phoenix'
"""
Given an array of integers and an integer k, find out whether there there are two distinct indices

i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        cdict = {}
        for i in range(len(nums)):
            if cdict.get(nums[i]) is None:
                cdict[nums[i]] = i
            elif i - cdict[nums[i]] <= k:
                return True
            else:
                cdict[nums[i]] = i
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))