class MyStack:
    def __init__(self):
        self.data = []

    def push(self, item):
        #always a constant complexity. Regardless of the stack size, placing one item onto the array will always be the same complexity. O(1) complexity is constant and is good
        self.data.append(item)

    def pop(self):
        #same complexity as above.
        #returns value and removes item
        item = self.data[len(self.data) - 1]
        self.data.remove(item)
        return item

    def peek(self):
        #same as above.
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        # if len(self.data) == 0:
        #     return True
        # else:
        #     return False
        return len(self.data) == 0

stack = MyStack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

print stack.peek()
