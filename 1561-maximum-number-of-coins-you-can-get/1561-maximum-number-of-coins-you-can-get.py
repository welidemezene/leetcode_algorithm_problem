class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        me = 0
        le = len(piles)
        s = le//3
        for i in range(le-s):
            if i % 2 !=0:
                me+=piles[i]
        return me        
        