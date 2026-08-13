class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        ar = preorder.split(',')
        n = len(ar)
        ct = 0
        for i in range(n-1, -1, -1):
            if ar[i] != '#': 
                if ct < 2: return False
                ct -= 2
                ct += 1
            else: ct += 1
        return ct == 1