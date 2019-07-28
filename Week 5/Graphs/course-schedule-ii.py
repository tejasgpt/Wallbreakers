class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        PROBLEM STATEMENT:
        There are a total of n courses you have to take, labeled from 0 to n-1.
        Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
        which is expressed as a pair: [0,1]
        Given the total number of courses and a list of prerequisite pairs, 
        return the ordering of courses you should take to finish all courses.
        There may be multiple correct orders, you just need to return one of them. 
        If it is impossible to finish all courses, return an empty array.
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        queue = collections.deque([])
        dic = collections.defaultdict(set)
        course = [0] * numCourses
        
        for pre,nxt in prerequisites:
            dic[nxt].add(pre)
            course[pre] += 1
            
        schedule = []
        for i in range(numCourses):
            if course[i] == 0:
                queue.append(i)
                schedule.append(i)
        
        while queue:
            node = queue.popleft()
            for i in dic[node]:
                course[i] -= 1
                if course[i] == 0:
                    schedule.append(i)
                    queue.append(i)
                    
        return schedule if len(schedule)==numCourses else []
