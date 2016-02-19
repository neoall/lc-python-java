# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rec_dfs(self,root):
        if root is not None:
            root.right,root.left=self.rec_dfs(root.left),self.rec_dfs(root.right)
        return root
        
    def ite_bfs(self,root):
        from collections import deque
        dq=deque()
        if root: dq.append(root)
        while len(dq)>0:
            cur=dq.popleft()
            cur.left,cur.right=cur.right,cur.left
            if cur.left: dq.append(cur.left)
            if cur.right: dq.append(cur.right)
            
        return root
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return [
                self.rec_dfs,
                self.ite_bfs,
            ][1](root)
