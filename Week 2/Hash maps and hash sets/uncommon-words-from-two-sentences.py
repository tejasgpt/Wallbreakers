class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        PROBLEM STATEMENT:
        We are given two sentences A and B.  
        (A sentence is a string of space separated words.Each word consists only of lowercase letters.)
        A word is uncommon if it appears exactly once in one of the sentences, 
        and does not appear in the other sentence.Return a list of all uncommon words. 
        You may return the list in any order.
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import defaultdict
        uncommon = defaultdict(int)
        for word in A.split():
            uncommon[word] += 1
        for word in B.split():
            uncommon[word] += 1
        return [word for word in uncommon if uncommon[word] == 1]
