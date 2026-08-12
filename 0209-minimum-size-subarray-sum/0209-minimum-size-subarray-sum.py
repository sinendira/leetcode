class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_window = float('inf')
        current_sum = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window as much as possible while the condition holds
            while current_sum >= target:
                min_window = min(min_window, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_window if min_window != float('inf') else 0