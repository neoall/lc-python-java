class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1,len2=len(word1),len(word2)
        if len1<len2: return self.minDistance(word2,word1)
        
        dp=[i for i in xrange(len2+1)]
        for i in xrange(len1):
            dp[0],lrc=i+1,i
            for j in xrange(1,len2+1):
                dp[j],lrc=min(dp[j]+1,dp[j-1]+1,lrc+(1 if word1[i]!=word2[j-1] else 0)),dp[j]
            
        return dp[-1]
