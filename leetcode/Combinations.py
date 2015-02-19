"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
__author__ = 'phoenix'


class Solution:
    # @return a list of lists of integers
    def recursion(self, n, k, res, res_list, list_num):
        if k == 0:
            res_list.append(res[:])
            return
        else:
            for i in range(len(list_num)):
                res.append(list_num[i])
                self.recursion(n, k-1, res, res_list, list_num[i+1:])
                res.pop()

    def combine(self, n, k):
        res_list = []
        list_num = [x for x in range(1, n+1)]
        self.recursion(n, k, [], res_list, list_num)
        return res_list

def main():
    o = Solution()
    print(o.combine(4, 3))

if __name__ == '__main__':
    main()