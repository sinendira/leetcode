class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # so 4 things are requried in here left top and right and bottom
        # so left starts at 0 , top also at 0 ,bottom at last row and rigth at last col
        rows , cols = len(matrix),len(matrix[0])
        left , top = 0, 0 
        bottom = rows - 1 
        right = cols-1
        # [top,left]                            right
        #  ____________________________________
        # |                                     |
        # |                                     |
        # |                                     |
        # |                                     |
        # |____________________________________ |
        # bottom
        ans = []#final matrix 
        while left<=right and top<=bottom:
                # left to right itr so top vaires
                for i in range(left,right+1):
                    ans.append(matrix[top][i])#top(row) stays same i(cols) itr
                top+=1
                # top to bottom via right 
                for i in range(top,bottom+1):
                    ans.append(matrix[i][right])#rows changes cols stays the same
                right-=1
                # right to left-via bottom
                if top<=bottom:
                    for i in range(right,left-1,-1):
                        ans.append(matrix[bottom][i])#cols changes row stays the same
                bottom-=1
                # bottom to top - via left
                if left<=right:
                    for i in range(bottom,top-1,-1):
                        ans.append(matrix[i][left])#rows changes cols stays the same
                left+=1

        return ans