class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]* len(boxes)
        balls,moves=0,0
        for i in range(len(boxes)):
            ans[i] = balls + moves
            moves = moves + balls
            balls += int(boxes[i])
        balls , moves = 0,0    
        for i in reversed(range(len(boxes))):
            ans[i] += balls + moves
            moves = moves + balls
            balls += int(boxes[i])
        return ans    

        