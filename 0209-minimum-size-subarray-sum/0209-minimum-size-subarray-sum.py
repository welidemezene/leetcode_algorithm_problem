class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        le = len(nums)
        sum1 = 0
        min1 = float("inf")
        l = 0
        for i in range(le):
            sum1 +=nums[i]
            while sum1 >= target:
                min1 = min(min1, i-l+1)
                sum1 -= nums[l]
                l+=1
        return min1 if min1 != float("inf") else 0       

        