
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        left , right = 0,0
        min1 = math.inf
        sum1 = 0
        check = False
        while right < length:
            sum1 +=nums[right]
            
            while sum1 >= target:
                min1 = min(min1, right - left +1 )
                sum1 -= nums[left]
                left +=1
                check = True
            
                
            right +=1
        if check:
            return min1
        else:
            return 0
                        

        