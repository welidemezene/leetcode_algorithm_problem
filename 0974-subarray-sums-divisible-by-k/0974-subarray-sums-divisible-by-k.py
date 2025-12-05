class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        freq = defaultdict(int)
        freq[0] = 1
        count1 = 0
        for num in nums:
            prefixsum += num
            comp = prefixsum % k
            if comp < 0 :
                comp+=k
            elif comp in freq:
                count1+= freq[comp]
                freq[comp]+=1
            else:
                freq[comp] = 1        
            
        return count1        


        