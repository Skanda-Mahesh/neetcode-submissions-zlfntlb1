class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)

        def costs(curr):
            if curr >= len(cost):
                return 0
            if dp[curr] == -1:
                ans = min(costs(curr+1), costs(curr+2)) + cost[curr]
                dp[curr] = ans
                return ans
            else:
                return dp[curr]
        return min(costs(0), costs(1))