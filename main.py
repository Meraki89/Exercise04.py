'''Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40'''

# class for holding the data, defaults to empty node if no data is given


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node

# Class for managing the list and nodes


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''
    Exercise Part 1,2 and 3:
    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values
    '''

    def clear(self):
        if self.size == 0:
            print("No nodes in list.")
        else:
            self.head = None
            print("Hey! Where have all my nodes gone?!")
            self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return data
            current = current.next
        return False

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return
        if data == self.head.data:
            self.head = self.head.next
            self.size -= 1
            print(f"Mission accomplished! We got rid of {data} successfully! No one likes {data} anyway!")
            return
        current = self.head
        while current.next is not None:
            if data == current.next.data:
                break
            current = current.next
        if current.next is None:
            print(f"{data} is not in the list")
        else:
            self.size -= 1
            print(f"Mission accomplished! We got rid of {data} successfully! No one likes {data} anyway!")
            current.next = current.next.next

    '''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).
    '''

class NodeDLL:
    '''Implement your node for the doubly linked list here'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def little_helper(self):
        prev = self.prev
        next = self.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev


class DoublyLinkedList:
    '''Implement your code for the doubly linked list here'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = NodeDLL(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        if self.size == 0:
            print("List is empty")
            return
        else:
            self.head = None
            self.tail = None
            print("Hey! Where have all my nodes gone?!")
            self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return data
            current = current.next
        return False

    def delete(self, data):
        if self.size == 0:
            print("List is empty")
            return

        elif self.head.data == data:
            self.head.little_helper()
            self.head = self.head.next
            print(f"Mission accomplished! We got rid of {data} successfully! No one likes {data} anyway!")
            self.size -= 1

        elif self.tail.data == data:
            self.tail.little_helper()
            self.tail = self.tail.prev
            print(f"Mission accomplished! We got rid of {data} successfully! No one likes {data} anyway!")
            self.size -= 1

        else:
            current = self.head.next
            while current:
                if current.data == data:
                    current.little_helper()
                    print(f"Mission accomplished! We got rid of {data} successfully! No one likes {data} anyway!")
                    self.size -= 1
                    return

                current = current.next
            print(f"{data} is not in the list")


    '''Exercise Part 5 and 6:
    Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    methods but you have to complete all methods below. Always return the correct data type according
    to the exercise sheet'''


class MyStack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop()

    def top(self):
        if self.elements:
            return self.elements[-1]

    def size(self):
        return int(len(self.elements))


class MyQueue:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop(0)

    def show_left(self):
        if self.elements:
            return self.elements[0]

    def show_right(self):
        if self.elements:
            return self.elements[-1]

    def size(self):
        return int(len(self.elements))
