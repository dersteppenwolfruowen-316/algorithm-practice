class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            # 维护一个单调递减的队列，因为前面比他小的一定不可能成为接下来的最大值了
            # 以及在滑动窗口外的左边数值可以去掉
            #滑动窗口框架
            # 1.元素进入窗口
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            # 2.元素出窗口
            if i - q[0] >= k:
                q.popleft()
                
            # 3.记录答案
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans
        