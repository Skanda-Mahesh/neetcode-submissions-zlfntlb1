class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        col = len(grid[0])
        def dfs(m:int, n:int, visited:set):
            if min(m, n) < 0 or m>=rows or n >= col:
                return 
            if grid[m][n] == '0':
                return
            if (m, n) in visited:
                return
            visited.add((m, n))

            dfs(m+1, n, visited)
            dfs(m, n+1, visited)
            dfs(m-1, n, visited)
            dfs(m, n-1, visited)
            return

        visited = set()
        count = 0
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        count += 1
                        dfs(i, j, visited)
        return count

            