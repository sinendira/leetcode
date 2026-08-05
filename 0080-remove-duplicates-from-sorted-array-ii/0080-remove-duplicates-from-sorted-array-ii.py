class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        s = 2
        for f in range(2,n):
            if nums[f]!=nums[s-2]:
                nums[s] = nums[f]
                s += 1
        return s