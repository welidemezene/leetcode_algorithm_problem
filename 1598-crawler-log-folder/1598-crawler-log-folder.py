class Solution:
    def minOperations(self, logs: List[str]) -> int:
        le = len(logs)
        stack = []
        s = 0
        for num in logs:
            if stack and num == "../":
                stack.pop()
            elif num != "./" and num != "../":
                stack.append(num)
        return len(stack)       
                




        