class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def costs(curr):
            if curr >= len(cost):
                return 0
            
            return min(costs(curr+1), costs(curr+2)) + cost[curr]
        
        return min(costs(0), costs(1))