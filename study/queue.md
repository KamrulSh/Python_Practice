### Author: [Kamrul Islam Shahin 🇧🇩](https://www.linkedin.com/in/mdkamrulshahin/)

# 🚀️ Queue Data Structure (15 days study plan)

- Linear data structure
- Follows the principle of **First In First Out FIFO)**
- First element inserted inside the queue is removed first.

![FIFO Representation of Queue](https://cdn.programiz.com/sites/tutorial2program/files/queue.png)

## 🚀️ Basic Operations of Queue

- **Enqueue** : Add an element to the end of the queue
- **Dequeue** : Remove an element from the front of the queue
- **IsEmpty** : Check if the queue is empty
- **IsFull** : Check if the queue is full
- **Peek** : Get the value of the front of the queue without removing it

## 🚀️ Implementing Queue using list

### \* Method 1

```py
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# it will raise and IndexError as the queue is now empty
print(queue.pop(0))
```

Output:

```
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/tmp/ipykernel_27562/3751923502.py in <module>
     21 # will raise and IndexError
     22 # as the queue is now empty
---> 23 print(queue.pop(0))

IndexError: pop from empty list
```

Drawbacks:

- It can run into speed issues as list are quite slow.
- The last command will raise an IndexError after calling .pop() on an empty queue.

### \* Method 2

![Enqueue and Dequeue Operations](https://cdn.programiz.com/sites/tutorial2program/files/Queue-program-enqueue-dequeue.png)

```py
# Custom queue implementation in Python
class Queue:

    # Initialize queue
    def __init__(self, size=1000):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue

    # Function to dequeue the front element
    def dequeue(self):
        # check for queue underflow
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x

    # Function to add an element to the queue
    def enqueue(self, value):
        # check for queue overflow
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    # Function to return the front element of the queue
    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]

    # Function to return the size of the queue
    def size(self):
        return self.count

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0

    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':

    # create a queue of capacity 5
    q = Queue(5)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print('The queue size is', q.size())
    print('The front element is', q.peek())
    q.dequeue()
    print('The front element is', q.peek())

    q.dequeue()
    q.dequeue()

    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
```

Output:

```
[None, None, None]
Enqueue: 1
[1, None, None]
Enqueue: 2
[1, 2, None]
Enqueue: 3
[1, 2, 3]
Overflow!! Terminating process.
[1, 2, 3]
Queue size: 3
Front element: 1
Dequeue: 1
[None, 2, 3]
Front element: 2
Dequeue: 2
[None, None, 3]
Dequeue: 3
[None, None, None]
The queue is empty
```

## 🚀️ Limitations of Queue

- After some enqueue and dequeue operations the queue will be full as it is implementation using list.
- And we can't use the queue list without resetting the queue.
- To solve this problem we have to use the **circular queue**.

## 🚀️ Implementing Queue using collections.deque

```py

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

q.popleft()
# q.popleft() will raise an IndexError as queue is now empty
```

Output:

```
Initial queue
deque(['a', 'b', 'c'])

Elements dequeued from the queue
a
b
c

Queue after removing elements
deque([])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/tmp/ipykernel_38809/465175385.py in <module>
     21 print(q)
     22
---> 23 q.popleft()
     24 # q.popleft() will raise an IndexError as queue is now empty

IndexError: pop from an empty deque
```

## 🚀️ Implementing Queue using queue.Queue

```py
from queue import Queue

# Initializing a queue
q = Queue(maxsize=3)

# qsize() give the maxsize of the Queue
print("Size:", q.qsize())

# Adding of element to queue
print("Elements added in the queue")
q.put('a')
q.put('b')
q.put('c')
print(q)
# Return Boolean for Full Queue
print("Full: ", q.full())

# Removing element from queue
print("Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty Queue
print("Empty:", q.empty())

q.put(1)
print("Empty:", q.empty())
print("Full:", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())

```

Output:

```
Size: 0
Elements added in the queue
<queue.Queue object at 0x7f4fdbfd6410>
Full:  True
Elements dequeued from the queue
a
b
c
Empty: True
Empty: False
Full: False
```

## 🚀️ Implementation of a Queue Using a Simple Linked List

![Queue Using a Simple Linked List](https://miro.medium.com/max/1400/1*Try9F1-thIr5Ex3m3pmyyA.jpeg)

```py
''' Node class represents a node of the list '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


'''' LnkedList class represents the linked list '''
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    ''' Check if the list (queue) is empty so returns True (self.head is None)
    or not so returns False (self.head is not None) '''

    def is_empty(self):
        return not self.head

    '''Add a new node to the end of the linked list (queue)'''

    def enqueue(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    ''' Remove the first node of the linked list (queue).
    If the linked list (queue) is empty returns a warning message '''

    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    ''' Return the first node of the linked list.
    If the linked list (queue) is empty returns a warning message'''

    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.head.value


if __name__ == '__main__':
    my_queue = LinkedList()

    my_queue.enqueue(Node("a"))
    my_queue.enqueue(Node("b"))
    my_queue.enqueue(Node("c"))

    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: a

    print(f"The element '{my_queue.dequeue()}' removed from the Queue")
    # The element 'a' removed from the Queue

    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: b
```

Output:

```
Queue first element: a
The element 'a' removed from the Queue
Queue first element: b
```

## 🚀️ Resources

- [Geeksforgeeks Queue in Python](https://www.geeksforgeeks.org/queue-in-python/)
- [Programiz queue](https://www.programiz.com/dsa/queue)
