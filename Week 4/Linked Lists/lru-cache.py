class DoublyListNode():
    def _init_(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def addNode(self,node):
        """
        Add new node after head.
        """
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def removeNode(self,node):
        """
        Remove existing node from doubly linked list.
        """
        node.prev.next, node.next.prev = node.next, node.prev
        
    def moveToHead(self,node):
        """
        Move given node to the head.
        """
        self.removeNode(node)
        self.addNode(node)
    
    def popTail(self):
        """
        Pop current tail.
        """
        popped = self.tail.prev
        self.removeNode(popped)
        return popped
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DoublyListNode(), DoublyListNode()
        
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key, None)
        if not node:
            return -1
        self.moveToHead(node)
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.map.get(key)
        
        if not node:
            new = DoublyListNode()
            new.key = key
            new.val = value
            
            self.map[key] = new
            self.addNode(new)
            self.size += 1
            
            if self.size > self.capacity:
                popped = self.popTail()
                del self.map[popped.key]
                self.size -= 1
        else:
            node.val = value
            self.moveToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
