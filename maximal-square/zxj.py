class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        mx=0
        if not matrix: return mx
        dp=[0]*len(matrix[0])
        for row in matrix:
            last=0
            for idx in xrange(len(row)):
                tmp=dp[idx]
                if row[idx]=='1':
                    dp[idx]=min((dp[idx-1] if idx else 0),tmp,last)+1
                    mx=max(mx,dp[idx])
                else:
                    dp[idx]=0
                last=tmp

        return mx*mx
