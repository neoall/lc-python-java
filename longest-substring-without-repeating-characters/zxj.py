class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rmax=0
        lmap={}
        si,ei=0,0
        for i,c in enumerate(s):
            if c in lmap and lmap[c]>=si:
                rmax=max(rmax,ei-si)
                si=lmap[c]+1
            lmap[c]=i
            ei=i+1
            
        return max(rmax,ei-si)
