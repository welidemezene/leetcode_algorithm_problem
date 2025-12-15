class Solution:
    def isValid(self, s: str) -> bool:
        freq = {")":"(","]":"[","}":"{"}
        stack = []
        for n in s:
            if n in freq.values():
                stack.append(n)
            elif n in freq.keys():
                if stack and freq[n] == stack[-1]:
                    stack.pop()
                    
                elif not stack or freq[n] != stack[-1]:
                    return False
        return stack == []              



        