class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSum = 0
        lans = 0 
        rans = len(heights)-1
        while lans < rans:
            total = min(heights[lans], heights[rans]) * (rans - lans)

            if total > maxSum: 
                maxSum = total
            
            if heights[lans] < heights[rans]: 
                lans+=1
            else: 
                rans-=1
        
        return maxSum
                

        