class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        curr=0
        given=0
        for i in range(0,n):
            curr+=nums[i]*i
            given+=nums[i]
        res=curr
        for i in range(n-1,-1,-1):
            curr+=given-(nums[i]*(n))
            res=max(res,curr)
        return res