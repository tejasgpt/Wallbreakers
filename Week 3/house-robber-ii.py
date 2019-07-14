class Solution(object):
    def rob(self, nums):
        """
        PROBLEM STATEMENT:
        Given a list of non-negative integers representing the amount of money of each house, 
        determine the maximum amount of money you can rob tonight without alerting the police.
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        if len(nums) < 4: 
            return max(nums)

        first, second = 0, 0
        for i in nums[:-1]: 
            first, second = second, max(first + i, second)

        one, two = 0, 0
        for i in nums[1:]: 
            one, two = two, max(one + i, two)
        return max(two, second)
