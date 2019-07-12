class Solution(object):
    def arrayPairSum(self, nums):
        """
        PROBLEM STATEMENT:
        Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
        say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
        for all i from 1 to n as large as possible.
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(0,len(nums),2):
            total += nums[i]
        return total

# ALTERNATE SOLUTION

class Solution(object):
    def arrayPairSum(self, nums):
        """
        PROBLEM STATEMENT:
        Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
        say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
        for all i from 1 to n as large as possible.
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
