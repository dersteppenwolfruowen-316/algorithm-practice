class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = defaultdict(int)
        for i in s1:
            s1_cnt[i] += 1
        k = len(s1)
        s2_cnt = defaultdict(int)
        
        for r,s in enumerate(s2):
            s2_cnt[s] += 1
            left = r - k + 1
            if left < 0:
                continue
            if s2_cnt == s1_cnt:
                return True
            s2_cnt[s2[left]] -= 1
            if s2_cnt[s2[left]] == 0:
                del s2_cnt[s2[left]]
        return False


        