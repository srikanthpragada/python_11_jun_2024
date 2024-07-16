class StackEmptyError(Exception):
    def __str__(self):
        return "Stack Empty!!"


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.length > 0:
            return self.data.pop()
        else:
            raise StackEmptyError()

    def peek(self):
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()


s = Stack()
try:
    print(s.pop())
except StackEmptyError as ex:
    print(ex)

s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
print(s.length)
