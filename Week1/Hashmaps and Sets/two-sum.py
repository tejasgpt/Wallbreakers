class Solution(object):
    def twoSum(self, nums, target):
        """
        PROBLEM STATEMENT:
        Given an array of integers, return indices of the two numbers 
        such that they add up to a specific target.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_num = {}
        for num in nums:
            hash_num[num] = 1

        for i in range(len(nums) - 1):
            if (target - nums[i]) not in hash_num:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
