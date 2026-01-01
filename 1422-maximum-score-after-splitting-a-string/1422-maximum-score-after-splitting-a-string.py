class Solution:
    def maxScore(self, s: str) -> int:
        count1 = s.count("1")
        zeros = 0
        ans = 0
        
        # return max1  
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros = zeros + 1
            
            else:    
                count1 = count1 - 1
            ans = max(ans, zeros + count1)    
        return ans    
