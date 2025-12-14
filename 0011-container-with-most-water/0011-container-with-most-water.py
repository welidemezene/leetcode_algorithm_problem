class Solution:
    def maxArea(self, height: List[int]) -> int:
        len1 = len(height)
        l,r = 0 , len1 -1
        max1 = 0
        min1 = 100000
        while l < r:
            min1 = min(height[l],height[r])
            max1 = max(max1, min1 * (r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return max1            

        