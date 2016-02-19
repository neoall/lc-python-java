class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ir,iw=0,0
        for ir in xrange(len(nums)):
            if nums[ir]:
                if iw!=ir: nums[iw]=nums[ir]
                iw+=1
        for i in xrange(iw,len(nums)):
            nums[i]=0
