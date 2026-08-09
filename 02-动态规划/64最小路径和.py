class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i:int, j:int) -> int:
            if i < 0 or j < 0 :
                return inf
            if i == 0 and j == 0:
                return grid[i][j]
            return min(dfs(i-1,j),dfs(i,j-1)) + grid[i][j]
        return dfs(len(grid)-1, len(grid[0]) -1) # i行j列
        
        