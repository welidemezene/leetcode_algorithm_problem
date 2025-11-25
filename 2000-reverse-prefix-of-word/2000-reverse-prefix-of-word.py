class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        le = len(word)
        
        for i in range(le):
            if word[i] == ch:
                d = i
                return word[0:d+1][::-1] + word[d+1:]       

                break
        return word        
       
        