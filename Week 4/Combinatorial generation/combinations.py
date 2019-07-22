class Solution(object):
    def combine(self, n, k):
        """
        PROBLEM STATEMENT:
        Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k > n:
            return []
        if n == 1:
            return [[n]]
        
        diff = (n - k) + 2
        combinations = [[i] for i in range(1, diff)]
        
        for num in range(1, k):
            combinations = [comb + [i] for comb in combinations for i in range(comb[-1] + 1, num + diff)]
            
        return combinations
