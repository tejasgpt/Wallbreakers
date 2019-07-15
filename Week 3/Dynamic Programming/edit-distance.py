class Solution(object):
    def minDistance(self, word1, word2):
        """
        PROBLEM STATEMENT:
        Given two words word1 and word2, 
        find the minimum number of operations required to convert word1 to word2.
        You have the following 3 operations permitted on a word:
        1. Insert a character
        2. Delete a character
        3. Replace a character
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        found = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        for k in range(len(word1) + 1):
            found[k][0] = k
        for l in range(len(word2) + 1):
            found[0][l] = l
            
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    found[i][j] = found[i-1][j-1]
                else:
                    found[i][j] = min(found[i-1][j], found[i-1][j-1], found[i][j-1]) + 1
                    
        return found[len(word1)][len(word2)]
