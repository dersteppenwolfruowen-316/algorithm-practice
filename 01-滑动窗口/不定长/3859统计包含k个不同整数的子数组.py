class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        def calc(distinct_limit: int) -> int:
            cnt = defaultdict(int)
            valid_m = 0
            ans = left = 0
            for num in nums:
                cnt[num] += 1
                if cnt[num] == m:
                    valid_m += 1
                while len(cnt) >= distinct_limit and valid_m >= k:
                    out = nums[left]
                    if cnt[out] == m:
                        valid_m -= 1
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out]
                    left += 1
                ans += left
            return ans

        return calc(k) - calc(k + 1)


        