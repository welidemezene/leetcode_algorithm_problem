class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res,l,r = 1,0,1
        prev = ""
        
        while r < len(arr):
            if arr[r] == arr[r-1]:
                l = r
                prev = "="
            elif arr[r] > arr[r-1] and prev != ">":
                res = max(res, r-l+1)
                prev= ">"
            elif arr[r] < arr[r-1] and prev != "<":
                res = max(res, r-l+1)
                prev = "<"
            else:
                l = r-1
            r+=1
        return res                  
        
       