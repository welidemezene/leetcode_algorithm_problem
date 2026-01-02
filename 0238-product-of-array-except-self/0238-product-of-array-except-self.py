class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        le = len(nums)

        left_product = 1
        for i in range(le):
            ans[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(le-1,-1,-1):
            ans[i] *= right_product
            right_product *= nums[i]
        return ans        