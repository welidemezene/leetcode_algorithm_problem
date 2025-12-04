class Solution:
    def maxArea(self, height: List[int]) -> int:
        min1 = float("inf")
        max1 = 0
        le = len(height)
        l,r = 0,le-1
        while l < r:
            min1 = min(height[l],height[r])
            valu = r - l
            max1 = max(max1, min1*valu)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1 
        return max1            


        