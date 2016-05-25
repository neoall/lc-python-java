class Solution(object):
    def dfs(self,dp,cpos,s,paths,rs):
        if cpos not in dp: return
        if cpos==0: rs.append(paths)
        for last in dp[cpos]:
            self.dfs(dp,last,s,s[last:cpos]+(' '+paths if len(paths)>0 else ''),rs)
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp={0:[]}
        if len(wordDict)>0:
            wlens={len(word) for word in wordDict}
            minlen,maxlen=min(wlens),max(wlens)
            for vlen in xrange(1,len(s)+1):
                for wlen in wlens:
                    last=vlen-wlen
                    if last>=0 and last in dp:
                        if s[last:vlen] in wordDict:
                            if vlen not in dp:
                                dp[vlen]=[]
                            dp[vlen].append(last)
        
        rs=[]
        self.dfs(dp,len(s),s,'',rs)
        return rs
