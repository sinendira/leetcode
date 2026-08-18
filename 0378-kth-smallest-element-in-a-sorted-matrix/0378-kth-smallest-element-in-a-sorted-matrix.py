class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        a = []

        for x in matrix:
            for y in x:
                a.append(y)

        
        a.sort()

        return a[k-1]
        