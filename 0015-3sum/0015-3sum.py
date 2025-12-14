class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len1 = len(nums)
       
        sum1 = 0
        stack = []
        nums.sort()
        for i in range(len1-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len1 -1
            while l < r:
                sum1 = nums[i]+nums[l]+nums[r]
                if sum1 == 0:
                    stack.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1    
                elif sum1 > 0:
                    r-=1
                else:
                    l+=1
        return stack                        

