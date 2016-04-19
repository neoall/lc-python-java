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
        cur=root
        stk=[]
        lastV=None
        pstk=None
        qstk=None
        while cur is not None or len(stk)>0:
            if cur is not None:
                stk.append(cur)
                cur=cur.left
            else:
                if stk[-1].right is not None and lastV is not stk[-1].right:
                    cur=stk[-1].right
                else:
                    if stk[-1] is p:
                        pstk=stk[:]
                    if stk[-1] is q:
                        qstk=stk[:]
                    if pstk is not None and qstk is not None:
                        break
                    lastV=stk.pop()
        cm=None
        for v1,v2 in zip(pstk,qstk):
            if v1 is v2:
                cm=v1
            else:
                break
        return cm
