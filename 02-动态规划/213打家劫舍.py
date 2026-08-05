class Solution:
    def rob(self, nums: List[int]) -> int:
        curr1 = curr2 =  0
        prev1 = prev2 = 0
        if len(nums) == 1:
            return nums[0]

        # 1.偷窃nums[0]
        for i in nums[:-1]:
            prev1, curr1 = curr1, max(curr1,prev1+i)
        # 2.不偷窃nums[0]
        for i in nums[1:]:
            prev2, curr2 = curr2, max(curr2, prev2+i)

        return max(curr1, curr2)

            
            
        