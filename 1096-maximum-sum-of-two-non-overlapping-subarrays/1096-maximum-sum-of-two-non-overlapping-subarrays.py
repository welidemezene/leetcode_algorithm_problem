class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
        # prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        def get(l, r):
            return nums[r] - (nums[l-1] if l > 0 else 0)
        
        res = 0
        
        # Case 1: L before M
        maxL = get(0, L-1)
        for i in range(L, len(nums)-M+1):
            maxL = max(maxL, get(i-L, i-1))
            res = max(res, maxL + get(i, i+M-1))
        
        # Case 2: M before L
        maxM = get(0, M-1)
        for i in range(M, len(nums)-L+1):
            maxM = max(maxM, get(i-M, i-1))
            res = max(res, maxM + get(i, i+L-1))
        
        return res
