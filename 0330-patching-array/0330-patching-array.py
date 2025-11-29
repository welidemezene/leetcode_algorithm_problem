class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        piches = 0
        curr_sum = 0
        i = 0
        while curr_sum < n and i < len(nums):
            if nums[i] <= curr_sum +1:
                curr_sum += nums[i]
                i+=1
            else:
                curr_sum += curr_sum +1
                piches +=1
        while curr_sum < n:
            curr_sum += curr_sum + 1
            piches +=1
        return piches                
            

        
        
       