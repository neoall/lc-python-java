class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 0-25 for a-z; 26 for leaf 
        self.trie=[None]*27
    
    def get_cid(self,c):
        return ord(c)-ord('a')
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur=self.trie
        for c in word:
            cid=self.get_cid(c)
            if cur[cid] is None: cur[cid]=[None]*27
            cur=cur[cid]
        cur[26]=True

    def rec_search(self,tt,word,idx):
        if tt is None: return False
        if idx==len(word): return bool(tt[26])
        c=word[idx]
        if c!='.':
            return self.rec_search(tt[self.get_cid(c)],word,idx+1)
        else:
            return any(self.rec_search(tt[i],word,idx+1) for i in xrange(26))
            
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        return self.rec_search(self.trie,word,0)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
