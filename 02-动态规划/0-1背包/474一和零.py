class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        nums = []
        for x in strs:
            a = x.count('0')
            b = x.count('1')
            nums.append((a, b))

        @cache
        def dfs(i:int, j:int, k:int) -> int:
            if i < 0:
                return 0
            res = dfs(i - 1, j, k) #不选
    
            if j >= nums[i][0] and k >= nums[i][1]:
                res = max(res, dfs(i - 1, j - nums[i][0], k - nums[i][1]) + 1) #选/不选
            return res
        
        return dfs(len(strs)-1,m,n)
