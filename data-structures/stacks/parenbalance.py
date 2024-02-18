def is_balanced(input_str):
    parenstack = Stack()
    for c in input_str:
        if c == "(":
            parenstack.push(c)
        elif c == ")":
            if parenstack.peek() == "(":
                parenstack.pop()
            else:
                return False
    if parenstack.peek() is None:
        return True
    else:
        return False


# don't modify below this line


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
