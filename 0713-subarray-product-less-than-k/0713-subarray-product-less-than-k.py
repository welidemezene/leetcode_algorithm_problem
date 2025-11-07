class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l,p = 0,1
        count = 0
        le = len(nums)
        for r in range(le):
            p*= nums[r]
            while p >= k:
                p //=nums[l]
                l+=1
            count+=1 + (r-l)
            
        return count        
