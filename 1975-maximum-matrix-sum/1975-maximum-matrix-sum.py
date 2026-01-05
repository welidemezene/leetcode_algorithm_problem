class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_negative = []
        lis = []
        total_sum = 0
        for n in matrix:
            for m in n:
                total_sum += abs(m)
                lis.append(abs(m))
                if m <= 0:
                    count_negative.append(m)

        if len(count_negative) % 2 == 0:
            return total_sum
        else:
            val = min(lis)
            return total_sum - (2 * abs(val))                
        