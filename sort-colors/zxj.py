class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i0,i2=0,len(nums)-1
        ir=0
        while ir<=i2:
            if nums[ir]==0:
                nums[i0],nums[ir]=nums[ir],nums[i0]
                i0+=1
                ir+=1
            elif nums[ir]==2:
                nums[i2],nums[ir]=nums[ir],nums[i2]
                i2-=1
            else:
                ir+=1
