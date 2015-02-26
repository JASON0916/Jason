"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
__author__ = 'phoenix'


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return A[0]
        else:
            curmax = curmin = ans = A[0]
            for i in range(1, len(A)):
                temp = curmin * A[i]
                curmin = min(A[i], min(curmax*A[i], temp))
                curmax = max(A[i], max(temp, curmax*A[i]))
                ans = max(curmax, ans)
            return ans

if __name__ == '__main__':
    o = Solution()
    print(o.maxProduct([6,3,6,-2,3,1,1,1,-1,4,2,4,-1,-4,0,-5,-2,6,4,-1,-3,0,5,5,1,0,0,1,5,-4,0,6,4,-4,-3,-6,-2,-2,-4,3,5,-5,-1,-3,-1,-1,-6,-5,-1,-1,-1,0,-6,2,1,-1,5,-6,-5,-3,6,4,3,-2,4,-2,-3,-1,0,-1,-1,-1,4,0,6,-1,4,4,-3,4,-3,-2,0,4,-3,-1,1,-2,0,-4,6,0,2,2,0,0,-2,1,4,-3]))