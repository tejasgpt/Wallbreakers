class Solution(object):
    def firstUniqChar(self, s):
        """
        PROBLEM STATEMENT:
        Given a string, find the first non-repeating character in it and return it's index. 
        If it doesn't exist, return -1.
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        for i in s:
            d[i] += 1
                
        for i in s:
            if d[i] == 1:
                return s.index(i)
        return -1
        
