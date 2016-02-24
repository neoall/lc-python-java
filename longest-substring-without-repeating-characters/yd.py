
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        beg = end = maxLen = 0
        cmap = {}
        for end in range(len(s)):
            if s[end] in cmap and beg <= cmap[s[end]]:
                beg = cmap[s[end]] + 1
            else:
                maxLen = max(maxLen, end - beg + 1)
            cmap[s[end]] = end
        return maxLen
