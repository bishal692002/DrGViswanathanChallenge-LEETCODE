# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dum = ListNode()         # Dummy node to build the result list
        current = dum            # Pointer to the current node in the result list
        carry = 0                # To store carry from each digit addition

        # Loop until both lists are fully traversed and no carry remains
        while l1 or l2 or carry:
            # Get current values from l1 and l2, or 0 if we've reached the end
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry     # Add digits along with carry
            carry = total // 10       # Update carry for the next step
            digital = total % 10      # Digit to store in the current node

            current.next = ListNode(digital)  # Create new node for this digit
            current = current.next            # Move to the next node

            # Move to the next nodes in l1 and l2 (if available)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dum.next              # Return the result list starting from next node
 