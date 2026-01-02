class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = prices[-1]
        max2 = 0
        le = len(prices)-1
        for i in range(le-1,-1,-1):
            if max1 > prices[i]:
                val = max1 - prices[i]
                max2 = max(val,max2)


            max1 = max(prices[i],max1)
        return max2    

        