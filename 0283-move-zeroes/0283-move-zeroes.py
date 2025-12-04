class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        le = len(nums)
        count1 = 0

        for i in range(le):
            if nums[i] != 0:
                count1 +=1
        ind = 0        
        for i in range(le):
            if nums[i] != 0 and ind < count1:
                nums[ind] = nums[i] 
                ind+=1
        for i in range(count1, le):
            nums[i] = 0               


        """
        Do not return anything, modify nums in-place instead.
        """
        