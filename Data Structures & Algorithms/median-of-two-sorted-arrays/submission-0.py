class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        merged = []

        i, j = 0, 0
        while i < len(num1) and j < len(num2):
            if nums1[i] < num2[j]:
                merged.append(num1[i])
                i+= 1
            else:
                merged.append(num2[j])
                j+= 1
        
        while i < len(num1):
            merged.append(num1[i])
            i+=1
        
        while j < len(num2):
            merged.append(num2[j])
            j += 1

        if len(merged) % 2 == 1:
            return float(merged[(len(merged) // 2)])
        else:
            tmp = merged[len(merged)//2] + merged[len(merged)//2 -1]
            tmp = tmp / 2
            return tmp