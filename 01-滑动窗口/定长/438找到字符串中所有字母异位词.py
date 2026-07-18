class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        k = len(p)
        p_cnt = defaultdict(int)
        s_cnt = defaultdict(int)
        for i in p :
            p_cnt[i] += 1
        for r, c in enumerate(s):
            s_cnt[c] += 1
            left = r - k + 1
            if left < 0:
                continue
            if s_cnt == p_cnt:
                res.append(left)
            s_cnt[s[left]] -= 1
            if s_cnt[s[left]] == 0:
                del s_cnt[s[left]]
        return res

        
