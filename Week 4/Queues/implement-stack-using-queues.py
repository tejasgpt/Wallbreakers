class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue2.insert(0,x)
        while self.queue1:
            self.queue2.insert(0, self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue1.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
