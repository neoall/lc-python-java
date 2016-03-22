class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        from bisect import bisect_left
        
        irmap={}
        for i,c in enumerate(s):
            if c not in irmap:
                irmap[c]=[]
            irmap[c].append(i)
                
        lmap={-1:1}
        for c in t:
            if c not in irmap: return 0
            nlmap={}
            for lastk in lmap:
                idx=bisect_left(irmap[c],lastk+1)
                for nxtp_idx in xrange(idx,len(irmap[c])):
                    nxtp=irmap[c][nxtp_idx]
                    nlmap[nxtp]=nlmap.get(nxtp,0)+lmap[lastk]
            lmap=nlmap
            
        return sum(lmap.values())
