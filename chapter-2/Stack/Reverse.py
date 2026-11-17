
class Node:
    def __init__(self, value):
        self.data = value
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

    def print(self):
        temp = self.top
        print("Stack Elements:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
st = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))

print("Original Stack:")
st.print()

print("Popped Element:", st.pop())

print("After Pop:")
st.print()
