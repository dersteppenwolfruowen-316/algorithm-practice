class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i == 0:
                return 0
                # 题目说 costs 的下标从 1 开始，但传入的 costs 的下标是从 0 开始的。访问数组的时候下标要减一
            return min(dfs(j) + (i-j)*(i-j) for j in range(max(i-3, 0), i)) + costs[i-1]
        return dfs(n)