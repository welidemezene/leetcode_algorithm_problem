from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        
        le1, le2 = len(s1), len(s2)
        if le1 > le2:
            return False
        
        # Build initial window
        for i in range(le1):
            freq1[s1[i]] += 1
            freq2[s2[i]] += 1
        
        if freq1 == freq2:
            return True
        
        left = 0
        for right in range(le1, le2):
            freq2[s2[right]] += 1
            freq2[s2[left]] -= 1
            
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            
            left += 1
            
            if freq1 == freq2:
                return True
        
        return False
