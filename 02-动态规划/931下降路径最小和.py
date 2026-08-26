class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dfs(i: int, j:int) -> int:
            if i < 0 or j >= len(matrix) or j< 0: #出界的边界情况
                return inf
            if i == 0: # 到达第一行的边界情况
                return matrix[0][j]
            return min(dfs(i-1, j), dfs(i-1,j+1), dfs(i-1,j-1)) + matrix[i][j]
        return min(dfs(n-1,k) for k in range(n))
        