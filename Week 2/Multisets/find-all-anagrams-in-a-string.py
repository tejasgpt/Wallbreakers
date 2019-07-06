class Solution(object):
    def findAnagrams(self, s, p):
        """
        PROBLEM STATEMENT:
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
        Strings consists of lowercase English letters only 
        and the length of both strings s and p will not be larger than 20,100.
        The order of output does not matter.
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if not s or len(s) < len(p):
            return res
        
        ds = [0]*256
        dp = [0]*256

        for i in range(len(p)):
            ds[ord(p[i])] += 1
            dp[ord(s[i])] += 1
            
        for i in range(len(s)-len(p)):
            if ds == dp:
                res.append(i)
            dp[ord(s[i])] -= 1
            dp[ord(s[i+len(p)])] += 1
            
        if ds == dp:
            res.append(len(s)-len(p))
            
        return res
