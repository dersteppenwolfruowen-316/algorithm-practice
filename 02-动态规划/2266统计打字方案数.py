class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # 相同连续数字可以1-3个代表一个字符
        # 将不同的数字进行分组，并长度作为target“爬楼梯”
        # 注意字符7，9有4个字母
        MOD = 1_000_000_007
        f = [1, 1, 2, 4]
        g = [1, 1, 2, 4]
        for _ in range(10 ** 5 - 3):  # 预处理所有长度的结果（巧妙）
            f.append((f[-1] + f[-2] + f[-3]) % MOD)
            g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

        ans = 1

        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if ch in "79" else f[m]) % MOD
        return ans
            