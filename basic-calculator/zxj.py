class Solution(object):
    _c0=ord('0')
    def gen(self,s):
        v=None
        for c in s:
            if c in '()+-':
                if v is not None:
                    yield v
                    v=None
                yield c
            else:
                cv=ord(c)-self._c0
                if 9>=cv>=0:
                    if v is None:
                        v=0
                    v=v*10+cv
        if v is not None:
            yield v
            
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        bpos=0 # 0 means pos
        rs=0
        lastsig=0 # 0 means pos
        for tk in self.gen(s):
            if tk=='(':
                bpos=bpos*2+bpos%2^lastsig
                lastsig=0
            elif tk==')':
                bpos=bpos/2
            elif tk=='+':
                lastsig=0
            elif tk=='-':
                lastsig=1
            else:
                rs+=(1,-1)[bpos%2^lastsig]*tk
                
        return rs
