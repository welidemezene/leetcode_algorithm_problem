class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        
        # dp[i][j] = min ASCII sum to make s1[:i] and s2[:j] equal
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: To match s1[:i] with an empty s2, 
        # we must delete all characters in s1[:i]
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            
        # Base case: To match an empty s1 with s2[:j],
        # we must delete all characters in s2[:j]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    # Characters match! No cost added.
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # No match. We either delete from s1 or s2.
                    # We take the minimum cost of the two choices.
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]), # Delete from s1
                        dp[i][j-1] + ord(s2[j-1])  # Delete from s2
                    )
                    
        return dp[n][m]