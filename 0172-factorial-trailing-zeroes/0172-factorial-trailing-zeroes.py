class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        fact =1


        for i in range(1,n):
            num = 5**i
            count +=(n//num)

            if num > n:
                return count
        return 0