class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSum = 0
        lans = 0 
        rans = 0

        for i in range (len(heights)):
            for j in range(i, len(heights)):

                volume = min(heights[i], heights[j]) * abs((j - i));
                if volume > maxSum:
                    maxSum = volume; 

        return maxSum 