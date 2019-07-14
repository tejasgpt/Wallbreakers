class Solution(object):
    def findContentChildren(self, g, s):
        """
        PROBLEM STATEMENT:
        Assume you are an awesome parent and want to give your children some cookies. 
        But, you should give each child at most one cookie. 
        Each child i has a greed factor gi, which is the minimum size of a cookie 
        that the child will be content with; and each cookie j has a size sj. 
        If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. 
        Your goal is to maximize the number of your content children and output the maximum number.
        Note:
        You may assume the greed factor is always positive. 
        You cannot assign more than one cookie to one child.
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s or not g:
            return 0
        
        g.sort()
        s.sort()
        
        cookies = 0
        i = j = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                cookies += 1
                i += 1
            j += 1
                
        return cookies
