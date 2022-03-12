# Stack Data Structure

- Linear data structure
- Follows the principle of **Last In First Out (LIFO)**
- Last element inserted inside the stack is removed first.

![represent the LIFO principle by using push and pop operation](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

## Stack operations:

- **push**: Pushes an item at the top of the stack.
- **pop**: Remove and return the item from the top of the stack.
- **peek**: Returns the item at the top of the stack without removing it.
- **size**: Returns the total number of items in the stack.
- **isEmpty**: Checks whether the stack is empty.
- **isFull**: Checks whether the stack is full.

## Implementing Stack using Arrays

### \* Method 1

```python
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
print('Initial stack:')
print(stack)

# pop() fucntion to pop
# element from stack in
# LIFO order
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
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False

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
stack.push(1)
stack.push(2)
print(stack.print())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print(stack.print())
print("peek:", stack.peek())
stack.push(3)
stack.push(4)
print(stack.print())
print("peek:", stack.peek())
```

## Referances

[1. Geeksforgeeks](https://www.geeksforgeeks.org/stack-data-structure-introduction-program/)

[2. Techiedelight](https://www.techiedelight.com/stack-implementation-python/)

[3. Programiz](https://www.programiz.com/dsa/stack)
