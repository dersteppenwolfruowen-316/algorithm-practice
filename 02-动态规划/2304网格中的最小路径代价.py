class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # 每个单元格的代价便是值+代价
        # 列的状态也需要记录
        # 双循环找
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i:int, j:int) -> int:
            if i == 0 :
                return grid[0][j]
            best = inf
            for k in range(n):
                prev = dfs(i-1, k) #上一步，子问题
                val = grid[i-1][k]
                best = min(best, prev + moveCost[val][j])
            return best + grid[i][j]
        return min(dfs(m - 1, j) for j in range(n))