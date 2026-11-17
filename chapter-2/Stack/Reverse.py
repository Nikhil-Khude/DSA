
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data


def reverse_stack(st1):
    q = Queue()

    while st1.top is not None:
        data = st1.pop()
        q.enqueue(data)

    while not q.is_empty():
        data = q.dequeue()
        st1.push(Node(data))


# Main Program
st1 = Stack()

st1.push(Node(10))
st1.push(Node(20))
st1.push(Node(30))
st1.push(Node(40))

print("Original Stack:")
st1.print_stack()

reverse_stack(st1)

print("Reversed Stack:")
st1.print_stack()
