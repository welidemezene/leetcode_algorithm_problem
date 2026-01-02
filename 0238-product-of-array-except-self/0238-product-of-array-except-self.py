class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stack1 = []
        stack2 = []
        ans = []
        le = len(nums)
        for i in range(le):
            if i == 0:
                stack1.append(1)
            else:
                p = stack1[-1] * nums[i-1]
                stack1.append(p)
        
        for i in reversed(range(le)):
           
            if i == le-1:
                stack2.append(1)
            else:
                s = stack2[-1] * nums[i+1]
                stack2.append(s)
        stack2.reverse()       
        for i in range(le):
            m = stack1[i] * stack2[i]
            ans.append(m)
        return ans                

        