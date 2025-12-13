class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for m in s:
            if m.isalnum():
                stack.append(m.lower())
        ans = "".join(stack)        
        if ans == ans[::-1]:
            return True
        else:
            return False            

        