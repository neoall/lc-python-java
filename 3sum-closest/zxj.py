class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        snums=sorted(nums)
        llen=len(nums)
        mx=None
        md=None
        for i0 in xrange(llen-2):
            i1=i0+1
            i2=llen-1
            while i1<i2:
                curx=snums[i0]+snums[i1]+snums[i2]
                curd=abs(curx-target)
                if md is None or curd<md:
                    mx,md=curx,curd
                if curx<target: i1+=1
                elif curx>target: i2-=1
                else: return target
        return mx
