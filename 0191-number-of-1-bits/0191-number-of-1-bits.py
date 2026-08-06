class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        return bits.count("1")