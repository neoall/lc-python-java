import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k=k-1
        arr=[i for i in xrange(1,n+1)]
        div=math.factorial(n-1)
        rs=[]
        ridx=n-1
        while k>0:
            ci=k/div
            rs.append(arr.pop(ci))
            k=k%div
            div/=ridx
            ridx-=1
            
        return ''.join(str(i) for i in rs+arr)
