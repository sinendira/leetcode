class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def recursive(l, r):
            if l >= r: return 0 
            res = inf
            for i in range(l, r):
                a = max(recursive(l, i-1), recursive(i+1, r))
                res = min(res, a+i)
            return res 
        return recursive(1, n)

