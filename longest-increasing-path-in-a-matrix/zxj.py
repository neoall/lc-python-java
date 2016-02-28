class Solution(object):
    def getPN(self,i,j,mem,matrix):
        if mem[i][j] is None:
            mx=0
            for di,dj in ((-1,0),(0,-1),(1,0),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj]>matrix[i][j]:
                    mx=max(mx,self.getPN(ni,nj,mem,matrix))
            mem[i][j]=mx+1
        return mem[i][j]
        

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        mem=[[None]*len(matrix[0]) for i in xrange(len(matrix))]
        mx=0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                mx=max(mx,self.getPN(i,j,mem,matrix))
                
        return mx
