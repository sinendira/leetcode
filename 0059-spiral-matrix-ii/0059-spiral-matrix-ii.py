class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # we need left right and other pointers
        left, right, top, bottom = 0, n-1, 0, n-1 
        val = 1
        res = []
        mat=[[0]*n for i in range(n)]
        # 4 loops after this
        # since this is a square amtrix no need to worry about edhee cases like vectors
        while left<right:
            for i in range(left, right+1):
                mat[top][i]=val
                val+=1

            for i in range(top+1, bottom+1):
                mat[i][right]=val
                val+=1

            # as last is excluded!!
            for i in range(right-1, left-1, -1):
                mat[bottom][i]=val
                val+=1
            
            for i in range(bottom-1, top, -1):
                mat[i][left]=val
                val+=1

            left+=1
            right-=1
            top+=1
            bottom-=1
            
        if n%2:
            mat[n//2][n//2]=n**2
        return mat
            