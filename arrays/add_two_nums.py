#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Algo:
    1. Add the numbers in the 2 lists while iterating both lists at the same time
    2. Keep the carry over and add to the result list.
    3. Reverse the result 
    4. Create a linked list with the reversed result list.

    Time complexity: O(N) - we make 1 pass where N is greater of the lengths of the 2 lists.
    Space complexity: O(N) - using a list of size N to store the result
    """
    result = []
    val1 = 0
    val2 = 0
    carry_over = 0

    while l1 is not None or l2 is not None or carry_over > 0:
        if l1 is not None:
            val1 = l1.value
        else:
            val1 = 0

        if l2 is not None:
            val2 = l2.value
        else:
            val2 = 0

        sum = val1 + val2 + carry_over
        carry_over = sum//10
        result.append(sum%10)
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    
    print(result)
    result.reverse()
    print(result)

    resListNode = ListNode(result[0], None)

    for i in range(1,len(result)):
        listNode = ListNode(result[i], resListNode)
        resListNode = listNode
    
    return resListNode


#l1 = ListNode(5, ListNode(4, ListNode(3, None)))
l1 = ListNode(5, None)
l2 = ListNode(5, None)
#l2 = ListNode(5, ListNode(6, None))
res = addTwoNumbers(l1, l2)
while res is not None:
    print(res.value, end="->")
    res = res.next