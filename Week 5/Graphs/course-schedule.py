class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        PROBLEM STATEMENT:
        There are a total of n courses you have to take, labeled from 0 to n-1.
        Given the total number of courses and a list of prerequisite pairs, 
        is it possible for you to finish all courses?
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        def visited(course):
            if visit[course] == -1:
                return False
            if visit[course] == 1:
                return True
            visit[course] = -1
            for preq in graph[course]:
                if not visited(preq):
                    return False
            visit[course] = 1
            return True
        
        for course in range(numCourses):
            if not visited(course):
                return False
        return True
