class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count1 = 0
        left = 0
        right = len(nums) -1
        while left < right:
            if nums[left] + nums[right] < target:
                count1 += right - left
                left +=1
            elif nums[left] + nums[right] >= target: 
                right -=1
        return count1           
        