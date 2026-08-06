class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(2, rowIndex+2):
            l = self.conlist(res[i-2])
            res.append(l)
        return res[rowIndex]
    
    def conlist(self, ar):
        len_new = len(ar)+1
        r = []
        for i in range(len_new):
            if i == 0:
                r.append(1)
                continue
            if i == len_new-1:
                r.append(1)
                continue
            # otherwise just sum
            r.append(ar[i-1]+ar[i])
        return r
            
            