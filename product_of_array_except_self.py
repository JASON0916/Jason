class Solution:

    # @param {integer[]} nums

    # @return {integer[]}

    def productExceptSelf(self, nums):
        if len(nums) <= 1:
        	return []
        res = []
        num_zero, product = 0, 1
        for num in nums:
        	if num == 0:
        		num_zero += 1
        	else:
        		product *= num
        if num_zero >= 2:
        	return [0]*len(nums)
        elif num_zero == 1:
        	index = nums.index(0)
        	return [0]*(index)+[product]+[0]*(len(nums)-index-1)
        else:
        	return [int(product/num) for num in nums]
