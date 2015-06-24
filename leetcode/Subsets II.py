class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = []
        def recursion(nums, res, temp):
            if len(temp) >= 0:
                res.append(temp[:])
            if len(nums) == 0:
                return
            else:
                i = 0
                while i < len(nums):
                    temp.append(nums[i])
                    recursion(nums[i+1:], res, temp)
                    temp.pop()
                    while i < len(nums)-1 and nums[i] == nums[i+1]:
                        i += 1
                    i += 1

        recursion(sorted(nums), res, [])
        return res


if __name__ == '__main__':
    print(Solution().subsetsWithDup([5,5,5,5,5]))