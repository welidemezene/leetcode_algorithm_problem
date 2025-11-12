class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max1 = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            max1 = max(max1, p-buy_price)    
        return max1    

       