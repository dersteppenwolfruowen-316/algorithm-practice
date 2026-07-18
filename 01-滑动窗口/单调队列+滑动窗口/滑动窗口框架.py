def longestSubarray(self, nums, limit):
    max_q, min_q = deque(), deque()
    left = ans = 0
    
    for right in range(len(nums)):
        # 1. 加入新元素，维护单调性
        while max_q and nums[max_q[-1]] < nums[right]:
            max_q.pop()
        max_q.append(right)
        
        while min_q and nums[min_q[-1]] > nums[right]:
            min_q.pop()
        min_q.append(right)
        
        # 2. 调整窗口（不满足条件时移动左指针）
        while nums[max_q[0]] - nums[min_q[0]] > limit:
            if max_q[0] == left:
                max_q.popleft()
            if min_q[0] == left:
                min_q.popleft()
            left += 1
        
        # 3. 更新答案
        ans = max(ans, right - left + 1)
    
    return ans