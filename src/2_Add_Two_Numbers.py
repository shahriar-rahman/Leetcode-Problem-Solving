# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Linked List
# Runtime: 78ms
# Memory: 16.44mb

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_head = ListNode(0)
        tail = temp_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                num1 = l1.val
            else:
                num1 = 0
            
            if l2 is not None:
                num2 = l2.val
            else:
                num2 = 0
           
            sum = num1 + num2 + carry
            num = sum % 10
            carry = sum // 10

            new_node = ListNode(num)
            tail.next = new_node
            tail = tail.next

            if l1 is not None:
                l1 = l1.next 
            else:
                l1 = None
                
            if l2 is not None:
                l2 = l2.next 
            else:
                l2 = None

        result = temp_head.next
        temp_head.next = None
        return result