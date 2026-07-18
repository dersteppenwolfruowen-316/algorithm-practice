class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        right = 0
        res = 0
        same_el = defaultdict(int)
        for c in s:
            same_el[c] += 1
            left = right - k + 1
            if left < 0:
                right += 1
                continue
            if len(same_el) == k:
                res += 1
            out = s[left]
            same_el[out] -= 1
            if same_el[out] == 0:
                del same_el[out]
            right += 1
        return res


        