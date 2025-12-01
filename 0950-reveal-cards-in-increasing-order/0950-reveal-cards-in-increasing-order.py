class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()

        idx = deque(range(len(deck)))
        res = [0] * len(deck)

        for d in deck:
            id = idx.popleft()
            res[id] = d
            if idx:
                idx.append(idx.popleft())
        return res        
           

        