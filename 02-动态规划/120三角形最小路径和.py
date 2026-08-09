class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(i:int, j:int) -> int:
            # 到达顶部
            if i == 0:
                return triangle[0][0]
            # 如果 j 超出上一行的范围，返回无穷大
            if j < 0 or j > i:
                return float('inf')
            return min(dfs(i-1,j),dfs(i-1,j-1)) + triangle[i][j]
        return min(dfs(len(triangle) - 1, k) for k in range(len(triangle[len(triangle) - 1])))
        