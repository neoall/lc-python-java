class Solution(object):
    def _dp(self,s1,s2,s3):
        if len(s1)>len(s2): return self._dp(s2,s1,s3)
        dp=[False]*(len(s1)+1)
        dp[0]=True
        for m1 in xrange(len(s1)):
            if s1[m1]==s3[m1]:
                dp[m1+1]=True
            else:
                break
        # dp[m1] means:
        # s3[:m1+m2+2] is interleaved with s2[:m2+1] and s1[:m1+1]
        
        for m2 in xrange(len(s2)):
            dp[0]=dp[0] and (s2[m2]==s3[m2])
            last=dp[0]
            for m1 in xrange(len(s1)):
                dp[m1+1]=(dp[m1+1] and s2[m2]==s3[m1+m2+1]) or (last and s1[m1]==s3[m1+m2+1])
                last=dp[m1+1]
        return dp[-1]
        
    def _dfs(self,s1,s2,s3):
        stk=[]
        visited={(0,0)}
        len1,len2,len3=len(s1),len(s2),len(s3)
        cur=(0,0)
        while cur is not None or len(stk)>0:
            if cur is not None:
                clen=sum(cur)
                if clen==len3: return True
                pot=(cur[0],cur[1]+1)
                if cur[1]<len2 and s2[cur[1]]==s3[clen] and pot not in visited:
                    stk.append(pot)
                    visited.add(pot)
                
                pot=(cur[0]+1,cur[1])
                if cur[0]<len1 and s1[cur[0]]==s3[clen] and pot not in visited:
                    cur=pot
                    visited.add(pot)
                else:
                    cur=None
            else:
                cur=stk.pop()
        return False
    
    def _bfs(self,s1,s2,s3):
        lset={(0,0)}
        len1,len2=len(s1),len(s2)
        for step in xrange(len(s3)):
            nset=set()
            for m1,m2 in lset:
                if m1<len1 and s1[m1]==s3[m1+m2]: nset.add((m1+1,m2))
                if m2<len2 and s2[m2]==s3[m1+m2]: nset.add((m1,m2+1))
            lset=nset
            if len(lset)==0: break 
        return len(lset)>0
        
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3): return False
        return [self._dp,self._dfs,self._bfs][2](s1,s2,s3)
        
