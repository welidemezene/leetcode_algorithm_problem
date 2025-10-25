class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        max1 = float("-inf")    
        for i in range(n-k+1):
            we = prefix[i+k] - prefix[i]
            max1 = max(max1, we)
        return max1/k    
                
        