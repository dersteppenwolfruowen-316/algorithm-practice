class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        # 创建一个栈,保存历史幂次
        MOD = 10**9 + 7
        ans = score = 0
        freq_map = {}
        for right, num in enumerate(nums):
            if num not in freq_map:
                score += num
                freq_map[num] = [num]
            else:
                last = freq_map[num][-1]
                cur = last * num % MOD
                score += cur - last # 增加：新幂次 - 旧幂次（是幂次不是和，所以要减去旧幂次）
                freq_map[num].append(cur) # 把新幂次压入栈
            if right >= k - 1: # 形成了窗口
                ans = max(ans, score % MOD)
                num = nums[right-k+1] 
                freq = freq_map[num] 
                score -= freq.pop() #减去当前最高幂次贡献
                if freq: score += freq[-1]  #但要加上次一级的幂次贡献
                else: del freq_map[num]# 该数字在窗口中完全消失了，不存在的话，就把这个幂次删掉
        return ans


            

        