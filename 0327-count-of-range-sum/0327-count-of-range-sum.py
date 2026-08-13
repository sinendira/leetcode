class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ps, ret = [0], 0
        for s in accumulate(nums):
            ret += bisect_right(ps, s - lower) - bisect_left(ps, s - upper)
            bisect.insort(ps, s)
        return ret