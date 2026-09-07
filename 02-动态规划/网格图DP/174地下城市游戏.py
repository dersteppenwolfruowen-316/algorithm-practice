class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 也就是所有可能路径的最大负值，便是最低初始点数
        # 同时必须保证每一个前缀和都要>=0，否则死亡
        # 因此dfs(i,j):进入房间 (i,j) 时，为了能安全走完剩下的路径（到达终点时血量 ≥1）所需的最低血量。
        m, n = len(dungeon), len(dungeon[0])
        @cache 
        def dfs(i:int, j:int) -> int:
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            if i == m - 1:
                return max(1, dfs(i, j + 1) - dungeon[i][j])
            if j == n - 1:
                return max(1, dfs(i + 1, j) - dungeon[i][j])
            need = min(dfs(i + 1, j), dfs(i, j + 1)) # 走完接下来路径需要的最小血量损失
            return max(1, need - dungeon[i][j]) # 如果加上当前的健康数不能比1小

        return dfs(0, 0)

        