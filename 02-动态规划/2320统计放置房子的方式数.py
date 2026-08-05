MOD = 1_000_000_007
MX = 10_001

f = [1, 2] # 从最小子问题开始，先提前算出所有长度下的放法
while len(f) < MX:
    # 子问题是k个地块内放置房子方式的放法总数
    f.append((f[-1] + f[-2]) % MOD) # f[i] = f[i-1] + f[i-2]

class Solution:

    def countHousePlacements(self, n: int) -> int:

        return f[n] ** 2 % MOD

        