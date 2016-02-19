# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rec_dfs(self,root):
        if root is None: return 0
        return max(self.rec_dfs(root.left),self.rec_dfs(root.right))+1
    
    def ite_dfs_fake(self,root):
        stk=[(root,1)]
        mx=0
        while len(stk)>0:
            cn,cd=stk.pop()
            if cn is not None:
                mx=max(mx,cd)
                stk.append((cn.left,cd+1))
                stk.append((cn.right,cd+1))
        return mx            
    
    def ite_dfs_post(self,root):
        cur=root
        stk=[]
        lastV=None
        mx=0
        while cur is not None or len(stk)>0:
            if cur is None:
                peek=stk[-1]
                if peek.right and peek.right is not lastV:
                    cur=peek.right
                else:        
                    mx=max(mx,len(stk))
                    lastV=stk.pop()
            else:
                stk.append(cur)
                cur=cur.left
        return mx

    def ite_bfs(self,root):
        from collections import deque
        dummy=TreeNode(0)
        mx=0
        dq=deque()
        if root: dq.append(root)
        while len(dq)>0:
            mx+=1
            dq.append(dummy)
            while dq[0] is not dummy:
                cur=dq.popleft()
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
            dq.popleft()
        return mx
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return [
            self.rec_dfs,
            self.ite_dfs_fake,
            self.ite_dfs_post,
            self.ite_bfs,
            ][3](root)
