"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
__author__ = 'phoenix'


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def recursion(self, S, res, res_list):
        if len(res) >= 0:
            res_list.append(res[:])
        if len(S) == 0:
            return
        else:
            for i in range(len(S)):
                res.append(S[i])
                self.recursion(S[i+1:], res, res_list)
                res.pop()

    def subsets(self, S):
        res_list = []
        self.recursion(sorted(S), [], res_list)
        return res_list


if __name__ == '__main__':
    o = Solution()
    print(o.subsets([4,1,0]))