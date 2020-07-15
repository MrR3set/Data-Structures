"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        del(self)
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        self.length+=1
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head=newNode

        # create instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance
        
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length-=1
            return value 
        else:
            self.head.next.prev = None
            value = self.head.value
            self.head = self.head.next
            self.length-=1
            return value
        # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None

        # return the value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        self.length+=1
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # create instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance
        
        # if DLL is not empty
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node       
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length-=1
            return value
        else:
            self.tail.prev.next = None
            value = self.tail.value
            self.tail = self.tail.prev
            self.length-=1
            return value
        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None

        # return the value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.head:
            if node.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev.delete()
                self.head.prev = None
        elif node is self.tail:
            if node.prev is None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.prev.delete()
                self.tail.next = None   
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.delete()
        self.length-=1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        currentNode = self.head
        maxValue = self.head.value
        while currentNode != None:
            if currentNode.value > maxValue:
                maxValue = currentNode.value
            currentNode = currentNode.next
        return maxValue