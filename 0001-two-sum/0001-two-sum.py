class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = 0
        for i in range(len(nums)-1):
            value = target - nums[i]
            for j in range(i+1,len(nums)):
                if value == nums[j]:
                    return([i,j])



             
        