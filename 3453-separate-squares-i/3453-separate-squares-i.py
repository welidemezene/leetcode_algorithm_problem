class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(s[2] * s[2] for s in squares)
        
        # Binary search range: from lowest y to highest y + side
        low = min(s[1] for s in squares)
        high = max(s[1] + s[2] for s in squares)
        
        # 100 iterations provide precision far beyond the 10^-5 required
        for _ in range(100):
            mid = (low + high) / 2
            area_below = 0
            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area_below += l * l
                else:
                    area_below += (mid - y) * l
            
            if area_below < total_area / 2:
                low = mid
            else:
                high = mid
                
        return low