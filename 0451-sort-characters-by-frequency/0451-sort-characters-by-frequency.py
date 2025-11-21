class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]]+=1
        sorted_item = sorted(freq.items(), key=lambda x : x[1] ,reverse=True)    
        st = ""
        for key,value in sorted_item:
            st += (key*value)
        return st    
