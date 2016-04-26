class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xall=reduce(lambda x,y:x^y,nums,0)
        mask=xall&(xall-1)^xall
        
        xs=[0,0]
        for n in nums:
            idx=1 if n&mask else 0
            xs[idx]=xs[idx]^n
            
        return xs
