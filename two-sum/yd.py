class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nmap = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in nmap:
                return [nmap[rest], i]
            nmap[nums[i]] = i
        return []