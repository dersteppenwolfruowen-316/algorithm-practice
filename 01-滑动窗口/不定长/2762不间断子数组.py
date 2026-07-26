class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        # 维护两个单调队列
        max_q = deque()  # 维护最大值（递减队列）
        min_q = deque()  # 维护最小值（递增队列）
        for i, num in enumerate(nums):
            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)

            while min_q and min_q[-1] > num:
                min_q.pop()
            min_q.append(num)
            while max_q[0] - min_q[0] > 2:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1
            ans += i - left + 1
        return ans
        