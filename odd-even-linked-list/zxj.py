# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dm1=ListNode(0)
        dm2=ListNode(0)
        p1,p2=dm1,dm2
        cur=head
        cnt=1
        while cur is not None:
            if cnt==0:
                p2.next=cur
                p2=cur
            else:
                p1.next=cur
                p1=cur
            cur=cur.next
            cnt^=1
            
        p2.next=None
        p1.next=dm2.next
        return dm1.next
