# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def lmost(self,nd):
        cnd=nd
        while cnd is not None:
            self.stk.append(cnd)
            cnd=cnd.left
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur=None
        self.stk=[]
        if root:
            self.lmost(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cur is None and len(self.stk)>0:
            self.cur=self.stk.pop()
            self.lmost(self.cur.right)
        
        return self.cur is not None
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            tmp=self.cur.val
            self.cur=None
            return tmp
        else:
            raise Exception("End of Iterator")

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
