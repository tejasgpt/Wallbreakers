class Solution(object):
    def subsets(self, nums):
        """
        PROBLEM STATEMENT:
        Given a set of distinct integers, nums, return all possible subsets (the power set).
        Note: The solution set must not contain duplicate subsets.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = [[]]
        for num in nums:
            for i in range(len(subs)):
                subs.append(subs[i]+[num])
        return subs
            
