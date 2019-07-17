class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        PROBLEM STATEMENT:
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        elif len(strs) == 1: 
            return strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            pre = min(len(prefix), len(strs[i]))
            while strs[i][:pre] != prefix[:pre]: 
                pre -= 1
            prefix = prefix[:pre]
        return prefix

# ALTERNATE SOLUTION

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        PROBLEM STATEMENT:
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0 : 
            return prefix

        for i in range(len(min(strs))):
            pre = strs[0][i]
            if all(st[i] == pre for st in strs):
                prefix += pre
            else:
                break
        return prefix
