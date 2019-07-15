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
        def isFirstMatch(s,p):
            return s[0] == p[0] or p[0] == '.'
        
        if not p:
            return len(s) == 0
        elif len(p) == 1:
            if len(s) == 1 and isFirstMatch(s,p):
                return True
            else:
                return False
        else:
            if p[1] == '*':
                while len(s) > 0 and isFirstMatch(s,p):
                    if self.isMatch(s,p[2:]):
                        return True
                    s = s[1:]
                return self.isMatch(s,p[2:])
            else:
                if len(s) > 0 and isFirstMatch(s,p):
                    return self.isMatch(s[1:],p[1:])
                else:
                    return False
