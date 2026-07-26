class Solution:
    def balancedString(self, s: str) -> int:
        # n一定是4的倍数
        n = len(s)
        k = n // 4
        cnt = Counter(s)
        left = 0
        ans = inf
        if len(cnt) == 4 and min(cnt.values()) == k:  
            return 0
        # 所有字符个数
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            # 统计滑动窗口外的个数
            while max(cnt.values()) <= k :
                ans = min(ans, right-left+1)
                cnt[s[left]] += 1
                left += 1
        return ans
