class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []
        
        # Helper: Calculate sum of every subtree and store it
        def get_sum(node):
            if not node: return 0
            # Post-order: children first, then self
            left = get_sum(node.left)
            right = get_sum(node.right)
            
            curr_sum = left + right + node.val
            all_sums.append(curr_sum)
            return curr_sum
        
        total_sum = get_sum(root)
        max_prod = 0
        
        # For every possible subtree, imagine cutting the edge above it
        for s in all_sums:
            product = s * (total_sum - s)
            max_prod = max(max_prod, product)
            
        return max_prod % (10**9 + 7)