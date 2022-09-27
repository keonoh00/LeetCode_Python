from typing import Optional


"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Simple initialization of variables
        currentNode = None
        carry = 0

        # We do not know which ListNode has longer length so in any case if at least one node is not None
        while l1 is not None or l2 is not None:
            # If there is carry from previous node sum, then start from carry
            current_sum = carry

            # This conditional statement indicates whether ListNode has ended or not
            if l1 is not None:
                # If ListNode did not end, add the value and reassign l1 as next node of l1 for next iternation
                current_sum += l1.val
                l1 = l1.next

            # This conditional statement indicates whether ListNode has ended or not
            if l2 is not None:
                # If ListNode did not end, add the value and reassign l2 as next node of l2 for next iternation
                current_sum += l2.val
                l2 = l2.next

            node = ListNode(current_sum % 10)
            carry = current_sum // 10

            # When we are adding the first node to the currentNode result
            if currentNode == None:
                # We need to set our head to node, otherwise currentNode at the end will be the last node
                # which we want the result to be the head of the ListNode
                head = currentNode = node
            else:
                currentNode.next = node
                # Set head of currentNode as next node to accept next node in next iteration
                currentNode = currentNode.next

        # After full iteration of both l1 and l2, if there is still carry left we need to add as our last node
        if carry > 0:
            currentNode.next = ListNode(carry)

        # We need to return the head not currentNode
        return head


"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
