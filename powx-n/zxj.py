class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0: return 1.0/self.myPow(x,-n)
        c=n
        r=1
        t=x
        while c>0:
            b=c&1
            c=c>>1
            if b:r*=t
            t=t*t
        return r
