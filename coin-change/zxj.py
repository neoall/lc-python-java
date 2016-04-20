class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins)==1:
            return amount/coins[0] if amount%coins[0]==0 else -1
        rmap={0:0}
        maxc=max(coins)
        tarrem=amount%maxc
        if tarrem==0: return amount/maxc
        scoins=[i for i in coins if i!=maxc]
        secmaxc=max(scoins)
        ub=None
        for camnt in xrange(1,amount+1):
            cands=[rmap[camnt-c] for c in scoins if camnt-c in rmap]
            if len(cands):
                mc=min(cands)
                extr=(amount-camnt)/maxc
                if ub is None or mc+1+extr<ub:
                    rmap[camnt]=mc+1
                    if camnt%maxc==tarrem:
                        ub=rmap[camnt]+extr
            if camnt>=secmaxc and camnt-secmaxc in rmap:
                rmap.pop(camnt-secmaxc)
                if len(rmap)==0: break
        return ub or -1
