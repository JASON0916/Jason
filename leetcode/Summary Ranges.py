__author__ = 'phoenix'
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start, end = 0, 0
        res = []
        while end < len(nums):
            if end+1 < len(nums) and nums[end+1] == nums[end]+1:
                end += 1
            else:
                if start == end:
                    res.append(str(nums[end]))
                else:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                start = end = end+1
        return res


if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7,8]))