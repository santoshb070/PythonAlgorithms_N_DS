from __future__ import print_function
from __future__ import print_function
__author__ = 'Santosh Bhamidipati'


class Stack(object):
    """ A stack is an abstract data type
    Stacks has 2 important operations
    1. push()
    2. pop()

    Push is for pushing an element into a stack
    pop for removing an element into a stack

Wiki link for Stacks is as follows:
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return not bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)


class StackOverflowError(BaseException):
    pass


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print('Stack demonstration:\n')
    print('Initial stack: ' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(), the stack is now: ' , str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(100)
    print('After push(100), the stack is now: ' , str(stack))
    print('is_empty(): ' + str(stack.is_empty()))
    print('size(): ' + str(stack.size()))
