class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        le = len(pushed)
        stack = []
        l = 0
        for i in range(le):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[l] and l < le:
                stack.pop()
                l+=1
        return not stack        

        