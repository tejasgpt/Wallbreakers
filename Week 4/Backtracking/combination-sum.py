class Solution(object):
    def combinationSum(self, candidates, target):
        """
        PROBLEM STATEMENT:
        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
        find all unique combinations in candidates where the candidate numbers sums to target.
        The same repeated number may be chosen from candidates unlimited number of times.
        Note:
            All numbers (including target) will be positive integers.
            The solution set must not contain duplicate combinations.
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates, nums, remains):
            if remains == 0:
                combSum.append(nums)
                return
            for i in range(len(candidates)):
                if remains >= candidates[i]:
                    backtrack(candidates[i:], nums+[candidates[i]], remains-candidates[i])  
                else:
                    break
        candidates.sort()
        combSum = []
        backtrack(candidates, [], target)
        return combSum
