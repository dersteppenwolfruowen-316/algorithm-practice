class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        del_ = float('-inf') # 记录删除操作的状态（比较删除和没有删除）
        ans = arr[0]
        for i in range(1,len(arr)):
            x = arr[i]
            del_ = max(del_ + x, no_del) #在当前x为结尾的子数组中删除哪个子数组和最大
            no_del = max(no_del, 0) + x # no_del就是正常的没有删除操作的子数组
            ans = max(ans, del_, no_del)
        return ans
        