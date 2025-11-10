class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        le = len(nums)
        l,count0,=0,0
        max1 = 0
        for i in range(le):
            if nums[i] == 0:
                count0 +=1
                  
            while count0 > 1:
               
                if nums[l] == 0:
                    count0-=1
                l+=1    
            max1 = max(max1, i-l)    
                
        
        return(max1)                

        