class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = sum(nums[0:k])
        
        max1 = sum1
        n = len(nums)
        for i in range(n-k):
            sum1 -= (nums[i])
            sum1 += (nums[i+k])
            max1 = max(max1, sum1)
        return max1 / k    

           

        