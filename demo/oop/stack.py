class StackEmptyError(Exception):
    def __str__(self):
        return "Stack Empty!!"

class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos >= 0:
            value = self.data[self.pos]
            self.pos -= 1
            return value
        else:
            raise StopIteration



class Stack:
    def __init__(self):
        self.data = []

    def __iter__(self):
        return Stack_Iterator(self.data)

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
# try:
#     print(s.pop())
# except StackEmptyError as ex:
#     print(ex)

s.push(10)
s.push(20)
s.push(30)

for v in s:
    print(v)


# print(s.peek())
# print(s.pop())
# print(s.length)
