from collections import defaultdict

class Solution(object):
    def build_dict(self,wordList,beginWord,endWord):
        tmap=defaultdict(set)
        tt=defaultdict(list)
        for w in wordList:
            for i in xrange(len(w)):
                tt[w[:i]+'?'+w[i+1:]].append(w)

        for k in tt:
            if len(tt[k])>1:
                for i in xrange(len(tt[k])):
                    for j in xrange(i+1,len(tt[k])):
                        tmap[tt[k][i]].add(tt[k][j])
                        tmap[tt[k][j]].add(tt[k][i])

        bset,eset=set(),set()
        for i in xrange(len(beginWord)):
            tw=beginWord[:i]+'?'+beginWord[i+1:]
            if tw in tt:
                bset.update(tt[tw])
        for i in xrange(len(endWord)):
            tw=endWord[:i]+'?'+endWord[i+1:]
            if tw in tt:
                eset.update(tt[tw])

        return tmap,bset,eset

    def find(self,curset,tmap,tarset1,tarset2,skipset):
        newset=set()
        for e in curset:
            for v in tmap[e]:
                if v in tarset1 or v in tarset2:
                    return set(),True
                if v not in curset and v not in skipset:
                    newset.add(v)

        return newset,False
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        if beginWord==endWord: return 0
        tmap,bset,eset=self.build_dict(wordList,beginWord,endWord)
        if beginWord in eset: return 2
        if len(bset&eset)>0: return 3
        c=2
        vbset,veset={beginWord},{endWord}
        found=False
        while not found and (len(bset)>0 or len(eset)>0):
            nbset,found=self.find(bset,tmap,veset,eset,vbset)
            if found:
                c+=1
                break

            neset,found=self.find(eset,tmap,vbset,bset,veset)
            if found:
                c+=1
                break
            
            t2=(len(nbset&neset)>0)
            c+=2
            if t2:
                found=True
            else:
                vbset.update(bset)
                veset.update(eset)
                bset,eset=nbset,neset

        if found:
            return c+1
        else:
            return 0
