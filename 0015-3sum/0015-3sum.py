class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        le = len(nums)
        lis = []
        for i in range(le-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = le-1
                
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    lis.append([nums[i],nums[l],nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1        

                elif s > 0:
                    r-=1
                else:
                    l+=1        
        return lis            