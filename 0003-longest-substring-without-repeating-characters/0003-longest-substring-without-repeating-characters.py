class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq1 = defaultdict(int)
        l = 0
        le = len(s)
        max1 = 0
        for i in range(le):
            freq1[s[i]]+=1
            while freq1[s[i]] > 1:
                freq1[s[l]]-=1
                l+=1
            max1 = max(max1, i-l+1)
        return max1        

        