class Solution:
    def climbStairs(self, n: int) -> int:
        def counts(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            
            return counts(curr+1) + counts(curr+2)
        
        return counts(0)