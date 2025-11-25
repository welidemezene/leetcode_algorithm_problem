class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        le = len(s)
        for n in s:
            if stack and n.isdigit():
                stack.pop()
            elif n.isalpha():
                stack.append(n)  
        st = ""          
        for m in stack:
            st += m
        return st    


        