"""
Creating a linked list, 2 classes. Create a class for Node object and
class for the linked list itself (consists of Nodes)
"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None