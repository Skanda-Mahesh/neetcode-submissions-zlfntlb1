class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## brute force
        l = 0
        r = 0
        maxprofit = 0
        for index in prices: 
            if prices[l] > prices[r]:
                l = r
            if prices[r] - prices[l] > maxprofit:
                maxprofit = prices[r] - prices[l]
            r += 1
                
        return maxprofit