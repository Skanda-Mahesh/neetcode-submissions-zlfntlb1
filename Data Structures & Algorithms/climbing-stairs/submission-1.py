class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def counts(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
                
            if dp[curr] == -1:
                ans = counts(curr+1) + counts(curr+2)
                dp[curr] = ans
                return ans
            else:
                return dp[curr]
            
        
        return counts(0)