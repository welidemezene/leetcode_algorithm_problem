class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif n == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif n == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y) 
            elif n == "/":
                x = stack.pop()
                y = stack.pop()
                
                stack.append(int(y/x))


                
                # return stack 
                
            else:
                stack.append(int(n))  
        return stack[-1]        

        