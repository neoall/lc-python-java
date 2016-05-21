class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indgr=[0]*numCourses
        oedges=[set() for i in xrange(numCourses)]
        for cs,pcs in prerequisites:
            indgr[cs]|=(1<<pcs)
            oedges[pcs].add(cs)
            
        snds=set()
        for i,cnt in enumerate(indgr):
            if cnt==0:
                snds.add(i)
        
        rs=[]
        while len(snds)>0:
            nd=snds.pop()
            rs.append(nd)
            for nnd in oedges[nd]:
                indgr[nnd]&=~(1<<nd)
                if indgr[nnd]==0:
                    snds.add(nnd)
        if len(rs)==numCourses:
            return rs
        else:
            return []
