class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate(n, k):
            x = [i+1 for i in range(k)]
            while True:
                yield x.copy()
                if x[-1] != n:
                    x[-1] += 1
                else:
                    i = 1
                    while x[-i] == n-i+1:
                        i += 1
                    x[-i] += 1
                    i -= 1
                    while i > 0:
                        x[-i] = x[-i-1] + 1
                        i -= 1
        ans = []
        c = math.comb(n, k)
        g = generate(n, k)
        for i in range(c):
            ans.append(next(g))
        return ans