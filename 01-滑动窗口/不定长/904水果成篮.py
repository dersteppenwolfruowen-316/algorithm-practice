class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        kind_count = defaultdict(int)
        left = 0
        ans = 0
        for i in range(len(fruits)):
            kind_count[fruits[i]] += 1
            while len(kind_count) > 2:
                kind_count[fruits[left]] -= 1
                if kind_count[fruits[left]] == 0:
                    del kind_count[fruits[left]]
                left += 1
            ans = max(ans, i - left + 1)
        return ans

        