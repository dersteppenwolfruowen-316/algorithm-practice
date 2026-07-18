class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        vol = 0
        for right, num in enumerate(arr):
            vol += num
            left = right - k + 1
            if left < 0:
                continue
            if vol/k >= threshold:
                res += 1
            vol -= arr[left]
        return res
