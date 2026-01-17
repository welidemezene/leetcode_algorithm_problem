class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # O(N^2) - Compare every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate Intersection Boundaries
                inter_blx = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bly = max(bottomLeft[i][1], bottomLeft[j][1])
                inter_trx = min(topRight[i][0], topRight[j][0])
                inter_try = min(topRight[i][1], topRight[j][1])
                
                # Calculate Width and Height of the intersection
                width = inter_trx - inter_blx
                height = inter_try - inter_bly
                
                if width > 0 and height > 0:
                    side = min(width, height)
                    if side > max_side:
                        max_side = side
                        
        return max_side * max_side