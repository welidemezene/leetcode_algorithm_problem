class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        le = len(s)
        if len(nums) == le:
            return False
        else:
            return True  
        