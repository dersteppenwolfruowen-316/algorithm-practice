class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
    
        # 子数组类动态规划
        val = 0
        n = len(s)
        val_dict = defaultdict(int)
        for i in range(len(chars)):
            val_dict[chars[i]] = vals[i]
        @cache
        def dfs(i: int) -> int:
            if s[i] in chars:
                val = val_dict[s[i]]
            else:
                val = ord(s[i]) - ord('a') + 1
            
            if i == 0:
                return val
            return max(dfs(i - 1), 0) + val
        
        if n == 0:
            return 0
        return max(0, max(dfs(i) for i in range(n)))
        