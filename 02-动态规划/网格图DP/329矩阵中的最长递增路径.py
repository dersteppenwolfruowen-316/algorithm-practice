class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 每一个元素都可能成为路径的开头
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        def dfs(r,c):
            if memo[r][c]!=0:
                return memo[r][c] # r,c 开始的最短路径已经有了
            max_len = 1
            direction = [(0,1), (0,-1), (1,0),(-1,0)] # 下，上，右，左
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]: #递增
                    max_len=max(max_len,dfs(nr,nc)+1)
            memo[r][c] = max_len
            return max_len

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        return ans
            