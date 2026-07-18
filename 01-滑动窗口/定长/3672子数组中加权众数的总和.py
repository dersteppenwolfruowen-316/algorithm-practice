class Solution:
    def modeWeight(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
            
        freq = defaultdict(int)
        sl = SortedList()  # 存储 (频率, 元素)
        ans = 0
        
        for right, num in enumerate(nums):
            if freq[num] > 0:
                sl.remove((freq[num], num))
            freq[num] += 1
            sl.add((freq[num], num))
            left = right - k + 1
            if left < 0:
                continue
            
            # 找到最大频率对应的最小元素
            max_freq = sl[-1][0]  # SortedList 最后一个元素频率最大
            
            # 二分查找第一个频率为 max_freq 的元素
            idx = sl.bisect_left((max_freq, -float('inf')))
            mode = sl[idx][1]  # 该频率下最小的元素
            
            ans += mode * max_freq
            left_num = nums[left]
            sl.remove((freq[left_num], left_num))
            
            # 更新频率
            freq[left_num] -= 1
            if freq[left_num] > 0:
                # 如果频率仍大于0，添加新的 (频率, 元素)
                sl.add((freq[left_num], left_num))
            else:
                del freq[left_num]
        
        return ans
        