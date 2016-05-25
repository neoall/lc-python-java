class Solution(object):
    
    def easy(self,s,wordDict):
        dp={0}
        if len(wordDict)>0:
            wlens={len(word) for word in wordDict}
            minlen,maxlen=min(wlens),max(wlens)
            for vlen in xrange(1,len(s)+1):
                for wlen in wlens:
                    if vlen-wlen>=0 and vlen-wlen in dp:
                        if s[vlen-wlen:vlen] in wordDict:
                            dp.add(vlen)
                            break
        
        return len(s) in dp
    
    def use_trie(self,s,wordDict):
        root={}
        _leaf=('leaf',)
        for word in wordDict:
            cur=root
            for c in word:
                if c not in cur:
                    cur[c]={}
                cur=cur[c]
            cur[_leaf]=1
            
        states=[root]
        valid=True
        for c in s:
            nxt_states=[]
            valid=False
            for state in states:
                if c in state:
                    nxt_states.append(state[c])
                    if _leaf in state[c]:
                        if not valid: nxt_states.append(root)
                        valid=True
            states=nxt_states
            
        return valid
            
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        return (self.easy,self.use_trie)[0](s,wordDict)
        
        
