class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l = 0
        max1 = 0
        for i,c in enumerate(s):
            freq[c] +=1
            while freq[c] > 1:
                freq[s[l]]-=1
                l+=1
            max1 = max(max1, i-l+1)   
        return max1     

        