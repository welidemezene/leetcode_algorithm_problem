class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        sum_x = 0
        sum_y = 0
        total = 0
        le = len(points)
        for i in range(1,le):
            sum_x = abs(points[i][0]-points[i-1][0])
            sum_y = abs(points[i][1]-points[i-1][1]) 
            total+= max(sum_x,sum_y)
        return total    
        
        
        