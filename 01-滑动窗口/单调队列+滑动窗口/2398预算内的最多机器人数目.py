class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left = 0
        ans = 0
        max_q = deque()
        window_sum = 0 
        # 滑动窗口和必须用变量维护，避免重复计算

        for right,x in enumerate (chargeTimes):
            while max_q and chargeTimes[max_q[-1]] < x:
                max_q.pop()
            max_q.append(right)
            window_sum += runningCosts[right]
            
            while max_q and chargeTimes[max_q[0]] + (right - left + 1)*window_sum > budget:
                if max_q and max_q[0] == left:
                    max_q.popleft()
                window_sum -= runningCosts[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans
