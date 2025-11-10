class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        le = len(s)
        l = 0
        max1 = 0
        res = 0
       
        
        freq1 = defaultdict(int)
        for i in range(le):
            freq1[s[i]]+=1
            max1 = max(freq1.values())

            curlen = i -l+1
            if curlen - max1 > k:
                freq1[s[l]]-=1
                l+=1
            res = max(res, i-l+1)
        return res       

        