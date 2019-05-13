class ListNode:
    def __init__(self, x, prev=None, next=None ):
        self.val = x
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return self.val
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val


class DoublyLinkedList:
    def __init__(self, node):
        self.head = node
    
    def addNode(self, node):
        """
        Add node at head. 
        O(1) insert
        """
        if self.head is None:
            self.head = node
        elif self.head.next is None:
            self.head.next = node
            node.prev = self.head
        else:
            temp = self.head.next
            self.head.next = node
            node.next = temp
            node.prev = self.head
    
    def deleteNode(self):
        """
        Delete node at head.
        O(1) delete.
        """
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = head.next
            return temp