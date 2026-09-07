class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        #增加一个方向参数k
        #定义dfs(i,j,k)为从方向k来到(i,j)的情况下，从(i,j)倒着回到起点(0,0)的方案数
        @cache
        def dfs(i:int, j:int, k:int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            if grid[i][j] == 0:
                return (dfs(i, j-1,0) + dfs(i-1,j,1)) % 1_000_000_007
            if k == 0:
                return dfs(i-1, j, 1)
            return dfs(i,j-1,0)
        
        return dfs(m-1,n-1,0)
