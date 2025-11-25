class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num not in "+-/*":
                stack.append(int(num))
            else:
                a = stack.pop()
                b = stack.pop()
                if num == "+":
                    stack.append(a+b)
                elif num == "-":
                    stack.append(b-a)
                elif num == "*":
                    stack.append(a*b)
                elif num == "/":
                    stack.append(int(b/a))          
        return stack[0]                  

            
           