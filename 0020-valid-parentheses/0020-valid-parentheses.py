class Solution:
    def isValid(self, s: str) -> bool:
        freq = {")":"(", "]":"[","}":"{"}
        stack = []
        
        for n in s:
            if n in "([{":
                stack.append(n)
            elif n in ")]}":
                if not stack or freq[n] != stack.pop():
                    return False
              
        return not stack                    

        