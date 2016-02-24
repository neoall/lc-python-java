class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or numRows <= 1:
            return s

        ret = list()
        nPerLevel = numRows * 2 - 2
        for i in range(numRows):
            for j in range(i, len(s), nPerLevel):
                if j < len(s):
                    ret.append(s[j])
                x = (j / nPerLevel + 1) * nPerLevel - i
                if i > 0 and i < numRows - 1 and x < len(s):
                    ret.append(s[x])
        return "".join(ret)
