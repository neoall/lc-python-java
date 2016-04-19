# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lv,uv=sorted([p.val,q.val])
        cur=root
        while cur is not None:
            if cur.val>uv:
                cur=cur.left
            elif cur.val<lv:
                cur=cur.right
            else:
                return cur
