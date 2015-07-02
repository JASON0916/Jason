__author__ = 'phoenix'


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if len(nums) <= 1:
            return nums
        res = []
        num1, num2 = 0, 0
        candidate1, candidate2 = nums[0], nums[1]
        for i in range(len(nums)):
            if nums[i] == candidate1:
                num1 += 1
            elif nums[i] == candidate2:
                num2 += 1
            else:
                if num1 < num2:
                    if num1 == 0:
                        candidate1 = nums[i]
                        num1 = 1
                    else:
                        num2 -= 1
                        num1 -= 1
                else:
                    if num2 == 0:
                        candidate2 = nums[i]
                        num2 = 1
                    else:
                        num1 -= 1
                        num2 -= 1
        num1, num2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                num1 += 1
            elif nums[i] == candidate2:
                num2 += 1
        if num1 > len(nums)/3:
            res.append(candidate1)
        if num2 > len(nums)/3:
            res.append(candidate2)
        return res




if __name__ == '__main__':
    print(Solution().majorityElement([1,3,3,4]))