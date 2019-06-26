class Solution(object):
    def singleNumber(self, nums):
        """
        PROBLEM STATEMENT:
        Given a non-empty array of integers, every element appears twice except for one. 
        Find that single one.
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
