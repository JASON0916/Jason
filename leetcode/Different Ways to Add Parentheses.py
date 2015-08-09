__author__ = 'phoenix'
"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


class Solution:
    # @param {string} input
    # @return {integer[]}

    def diffWaysToCompute(self, input):
        res = []
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in range(len(left)):
                    for k in range(len(right)):
                        if input[i] == '+':
                            res.append(left[j]+right[k])
                        elif input[i] == '-':
                            res.append(left[j]-right[k])
                        elif input[i] == '*':
                            res.append(left[j]*right[k])
        if len(res) == 0:
            res.append(int(input))
        return res


if __name__ == '__main__':
    ls = "0+1"
    print Solution().diffWaysToCompute(ls)