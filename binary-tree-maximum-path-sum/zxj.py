# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathRE(self,root,rs):
        if root is None:
            return 0
        lm,rm=self.maxPathRE(root.left,rs),self.maxPathRE(root.right,rs)
        cmax=root.val+max(lm,0)+max(rm,0)
        if rs[0] is None or rs[0]<cmax:
            rs[0]=cmax
        return max(lm,rm,0)+root.val
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rs=[None]
        self.maxPathRE(root,rs)
        return rs[0]
