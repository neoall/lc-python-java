class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        btrick=False
        
        if btrick:
            return num and (num%9 or 9)
        else:
            c=num
            while c>9:
                nc=0
                while c>0:
                    nc+=c%10
                    c/=10
                c=nc
            return c
