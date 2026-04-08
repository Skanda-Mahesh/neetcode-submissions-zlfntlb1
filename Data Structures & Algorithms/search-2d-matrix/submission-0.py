class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First apply binary search to find the correct col
        # Then apply to find the element in the row 

        leftCol = 0
        rightCol = len(matrix) -1
        
        while leftCol <= rightCol: 
            mid = (leftCol + rightCol) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                left = 0
                right = len(matrix[mid]) -1

                while left <= right: 
                    midInner = (left + right) // 2

                    if matrix[mid][midInner] == target:
                        return True
                    elif matrix[mid][midInner] > target:
                        right = midInner -1
                    elif matrix[mid][midInner] < target: 
                        left = midInner +1
                return False
            elif matrix[mid][0] > target: 
                rightCol = mid -1
            elif matrix[mid][0] < target: 
                leftCol = mid +1 
            
        return False 