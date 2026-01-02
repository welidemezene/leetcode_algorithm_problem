class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        lis = []
        for l in digits:
            s += str(l)
        n = int(s)
        n+=1
        k = str(n)
        for m in k:
            lis.append(int(m))
        return lis    
              

        