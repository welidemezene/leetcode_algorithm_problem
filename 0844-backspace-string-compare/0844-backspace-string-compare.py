class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        le = len(s)
        le1 = len(t)
        stack1 = []
        stack2 = []
        for n in s:
            if stack1 and n == "#":
                stack1.pop()
            elif n != "#":
                stack1.append(n)
        for m in t:
            if stack2 and m == "#":
                stack2.pop()
            elif m != "#":
                stack2.append(m)
        if stack1 == stack2:
            return True
        else:
            return False                            

        