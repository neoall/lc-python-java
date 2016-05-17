class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix)==0: return
        lastRow=[0]*len(matrix[0])
        self.smtx=[]
        for orow in matrix:
            currow=[]
            lc,lrc=0,0
            for v,lr in zip(orow,lastRow):
                nv=v+lr+lc-lrc
                currow.append(nv)
                lc=nv
                lrc=lr
            self.smtx.append(currow)
            lastRow=currow

    def sumORegion(self,row,col):
        return self.smtx[row][col] if row>=0 and col>=0 else 0
    
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumORegion(row2,col2) \
            - self.sumORegion(row2,col1-1) \
            - self.sumORegion(row1-1,col2) \
            + self.sumORegion(row1-1,col1-1)


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
