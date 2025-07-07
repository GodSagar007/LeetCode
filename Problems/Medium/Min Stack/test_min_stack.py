import pytest

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def test_min_stack_sequence():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3   # Min is -3
    s.pop()
    assert s.top() == 0       # Top is 0
    assert s.getMin() == -2   # Min is -2

def test_min_stack_push_pop():
    s = MinStack()
    s.push(2)
    s.push(0)
    s.push(3)
    s.push(0)
    assert s.getMin() == 0    # Min is 0
    s.pop()
    assert s.getMin() == 0    # Min is still 0
    s.pop()
    assert s.getMin() == 0    # Min is still 0
    s.pop()
    assert s.getMin() == 2    # Min is 2 after popping 0 and 0

def test_min_stack_single_element():
    s = MinStack()
    s.push(5)
    assert s.top() == 5
    assert s.getMin() == 5
    s.pop()
    # after this point, stack is empty; further pops would raise error (not tested here)

def test_min_stack_with_negatives():
    s = MinStack()
    s.push(-1)
    s.push(-2)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.getMin() == -2
    s.pop()
    assert s.getMin() == -1

def test_min_stack_duplicate_mins():
    s = MinStack()
    s.push(2)
    s.push(2)
    s.push(1)
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 2
