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
        def rec(x, y):
            if not distance[x][y]:
                if x == 0:
                    distance[x][y] = y
                elif y == 0:
                    distance[x][y] = x
                elif word1[x-1] == word2[y-1]:
                    distance[x][y] = rec(x-1, y-1)
                else:
                    distance[x][y] = min(rec(x-1, y), rec(x, y-1), rec(x-1, y-1)) + 1
            return distance[x][y]

        distance = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        return rec(len(word1), len(word2))
