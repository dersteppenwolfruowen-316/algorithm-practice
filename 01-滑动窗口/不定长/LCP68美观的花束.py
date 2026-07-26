class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        flower_cnt = defaultdict(int)
        left = 0
        ans = 0
        for i, f in enumerate(flowers):
            flower_cnt[f] += 1

            while flower_cnt[f] > cnt:
                flower_cnt[flowers[left]] -= 1
                if flower_cnt[flowers[left]] == 0:
                    del flower_cnt[flowers[left]]
                left += 1
            ans += i - left + 1
        return ans
