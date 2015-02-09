"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.
"""

__author__ = 'phoenix'

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        length = len(num)
        if length < 2:
            return 0
        a = min(num)
        b = max(num)
        bucket_len = int(0.5 + 1.0 * (b - a) / (length - 1))
        buckets = {}
        for i in num:
            loc = int((i - a) / bucket_len)
            bucket = buckets.get(loc)
            if bucket is None:
                bucket = {'min': i, 'max': i}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], i)
                bucket['max'] = max(bucket['max'], i)
        max_gap = 0
        for x in range(bucket_len):
            if buckets.get(x) is None:
                continue
            y = x + 1
            while y < bucket_len and buckets.get(y) is None:
                y += 1
            if y < bucket_len:
                max_gap = max(max_gap, buckets[y]['min'] - buckets[x]['max'])
        return max_gap

if __name__ == '__main__':
    o = Solution()
    num1 = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
    # answer is 2901
    print(o.maximumGap(num1))