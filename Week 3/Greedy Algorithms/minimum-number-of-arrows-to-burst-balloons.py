class Solution(object):
    def findMinArrowShots(self, points):
        """
        PROBLEM STATEMENT:
        Find the minimum number of arrows that must be shot to burst all balloons.
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0 
        
        points.sort(key=lambda x:x[1])
        last = -float('inf')
        arrow = 0
        
        for point in points:
            if point[0] > last:
                arrow += 1
                last = point[1]
                
        return arrow
