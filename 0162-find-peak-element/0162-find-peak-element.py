class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans = 0
        max_val = max(nums)
        for val,key in enumerate(nums):
            if key == max_val:
                ans = val
        return ans
        