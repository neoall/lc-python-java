class Solution(object):
    def sm(self,cs,cp):
        return cp=='.' or cs==cp
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[False]*len(p)
        
        for ip in xrange(len(p)):
            if ip%2==1:
                if p[ip]=='*':
                    dp[ip]=True
                else:
                    break
        #print -1,dp
        
        for i in xrange(len(s)):
            si=s[i]
            pj=None
            
            lasti_j_1=i==0
            for j in xrange(len(p)):
                lastpj=pj
                pj=p[j]
                tmp=dp[j]
                if pj!='*':
                    dp[j]=lasti_j_1 and self.sm(si,pj)
                else:
                    dp[j]=(j>=2 and dp[j-2]) or ((lasti_j_1 or dp[j]) and self.sm(si,lastpj))
                lasti_j_1=tmp
            
            #print i,s[:i+1],dp
        if len(dp)>0:
            return dp[-1]
        else:
            return len(s)==0
