class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost): return -1
        si=None
        accu=0
        for idx in xrange(len(gas)):
            accu+=gas[idx]-cost[idx]
            if accu<0: si,accu=None,0
            elif si is None: si=idx
            
        return si
