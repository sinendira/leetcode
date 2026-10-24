class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot split it into two equal integer subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # dp[i] will be True if a subset sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True # Base case: a sum of 0 is always possible
        
        for num in nums:
            # Move backwards to ensure we don't use the same element multiple times
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
                    
        return dp[target]