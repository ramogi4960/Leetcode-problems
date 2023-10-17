"""
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:
FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position
choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].

Example 1:
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle",
"popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)


Constraints:

1 <= val <= 109
At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.
"""


class FrontMiddleBackQueue:

    def __init__(self):
        # let it be a normal list
        self.q = []

    def pushFront(self, val: int) -> None:
        # push val into the front of q
        self.q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        # this pushes val into len(q)//2
        self.q.insert(len(self.q)//2, val)

    def pushBack(self, val: int) -> None:
        # this pushes val into the end of q
        self.q.append(val)

    def popFront(self) -> int:
        # removes and returns the val at q[0] or returns -1 if q is empty
        if not self.q: return -1
        return self.q.pop(0)

    def popMiddle(self) -> int:
        # this pops the val at len(q)//2 if len(q) is odd else len(q)//2 - 1
        if not self.q: return -1
        if len(self.q) % 2 == 0:
            return self.q.pop(len(self.q)//2 - 1)
        else:
            return self.q.pop(len(self.q)//2)

    def popBack(self) -> int:
        # this pops the end val of q or returns -1 if q is empty
        if not self.q: return -1
        return self.q.pop()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()