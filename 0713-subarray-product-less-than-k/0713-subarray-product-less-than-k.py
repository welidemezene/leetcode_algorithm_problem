class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        le = len(nums)
        pr = 1
        l = 0
        count1 = 0
        for i in range(le):
            pr*=nums[i]
            while pr >= k:
                pr//=nums[l]
                l+=1
            count1+=(i-l+1)
        return count1        
        