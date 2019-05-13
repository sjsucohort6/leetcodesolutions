# Definition for singly-linked list node.
class ListNode:
    def __init__(self, x, l2=None):
        self.val = x
        self.next = l2
    
    def __str__(self):
        return str(self.val)
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val

class SinglyLinkedList:
    def __init__(self, node):
        self.head = node
    
    def addNode(self, node):
        """
        Add node at head. 
        O(1) insert
        """
        if self.head is None:
            self.head = node
        else:
            temp = self.head.next
            self.head = node
            self.head.next = temp
    
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
    
    def __eq__(self, other):
        n1 = self
        n2 = other

        if self.size() != other.size():
            return False

        while n1 is not None:
            if n1.val != n2.val:
                return False
            else:
                n1 = n1.next
                n2 = n2.next
        return True

    def __str__(self):
        node = self
        s = ''
        while node is not None:
            s +=  '->' + str(node.val)
            node = node.next 
        return s
    
    def size(self):
        n = self
        sz = 0
        while n is not None:
            sz += 1
            n = n.next
        return sz