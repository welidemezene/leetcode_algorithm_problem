class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        dict1 = defaultdict(int)
        max1 = 0

        left , right = 0,0
        while right < length:
            dict1[s[right]] +=1
            
            while dict1[s[right]] > 1:
                dict1[s[left]] -=1
                left +=1
            max1 = max(max1, right - left +1)  
            right +=1
        return max1         
            


        