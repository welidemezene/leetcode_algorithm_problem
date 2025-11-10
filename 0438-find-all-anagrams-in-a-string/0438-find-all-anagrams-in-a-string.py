class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        le = len(s)
        le1= len(p)
        if le1 > le:
            return []
        res = []
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for i in range(le1):
            freq1[s[i]]+=1
            freq2[p[i]]+=1
        
        if freq1 == freq2:
            res.append(0)
        l = 0    
        for j in range(le1, le):
            freq1[s[j]]+=1
            freq1[s[l]]-=1
            if freq1[s[l]] == 0:
                del freq1[s[l]]
            l+=1
            
            if freq2 == freq1:
                res.append(l)   
        return res        

    