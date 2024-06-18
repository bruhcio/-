class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, e):
        self.top = Node(e, self.top)

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def display(self):
        if self.isEmpty():
            print("비어있음")
            return
        else:
            node = self.top
            while node:
                print(node.data, end = ' ')
                node = node.link
            print()
if __name__ == "__main__":
    s = LinkedStack()
    s.push('Y')
    s.display()
    s.push('J')
    s.display()
    s.push('H')
    s.display()

    s.pop()
    s.display()

    print(s.peek())