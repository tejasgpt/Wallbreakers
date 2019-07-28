class MyHashSet(object):

    def __init__(self):
        """
        Design a HashSet without using any built-in hash table libraries.
        Initialize your data structure here.
        """
        self.set = {}

    def add(self, key):
        """
        Insert a value into the HashSet.
        :type key: int
        :rtype: None
        """
        if key not in self.set:
            self.set[key] = 1

    def remove(self, key):
        """
        Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.pop(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
