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
