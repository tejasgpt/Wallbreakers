class Solution(object):
    def partitionLabels(self, S):
        """
        PROBLEM STATEMENT:
        A string S of lowercase letters is given. 
        We want to partition this string into as many parts as possible so that 
        each letter appears in at most one part, 
        and return a list of integers representing the size of these parts.
        :type S: str
        :rtype: List[int]
        """
        letters = dict()
        for ind in range(len(S)):
            letters[S[ind]] = ind
        
        labels = []
        left, right = 0, 0
        for ind in range(len(S)):
            right = max(right, letters[S[ind]])
            if ind == right:
                labels.append(ind - left + 1)
                left = ind + 1
        return labels
