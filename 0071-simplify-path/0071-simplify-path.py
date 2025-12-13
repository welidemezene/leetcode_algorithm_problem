class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        for m in s:
            if m == "" or m == ".":
                continue
            elif m == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(m)    
        return "/"+"/".join(stack)         


        