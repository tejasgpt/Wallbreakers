class Solution(object):
    def canPartition(self, nums):
        """
        PROBLEM STATEMENT:
        Given a non-empty array containing only positive integers, find if the array can be partitioned into
        two subsets such that the sum of elements in both subsets is equal.
        Note:
            Each of the array element will not exceed 100.
            The array size will not exceed 200.
        :type nums: List[int]
        :rtype: bool
        """
        target = {}

        def canFindSum(nums, tar, curr):
            if tar in target:
                return target[tar]

            if not tar:
                target[tar] = True
            
            elif tar > 0:
                target[tar] = False
                
                for idx in range(curr, len(nums)):
                    if canFindSum(nums, tar - nums[idx], idx + 1):
                        target[tar] = True
                        break
    
                return target[tar]
        
        total = sum(nums)
        
        if total % 2:
            return False

        return canFindSum(nums, total/2, 0)
