class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        while n!=0:
            r+=n&1
            n=n>>1
        return r
