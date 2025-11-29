class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        list = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        slidi = sum(list[0:k])
        max1 = slidi
        l = 0
        for i in range(k, len(list)):
            slidi += list[i]
            slidi -= list[l]
            l+=1
            max1 = max(max1, slidi)
        return max1    


        