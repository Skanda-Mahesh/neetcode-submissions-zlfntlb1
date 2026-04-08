class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## brute force
        L = 0 
        R = 0 
        maxProfit = 0
        globalmax = 0
        for index, i in enumerate(prices):
            maxProfit = 0
            print(prices[index:])
            for j in prices[index:]:
                print(f"{j} - {i} = {j-i}")
                if j - i > maxProfit:
                    maxProfit = j - i
            if maxProfit > globalmax:
                globalmax = maxProfit
                
        return globalmax