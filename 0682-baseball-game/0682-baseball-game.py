class Solution:
    def calPoints(self, operations: List[str]) -> int:
        le = len(operations)
        stack = []
        for s in operations:
            if s == "+" and stack:
                stack.append(stack[-1] + stack[-2])
            elif s == "D" and stack:
                stack.append(2 * stack[-1])
            elif s == "C" and stack:
                stack.pop()
            else:
                stack.append(int(s))  
        return sum(stack)                  

        