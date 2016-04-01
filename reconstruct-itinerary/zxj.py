class Solution(object):
    def dfs(self,ckey,rlist,tmap,tlen):
        rlist.append(ckey)
        if tlen==len(rlist): return True
        
        tcnt=0
        clen=len(tmap[ckey])
        while tcnt<clen:
            tcnt+=1
            nxt=tmap[ckey].popleft()
            rs=self.dfs(nxt,rlist,tmap,tlen)
            if rs: return True
            rlist.pop()
            tmap[ckey].append(nxt)
                
        return False
    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict,deque
        tmap=defaultdict(list)
        for tfrom,tto in tickets:
            tmap[tfrom].append(tto)
        
        for tkey in tmap: tmap[tkey]=deque(sorted(tmap[tkey]))
        
        cur='JFK'
        rlist=[]
        rs=self.dfs(cur,rlist,tmap,len(tickets)+1)

        return rlist
