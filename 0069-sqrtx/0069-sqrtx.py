class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        num = x

        while num * num > x:
            num = (num + x // num) // 2

        return num