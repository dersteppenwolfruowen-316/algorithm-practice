class Solution:


    def maximumTotalDamage(self, power: List[int]) -> int:
        # 注意是伤害值不能重复
        # 因此同样转为值域数组
        cnt = Counter(power)
        a = sorted(cnt)

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1 # 找到满足差值大于2的最小伤害值
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
        
        return dfs(len(a)-1)