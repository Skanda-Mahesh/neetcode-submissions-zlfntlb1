class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        col = len(grid[0])
        visited = set()
        def dfs(m, n, visited):
            if min(m, n) < 0 or m >= rows or n >= col or grid[m][n] == 0:
                return 0
            if (m, n) in visited:
                return 0
            if grid[m][n] == 1:
                count = 0
                visited.add((m,n))
                count += dfs(m+1, n, visited)
                count += dfs(m, n+1, visited)
                count += dfs(m-1, n, visited)
                count += dfs(m, n-1, visited)
                return count + 1
        ans = []
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans.append(dfs(i,j, visited))
        
        return max(ans) if ans else 0
            
            