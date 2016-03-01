class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mi=len(s)
        while mi>0:
            mmap={}
            matched=True
            i=0
            while matched and i<mi/2:
                mir=mi-1-i
                if s[i]!=s[mir]:
                    matched=False
                    mi=mmap.get(s[mir],-1)+mir+1
                else:
                    mmap[s[i]]=i
                    i+=1
            if matched:
                return s[mi:][::-1]+s
        return s[1:][::-1]+s
