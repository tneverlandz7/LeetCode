class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        ans = float("inf")
        sum = 0

        for right,x in enumerate(nums):
            sum += x
            while sum >= target:
                sum -= nums[left]
                ans = min(ans,right-left+1)
                left += 1
            
        
        return ans if ans<=len(nums) else 0