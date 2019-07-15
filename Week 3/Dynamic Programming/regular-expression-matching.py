class Solution(object):
    def isMatch(self, s, p):
        """
        PROBLEM STATEMENT:
        Given an input string (s) and a pattern (p),
        implement regular expression matching with support for '.' and '*'.
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        Note:
        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
        :type s: str
        :type p: str
        :rtype: bool
        """
        re = [[False]*(len(p)+1) for i in range(len(s)+1)]
        re[0][0] = True
        
        for i in range(len(s)+1): 
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    re[i][j] = i > 0 and re[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1]=='.')
                else:  
                    re[i][j] = re[i][j-2] or (i>0 and re[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                    
        return re[len(s)][len(p)]
