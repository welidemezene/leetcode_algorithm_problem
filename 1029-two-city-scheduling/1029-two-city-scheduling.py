class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sor = sorted(costs, key=lambda x : x[0] - x[1])
        sa = 0
        sb = 0

        for i in range(len(costs)//2):
            sa += sor[i][0]
        for i in range(len(costs)//2, len(costs)):
            sb += sor[i][1]
        return sa + sb        