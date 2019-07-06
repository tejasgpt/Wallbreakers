class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        PROBLEM STATEMENT:
        Return the number of groups of special-equivalent strings from A.
        :type A: List[str]
        :rtype: int
        """
        group = set()
        for word in A:
            odds = word[::2]
            evens = word[1::2]
            group.add((str(sorted(odds)),str(sorted(evens))))
        return len(group)
        
 # Alternate Solution 
 
 class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        PROBLEM STATEMENT:
        Return the number of groups of special-equivalent strings from A.
        :type A: List[str]
        :rtype: int
        """
        group = set()
        for word in A:
            even = []
            S = ["0" for _ in range(26)]
            
            for i in range(0,len(word),2):
                S[ord(word[i])-ord('a')] = 1
                
            odd = []
            T = ["0" for _ in range(26)]
            
            for j in range(1,len(word),2):
                T[ord(word[j])-ord('a')] = 1
                
            if tuple([str(S),str(T)]) not in group:
                group.add(tuple([str(S),str(T)]))
                
        return len(group)
