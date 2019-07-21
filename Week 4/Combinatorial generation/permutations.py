class Solution(object):
    def permute(self, nums):
        """
        PROBLEM STATEMENT:
        Given a collection of distinct integers, return all possible permutations.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
    		return [nums]
        
    	perms = []
    	for i in range(len(nums)):
    		for perm in self.permute(nums[:i] + nums[i+1:]):
    			perms.append([nums[i]] + perm)
    	return perms
