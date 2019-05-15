class LinkedStack:

    class _Node:

        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):

        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e,self._head)   # next = self._head 
                                                # because currently its the only Node
                                                # and it will be next Node for new Node
                                                # & then self._head is reset to HEAD
        self._size +=1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -=1
        return answer

stack1 = LinkedStack()
stack1.push(5)
stack1.push(7)
print (stack1.is_empty())
print (stack1.__len__())
print (stack1.top())
print (stack1.pop())
print (stack1.top())