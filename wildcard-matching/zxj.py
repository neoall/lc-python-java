class Solution(object):
    def sp(self,p):
        rs=[]
        cur=''
        lc=None
        for c in p:
            if c!='*':
                cur+=c
            elif lc!='*':
                rs.append(cur)
                cur=''

            lc=c
        rs.append(cur)
        return rs
        
    def bm(self,s,p):
        for cs,cp in zip(s,p):
            if cp!='?' and cs!=cp:
                return False
        return True

    def sm(self,s,bsi,esi,p):
        # ideally, can be done with modified KMP with O(s+p)
        wl=len(p)
        for i in xrange(bsi,esi-wl+1):
            if self.bm(s[i:i+wl],p): return i+wl
        return None

    def isMatch(self, s, p):
        """                                                                                                                                   
        :type s: str                                                                                                                          
        :type p: str                                                                                                                          
        :rtype: bool                                                                                                                          
        """
        rp=self.sp(p)
        if len(rp)==1:
            return len(s)==len(p) and self.bm(s,p)
        elif self.bm(s[:len(rp[0])],rp[0]) and self.bm(s[-len(rp[-1]):],rp[-1]):
            bsi,esi=len(rp[0]),len(s)-len(rp[-1])
            if bsi>esi:	return False
            for pi in xrange(1,len(rp)-1):
                cp=rp[pi]
		mei=self.sm(s,bsi,esi,cp)
                if mei is None: return False
                bsi=mei
            return True

        return False
