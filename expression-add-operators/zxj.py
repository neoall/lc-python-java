from itertools import product

class Solution(object):
    def mul(self,num,start,end):
        if num[start]=='0' and end-start>1:
            v2s=self.mul(num,start+1,end)
            for v2 in v2s:
                yield 0,'0*'+v2[1]
            return
        for i in xrange(end-start):
            v1=int(num[start:i+start+1])
            if i<end-start-1:
                v2s=self.mul(num,i+start+1,end)
                for v2 in v2s:
                    yield v1*v2[0],num[start:i+start+1]+'*'+v2[1]
            else:
                yield v1,num[start:end]
                
    def partial(self,num,start):
        for i in xrange(start,len(num)):
            v1s=self.mul(num,start,i+1)
            if i<len(num)-1:
                v2s=self.partial(num,i+1)
                for v1,v2 in product(v1s,v2s):
                    yield v1[0]+v2[0],v1[1]+"+"+v2[1]
                    yield v1[0]-v2[0],v1[1]+'-'+v2[1]
            else:
                for v1 in v1s:
                    yield v1
                
    def flip(self,sz,t):
        nsz=''
        smaps=[{},{'+':'-','-':'+'}]
        for c in sz:
            nsz+=smaps[t].get(c,c)
            if c=='-':t=1-t
        return nsz
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        rlist=[]
        
        for i in xrange(len(num)):
            v1s=self.mul(num,0,i+1)
            if i<len(num)-1:
                v2s=self.partial(num,i+1)
                for v1,v2 in product(v1s,v2s):
                    if v1[0]+v2[0]==target:
                        rlist.append(v1[1]+'+'+self.flip(v2[1],0))
                    if v1[0]-v2[0]==target:
                        rlist.append(v1[1]+'-'+self.flip(v2[1],1))
            else:
                for v1 in v1s:
                    if v1[0]==target: rlist.append(v1[1])
        return rlist
