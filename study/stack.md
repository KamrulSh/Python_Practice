#### Author: [Kamrul Islam Shahin 🇧🇩](https://www.linkedin.com/in/mdkamrulshahin/https:/)

# 🚀️ Stack Data Structure (30 days study plan)

- Linear data structure
- Follows the principle of **Last In First Out (LIFO)**
- Last element inserted inside the stack is removed first.

![represent the LIFO principle by using push and pop operation](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

## 🚀️ Stack operations:

- **push**: Pushes an item at the top of the stack.
- **pop**: Remove and return the item from the top of the stack.
- **peek**: Returns the item at the top of the stack without removing it.
- **size**: Returns the total number of items in the stack.
- **isEmpty**: Checks whether the stack is empty.
- **isFull**: Checks whether the stack is full.

## 🚀️ Implementing Stack using Arrays

### \* Method 1

```python
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
print('Initial stack:')
print(stack)

# pop() fucntion to pop element from stack in LIFO order
print('Elements poped from stack:')
print(stack.pop())
print(stack.pop())
print('Stack after elements are poped:')
print(stack)
print(stack.pop())
```

Output:

```
Initial stack:
['a', 'b']
Elements poped from stack:
b
a
Stack after elements are poped:
[]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/tmp/ipykernel_146307/3602183844.py in <module>
     16 print('Stack after elements are poped:')
     17 print(stack)
---> 18 print(stack.pop())

IndexError: pop from empty list
```

#### Drawbacks

- It can run into speed issues as it grows.
- The last command will raise an IndexError after calling .pop() on an empty stack.

### \* Method 2

```python
class Stack:
    def __init__(self):
        self.stack = []

    # Use list append method to push element
    def push(self, val):
        self.stack.append(val)
        return val

    # Stack is empty when stack size is 0
    def isEmpty(self):
        return len(self.stack) == 0

    # Use list pop method to remove element
    def pop(self):
        if self.isEmpty():
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    # Use peek to look at the top of the stack
    def peek(self):
        if self.isEmpty():
            return ("No element in the Stack")
        else:
            return self.stack[-1]

    def print(self):
        return self.stack


stack = Stack()
print("push:", stack.push(1))
print("push:", stack.push(2))
print(stack.print())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print(stack.print())
print("peek:", stack.peek())
print("push:", stack.push(3))
print("push:", stack.push(4))
print(stack.print())
print("peek:", stack.peek())
```

Output:

```
push: 1
push: 2
[1, 2]
pop: 2
pop: 1
pop: No element in the Stack
[]
peek: No element in the Stack
push: 3
push: 4
[3, 4]
peek: 4
```

### \* Method 3 (Implementing all operations)

```python
class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    # Use list append method to push element
    def push(self, val):
        if self.isFull():
            return ("Stack overflow")
        else:
            self.top += 1
            self.stack[self.top] = val
            return val

    # Stack is full when self.size is equal to top + 1
    def isFull(self):
        return self.size == self.top + 1

    # Stack is empty when top is -1
    def isEmpty(self):
        return self.top == -1
        # OR return self.size() == 0

    # Use list pop method to remove element and set as None
    def pop(self):
        if self.isEmpty():
            return ("Stack underflow")
        else:
            topVal = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return topVal

    # Use peek to look at the top of the stack
    def peek(self):
        if self.isEmpty():
            return ("Stack empty")
        else:
            return self.stack[self.top]

    # Stack size
    def size(self):
        return self.top + 1

    def print(self):
        return self.stack


stack = Stack(3)
print("push:", stack.push(1))
print("push:", stack.push(2))
print(stack.print())
print("pop:", stack.pop())
print("pop:", stack.pop())
print(stack.print())
print("pop:", stack.pop())
print("peek:", stack.peek())
print("push:", stack.push(3))
print("push:", stack.push(4))
print("push:", stack.push(5))
print("push:", stack.push(6))
print(stack.print())
print("peek:", stack.peek())
```

Output:

```
push: 1
push: 2
[1, 2, None]
pop: 2
pop: 1
[None, None, None]
pop: Stack underflow
peek: Stack empty
push: 3
push: 4
push: 5
push: Stack overflow
[3, 4, 5]
peek: 5
```

## 🚀️ Implementing Stack using deque

```python
from collections import deque
stack = deque()

# append() function to push element in the stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
# pop() fucntion to pop element from stack in LIFO order
print("pop:", stack.pop())
# appendleft() function to push element in the left side of the stack
stack.appendleft(11)
print(stack)
stack.append(12)
print(stack)
print("popleft:", stack.popleft())
print(stack)
print("peek:", stack[-1])
print("pop:", stack.pop())
print(stack)
print("popleft:", stack.popleft())
print(stack)
```

Output:

```
deque([1, 2, 3])
pop: 3
deque([11, 1, 2])
deque([11, 1, 2, 12])
popleft: 11
deque([1, 2, 12])
peek: 12
pop: 12
deque([1, 2])
popleft: 1
deque([2])
```

## 🚀️ Implementing Stack using LifoQueue

```python
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
# qsize() show the number of elements in the stack
print("Size:",stack.qsize())
# put() function to push element in the stack
stack.put(1)
print("Full:", stack.full())
stack.put(2)
stack.put(3)
print("Full:", stack.full())
print("Size:", stack.qsize())
# get() fucntion to pop element from stack in LIFO order
print("pop:",stack.get())
print("pop:",stack.get())
print("pop:",stack.get())
print("Empty:", stack.empty())
```

Output:

```
Size: 0
Full: False
Full: True
Size: 3
pop: 3
pop: 2
pop: 1
Empty: True
```

## 🚀️ Referances

[1. Geeksforgeeks](https://www.geeksforgeeks.org/stack-data-structure-introduction-program/)
[2. Techiedelight](https://www.techiedelight.com/stack-implementation-python/)
[3. Programiz](https://www.programiz.com/dsa/stack)
[4. RealPython](https://realpython.com/how-to-implement-python-stack/)
