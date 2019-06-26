class Solution(object):
    def findCircleNum(self, M):
        """
        PROBLEM STATEMENT:
        Given a N*N matrix M representing the friend relationship between students in the class. 
        If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
        And you have to output the total number of friend circles among all the students.
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        direct = UniFind(N)
        
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j]:
                    direct.union(i,j)
        
        return sum([direct.find(x) == x for x in range(N)])
    
class UniFind:
    def __init__(self, N):
        self.num = range(N)

    def find(self, x):
        if self.num[x] != x:
            self.num[x] = self.find(self.num[x])
        return self.num[x]

    def union(self, x, y):
        self.num[self.find(x)] = self.find(y)
