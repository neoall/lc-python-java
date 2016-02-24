class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d=1
        span=n-m+1
        rs=0
        while d<=n:
            nd=(d<<1)
            if span<nd and d<=m%nd<=n%nd: rs|=d
            d=nd
            
        return rs
