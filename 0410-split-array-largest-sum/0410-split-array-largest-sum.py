class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        def canSplit(limit):
            splitCount=1
            curSum=0

            for num in nums:
                if curSum+num<=limit:
                    curSum+=num
                else:
                    splitCount+=1
                    curSum=num
            return splitCount<=k

        while low<high:
            mid=(low+high)//2

            if canSplit(mid):
                high=mid
            else:
                low=mid+1
        return low

        