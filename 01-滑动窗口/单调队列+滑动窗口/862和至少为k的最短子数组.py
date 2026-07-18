class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 前缀和 + 单调队列
        # 含负数时滑动窗口失败
        n = len(nums)
        # 计算前缀和
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')
        q = deque() # 维护前缀和的单调递增
        for i in range(n+1):
            #检查当前前缀和能否和队首形成满足条件的子数组
            while q and prefix[i] - prefix[q[0]] >= k:
                ans = min(ans, i - q[0])
                q.popleft() # 和至少就先popleft

            # 维护单调递增队列
            # 如果 prefix[i] <= prefix[q[-1]],队尾不够小
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()
            q.append(i)
        return ans if ans!= float('inf') else -1


        