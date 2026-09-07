class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        memo = [[0]*n for _ in range(m)]
        h = (m+n-1)
        if h % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        # 看题解：加入另一个变量来判断字符串是否平衡(左括号+1，右括号-1)
        @cache
        def dfs(i:int,j:int, c:int) -> bool:
            if c > m - i + n-j -1: # 右边是剩下还有几步
                return False
            if i == m-1 and j == n-1:
                return c == 1
            c += 1 if grid[i][j] == "(" else -1
            return c >=0 and (i < m-1 and dfs(i+1,j,c) or j < n-1 and dfs(i, j+1,c)) # 左括号一定大于等于右括号才合法，因此 c>=0
        return dfs(0,0,0)