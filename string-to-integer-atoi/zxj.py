class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        statemap={
            'start':{'bspace','sign','number'},
            'bspace':{'bspace','sign','number'},
            'sign':{'number'},
            'number':{'number','end'},
            }
        charmap={' ':'bspace','+':'sign','-':'sign'}
        charmap.update((ic,'number') for ic in '0123456789')
        status='start'
        v=0
        bsig=1
        for c in str:
            nxt_stat=charmap.get(c)
            if nxt_stat is None: break
            if nxt_stat not in statemap[status]:
                return 0
            if nxt_stat=='sign' and c=='-': bsig=-1
            if nxt_stat=='number':
                if ' ' in charmap: charmap.pop(' ')
                ad=ord(c)-ord('0')
                if v<214748364 or (v==214748364 and ((bsig==1 and ad<7) or (bsig==-1 and ad<8))):
                    v=v*10+ad
                elif bsig==1: 
                    return 2147483647
                else:
                    return -2147483648
            status=nxt_stat
        if 'end' not in statemap[status]: return 0
        return bsig*v
