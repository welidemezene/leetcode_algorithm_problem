class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        max1 = 0
        left = 0
        for n in s:
            freq[n]+=1
           
            while freq[n] > 1:
                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
            max1 = max(max1,len(freq))    
        return max1         
        