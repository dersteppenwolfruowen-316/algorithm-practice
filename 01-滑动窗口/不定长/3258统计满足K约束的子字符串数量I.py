class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        ans = 0
        left = 0
        cnt = [0] * 2
        for right, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            ans += right - left + 1 # 越短越合法
        return ans


        