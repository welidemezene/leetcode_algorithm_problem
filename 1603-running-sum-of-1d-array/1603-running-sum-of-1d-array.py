class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * (length + 1)
        for i in range(1,length + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
        return prefix[1:]   

        