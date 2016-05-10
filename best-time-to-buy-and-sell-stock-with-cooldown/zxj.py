class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b,s,c=None,0,0
        for v in prices:
            b,s,c=max(b,c-v) if b is not None else -v, v+b if b is not None else 0, max(c,s)
        return max(s,c)
