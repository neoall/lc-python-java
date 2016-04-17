class DLNode(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
        
def dln_connect(nd1,nd2):
    if nd1 is not None and nd2 is not None:
        nd1.next=nd2
        nd2.prev=nd1
    
class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.nmap={}
        self.lhead=DLNode(0,0)
        self.ltail=DLNode(0,0)
        dln_connect(self.lhead,self.ltail)
        
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.nmap:
            nd=self.nmap[key]
            dln_connect(nd.prev,nd.next)
            phd=self.lhead.next
            dln_connect(self.lhead,nd)
            dln_connect(nd,phd)
            return nd.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.nmap:
            self.nmap[key].value=value
        else:
            nd=DLNode(key,value)
            self.nmap[key]=nd
            if len(self.nmap)>self.capacity:
                dnd=self.ltail.prev
                dln_connect(dnd.prev,self.ltail)
                self.nmap.pop(dnd.key)
        self.get(key)
