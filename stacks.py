print ('Hello, World!')

from pythonds.basic.stack import Stack

s = Stack()
s.push('1')
s.push('2')

print(s.peek())
# returns top value, but DOESNT remove
print(s.pop())
print(s.pop())
# shows and removes the top most item on the Stack
