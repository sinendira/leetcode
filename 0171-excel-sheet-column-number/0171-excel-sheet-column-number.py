# {'A': 1, ... , 'Z': 26}
ALPHAVALS = { c:i for i, c in enumerate('_ABCDEFGHIJKLMNOPQRSTUVWXYZ') }
ALPHANUMERY = 26

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        numeryLevel = 0 # 0->ones, 1->26, 2->26**2, etc
        while len(columnTitle) > 0:
            c = columnTitle[-1]
            if c not in ALPHAVALS:
                raise ValueError(f"Got invalid char '{c}' not found in ALHPAVALS")
            res += ALPHAVALS[c] * (ALPHANUMERY ** numeryLevel)
            numeryLevel += 1
            columnTitle = columnTitle[:-1]
        return res