"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
__author__ = 'phoenix'


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def recursion(self, candidates, target, res, res_list):
        if target == 0:
            if res not in res_list:
                res_list.append(res[:])
            return
        elif target < 0:
            return
        else:
            for i in range(len(candidates)):
                if candidates[i] > target:
                    return
                else:
                    res.append(candidates[i])
                    self.recursion(candidates[i+1:], target-candidates[i], res, res_list)
                    res.pop()

    def combinationSum2(self, candidates, target):
        res_list = []
        self.recursion(sorted(candidates), target, [], res_list)
        return res_list


if __name__ == '__main__':
    o = Solution()
    print(o.combinationSum2(	[13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25))