"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions
 of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is
empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
(double-ended queue) as long as you use only a queue's standard operations.

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack(object):

    def __init__(self):
        self.head = None

    def push(self, x):
        if not self.head:
            self.head = Node(x)
        else:
            a = self.head
            self.head = Node(x)
            self.head.next = a

    def pop(self):
        a = self.head
        if not a.next:
            self.head = None
            return a.data
        else:
            self.head = a.next
            return a.data

    def top(self):
        return self.head.data

    def empty(self):
        if not self.head:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
