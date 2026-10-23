# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        l = head
        while l:
            length += 1
            l = l.next

        l = head
        for i in range(math.ceil(length / 2) - 1):
            l = l.next

        second_half_head = l.next
        l.next = None

        prev_node = None
        while second_half_head:
            temp = second_half_head.next
            second_half_head.next = prev_node
            prev_node = second_half_head
            
            if temp is None:
                break

            second_half_head = temp

        flag = True
        while head and second_half_head:

            if flag:
                temp = head.next
                head.next = second_half_head
                second_half_head = second_half_head.next
                head = head.next
                head.next = temp
                flag = False
            else:
                head = head.next
                flag = True

