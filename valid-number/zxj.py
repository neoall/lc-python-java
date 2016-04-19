class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        statemap={
            'bsp':{'bsp','sig','num','tdot'},
            'sig':{'num','tdot'},
            'tdot':{'dnum'},
            'num':{'num','dot','e','esp'},
            'dnum':{'dnum','e','esp'},
            'dot':{'dnum','e','esp'},
            'e':{'esig','enum'},
            'esig':{'enum'},
            'enum':{'enum','esp'},
            'esp':{'esp'}
            }
        charmap={
            ' ':'sp',
            '+':'sig',
            '-':'sig',
            'e':'e',
            'E':'e',
            '.':'dot'
            }
        charmap.update((ic,'num') for ic in '0123456789')
        csmap={'sp':'bsp','dot':'tdot'}
        
        stat='bsp'
        for c in s:
            ccat=charmap.get(c)
            if ccat is None: return False
            nxt_stat=csmap.get(ccat,ccat)
            if nxt_stat not in statemap[stat]: return False
            if nxt_stat!='bsp': csmap['sp']='esp'
            if nxt_stat=='num':
                csmap['dot']='dot'
            elif nxt_stat in ('dot','tdot'):
                csmap['num']='dnum'
            elif nxt_stat=='e':
                csmap['num']='enum'
                csmap['sig']='esig'
                
            stat=nxt_stat
        
        return 'esp' in statemap[stat]
