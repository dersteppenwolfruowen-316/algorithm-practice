class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # = yi + yj + (xj - xi)
        # = (yi - xi) + (yj + xj) 先变形
        # q存储yi-xi的单调递增的索引
        q = deque() # 存储所有候选左端点的索引，队列直接维护左端点
        ans = -float('inf')
        
        for j in range(len(points)):
            xj, yj = points[j]
            # 1.移除j点下不满足xj-xi <= k的点
            while q and xj - points[q[0]][0] > k:
                q.popleft() # 左端点前进
            #2.计算答案（队首的yi-xi最大值）
            if q:
                i = q[0]
                ans = max(ans, (points[i][1] - points[i][0]) + (yj+xj))
            #3.维护单调递增队列（当前点的yi-xi）
            while q and (points[q[-1]][1] - points[q[-1]][0]) <= yj-xj:
                q.pop()
            q.append(j)
        return ans




        