class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)
        
        # 对于每个位置i，检查是否在某个key的k范围内（而不是2k）
        for i in range(n):
            # 检查i附近k范围内是否有key
            left = max(0, i - k)
            right = min(n - 1, i + k)
            
            for j in range(left, right + 1):
                if nums[j] == key:
                    ans.append(i)
                    break  # 找到一个key就够，跳出循环
        
        return ans
                
        