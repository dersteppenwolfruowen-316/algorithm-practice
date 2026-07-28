class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        left = ans = freq = 0
        ch_count = defaultdict(int)
        for right, c in enumerate(s):
            ch_count[c] += 1
            while ch_count[c] == k:
                ch_count[s[left]] -= 1
                if ch_count[s[left]] == 0:
                    del ch_count[s[left]]

                left += 1
            ans += left
        return ans