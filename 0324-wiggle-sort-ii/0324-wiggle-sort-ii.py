class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = sorted(nums)
        n = len(nums)
        
        mid = (n + 1) // 2
        left = sorted_nums[:mid]
        right = sorted_nums[mid:]
        
        for i in range(len(left)):
            nums[2 * i] = left[-(i + 1)]
            
        for i in range(len(right)):
            nums[2 * i + 1] = right[-(i + 1)]