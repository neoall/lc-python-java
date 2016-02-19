class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.helper(l1, l2, 0)
    
    def helper(self, l1, l2, c):
        if l1 is None and l2 is None and c == 0:
            return None
        c += 0 if l1 is None else l1.val
        c += 0 if l2 is None else l2.val
        node = ListNode(c % 10)
        node.next = self.helper(None if l1 is None else l1.next, None if l2 is None else l2.next, c / 10)
        return node
