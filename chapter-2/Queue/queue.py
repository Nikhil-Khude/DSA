
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            print("Queue is Empty")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    def print_queue(self):
        temp = self.front

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Original Queue:")
q.print_queue()

print("Deleted Element:", q.dequeue())

print("After Dequeue:")
q.print_queue()
