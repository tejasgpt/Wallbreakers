class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        PROBLEM STATEMENT:
        Given an array of integers nums and a positive integer k, 
        find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1: 
            return True

        if k > len(nums): 
            return False

        total = sum(nums)
        if total % k: 
            return False

        target = total/k
        visit = [0] * len(nums)

        nums.sort(reverse=True)
        
        def partition(k, ind=0, tot=0, cnt=0):
            if k == 1: 
                return True
            if tot == target and cnt > 0:
                return partition(k-1)
            for i in range(ind,len(nums)):
                if not visit[i] and (tot + nums[i]) <= target:
                    visit[i] = 1
                    if partition(k, i+1, tot+nums[i], cnt+1): 
                        return True
                    visit[i] = 0
            return False

        return partition(k)
