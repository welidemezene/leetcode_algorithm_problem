class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        le = len(temperatures)
        ans = [0] * le
        stack = []
        for i,n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ind = i - prev_index
                ans[prev_index] = ind
            stack.append(i)
        return ans        
        
        