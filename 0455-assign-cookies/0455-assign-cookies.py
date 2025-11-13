class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        le = len(s)
        le1 = len(g)
        g.sort()
        s.sort()
        l,r=0,0
        while r< le and l<le1:
            if s[r] >= g[l]:
                l+=1
                
            r+=1
        return l       

        