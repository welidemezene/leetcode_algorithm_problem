class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum , rightsum = 0, sum(nums)
        for idx, el in enumerate(nums):
            rightsum -= el
            if leftsum == rightsum:
                return idx
            leftsum += el
        return -1        
        