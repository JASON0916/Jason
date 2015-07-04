__author__ = 'phoenix'
"""
an array with N intergers given, how to delete the duplicates in it?
time: O(n)
space: O(1)
"""


class Solution:
    # @param nums: a list of ints
    # @return a list of ints withou\t duplicates
    def delete_duplicate(self, nums):
        length = int(max(nums)/32)+1
        num_list = [0]*length
        i = 0
        bitmask = 0x1F
        while i < len(nums):
            indicy1, indicy2 = int(nums[i]/32), nums[i] % 32
            bit = 1 << indicy2
            if bit & num_list[indicy1]:
                nums.pop(i)
            else:
                num_list[indicy1] |= 1 << indicy2
                i += 1
        return nums


if __name__ == '__main__':
    print(Solution().delete_duplicate([1,11,1,1,1,1,5,1,5,5,5,5,]))