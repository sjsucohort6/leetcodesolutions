import unittest

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ds.linked_list import ListNode



class Solution:
    def mergeTwoLists(self, l1, l2):
        head = None
        cur = None
        n1 = l1
        n2 = l2
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        while n1 is not None or n2 is not None:
            if head is None:
                if n1 is not None and n2 is not None:
                    if n1.val < n2.val:
                        head = ListNode(n1.val, ListNode(n2.val))
                    else: 
                        head = ListNode(n2.val, ListNode(n1.val))
                    cur = head.next
                elif n1 is not None:
                    head = ListNode(n1.val)
                    cur = head
                elif n2 is not None:
                    head = ListNode(n2.val)
                    cur = head
            else:
                if n1 is not None and n2 is not None:
                    if n1.val < n2.val:
                        n = ListNode(n1.val, ListNode(n2.val))
                    else: 
                        n = ListNode(n2.val, ListNode(n1.val))
                elif n1 is not None:
                    n = ListNode(n1.val)
                elif n2 is not None:
                    n = ListNode(n2.val)
                if cur.val < n.val:
                    cur.next = n
                    cur = n
                    if n.next is not None:
                        cur = n.next
                else:
                    temp = cur.val
                    cur.val = n.val
                    n.val = temp
                    cur.next = n
                    if n.next is not None:
                        cur = n.next
                    else:
                        cur = n
            if n1 is not None:
                n1 = n1.next
            if n2 is not None:
                n2 = n2.next

        return head


class Test (unittest.TestCase):
    def testme(self):
        s = Solution()
        l1 = ListNode(1, ListNode(2,ListNode(4)))
        l2 = ListNode(1, ListNode(3,ListNode(4)))
        res = ListNode(1, ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(1, ListNode(2))
        l1 = ListNode(3)
        res = ListNode(1,ListNode(2, ListNode(3)))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(1, ListNode(2))
        l1 = None
        res = ListNode(1, ListNode(2))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(2)
        l1 = ListNode(1)
        res = ListNode(1, ListNode(2))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(5)
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        res = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(-9, ListNode(3))
        l1 = ListNode(5, ListNode(7))
        res = ListNode(-9, ListNode(3, ListNode(5, ListNode(7))))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(5)
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        res = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

        l2 = ListNode(1, ListNode(2, ListNode(4)))
        l1 = ListNode(1, ListNode(3, ListNode(4)))
        res = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        self.assertEqual(s.mergeTwoLists(l1, l2), res)

if __name__ == "__main__":
    unittest.main()