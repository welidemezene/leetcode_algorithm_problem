class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for sm in s:
            if sm.isalnum():
                st += sm.lower()
        if st == st[::-1]:
            return True
        else:
            return False            
        
      