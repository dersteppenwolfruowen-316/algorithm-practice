class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        memo = [[0]*n for _ in range(m)]
        count = 0
        def dfs(i:int,j:int) -> int:
            if memo[i][j] != 0:
                return memo[i][j]
            directions = [(0,1), (0,-1),(1,0),(-1,0)]
            total = 1
            for dr, dc in directions:
                nr, nc = i +dr, j + dc
                if  0<= i+dr < m and 0<= j + dc < n and grid[nr][nc] > grid[i][j]:
                    total += dfs(nr,nc)
            total %= MOD
            memo[i][j] = total
            return total
        

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
        return ans
