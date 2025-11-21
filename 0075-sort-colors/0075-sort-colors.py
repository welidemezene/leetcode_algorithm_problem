class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]]+=1
        le = freq[0]    
        for i in range(le):
            nums[i] = 0
        le1 = freq[1]    
        for i in range(le, le+le1):
            nums[i] = 1
        for i in range(le+le1, len(nums)):
            nums[i] = 2            
        
        