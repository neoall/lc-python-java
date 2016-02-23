class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cmap=Counter(s)
        rset=set()
        rs=[]
        for k in s:
            cmap[k]-=1
            if k not in rset: 
                while len(rs)>0 and k<rs[-1] and cmap[rs[-1]]>0:
                    rset.remove(rs[-1])
                    rs.pop()
                    
                rs.append(k)
                rset.add(k)
                
        return ''.join(rs)
