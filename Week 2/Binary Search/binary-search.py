class Solution(object):
    def search(self, nums, target):
        """
        PROBLEM STATEMENT:
        Given a sorted (in ascending order) integer array nums of n elements and a target value, 
        write a function to search target in nums. 
        If target exists, then return its index, otherwise return -1.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
