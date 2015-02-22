"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
__author__ = 'phoenix'


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def recursion(self, num, res, res_list):
        if len(num) == 0:
            res_list.append(res[:])
            return
        else:
            for i in range(len(num)):
                res.append(num[i])
                temp_list = num[0:i] + num[i+1:]
                self.recursion(temp_list, res, res_list)
                res.pop()

    def permute(self, num):
        res_list = []
        self.recursion(num, [], res_list)
        return res_list

if __name__ == '__main__':
    o = Solution()
    print(o.permute([1,2,3,4]))