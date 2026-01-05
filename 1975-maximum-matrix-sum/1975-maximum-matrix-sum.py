class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs_sum = 0
        min_abs_val = float('inf')
        neg_count = 0
        
        for row in matrix:
            for val in row:
                total_abs_sum += abs(val)
                min_abs_val = min(min_abs_val, abs(val))
                if val < 0:
                    neg_count += 1
        
        # If there's an odd number of negatives, one MUST stay negative.
        # We pick the smallest one to stay negative to minimize the loss.
        if neg_count % 2 == 1:
            return total_abs_sum - 2 * min_abs_val
        
        return total_abs_sum