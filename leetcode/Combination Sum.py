"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
__author__ = 'phoenix'

"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def recursion(self, candidates, res, target, sol):
        if target < 0:
            sol.clear()
            return
        if target in candidates:
            sol.append(target)
            res.append(sol[:])
            index = candidates.index(target)
            candidates.pop(index)
            self.recursion(candidates, res, target, [])
        else:
            for num in candidates:
                if num < target:
                    sol.append(num)
                    self.recursion(candidates, res, target - num, sol)
                else:
                    break

    def combinationSum(self, candidates, target):
        res = []
        self.recursion(candidates, res, target, [])
        return res


if __name__ == '__main__':
    o = Solution()
    print(o.combinationSum([1,2], 3))
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def combinationSum2(candidates, target, index, res, res_list):
            if target == 0:
                res_list.append(list(res))
                return
            while index < len(candidates) and target >= candidates[index]:
                res.append(candidates[index])
                combinationSum2(candidates, target-candidates[index], index, res, res_list)
                res.pop()
                index += 1

        res_list = []
        candidates.sort()
        combinationSum2(candidates, target, 0, [], res_list)
        return res_list


def main():
    sol = Solution()
    candidates = [1, 2]
    target = 3
    print(sol.combinationSum(candidates, target))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))