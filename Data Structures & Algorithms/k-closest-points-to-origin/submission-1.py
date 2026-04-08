class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        comb = []

        for i in points:
            dist = math.sqrt(abs(i[0] ** 2 + i[1] ** 2))
            comb.append([i[0], i[1], dist])
        
        comb.sort(key = lambda x : x[2])
        print(comb)
        ans = [row[:2] for row in comb]
        
        return ans[:k]