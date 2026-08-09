class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(i:int, j:int) -> int:
            if i<0 or j<0 or obstacleGrid[i][j] : #如果子问题是一个障碍，就自动返回0，因此下面不需要再分是否障碍的情况（弄清楚子问题）
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i-1,j) + dfs(i,j-1)
            
        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        