from collections import defaultdict
import itertools

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
        newmap=defaultdict(set)
        foundmap=defaultdict(set)
        for e in curset:
            for v in tmap[e]:
                if v in tarset1 or v in tarset2:
                    foundmap[v].add(e)
                if v not in curset and v not in skipset:
                    newmap[v].add(e)
        if len(foundmap)>0: return foundmap,True
        return newmap,False
        
    def join(self,amap,bmap):
        if len(amap)>len(bmap): 
            rb,ra=self.join(bmap,amap)
            return ra,rb
        ra,rb={},{}
        for k in amap:
            if k in bmap:
                ra[k]=amap[k]
                rb[k]=bmap[k]
        return ra,rb
    
    def chain(self,iter,vmap):
        if type(iter)==str:
            yield [iter]
        else:
            for w in iter:
                for x in self.chain(vmap[w],vmap):
                     yield [w]+x
        
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord==endWord: return [[beginWord]]
        tmap,bset,eset=self.build_dict(wordlist,beginWord,endWord)
        if beginWord in eset: return [[beginWord,endWord]]
        iset=bset&eset
        if len(iset)>0: return [t for t in itertools.product((beginWord,),iset,(endWord,))]
        
        vbmap,vemap={beginWord:True},{endWord:True}
        bmap={x:beginWord for x in bset}
        emap={x:endWord for x in eset}
        found=False
        fmap=None
        while not found and (len(bmap)>0 or len(emap)>0):
            nbmap,found=self.find(bmap,tmap,vemap,emap,vbmap)
            if found:
                fmap=nbmap
                vbmap.update(bmap)
                vemap.update(emap)
            else:
                nemap,found=self.find(emap,tmap,vbmap,bmap,vemap)
                jbmap,jemap=self.join(nbmap,nemap)
                vbmap.update(bmap)
                vemap.update(emap)
                if jbmap:
                    found=True
                    fmap=jbmap
                    vbmap.update(jbmap)
                    vemap.update(jemap)
                else:
                    bmap,emap=nbmap,nemap
        
        rs=[]
        if found:
            for k in fmap:
                for c1,c2 in itertools.product(self.chain(fmap[k],vbmap),self.chain({k},vemap)):
                    rs.append(c1[::-1]+c2)
        return rs
        
