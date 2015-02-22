"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""
__author__ = 'phoenix'


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0:
            return -1
        sum_list = start = passed = 0
        for i in range(len(gas)):
            sum_list += gas[i] - cost[i]
            if passed < 0:
                start = i
                passed = gas[i] - cost[i]
            else:
                passed += gas[i] - cost[i]
        if sum_list < 0:
            return -1
        else:
            return start

if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([3,-7,2,-1,3], [0,0,0,0,0]))
