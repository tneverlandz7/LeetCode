class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        prod = 1 
        ans = 0

        if k<=1:
            return 0

        for right, x in enumerate(nums):
            prod *= x
            while left<=right and prod >= k:
                prod /= nums[left]
                left += 1
            ans+=right-left+1

        return ans
            
                