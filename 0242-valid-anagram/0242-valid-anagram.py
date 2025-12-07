class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        le = len(s)
        le1 = len(t)
        freq = defaultdict(int)
        if le != le1:
            return False
        for m in s:
            freq[m]+=1
        for l in t:
            if l in freq.keys():
                freq[l]-=1
                if freq[l] == 0:
                    del freq[l]     
            else:
                return False
        return True                

        