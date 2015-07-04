__author__ = 'phoenix'
"""
an array with N intergers given, how to delete the duplicates in it?
time: O(n)
space: O(1)
"""


class Solution:
    # @param nums: a list of ints
    # @return a list of ints without duplicates
    def delete_duplicate(self, nums):
        length = int(max(nums)/32)+1
        num_list = [0]*length
        i = 0
        bitmask = 0x1F
        while i < len(nums):
            indicy1, indicy2 = int(nums[i]/32), nums[i]%32
            if (num_list[indicy1] >> indicy2) & bitmask == 1:
                nums.pop(i)
            elif (num_list[indicy1] >> indicy2) & bitmask == 0:
                num_list[indicy1] |= 0x01 << indicy2
                i += 1
        return nums


if __name__ == '__main__':
    print(Solution().delete_duplicate([1,11,1,1,5]))